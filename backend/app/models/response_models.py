from pydantic import BaseModel, Field
from typing import Dict, Optional


class HealthResponse(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="API status (healthy/degraded/unhealthy)")
    message: str = Field(..., description="Status message")
    version: str = Field(..., description="API version")


class PredictionResponse(BaseModel):
    """Prediction response model"""
    prediction: str = Field(..., description="Predicted lesion class")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Prediction confidence (0-1)")
    probabilities: Dict[str, float] = Field(..., description="Probability for each class")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prediction": "Leukoplakia",
                "confidence": 0.91,
                "probabilities": {
                    "Normal": 0.02,
                    "Leukoplakia": 0.91,
                    "Erythroplakia": 0.03,
                    "Ulcer": 0.02,
                    "Oral Squamous Cell Carcinoma": 0.02
                }
            }
        }


class ErrorResponse(BaseModel):
    """Error response model"""
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Additional error details")


