# 🦷 Oral Lesion Model Evaluation - Google Colab Script
# Copy this entire file and run it in Google Colab!

"""
INSTRUCTIONS:
1. Go to: https://colab.research.google.com/
2. File > New Notebook
3. Copy-paste this entire script into a code cell
4. Run it!
"""

# ============================================================================
# STEP 1: Mount Google Drive
# ============================================================================
from google.colab import drive, files
drive.mount('/content/drive')
print("✅ Google Drive mounted!")

# ============================================================================
# STEP 2: Install Dependencies
# ============================================================================
print("\n📦 Installing dependencies...")
!pip install tensorflow scikit-learn matplotlib seaborn -q
print("✅ Dependencies installed!")

# ============================================================================
# STEP 3: Upload Model
# ============================================================================
print("\n📤 Please upload your oral_lesion_model.h5 file:")
uploaded = files.upload()
model_filename = list(uploaded.keys())[0]
print(f"✅ Model uploaded: {model_filename}")

# ============================================================================
# STEP 4: Configure Dataset Path
# ============================================================================
# 🔧 UPDATE THIS to match your Google Drive structure
DATASET_PATH = '/content/drive/MyDrive/Oral Images Dataset'

# If your dataset has a different path in Drive, update above
# Examples:
# DATASET_PATH = '/content/drive/MyDrive/datasets/oral-lesion-data'
# DATASET_PATH = '/content/drive/MyDrive/Oral_Images_Dataset'

print(f"\n📂 Dataset path: {DATASET_PATH}")

# ============================================================================
# STEP 5: Load Model and Data
# ============================================================================
import tensorflow as tf
import numpy as np
import os

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

print("\n📦 Loading model...")
model = tf.keras.models.load_model(model_filename)
print(f"✅ Model loaded! Input: {model.input_shape}, Output: {model.output_shape}")

print("\n📂 Loading test dataset...")
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle=False
)
print(f"✅ Loaded {test_generator.samples} images")
print(f"   Classes: {test_generator.class_indices}")

# ============================================================================
# STEP 6: Run Evaluation
# ============================================================================
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score,
    recall_score, f1_score
)

print("\n🔬 Running evaluation (this may take a few minutes)...")
predictions = model.predict(test_generator, verbose=1)
y_pred = (predictions > 0.5).astype(int).flatten()
y_true = test_generator.classes

# Calculate metrics
cm = confusion_matrix(y_true, y_pred)
tn, fp, fn, tp = cm.ravel()
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)
sensitivity = recall
specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
f1 = f1_score(y_true, y_pred, zero_division=0)

print("\n✅ Evaluation complete!")

# ============================================================================
# STEP 7: Display Results
# ============================================================================
print("\n" + "="*70)
print("🎯 MODEL PERFORMANCE METRICS")
print("="*70)
print(f"\n📊 Dataset: {len(y_true)} images ({tn + fp} Benign, {tp + fn} Malignant)")
print(f"\n🔢 Confusion Matrix:")
print(f"   Actually Benign:    TN={tn:4d}  FP={fp:4d}")
print(f"   Actually Malignant: FN={fn:4d}  TP={tp:4d}")
print(f"\n✅ Performance Metrics:")
print(f"   Accuracy:    {accuracy:6.1%}")
print(f"   Precision:   {precision:6.1%}")
print(f"   Sensitivity: {sensitivity:6.1%}")
print(f"   Specificity: {specificity:6.1%}")
print(f"   F1-Score:    {f1:6.1%}")
print("="*70)

# ============================================================================
# STEP 8: Export Results
# ============================================================================
results_text = f"""ORAL LESION MODEL - PERFORMANCE METRICS
{'='*70}

Dataset: {len(y_true)} images ({tn + fp} Benign, {tp + fn} Malignant)

Confusion Matrix:
- True Negatives (TN): {tn}
- False Positives (FP): {fp}
- False Negatives (FN): {fn}
- True Positives (TP): {tp}

Performance Metrics:
- Accuracy: {accuracy:.1%}
- Precision: {precision:.1%}
- Sensitivity: {sensitivity:.1%}
- Specificity: {specificity:.1%}
- F1-Score: {f1:.1%}

{'='*70}

FOR README.md:
### Model Performance Metrics
- **Overall Accuracy**: {accuracy:.1%}
- **Sensitivity**: {sensitivity:.1%}
- **Specificity**: {specificity:.1%}
- **Precision**: {precision:.1%}
- **F1-Score**: {f1:.1%}
- **Test Dataset**: {len(y_true)} images

{'='*70}

FOR ForDentists.js (lines 64-67):
<li>Overall Accuracy: <strong>{accuracy:.1%}</strong></li>
<li>Sensitivity: <strong>{sensitivity:.1%}</strong></li>
<li>Specificity: <strong>{specificity:.1%}</strong></li>
<li>Training Dataset: <strong>{len(y_true)} images</strong></li>
"""

with open('model_metrics.txt', 'w') as f:
    f.write(results_text)

print("\n💾 Results saved!")
files.download('model_metrics.txt')

# ============================================================================
# STEP 9: Plot Confusion Matrix
# ============================================================================
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Benign', 'Malignant'],
            yticklabels=['Benign', 'Malignant'])
plt.title('Confusion Matrix', fontsize=14, fontweight='bold')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📥 Downloading confusion matrix...")
files.download('confusion_matrix.png')

print("\n✅ ALL DONE! Check your downloads folder for:")
print("   - model_metrics.txt (contains all metrics)")
print("   - confusion_matrix.png (visualization)")


