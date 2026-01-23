"""
Oral Lesion Model Training Script
Uses EfficientNetB0 with Transfer Learning for better accuracy
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# ============== CONFIGURATION ==============
# Update this path to your dataset folder
DATASET_PATH = r"C:\Users\sh\Downloads\sem 3\dtl el\dataset"  # <-- UPDATE THIS!

# Or if your data is already split:
# TRAIN_PATH = r"path\to\train"
# VAL_PATH = r"path\to\val"

IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 50
LEARNING_RATE = 0.0001

# Output model path
OUTPUT_MODEL_PATH = "models/oral_lesion_model_new.h5"


def check_gpu():
    """Check if GPU is available"""
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"✅ GPU detected: {gpus}")
        # Enable memory growth to avoid OOM
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        return True
    else:
        print("⚠️ No GPU detected. Training will be slower on CPU.")
        return False


def create_data_generators(dataset_path):
    """Create training and validation data generators with augmentation"""
    
    # Heavy augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.3,
        horizontal_flip=True,
        vertical_flip=True,
        brightness_range=[0.8, 1.2],
        fill_mode='nearest',
        validation_split=0.2  # 80% train, 20% validation
    )
    
    # No augmentation for validation (just rescale)
    val_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    
    print(f"\n📂 Loading dataset from: {dataset_path}")
    
    # Training generator
    train_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary',
        subset='training',
        shuffle=True
    )
    
    # Validation generator
    val_generator = val_datagen.flow_from_directory(
        dataset_path,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary',
        subset='validation',
        shuffle=False
    )
    
    print(f"\n📊 Dataset Summary:")
    print(f"   Training samples: {train_generator.samples}")
    print(f"   Validation samples: {val_generator.samples}")
    print(f"   Classes: {train_generator.class_indices}")
    
    return train_generator, val_generator


def build_model():
    """Build EfficientNetB0 model with transfer learning"""
    
    print("\n🏗️ Building EfficientNetB0 model...")
    
    # Load pre-trained EfficientNetB0 (without top layer)
    base_model = EfficientNetB0(
        weights='imagenet',
        include_top=False,
        input_shape=(*IMG_SIZE, 3)
    )
    
    # Freeze base model layers initially
    base_model.trainable = False
    
    # Add custom classification head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.3)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.3)(x)
    output = Dense(1, activation='sigmoid')(x)  # Binary classification
    
    model = Model(inputs=base_model.input, outputs=output)
    
    # Compile model
    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    print(f"   Total layers: {len(model.layers)}")
    print(f"   Trainable params: {model.count_params():,}")
    
    return model, base_model


def train_model(model, base_model, train_gen, val_gen):
    """Train the model with callbacks"""
    
    # Callbacks
    callbacks = [
        EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            min_lr=1e-7,
            verbose=1
        ),
        ModelCheckpoint(
            OUTPUT_MODEL_PATH,
            monitor='val_accuracy',
            save_best_only=True,
            verbose=1
        )
    ]
    
    # Phase 1: Train only the top layers
    print("\n" + "="*50)
    print("📈 PHASE 1: Training top layers (base frozen)")
    print("="*50)
    
    history1 = model.fit(
        train_gen,
        epochs=15,
        validation_data=val_gen,
        callbacks=callbacks,
        verbose=1
    )
    
    # Phase 2: Fine-tune the entire model
    print("\n" + "="*50)
    print("📈 PHASE 2: Fine-tuning entire model")
    print("="*50)
    
    # Unfreeze base model
    base_model.trainable = True
    
    # Recompile with lower learning rate
    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE / 10),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    history2 = model.fit(
        train_gen,
        epochs=EPOCHS - 15,
        initial_epoch=15,
        validation_data=val_gen,
        callbacks=callbacks,
        verbose=1
    )
    
    return history1, history2


def plot_training_history(history1, history2):
    """Plot training curves"""
    
    # Combine histories
    acc = history1.history['accuracy'] + history2.history['accuracy']
    val_acc = history1.history['val_accuracy'] + history2.history['val_accuracy']
    loss = history1.history['loss'] + history2.history['loss']
    val_loss = history1.history['val_loss'] + history2.history['val_loss']
    
    epochs_range = range(1, len(acc) + 1)
    
    plt.figure(figsize=(12, 4))
    
    # Accuracy plot
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, 'b-', label='Training Accuracy')
    plt.plot(epochs_range, val_acc, 'r-', label='Validation Accuracy')
    plt.axvline(x=15, color='g', linestyle='--', label='Fine-tuning starts')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    
    # Loss plot
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, 'b-', label='Training Loss')
    plt.plot(epochs_range, val_loss, 'r-', label='Validation Loss')
    plt.axvline(x=15, color='g', linestyle='--', label='Fine-tuning starts')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('training_history.png')
    print("\n📊 Training curves saved to 'training_history.png'")


def main():
    print("="*60)
    print("🦷 ORAL LESION MODEL TRAINING")
    print("   Using EfficientNetB0 with Transfer Learning")
    print("="*60)
    
    # Check GPU
    check_gpu()
    
    # Check if dataset path exists
    if not os.path.exists(DATASET_PATH):
        print(f"\n❌ ERROR: Dataset not found at: {DATASET_PATH}")
        print("\n📝 Please update DATASET_PATH in this script to point to your dataset.")
        print("   Your dataset folder should have this structure:")
        print("   dataset/")
        print("   ├── benign_lesions/    (or 'Benign')")
        print("   │   ├── image1.jpg")
        print("   │   └── ...")
        print("   └── malignant_lesions/ (or 'Malignant')")
        print("       ├── image1.jpg")
        print("       └── ...")
        return
    
    # Create output directory
    os.makedirs(os.path.dirname(OUTPUT_MODEL_PATH), exist_ok=True)
    
    # Create data generators
    train_gen, val_gen = create_data_generators(DATASET_PATH)
    
    # Build model
    model, base_model = build_model()
    
    # Train
    history1, history2 = train_model(model, base_model, train_gen, val_gen)
    
    # Plot training history
    try:
        plot_training_history(history1, history2)
    except Exception as e:
        print(f"⚠️ Could not plot training history: {e}")
    
    # Final evaluation
    print("\n" + "="*50)
    print("📊 FINAL EVALUATION")
    print("="*50)
    
    val_loss, val_acc = model.evaluate(val_gen, verbose=0)
    print(f"   Validation Loss: {val_loss:.4f}")
    print(f"   Validation Accuracy: {val_acc:.2%}")
    
    print(f"\n✅ Model saved to: {OUTPUT_MODEL_PATH}")
    print("\n🔄 To use this model, replace the old one:")
    print(f"   1. Backup: models/oral_lesion_model.h5")
    print(f"   2. Rename: {OUTPUT_MODEL_PATH} → models/oral_lesion_model.h5")
    print("   3. Restart backend server")


if __name__ == "__main__":
    main()

