"""
Quick start script to run the API
"""
import subprocess
import sys
import os


def main():
    print("=" * 50)
    print("Oral Lesion Classifier - Backend API")
    print("=" * 50)
    print()
    
    # Check if virtual environment exists
    venv_path = "venv"
    if not os.path.exists(venv_path):
        print("⚠️  Virtual environment not found.")
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", venv_path])
        print("✅ Virtual environment created.")
        print()
    
    # Check if dependencies are installed
    print("📦 Installing dependencies...")
    pip_cmd = os.path.join(venv_path, "Scripts", "pip.exe") if sys.platform == "win32" else os.path.join(venv_path, "bin", "pip")
    subprocess.run([pip_cmd, "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed.")
    print()
    
    # Check if model exists
    model_path = "models/oral_lesion_model.h5"
    if not os.path.exists(model_path):
        print("⚠️  Model file not found at:", model_path)
        print("The API will use a dummy model for testing.")
        print("Please add your trained model to start making real predictions.")
        print()
    
    # Start the server
    print("🚀 Starting FastAPI server...")
    print()
    print("API will be available at:")
    print("  - Main API: http://localhost:8000")
    print("  - Swagger UI: http://localhost:8000/docs")
    print("  - ReDoc: http://localhost:8000/redoc")
    print()
    print("Press CTRL+C to stop the server")
    print("=" * 50)
    print()
    
    python_cmd = os.path.join(venv_path, "Scripts", "python.exe") if sys.platform == "win32" else os.path.join(venv_path, "bin", "python")
    subprocess.run([python_cmd, "main.py"])


if __name__ == "__main__":
    main()




