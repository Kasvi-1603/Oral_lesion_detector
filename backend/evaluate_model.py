"""
Model Evaluation Script
Calculates real performance metrics for the oral lesion classifier

Usage:
    python evaluate_model.py
"""

import os
import numpy as np
import tensorflow as tf
from pathlib import Path
from sklearn.metrics import (
    confusion_matrix, 
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
MODEL_PATH = "models/oral_lesion_model.h5"
TEST_DATA_PATH = "test_data"  # Update with your dataset path
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

def load_test_data():
    """Load and preprocess test dataset"""
    print("📂 Loading test dataset...")
    
    if not os.path.exists(TEST_DATA_PATH):
        print(f"❌ Test data directory not found: {TEST_DATA_PATH}")
        print(f"\n📥 Please organize your dataset like this:")
        print(f"   {TEST_DATA_PATH}/")
        print(f"   ├── Benign/")
        print(f"   │   ├── image1.jpg")
        print(f"   │   ├── image2.jpg")
        print(f"   │   └── ...")
        print(f"   └── Malignant/")
        print(f"       ├── image1.jpg")
        print(f"       ├── image2.jpg")
        print(f"       └── ...")
        return None
    
    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255
    )
    
    try:
        test_generator = test_datagen.flow_from_directory(
            TEST_DATA_PATH,
            target_size=IMAGE_SIZE,
            batch_size=BATCH_SIZE,
            class_mode='binary',  # Binary classification: Benign (0) vs Malignant (1)
            shuffle=False  # Important: don't shuffle for evaluation
        )
        return test_generator
    except Exception as e:
        print(f"❌ Error loading test data: {str(e)}")
        return None

def evaluate_model(model, test_generator):
    """Evaluate model and calculate metrics"""
    print("\n🔬 Running model evaluation...")
    
    # Get predictions
    print("   Making predictions...")
    predictions = model.predict(test_generator, verbose=1)
    
    # Convert probabilities to class labels
    # predictions > 0.5 means Malignant, <= 0.5 means Benign
    y_pred = (predictions > 0.5).astype(int).flatten()
    y_true = test_generator.classes
    
    print(f"   Total predictions: {len(y_pred)}")
    print(f"   Predicted Benign: {np.sum(y_pred == 0)}")
    print(f"   Predicted Malignant: {np.sum(y_pred == 1)}")
    
    # Calculate confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)  # Sensitivity
    f1 = f1_score(y_true, y_pred, zero_division=0)
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    return {
        'confusion_matrix': cm,
        'TP': int(tp),
        'TN': int(tn),
        'FP': int(fp),
        'FN': int(fn),
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'sensitivity': recall,  # Same as recall
        'specificity': specificity,
        'f1_score': f1,
        'y_true': y_true,
        'y_pred': y_pred,
        'total_samples': len(y_true)
    }

def print_results(metrics):
    """Print formatted results"""
    print("\n" + "="*70)
    print("🎯 MODEL PERFORMANCE METRICS")
    print("="*70)
    
    print(f"\n📊 Dataset Information:")
    print(f"   Total test samples: {metrics['total_samples']}")
    print(f"   Benign samples (actual): {metrics['TN'] + metrics['FP']}")
    print(f"   Malignant samples (actual): {metrics['TP'] + metrics['FN']}")
    
    print(f"\n🔢 Confusion Matrix:")
    print(f"                    Predicted Benign    Predicted Malignant")
    print(f"   Actually Benign:      {metrics['TN']:4d} (TN)          {metrics['FP']:4d} (FP)")
    print(f"   Actually Malignant:   {metrics['FN']:4d} (FN)          {metrics['TP']:4d} (TP)")
    
    print(f"\n✅ Performance Metrics:")
    print(f"   Accuracy:    {metrics['accuracy']:6.1%}  - Overall correctness")
    print(f"   Precision:   {metrics['precision']:6.1%}  - When model says 'Malignant', how often correct?")
    print(f"   Sensitivity: {metrics['sensitivity']:6.1%}  - How many actual cancers did we catch?")
    print(f"   Specificity: {metrics['specificity']:6.1%}  - How many benign cases did we correctly identify?")
    print(f"   F1-Score:    {metrics['f1_score']:6.1%}  - Balance between precision and sensitivity")
    
    # Clinical interpretation
    print(f"\n🏥 Clinical Interpretation:")
    missed_cancers = metrics['FN']
    false_alarms = metrics['FP']
    print(f"   ✅ Correctly identified {metrics['TP']} malignant cases")
    print(f"   ✅ Correctly identified {metrics['TN']} benign cases")
    if missed_cancers > 0:
        print(f"   ⚠️  Missed {missed_cancers} malignant cases (FALSE NEGATIVES - CRITICAL!)")
    if false_alarms > 0:
        print(f"   ⚠️  {false_alarms} false alarms (FALSE POSITIVES - benign classified as malignant)")
    
    print("\n" + "="*70)
    
    # LaTeX format for academic papers
    print("\n📝 LaTeX Format (for papers/reports):")
    print("\\begin{itemize}")
    print(f"    \\item Overall Accuracy: {metrics['accuracy']:.1%}")
    print(f"    \\item Sensitivity (Recall): {metrics['sensitivity']:.1%}")
    print(f"    \\item Specificity: {metrics['specificity']:.1%}")
    print(f"    \\item Precision: {metrics['precision']:.1%}")
    print(f"    \\item F1-score: {metrics['f1_score']:.1%}")
    print(f"    \\item Test Dataset Size: {metrics['total_samples']} images")
    print("\\end{itemize}")
    
    print("\n" + "="*70)
    
    # For README/Documentation
    print("\n📋 Markdown Format (for README.md):")
    print("```")
    print("### Model Performance Metrics")
    print("")
    print(f"- **Overall Accuracy**: {metrics['accuracy']:.1%}")
    print(f"- **Sensitivity (Recall)**: {metrics['sensitivity']:.1%}")
    print(f"- **Specificity**: {metrics['specificity']:.1%}")
    print(f"- **Precision**: {metrics['precision']:.1%}")
    print(f"- **F1-Score**: {metrics['f1_score']:.1%}")
    print(f"- **Test Dataset Size**: {metrics['total_samples']} images")
    print("```")
    print("\n" + "="*70)

