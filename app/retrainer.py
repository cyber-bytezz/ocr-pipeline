import time
import datetime
import random
import os

CORRECTION_FILE = "app/logs/corrections.jsonl"
LOG_FILE = "app/logs/retrain.log"
STATUS_FILE = "app/logs/status.txt"
MODEL_FILE = "app/model_version.txt"

def get_correction_count():
    if not os.path.exists(CORRECTION_FILE):
        return 0
    with open(CORRECTION_FILE, "r", encoding="utf-8") as f:
        return len([l for l in f if l.strip()])

def write_status(status):
    with open(STATUS_FILE, "w") as f:
        f.write(status)

def simulate_training(epoch_count=3):
    cer_before = round(random.uniform(0.10, 0.15), 2)
    cer_after = round(cer_before - random.uniform(0.02, 0.04), 2)
    print(f"[Retrain] Triggered at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    for i in range(1, epoch_count + 1):
        print(f"▶ Epoch {i} - Loss: {round(random.uniform(0.2, 0.4), 2)}")
        time.sleep(0.5)
    print(f"✅ CER improved: {cer_before} -> {cer_after}")
    return cer_before, cer_after

def retrain():
    while True:
        count = get_correction_count()
        if count >= 3:
            write_status("retraining")
            with open(MODEL_FILE, "r+") as f:
                version = f.read().strip()
                num = int(version.split(".")[-1]) + 1
                new_version = f"v2.{num}"
                f.seek(0)
                f.write(new_version)
                f.truncate()

            cer_before, cer_after = simulate_training()
            model_save_path = f"models/model_{new_version}.pt"
            os.makedirs("models", exist_ok=True)
            with open(model_save_path, "w") as mf:
                mf.write("model data")

            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(f"[{now}] Model: {new_version} | CER: {cer_before} -> {cer_after} | Corrections: {count}\\n")

            open(CORRECTION_FILE, "w").truncate(0)
            write_status("idle")
        else:
            write_status("idle")
        print(f"[Idle] No new corrections (need at least 3). Current: {count}. Next check in 20s...")
        time.sleep(20)

if __name__ == "__main__":
    retrain()