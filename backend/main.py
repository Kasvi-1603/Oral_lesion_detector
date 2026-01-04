from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from typing import Dict
import logging

from app.services.image_processor import ImageProcessor
from app.services.model_service import ModelService
from app.models.response_models import PredictionResponse, HealthResponse
from app.core.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Oral Lesion Classifier API",
    description="API for detecting and classifying oral lesions using deep learning",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
image_processor = ImageProcessor()
model_service = ModelService()


@app.on_event("startup")
async def startup_event():
    """Load ML model on startup"""
    logger.info("Starting up Oral Lesion Classifier API...")
    try:
        model_service.load_model()
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")


@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint - API health check"""
    return HealthResponse(
        status="healthy",
        message="Oral Lesion Classifier API is running",
        version="1.0.0"
    )


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    model_loaded = model_service.is_model_loaded()
    return HealthResponse(
        status="healthy" if model_loaded else "degraded",
        message="Model loaded" if model_loaded else "Model not loaded",
        version="1.0.0"
    )


@app.post("/predict", response_model=PredictionResponse)
async def predict_lesion(file: UploadFile = File(...)):
    """
    Predict oral lesion type from uploaded image
    
    Args:
        file: Uploaded image file (JPEG, PNG, JPG)
    
    Returns:
        PredictionResponse with prediction, confidence, and class probabilities
    """
    try:
        # Validate file type
        if not file.content_type.startswith("image/"):
            raise HTTPException(
                status_code=400,
                detail="Invalid file type. Please upload an image file (JPEG, PNG, JPG)"
            )
        
        # Read image file
        contents = await file.read()
        logger.info(f"Received image: {file.filename}, size: {len(contents)} bytes")
        
        # Process image
        processed_image = image_processor.process_image(contents)
        
        # Get prediction from model
        prediction_result = model_service.predict(processed_image)
        
        logger.info(f"Prediction: {prediction_result['prediction']} with confidence {prediction_result['confidence']:.2f}")
        
        return PredictionResponse(**prediction_result)
    
    except ValueError as ve:
        logger.error(f"Validation error: {str(ve)}")
        raise HTTPException(status_code=400, detail=str(ve))
    
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )


@app.post("/batch-predict")
async def batch_predict(files: list[UploadFile] = File(...)):
    """
    Predict multiple oral lesion images at once
    
    Args:
        files: List of uploaded image files
    
    Returns:
        List of predictions for each image
    """
    try:
        if len(files) > 10:
            raise HTTPException(
                status_code=400,
                detail="Maximum 10 images allowed per batch"
            )
        
        results = []
        
        for file in files:
            if not file.content_type.startswith("image/"):
                results.append({
                    "filename": file.filename,
                    "error": "Invalid file type"
                })
                continue
            
            try:
                contents = await file.read()
                processed_image = image_processor.process_image(contents)
                prediction_result = model_service.predict(processed_image)
                
                results.append({
                    "filename": file.filename,
                    **prediction_result
                })
            except Exception as e:
                results.append({
                    "filename": file.filename,
                    "error": str(e)
                })
        
        return JSONResponse(content={"results": results})
    
    except Exception as e:
        logger.error(f"Error during batch prediction: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing batch: {str(e)}"
        )


@app.get("/classes")
async def get_classes():
    """Get available lesion classes"""
    return {
        "classes": settings.CLASS_NAMES,
        "num_classes": len(settings.CLASS_NAMES)
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

