"""
Image processor tests
"""
import pytest
import numpy as np
from PIL import Image
import io

from app.services.image_processor import ImageProcessor


@pytest.fixture
def image_processor():
    return ImageProcessor()


def create_test_image(width=224, height=224, mode='RGB') -> bytes:
    """Create a test image"""
    img = Image.new(mode, (width, height), color='red')
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    return img_bytes.getvalue()


def test_process_image_valid(image_processor):
    """Test processing valid image"""
    image_data = create_test_image()
    result = image_processor.process_image(image_data)
    
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 224, 224, 3)
    assert result.dtype == np.float32


def test_process_image_rgba(image_processor):
    """Test processing RGBA image"""
    image_data = create_test_image(mode='RGBA')
    result = image_processor.process_image(image_data)
    
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 224, 224, 3)  # Should convert to RGB


def test_process_image_grayscale(image_processor):
    """Test processing grayscale image"""
    image_data = create_test_image(mode='L')
    result = image_processor.process_image(image_data)
    
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 224, 224, 3)  # Should convert to RGB


def test_process_image_too_small(image_processor):
    """Test processing image that's too small"""
    image_data = create_test_image(width=20, height=20)
    
    with pytest.raises(ValueError, match="too small"):
        image_processor.process_image(image_data)


def test_process_image_too_large(image_processor):
    """Test processing image that's too large"""
    image_data = create_test_image(width=5000, height=5000)
    
    with pytest.raises(ValueError, match="too large"):
        image_processor.process_image(image_data)


def test_process_image_invalid_data(image_processor):
    """Test processing invalid image data"""
    invalid_data = b"not an image"
    
    with pytest.raises(ValueError):
        image_processor.process_image(invalid_data)


def test_normalize(image_processor):
    """Test normalization"""
    test_array = np.ones((224, 224, 3), dtype=np.float32) * 0.5
    normalized = image_processor._normalize(test_array)
    
    assert isinstance(normalized, np.ndarray)
    assert normalized.shape == test_array.shape


def test_denormalize(image_processor):
    """Test denormalization"""
    test_array = np.zeros((224, 224, 3), dtype=np.float32)
    denormalized = image_processor.denormalize(test_array)
    
    assert isinstance(denormalized, np.ndarray)
    assert denormalized.dtype == np.uint8
    assert denormalized.shape == test_array.shape


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

