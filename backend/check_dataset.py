"""
Quick Dataset Setup Helper
Checks if your test dataset is organized correctly
"""

import os
from pathlib import Path

def check_dataset_structure():
    """Check if test dataset is properly organized"""
    
    print("="*70)
    print("🔍 DATASET STRUCTURE CHECKER")
    print("="*70)
    
    test_data_path = Path("test_data")
    
    # Check if test_data directory exists
    if not test_data_path.exists():
        print("\n❌ 'test_data' directory not found!")
        print("\n📝 Please create the following structure:")
        print("\n   backend/")
        print("   ├── test_data/              ← CREATE THIS")
        print("   │   ├── Benign/             ← CREATE THIS")
        print("   │   │   └── (benign images)")
        print("   │   └── Malignant/          ← CREATE THIS")
        print("   │       └── (malignant images)")
        print("   ├── models/")
        print("   │   └── oral_lesion_model.h5")
        print("   └── evaluate_model.py")
        print("\n💡 Steps:")
        print("   1. Create 'test_data' folder in backend/")
        print("   2. Create 'Benign' and 'Malignant' folders inside test_data/")
        print("   3. Move your images to the correct folders")
        print("   4. Run this script again to verify")
        return False
    
    print("\n✅ 'test_data' directory found!")
    
    # Check for Benign folder
    benign_path = test_data_path / "Benign"
    malignant_path = test_data_path / "Malignant"
    
    issues = []
    
    if not benign_path.exists():
        issues.append("❌ 'Benign' folder not found in test_data/")
    else:
        benign_images = list(benign_path.glob("*.[jJ][pP][gG]")) + \
                        list(benign_path.glob("*.[jJ][pP][eE][gG]")) + \
                        list(benign_path.glob("*.[pP][nN][gG]"))
        if len(benign_images) == 0:
            issues.append("⚠️  'Benign' folder is empty!")
        else:
            print(f"✅ Found {len(benign_images)} benign images")
    
    if not malignant_path.exists():
        issues.append("❌ 'Malignant' folder not found in test_data/")
    else:
        malignant_images = list(malignant_path.glob("*.[jJ][pP][gG]")) + \
                           list(malignant_path.glob("*.[jJ][pP][eE][gG]")) + \
                           list(malignant_path.glob("*.[pP][nN][gG]"))
        if len(malignant_images) == 0:
            issues.append("⚠️  'Malignant' folder is empty!")
        else:
            print(f"✅ Found {len(malignant_images)} malignant images")
    
    if issues:
        print("\n⚠️  Issues found:")
        for issue in issues:
            print(f"   {issue}")
        return False
    
    # All checks passed
    total_images = len(benign_images) + len(malignant_images)
    print(f"\n🎉 Dataset structure is correct!")
    print(f"   Total test images: {total_images}")
    print(f"   - Benign: {len(benign_images)}")
    print(f"   - Malignant: {len(malignant_images)}")
    
    print("\n✅ You're ready to run the evaluation!")
    print("   Run: python evaluate_model.py")
    
    return True

if __name__ == "__main__":
    check_dataset_structure()
    print("\n" + "="*70)