def plot_confusion_matrix(metrics):
    """Plot and save confusion matrix"""
    try:
        plt.figure(figsize=(10, 8))
        
        # Create confusion matrix plot
        sns.heatmap(
            metrics['confusion_matrix'], 
            annot=True, 
            fmt='d', 
            cmap='Blues',
            xticklabels=['Benign', 'Malignant'],
            yticklabels=['Benign', 'Malignant'],
            cbar_kws={'label': 'Count'}
        )
        
        plt.title('Confusion Matrix - Oral Lesion Classifier', fontsize=14, fontweight='bold')
        plt.ylabel('True Label', fontsize=12)
        plt.xlabel('Predicted Label', fontsize=12)
        
        # Add metrics text
        accuracy = metrics['accuracy']
        text = f"Accuracy: {accuracy:.1%}\n"
        text += f"Sensitivity: {metrics['sensitivity']:.1%}\n"
        text += f"Specificity: {metrics['specificity']:.1%}"
        plt.text(1.5, 2.5, text, fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
        print("\n💾 Confusion matrix saved as 'confusion_matrix.png'")
        plt.close()
    except Exception as e:
        print(f"\n⚠️  Could not save confusion matrix plot: {str(e)}")

def main():
    """Main evaluation function"""
    print("="*70)
    print("🦷 ORAL LESION MODEL EVALUATION")
    print("="*70)
    
    # Check if model exists
    if not os.path.exists(MODEL_PATH):
        print(f"\n❌ Model not found at {MODEL_PATH}")
        print("Please ensure the model file exists!")
        return
    
    print(f"\n📦 Loading model from {MODEL_PATH}...")
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("✅ Model loaded successfully!")
        print(f"   Model input shape: {model.input_shape}")
        print(f"   Model output shape: {model.output_shape}")
    except Exception as e:
        print(f"❌ Error loading model: {str(e)}")
        return
    
    # Load test data
    test_generator = load_test_data()
    if test_generator is None:
        return
    
    print(f"✅ Loaded {test_generator.samples} test images")
    print(f"   Classes found: {test_generator.class_indices}")
    print(f"   Class distribution:")
    unique, counts = np.unique(test_generator.classes, return_counts=True)
    for cls, count in zip(unique, counts):
        class_name = list(test_generator.class_indices.keys())[list(test_generator.class_indices.values()).index(cls)]
        print(f"      {class_name}: {count} images")
    
    # Evaluate
    metrics = evaluate_model(model, test_generator)
    
    # Print results
    print_results(metrics)
    
    # Plot confusion matrix
    plot_confusion_matrix(metrics)
    
    print("\n✅ Evaluation complete!")
    print("\n💡 Next steps:")
    print("   1. Review the metrics above")
    print("   2. Check confusion_matrix.png for visualization")
    print("   3. Update your README.md with these real metrics")
    print("   4. Update ForDentists.js with accurate performance numbers")

if __name__ == "__main__":
    main()


