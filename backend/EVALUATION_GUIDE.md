# 📊 Model Evaluation Guide

## Get Real Performance Metrics for Your Model

This guide will help you calculate the **actual performance metrics** of your oral lesion classification model.

---

## 📥 Step 1: Download the Dataset

1. **Download from Google Drive**: 
   - Link: https://drive.google.com/drive/folders/1nQFdnnYRoBaTzQRuDGHs77ribOfMz8R3?usp=drive_link
   - Download the "Oral Images Dataset" folder

2. **Extract the dataset** to your computer

---

## 📁 Step 2: Organize the Dataset

Organize your downloaded dataset in the `backend/` folder like this:

```
backend/
├── test_data/
│   ├── Benign/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ... (all benign images)
│   └── Malignant/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── ... (all malignant images)
├── models/
│   └── oral_lesion_model.h5
└── evaluate_model.py
```

**Important:**
- Create a folder called `test_data` in the `backend/` directory
- Inside `test_data`, create two folders: `Benign` and `Malignant`
- Put all benign/normal images in the `Benign` folder
- Put all malignant/cancerous images in the `Malignant` folder

---

## 🔧 Step 3: Install Required Dependencies

If not already installed, you need these packages:

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
venv\Scripts\activate

# Install evaluation dependencies
pip install scikit-learn matplotlib seaborn
```

---

## ▶️ Step 4: Run the Evaluation

```bash
# Make sure you're in backend/ directory with venv activated
python evaluate_model.py
```

---

## 📊 Step 5: Review Results

The script will output:

### 1. **Console Output**
- Confusion Matrix (TP, TN, FP, FN)
- Accuracy, Precision, Sensitivity, Specificity, F1-Score
- Clinical interpretation
- LaTeX format (for papers)
- Markdown format (for README)

### 2. **Confusion Matrix Image**
- Saved as `confusion_matrix.png` in backend directory
- Visual representation of model performance

---

## 📝 Step 6: Update Your Documentation

After getting real metrics, update these files:

### Update `README.md`
Add the metrics in the "Features" or "Model Performance" section

### Update `frontend/oral-lesion-ui/src/pages/ForDentists.js`
Replace placeholder metrics (lines 64-67) with real values:

```javascript
<div className="highlight-box">
  <h3>Model Performance Metrics</h3>
  <ul>
    <li>Overall Accuracy: <strong>XX.X%</strong></li>
    <li>Sensitivity: <strong>XX.X%</strong></li>
    <li>Specificity: <strong>XX.X%</strong></li>
    <li>Training Dataset: <strong>XXXX images</strong></li>
  </ul>
</div>
```

---

## 🎯 Understanding the Metrics

| Metric | What It Means | Why It Matters |
|--------|---------------|----------------|
| **Accuracy** | Overall correctness | General performance indicator |
| **Sensitivity** | How many cancers we catch | **CRITICAL** - Don't miss cancers! |
| **Specificity** | How many benign correctly identified | Reduces unnecessary biopsies |
| **Precision** | When we say "cancer", how often correct? | Confidence in positive predictions |
| **F1-Score** | Balance of precision & sensitivity | Overall model quality |

### For Medical AI:
- **High Sensitivity (>90%)** is CRITICAL - you don't want to miss cancers!
- **High Specificity (>85%)** is important - reduces false alarms
- **Balance** between both is ideal

---

## ⚠️ Troubleshooting

### Error: "Test data directory not found"
- Make sure you created `backend/test_data/` folder
- Check that it contains `Benign/` and `Malignant/` subfolders

### Error: "Found 0 images"
- Ensure images are in the correct folders
- Check that images are in supported formats (.jpg, .jpeg, .png)
- Make sure folder names are exactly "Benign" and "Malignant"

### Error: "Model not found"
- Ensure `oral_lesion_model.h5` exists in `backend/models/`

---

## 📧 Questions?

If you encounter any issues:
1. Check the error message carefully
2. Verify folder structure matches the guide
3. Ensure all dependencies are installed

---

**Good luck with your evaluation!** 🎉


