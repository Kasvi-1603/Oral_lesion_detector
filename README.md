# 🦷 Oral Lesion Classifier

AI-powered web application for binary classification of oral lesions using deep learning.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-green)
![React](https://img.shields.io/badge/React-18.0-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20.0-orange)

---

## 📋 Overview

This is a full-stack machine learning application that performs **binary classification** of oral lesion images. The system classifies images as either:
- **Benign** (non-cancerous)
- **Malignant** (cancerous)

The project demonstrates practical integration of deep learning models in web applications using modern technologies.

---

## 🔬 Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **TensorFlow/Keras** - Deep learning model
- **Python 3.10+** - Programming language
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **React Router** - Navigation
- **Modern CSS** - Styling

### AI Model
- **Binary CNN Classifier** - TensorFlow/Keras model
- Image size: 224×224 pixels
- Output: Benign/Malignant classification

---

## 📁 Project Structure

```
Oral-Lesion-Classifier/
├── backend/
│   ├── app/
│   │   ├── core/           # Configuration
│   │   ├── models/         # Response models
│   │   └── services/       # Business logic
│   ├── models/             # ML model files
│   ├── main.py             # FastAPI entry point
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── oral-lesion-ui/
│       ├── src/
│       │   ├── components/ # Reusable components
│       │   ├── pages/      # Page components
│       │   └── services/   # API integration
│       └── package.json    # Node dependencies
└── README.md
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Node.js 16+ and npm
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Oral-Lesion-Classifier.git
cd Oral-Lesion-Classifier
```

### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**✅ ML Model Included**

The trained model file (`oral_lesion_model.h5`) is included in the repository at `backend/models/oral_lesion_model.h5`. No additional download required!

### 3. Frontend Setup

```bash
# Navigate to frontend (from root)
cd frontend/oral-lesion-ui

# Install dependencies
npm install
```

---

## ▶️ Running the Application

### Start Backend Server

```bash
# From backend/ directory with venv activated
python main.py
```

Backend will run on: `http://localhost:8888`

API Documentation: `http://localhost:8888/docs`

### Start Frontend Server

```bash
# From frontend/oral-lesion-ui/ directory
npm start
```

Frontend will run on: `http://localhost:3000` (or next available port)

---

## 🎯 Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Click "Get Started" or "Predict" in the navigation
3. Upload an oral lesion image (JPEG/PNG)
4. Click "Analyze Image"
5. View the binary classification result (Benign/Malignant) with confidence score

---

## 📊 Features

- ✅ Real-time binary image classification
- ✅ RESTful API with FastAPI
- ✅ Multi-page React application
- ✅ Responsive design
- ✅ Confidence score visualization
- ✅ Professional UI/UX
- ✅ Interactive API documentation (Swagger)

---

## 🎓 Project Objectives

This academic project demonstrates:
1. Full-stack ML application development
2. Integration of TensorFlow models with web APIs
3. Modern frontend-backend architecture
4. REST API design and implementation
5. Responsive web interface design

---

## 🔮 Future Enhancements

- Multi-class classification for specific lesion types
- Model explainability (Grad-CAM visualization)
- User authentication and history tracking
- Mobile application development
- Clinical validation and testing
- Real-time model training feedback

---

## 👥 Team

- **Person 1** - ML Model Training & Data Processing
- **Person 2** - Backend Development & API Integration
- **Person 3** - Frontend Development & UI/UX
- **Person 4** - Testing, Integration & Documentation

---

## ⚠️ Disclaimer

**This is an educational project developed for academic purposes only.**

- Not FDA-approved or clinically validated
- Not intended for actual medical diagnosis
- Should not replace professional medical advice
- Always consult qualified healthcare professionals for medical diagnosis

---

## 📝 License

This project is developed for educational purposes as part of academic coursework.

---

## 🐛 Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Windows - Kill process on port 8888
netstat -ano | findstr :8888
taskkill /PID <PID> /F
```

**Module not found:**
```bash
pip install -r requirements.txt
```

### Frontend Issues

**Port already in use:**
```bash
# Set custom port (Windows PowerShell)
$env:PORT=3001; npm start
```

**npm command not found:**
- Ensure Node.js is installed
- Add Node.js to system PATH

---

## 📞 Contact

For questions or issues, please contact:
- Email: your.email@example.com
- GitHub Issues: [Link to your repo issues]

---

## 🙏 Acknowledgments

- TensorFlow/Keras team for the deep learning framework
- FastAPI developers for the excellent web framework
- React team for the frontend library
- Our academic advisors and mentors

---

**⭐ If you find this project helpful, please give it a star!**

