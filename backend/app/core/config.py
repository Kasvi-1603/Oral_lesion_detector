from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings and configuration"""
    
    # API Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # CORS Settings
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
        "http://localhost:3003",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3002",
        "http://127.0.0.1:3003",
    ]
    
    # Model Settings
    MODEL_PATH: str = os.path.join("models", "oral_lesion_model.h5")
    MODEL_TYPE: str = "tensorflow"  # tensorflow, pytorch, onnx
    
    # Image Processing Settings
    IMAGE_SIZE: tuple = (224, 224)
    IMAGE_CHANNELS: int = 3
    
    # Class Names (Update these based on your actual classes)
    CLASS_NAMES: List[str] = [
        "Normal",
        "Leukoplakia",
        "Erythroplakia",
        "Ulcer",
        "Oral Squamous Cell Carcinoma"
    ]
    
    # Preprocessing Settings
    NORMALIZE_MEAN: List[float] = [0.485, 0.456, 0.406]  # ImageNet means
    NORMALIZE_STD: List[float] = [0.229, 0.224, 0.225]   # ImageNet stds
    
    # File Upload Settings
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: List[str] = ["jpg", "jpeg", "png"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

