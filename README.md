# 🧠 OCR-AI Monitoring Dashboard

An AI-powered OCR (Optical Character Recognition) system designed to digitize historical and regional language manuscripts with real-time retraining, live monitoring dashboard, model versioning, and self-learning capabilities — fully powered on Raspberry Pi.


---

## 📸 Project Highlights

- 🔁 **Auto-Retraining** based on correction logs
- 📊 **Live Monitoring Dashboard** with graphs (CER trend + OCR accuracy)
- 🧠 **Model Versioning System** (v2.3, v2.4, ...)
- ⚡ **Real-Time System Metrics** (RAM, CPU)
- 🌀 **Simulated OCR Uploads** for dynamic feedback
- 📈 **Chart.js integrated UI**
- 🌐 **FastAPI backend** + Jinja2 dashboard

---

## 🧰 Folder Structure

```
OCR-AI/
├── app/
│   ├── logs/                 # retrain logs, status, OCR stats
│   ├── models/               # model_v2.X.pt files
│   ├── templates/            # dashboard.html
│   ├── main.py               # FastAPI app with dashboard endpoints
│   ├── retrainer.py          # Auto-retrainer engine
│   ├── utils.py              # (optional helpers)
│   └── model_version.txt     # current model version
│
├── scripts/
│   ├── run_api.py            # Launch FastAPI
│   ├── run_retrainer.py      # Background retraining loop
│   ├── simulate_activity.py  # OCR + corrections loop
│   ├── system_monitor.py     # Live RAM/CPU stats
│   └── log_viewer.py         # Live retrain.log viewer
│
├── setup.sh                  # Auto-setup script (optional)
├── README.md
└── venv/                     # Python virtual environment
```

---

## 🚀 Installation (Windows or Raspberry Pi)

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/ocr-ai.git
cd ocr-ai
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate        # On Raspberry Pi / Linux
# OR
venv\Scripts\activate         # On Windows (PowerShell)
```

### 3. Install Requirements
```bash
pip install fastapi uvicorn jinja2 psutil requests
```

---

## 🏁 Start All 5 Terminals

### 🧠 Terminal 1: Start FastAPI Server
```bash
python scripts/run_api.py
```

### 🧪 Terminal 2: Auto-Retrainer Loop
```bash
python scripts/run_retrainer.py
```

### 📊 Terminal 3: Simulated OCR + Corrections
```bash
python scripts/simulate_activity.py
```

### 🖥️ Terminal 4: Live System Monitor (optional)
```bash
python scripts/system_monitor.py
```

### 📈 Terminal 5: View Retrain Logs (optional)
```bash
python scripts/log_viewer.py
```

---

## 🌐 Access Dashboard

Open in your browser:
```
http://127.0.0.1:8000/dashboard
```

---

## 📌 Notes for Raspberry Pi Setup

1. Ensure you use **Raspberry Pi OS (64-bit)**  
2. Activate swap memory (`sudo dphys-swapfile setup && sudo dphys-swapfile swapon`)  
3. You can use `screen` or `tmux` to keep 5 terminals running  
4. Add startup service with systemd (optional)

---

## 📄 Output Demo

### Dashboard Preview:
- CER line graph
- OCR accuracy bars
- Live retrain logs
- Model dropdown
- Retraining status: idle/running
- Real RAM/CPU monitoring

---

## ✅ Made For

- 👨‍🎓 Final Year AI/ML Projects
- 🖨️ Digitizing Regional Scripts (Tamil, Telugu, etc.)
- 💻 Edge Inference on Raspberry Pi
- 🎓 Skill-building in Python, FastAPI, Jinja2, psutil

---

## 🙏 Credits

- Developed by: `Aro`
- Inspired by Tesseract, PyTorch pipelines, and embedded AI practices

---

## 📜 License

MIT License — use freely for educational and research purposes.
