# Oral Lesion Classifier - Frontend

React frontend for the Oral Lesion Classifier project.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm start
```

The app will open at http://localhost:3000

## 🔗 Backend Connection

The frontend connects to the backend API at: **http://localhost:8001**

Make sure the backend is running before starting the frontend!

## 📁 Project Structure

```
oral-lesion-ui/
├── public/
│   └── index.html
├── src/
│   ├── App.js              # Main application component
│   ├── App.css             # Styles
│   ├── index.js            # Entry point
│   ├── components/
│   │   └── ImageUpload.js  # Image upload component
│   └── services/
│       └── api.js          # Backend API calls
└── package.json
```

## ✨ Features

- Image upload with preview
- Real-time prediction from backend
- Confidence scores display
- All class probabilities visualization
- Medical disclaimer
- Beautiful, responsive UI

## 🔧 Configuration

To change the backend API URL, edit `src/services/api.js`:

```javascript
const API_BASE_URL = 'http://localhost:8001';
```

## 📱 Usage

1. Start the backend API (port 8001)
2. Start the frontend (`npm start`)
3. Open http://localhost:3000
4. Upload an oral cavity image
5. View prediction results!

