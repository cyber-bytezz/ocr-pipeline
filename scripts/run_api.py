import os
import subprocess
import sys

# Ensure we run from project root
os.chdir(os.path.dirname(os.path.dirname(__file__)))

def run_api():
    print("🖥️  [Terminal 1] Starting OCR Inference Server\n" + "="*55)
    subprocess.run([
        sys.executable, "-m", "uvicorn", "app.main:app",
        "--host", "127.0.0.1",
        "--port", "8000"
    ])

if __name__ == "__main__":
    run_api()
