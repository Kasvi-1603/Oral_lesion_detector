# 🚀 EASY WAY: Get Real Metrics Using Google Colab (NO LOCAL STORAGE NEEDED!)

## ✅ This Method:
- **Uses Google Colab** (free cloud computing)
- **Dataset stays in Google Drive** (no download to your PC!)
- **Takes 5-10 minutes total**
- **You get real metrics!**

---

## 📋 Step-by-Step (Super Easy!)

### Step 1: Go to Google Colab
1. Open: https://colab.research.google.com/
2. Sign in with your Google account
3. Click: **File > New Notebook**

---

### Step 2: Copy the Script
1. Open `backend/colab_evaluation.py` in this project
2. **Copy the ENTIRE contents** (Ctrl+A, Ctrl+C)
3. **Paste** into the Colab notebook cell

---

### Step 3: Run It!
1. Click the ▶️ **Play button** (or press Shift+Enter)
2. When prompted:
   - **Mount Google Drive**: Click "Connect to Google Drive" → Allow access
   - **Upload model**: Choose `backend/models/oral_lesion_model.h5` from your computer
3. Wait 5-10 minutes while it processes...

---

### Step 4: Download Results
The script will automatically download 2 files:
1. **`model_metrics.txt`** - All your real metrics in text format
2. **`confusion_matrix.png`** - Visual chart

---

## 🔧 Important: Update Dataset Path

In the script, around line 32, you'll see:
```python
DATASET_PATH = '/content/drive/MyDrive/Oral Images Dataset'
```

**Change this** to match where your dataset is in Google Drive!

To find the correct path:
1. After mounting Drive in Colab
2. Click the 📁 folder icon on the left
3. Navigate to your dataset folder
4. Right-click → "Copy path"
5. Paste that path in the script

---

## 📊 What You'll Get

### In `model_metrics.txt`:
```
ORAL LESION MODEL - PERFORMANCE METRICS
==================================================

Performance Metrics:
- Accuracy: XX.X%
- Precision: XX.X%
- Sensitivity: XX.X%
- Specificity: XX.X%
- F1-Score: XX.X%

FOR README.md:
[Ready-to-paste markdown format]

FOR ForDentists.js:
[Ready-to-paste HTML format]
```

### Plus:
- Confusion matrix PNG image
- Ready-to-use formats for README and ForDentists.js

---

## 🎯 After Getting Results

1. **Open `model_metrics.txt`** (downloaded file)
2. **Copy the metrics**
3. **Update your project:**
   - `README.md` - Paste the README section
   - `frontend/oral-lesion-ui/src/pages/ForDentists.js` - Paste the HTML section (lines 64-67)
4. **Commit to GitHub**

---

## ⚠️ Troubleshooting

**Error: "Directory not found"**
→ Fix the `DATASET_PATH` (see step above)

**Error: "Model file not found"**
→ Make sure you uploaded the .h5 file when prompted

**"Out of memory" error**
→ In Colab: Runtime > Change runtime type > GPU

---

## ✨ That's It!

**Total time: 10 minutes**  
**Storage needed on your PC: 0 MB** (just the model file ~8MB)  
**Cost: $0** (Google Colab is free!)

---

**Questions?** The script has comments explaining each step!


