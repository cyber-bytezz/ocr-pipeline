import time
import random
import requests
from datetime import datetime
import json
import os

OCR_ENDPOINT = "http://127.0.0.1:8000/tamil-ocr"
CORRECTION_FILE = "app/logs/corrections.jsonl"
STATS_FILE = "app/logs/ocr_stats.jsonl"

def simulate_ocr_request():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] 🔁 Simulating OCR upload...")

    try:
        response = requests.post(OCR_ENDPOINT)
        if response.status_code == 200:
            data = response.json()
            accuracy = data.get('accuracy')
            segments = data.get('segments')
            model = data.get('version')
            print(f"✅ OCR → Accuracy: {accuracy*100:.1f}% | Segments: {segments} | Model: {model}")

            # Log to stats file
            os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)
            with open(STATS_FILE, "a", encoding="utf-8") as f:
                json.dump({
                    "timestamp": now,
                    "accuracy": accuracy,
                    "segments": segments,
                    "model": model
                }, f)
                f.write("\n")

        else:
            print(f"❌ OCR failed with status: {response.status_code}")

    except Exception as e:
        print(f"❌ OCR simulation error: {e}")

def simulate_corrections():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] 📝 Injecting 3 corrections...")
    try:
        os.makedirs(os.path.dirname(CORRECTION_FILE), exist_ok=True)
        with open(CORRECTION_FILE, "a", encoding="utf-8") as f:
            for i in range(3):
                f.write(f"correction_{random.randint(1000,9999)}\n")
        print("✅ Corrections added.\n")
    except Exception as e:
        print(f"❌ Correction log error: {e}")

if __name__ == "__main__":
    print("🚀 OCR Activity Simulator Started")
    print("=" * 55)
    while True:
        simulate_ocr_request()
        time.sleep(20)
        simulate_ocr_request()
        time.sleep(10)
        simulate_corrections()
        time.sleep(20)
