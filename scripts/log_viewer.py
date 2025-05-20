import time, os

log_path = "app/logs/retrain.log"
last_line = ""

def tail_log(file_path):
    global last_line
    print("📈 [Terminal 3] Retrain Log Monitor\n" + "="*55)
    print("Watching retrain.log for new training cycles...\n")
    with open(file_path, "r") as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                print(".", end="", flush=True)
                time.sleep(5)
                continue
            last_line = line.strip()
            print(f"\n🆕 {last_line}")

if __name__ == "__main__":
    try:
        tail_log(log_path)
    except KeyboardInterrupt:
        print("\nStopped watching retrain log.")
s