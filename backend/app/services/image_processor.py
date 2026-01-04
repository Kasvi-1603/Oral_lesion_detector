import cv2
import numpy as np
from PIL import Image
import io
from typing import Union
import logging

from app.core.config import settings

logger = logging.getLogger(__name__)


class ImageProcessor:
    """Handles image preprocessing for model inference"""
    
    def __init__(self):
        self.image_size = settings.IMAGE_SIZE
        self.normalize_mean = np.array(settings.NORMALIZE_MEAN)
        self.normalize_std = np.array(settings.NORMALIZE_STD)
    
    def process_image(self, image_data: bytes) -> np.ndarray:
        """
        Process uploaded image for model inference
        
        Args:
            image_data: Raw image bytes
        
        Returns:
            Preprocessed image as numpy array ready for model inference
        """
        try:
            # Convert bytes to PIL Image
            image = Image.open(io.BytesIO(image_data))
            
            # Convert to RGB if needed (handles RGBA, grayscale, etc.)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Validate image
            self._validate_image(image)
            
            # Resize image
            image = image.resize(self.image_size, Image.Resampling.LANCZOS)
            
            # Convert to numpy array
            image_array = np.array(image, dtype=np.float32)
            
            # Normalize pixel values to [0, 1]
            image_array = image_array / 255.0
            
            # Apply ImageNet normalization (if using transfer learning)
            image_array = self._normalize(image_array)
            
            # Add batch dimension
            image_array = np.expand_dims(image_array, axis=0)
            
            logger.info(f"Image processed successfully. Shape: {image_array.shape}")
            
            return image_array
        
        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            raise ValueError(f"Failed to process image: {str(e)}")
    
    def _validate_image(self, image: Image.Image) -> None:
        """
        Validate image dimensions and format
        
        Args:
            image: PIL Image object
        
        Raises:
            ValueError: If image is invalid
        """
        # Check minimum dimensions
        if image.width < 32 or image.height < 32:
            raise ValueError("Image dimensions too small. Minimum size is 32x32 pixels")
        
        # Check maximum dimensions
        if image.width > 4096 or image.height > 4096:
            raise ValueError("Image dimensions too large. Maximum size is 4096x4096 pixels")
    
    def _normalize(self, image_array: np.ndarray) -> np.ndarray:
        """
        Apply ImageNet normalization
        
        Args:
            image_array: Image as numpy array with values in [0, 1]
        
        Returns:
            Normalized image array
        """
        # Normalize using ImageNet mean and std
        normalized = (image_array - self.normalize_mean) / self.normalize_std
        return normalized
    
    def denormalize(self, image_array: np.ndarray) -> np.ndarray:
        """
        Reverse normalization for visualization
        
        Args:
            image_array: Normalized image array
        
        Returns:
            Denormalized image array
        """
        denormalized = (image_array * self.normalize_std) + self.normalize_mean
        denormalized = np.clip(denormalized * 255, 0, 255).astype(np.uint8)
        return denormalized
    
    def apply_augmentation(self, image_array: np.ndarray) -> np.ndarray:
        """
        Apply data augmentation (for test-time augmentation if needed)
        
        Args:
            image_array: Input image array
        
        Returns:
            Augmented image array
        """
        # This can be used for test-time augmentation
        # Currently just returns the same image
        return image_array

