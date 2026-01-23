# 🚀 Quick Start Guide - Run in CMD

## First Time Setup (Only Once)

### 1. Backend Setup
```cmd
cd /d "C:\Users\sh\Downloads\sem 3\dtl el\Oral-Lesion-Classifier\backend"
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Frontend Setup
```cmd
cd /d "C:\Users\sh\Downloads\sem 3\dtl el\Oral-Lesion-Classifier\frontend\oral-lesion-ui"
npm install
```

---

## Every Time You Run (Quick Commands)

### Open 2 CMD Windows

**CMD Window 1 - Backend:**
```cmd
cd /d "C:\Users\sh\Downloads\sem 3\dtl el\Oral-Lesion-Classifier\backend"
venv\Scripts\activate
python main.py
```
✅ Backend runs on: `http://localhost:8000`

**CMD Window 2 - Frontend:**
```cmd
cd /d "C:\Users\sh\Downloads\sem 3\dtl el\Oral-Lesion-Classifier\frontend\oral-lesion-ui"
npm start
```
✅ Frontend opens automatically at: `http://localhost:3000`

---

## What You'll See

**Backend (CMD 1):**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
INFO:main:Model loaded successfully
```

**Frontend (CMD 2):**
```
Compiled successfully!
webpack compiled with 1 warning

You can now view oral-lesion-ui in the browser.
  Local:            http://localhost:3000
```

---

## Stop the Servers

Press `Ctrl + C` in each CMD window to stop the servers.

---

## Troubleshooting

### If Backend Port 8000 is Busy:
```cmd
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### If Frontend Port 3000 is Busy:
```cmd
set PORT=3001
npm start
```

### If Python Not Found:
Make sure you installed Python 3.11 and added it to PATH during installation.

### If npm Not Found:
Add Node.js to PATH:
1. Search "Environment Variables" in Windows
2. Edit PATH
3. Add: `C:\Program Files\nodejs\`

---

## Project Structure

```
Oral-Lesion-Classifier/
├── backend/
│   ├── venv/              # Python virtual environment (created by you)
│   ├── models/
│   │   └── oral_lesion_model.h5  # AI model (31MB)
│   ├── main.py           # FastAPI server
│   ├── requirements.txt  # Python dependencies
│   └── app/              # Backend code
├── frontend/
│   └── oral-lesion-ui/
│       ├── node_modules/ # npm packages (created by npm install)
│       ├── src/          # React code
│       ├── package.json  # npm dependencies
│       └── public/       # Static files
└── README.md            # Full documentation
```

---

## For Demo Day

1. Open 2 CMD windows
2. Run backend (CMD 1)
3. Run frontend (CMD 2)
4. Open browser to `http://localhost:3000`
5. Upload a test image
6. Show the binary classification results!

---

## GitHub Repository

Your code is saved at: `https://github.com/Kasvi-1603/Oral_lesion_detector`

To update GitHub after changes:
```cmd
cd /d "C:\Users\sh\Downloads\sem 3\dtl el\Oral-Lesion-Classifier"
git add .
git commit -m "Your message here"
git push
```

---

## Important Files

- **Backend Main:** `backend/main.py`
- **Frontend Main:** `frontend/oral-lesion-ui/src/App.js`
- **Analysis Page:** `frontend/oral-lesion-ui/src/pages/Analysis.js`
- **AI Model:** `backend/models/oral_lesion_model.h5`
- **API Config:** `frontend/oral-lesion-ui/src/services/api.js`

---

**Everything is saved! Just follow these commands next time you open the project! 🎉**



