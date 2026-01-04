"""
API endpoint tests
Run with: pytest tests/
"""
import pytest
from fastapi.testclient import TestClient
from main import app
import io
from PIL import Image

client = TestClient(app)


def create_test_image() -> bytes:
    """Create a test image in memory"""
    img = Image.new('RGB', (224, 224), color='red')
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    return img_bytes.getvalue()


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()
    assert response.json()["status"] == "healthy"


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "message" in data
    assert "version" in data


def test_get_classes():
    """Test get classes endpoint"""
    response = client.get("/classes")
    assert response.status_code == 200
    data = response.json()
    assert "classes" in data
    assert "num_classes" in data
    assert isinstance(data["classes"], list)
    assert len(data["classes"]) > 0


def test_predict_endpoint_with_image():
    """Test prediction with valid image"""
    test_image = create_test_image()
    
    response = client.post(
        "/predict",
        files={"file": ("test.jpg", test_image, "image/jpeg")}
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Check response structure
    assert "prediction" in data
    assert "confidence" in data
    assert "probabilities" in data
    
    # Check data types
    assert isinstance(data["prediction"], str)
    assert isinstance(data["confidence"], float)
    assert isinstance(data["probabilities"], dict)
    
    # Check confidence range
    assert 0 <= data["confidence"] <= 1


def test_predict_endpoint_without_file():
    """Test prediction without file"""
    response = client.post("/predict")
    assert response.status_code == 422  # Unprocessable Entity


def test_predict_endpoint_with_invalid_file_type():
    """Test prediction with invalid file type"""
    response = client.post(
        "/predict",
        files={"file": ("test.txt", b"not an image", "text/plain")}
    )
    assert response.status_code == 400


def test_batch_predict_endpoint():
    """Test batch prediction"""
    test_image1 = create_test_image()
    test_image2 = create_test_image()
    
    response = client.post(
        "/batch-predict",
        files=[
            ("files", ("test1.jpg", test_image1, "image/jpeg")),
            ("files", ("test2.jpg", test_image2, "image/jpeg"))
        ]
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 2


def test_batch_predict_too_many_files():
    """Test batch prediction with too many files"""
    files = [
        ("files", (f"test{i}.jpg", create_test_image(), "image/jpeg"))
        for i in range(11)  # More than maximum (10)
    ]
    
    response = client.post("/batch-predict", files=files)
    assert response.status_code == 400


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

