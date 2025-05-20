import time
import platform
import os

def get_ram():
    try:
        import psutil
        mem = psutil.virtual_memory()
        return f"{mem.used // (1024*1024)}MB / {mem.total // (1024*1024)}MB"
    except:
        return "Unavailable (install psutil)"

def get_cpu():
    try:
        import psutil
        return f"{psutil.cpu_percent()}%"
    except:
        return "Unavailable (install psutil)"

def get_model_version():
    try:
        with open("app/model_version.txt") as f:
            return f.read().strip()
    except:
        return "N/A"

def monitor():
    print("📦 [Terminal 4] OCR-AI System Monitor Dashboard\n" + "="*55)
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print("📊 Real-time System Metrics")
        print("══════════════════════════════════════════════")
        print(f"🧠 RAM Usage     : {get_ram()}")
        print(f"🔥 CPU Load      : {get_cpu()}")
        print(f"🧪 Model Version : {get_model_version()}")
        print("🕒 Refreshing every 5 seconds...\n")
        time.sleep(5)

if __name__ == "__main__":
    monitor()
