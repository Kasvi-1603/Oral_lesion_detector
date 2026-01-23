"""
Semi-Automated Dataset Setup
This script helps you organize your downloaded dataset quickly
"""

import os
import shutil
from pathlib import Path

def setup_test_data():
    """Help organize the test dataset"""
    
    print("="*70)
    print("🔧 DATASET SETUP ASSISTANT")
    print("="*70)
    
    # Check if test_data exists
    test_data_path = Path("test_data")
    if not test_data_path.exists():
        print("\n📁 Creating 'test_data' directory...")
        test_data_path.mkdir(exist_ok=True)
        print("   ✅ Created!")
    else:
        print("\n✅ 'test_data' directory already exists")
    
    # Create Benign folder
    benign_path = test_data_path / "Benign"
    if not benign_path.exists():
        print("📁 Creating 'Benign' folder...")
        benign_path.mkdir(exist_ok=True)
        print("   ✅ Created!")
    else:
        print("✅ 'Benign' folder already exists")
    
    # Create Malignant folder
    malignant_path = test_data_path / "Malignant"
    if not malignant_path.exists():
        print("📁 Creating 'Malignant' folder...")
        malignant_path.mkdir(exist_ok=True)
        print("   ✅ Created!")
    else:
        print("✅ 'Malignant' folder already exists")
    
    print("\n" + "="*70)
    print("✅ Folder structure created!")
    print("="*70)
    
    print("\n📥 NOW YOU NEED TO:")
    print("\n1. Download dataset from:")
    print("   https://drive.google.com/drive/folders/1nQFdnnYRoBaTzQRuDGHs77ribOfMz8R3")
    
    print("\n2. Extract the downloaded folder")
    
    print("\n3. Copy images to the correct folders:")
    print(f"   - Benign images → backend/test_data/Benign/")
    print(f"   - Malignant images → backend/test_data/Malignant/")
    
    print("\n4. After copying, run:")
    print("   python check_dataset.py")
    
    print("\n5. Then run evaluation:")
    print("   python evaluate_model.py")
    
    print("\n" + "="*70)
    
    # Show absolute paths to make it easier
    abs_benign = benign_path.absolute()
    abs_malignant = malignant_path.absolute()
    
    print("\n📂 Absolute paths (for copy-paste):")
    print(f"\n   Benign folder:")
    print(f"   {abs_benign}")
    print(f"\n   Malignant folder:")
    print(f"   {abs_malignant}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    setup_test_data()


