import subprocess
import os
import sys

# Run from root for consistency
os.chdir(os.path.dirname(os.path.dirname(__file__)))

def run_retrainer():
    print("🧠 [Terminal 2] Auto-Retraining Engine Initialized\n" + "="*60)
    subprocess.run([sys.executable, "app/retrainer.py"])

if __name__ == "__main__":
    run_retrainer()
