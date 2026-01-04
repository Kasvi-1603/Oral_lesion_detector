import numpy as np
import logging
import os
from typing import Dict, Optional
import tensorflow as tf

from app.core.config import settings

logger = logging.getLogger(__name__)


class ModelService:
    """Handles ML model loading and inference"""
    
    def __init__(self):
        self.model: Optional[tf.keras.Model] = None
        self.class_names = settings.CLASS_NAMES
        self.model_path = settings.MODEL_PATH
    
    def load_model(self) -> None:
        """Load the trained ML model"""
        try:
            if not os.path.exists(self.model_path):
                logger.warning(f"Model file not found at {self.model_path}")
                logger.warning("Using dummy model for testing. Please place your trained model at the specified path.")
                self._create_dummy_model()
                return
            
            logger.info(f"Loading model from {self.model_path}")
            
            # Load TensorFlow/Keras model
            if settings.MODEL_TYPE == "tensorflow":
                # Load with compile=False to avoid compatibility issues
                self.model = tf.keras.models.load_model(self.model_path, compile=False)
                
                # Recompile the model
                self.model.compile(
                    optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy']
                )
                logger.info(f"Model loaded and compiled successfully")
                logger.info(f"Model input shape: {self.model.input_shape}")
                logger.info(f"Model output shape: {self.model.output_shape}")
            
            # Add support for PyTorch models if needed
            elif settings.MODEL_TYPE == "pytorch":
                # import torch
                # self.model = torch.load(self.model_path)
                raise NotImplementedError("PyTorch model loading not yet implemented")
            
            # Add support for ONNX models if needed
            elif settings.MODEL_TYPE == "onnx":
                # import onnxruntime as ort
                # self.model = ort.InferenceSession(self.model_path)
                raise NotImplementedError("ONNX model loading not yet implemented")
            
            else:
                raise ValueError(f"Unsupported model type: {settings.MODEL_TYPE}")
        
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            logger.warning("Creating dummy model for testing")
            self._create_dummy_model()
    
    def _create_dummy_model(self) -> None:
        """Create a dummy model for testing when actual model is not available"""
        logger.info("Creating dummy model for testing purposes")
        
        # Simple dummy model that outputs random predictions
        input_layer = tf.keras.layers.Input(shape=(*settings.IMAGE_SIZE, settings.IMAGE_CHANNELS))
        x = tf.keras.layers.GlobalAveragePooling2D()(input_layer)
        output_layer = tf.keras.layers.Dense(len(self.class_names), activation='softmax')(x)
        
        self.model = tf.keras.Model(inputs=input_layer, outputs=output_layer)
        logger.info("Dummy model created")
    
    def is_model_loaded(self) -> bool:
        """Check if model is loaded"""
        return self.model is not None
    
    def predict(self, image_array: np.ndarray) -> Dict[str, any]:
        """
        Make prediction on preprocessed image
        
        Args:
            image_array: Preprocessed image array (batch_size, height, width, channels)
        
        Returns:
            Dictionary containing prediction, confidence, and probabilities
        """
        try:
            if self.model is None:
                raise RuntimeError("Model not loaded. Please load the model first.")
            
            # Make prediction
            predictions = self.model.predict(image_array, verbose=0)
            
            # Check if binary classification (output shape is (1,) or (1, 1))
            if predictions.shape[-1] == 1 or len(predictions.shape) == 2 and predictions.shape[1] == 1:
                # Binary classification model (Benign vs Malignant)
                malignant_prob = float(predictions[0][0] if len(predictions.shape) > 1 else predictions[0])
                benign_prob = 1.0 - malignant_prob
                
                # Determine predicted class
                if malignant_prob > 0.5:
                    predicted_class = "Malignant"
                    confidence = malignant_prob
                else:
                    predicted_class = "Benign"
                    confidence = benign_prob
                
                # Binary classification probabilities
                class_probabilities = {
                    "Benign": benign_prob,
                    "Malignant": malignant_prob
                }
                
                logger.info(f"Binary prediction: {predicted_class} ({confidence:.2%})")
            
            else:
                # Multi-class classification model
                probabilities = predictions[0]
                
                # Get predicted class index
                predicted_idx = np.argmax(probabilities)
                
                # Get predicted class name
                predicted_class = self.class_names[predicted_idx]
                
                # Get confidence score
                confidence = float(probabilities[predicted_idx])
                
                # Create probabilities dictionary
                class_probabilities = {
                    class_name: float(prob)
                    for class_name, prob in zip(self.class_names, probabilities)
                }
                
                logger.info(f"Multi-class prediction: {predicted_class} ({confidence:.2%})")
            
            return {
                "prediction": predicted_class,
                "confidence": confidence,
                "probabilities": class_probabilities
            }
        
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise RuntimeError(f"Prediction failed: {str(e)}")
    
    def get_model_info(self) -> Dict[str, any]:
        """Get information about the loaded model"""
        if self.model is None:
            return {"status": "not_loaded"}
        
        return {
            "status": "loaded",
            "input_shape": self.model.input_shape,
            "output_shape": self.model.output_shape,
            "num_classes": len(self.class_names),
            "classes": self.class_names
        }

