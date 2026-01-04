# Oral Lesion Classifier - Backend API

FastAPI backend for detecting and classifying oral lesions using deep learning.

## 🚀 Features

- **Image Upload & Processing**: Accepts oral cavity images (JPEG, PNG)
- **ML Model Inference**: Classifies lesions using pre-trained CNN model
- **RESTful API**: Clean, documented endpoints
- **Batch Prediction**: Process multiple images at once
- **Error Handling**: Comprehensive validation and error responses
- **CORS Support**: Ready for frontend integration
- **Auto Documentation**: Swagger UI and ReDoc included

## 📋 Prerequisites

- Python 3.8+
- pip
- (Optional) Virtual environment

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Kasvi-1603/Oral_lesion_detector_backend.git
cd Oral_lesion_detector_backend
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
# Copy example env file
cp .env.example .env

# Edit .env with your settings
```

5. **Add your trained model**
```bash
# Create models directory
mkdir models

# Place your trained model file here
# models/oral_lesion_model.h5
```

## 🚀 Running the API

### Development Mode
```bash
python main.py
```

or

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📡 API Endpoints

### Health Check
```http
GET /
GET /health
```

### Get Available Classes
```http
GET /classes
```

### Single Image Prediction
```http
POST /predict
Content-Type: multipart/form-data

file: <image_file>
```

**Response:**
```json
{
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
```

### Batch Prediction
```http
POST /batch-predict
Content-Type: multipart/form-data

files: <image_file_1>
files: <image_file_2>
...
```

## 🧪 Testing the API

### Using cURL
```bash
# Health check
curl http://localhost:8000/health

# Predict single image
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/image.jpg"
```

### Using Python
```python
import requests

# Predict
url = "http://localhost:8000/predict"
files = {"file": open("test_image.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

### Using Postman
1. Open Postman
2. Create POST request to `http://localhost:8000/predict`
3. Select Body → form-data
4. Add key `file` (type: File)
5. Upload an image
6. Send request

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py              # Configuration settings
│   ├── models/
│   │   ├── __init__.py
│   │   └── response_models.py     # Pydantic response models
│   └── services/
│       ├── __init__.py
│       ├── image_processor.py     # Image preprocessing
│       └── model_service.py       # ML model inference
├── models/
│   └── oral_lesion_model.h5       # Trained model (you need to add this)
├── main.py                         # FastAPI application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore
└── README.md
```

## 🔧 Configuration

Edit `app/core/config.py` or `.env` file:

```python
# API Settings
HOST = "0.0.0.0"
PORT = 8000
DEBUG = True

# Model Settings
MODEL_PATH = "models/oral_lesion_model.h5"
MODEL_TYPE = "tensorflow"

# Image Processing
IMAGE_SIZE = (224, 224)

# Class Names (Update based on your model)
CLASS_NAMES = [
    "Normal",
    "Leukoplakia",
    "Erythroplakia",
    "Ulcer",
    "Oral Squamous Cell Carcinoma"
]
```

## 🧠 Adding Your Trained Model

1. Train your model (Person 1's responsibility)
2. Export model as `.h5` file
3. Place in `models/` directory
4. Update `MODEL_PATH` in config if needed
5. Update `CLASS_NAMES` to match your model's classes

**Model Requirements:**
- Input shape: (batch_size, 224, 224, 3)
- Output: Softmax probabilities for each class
- Format: TensorFlow/Keras `.h5` file

## 🛡️ Error Handling

The API handles various error cases:
- Invalid file types
- Corrupted images
- Model not loaded
- Processing errors
- File size limits

## 🔒 Security Considerations

⚠️ **Medical Disclaimer Required:**
```
This tool is intended for educational and research purposes only 
and should not be used as a substitute for professional medical diagnosis.
```

## 📝 API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs (Interactive testing)
- **ReDoc**: http://localhost:8000/redoc (Clean documentation)

## 🤝 Integration with Frontend

Frontend can make API calls like:

```javascript
const formData = new FormData();
formData.append('file', imageFile);

const response = await fetch('http://localhost:8000/predict', {
  method: 'POST',
  body: formData
});

const result = await response.json();
console.log(result.prediction, result.confidence);
```

## 🐛 Troubleshooting

**Model not found?**
- The API will use a dummy model for testing
- Add your actual trained model to `models/` directory

**CORS errors?**
- Update `ALLOWED_ORIGINS` in `config.py`
- Add your frontend URL

**Image processing errors?**
- Check image format (JPEG, PNG, JPG)
- Verify image is not corrupted
- Check image dimensions (min 32x32, max 4096x4096)

## 📚 Technologies Used

- **FastAPI**: Modern web framework
- **TensorFlow**: ML model inference
- **Pillow & OpenCV**: Image processing
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server

## 👥 Team

**Backend Developer (Person 2)**
- API Development: FastAPI implementation
- Image Processing: Preprocessing pipeline
- Model Integration: Inference service
- Documentation: API docs and README

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

- Dataset providers
- Medical imaging community
- Open source ML frameworks

