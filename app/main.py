from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import random, datetime, os, json

app = FastAPI()

# CORS setup for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

# 📥 OCR Simulation Endpoint
@app.post("/tamil-ocr")
async def ocr_endpoint(req: Request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app/model_version.txt") as f:
        version = f.read().strip()

    accuracy = round(random.uniform(0.85, 0.92), 2)
    segments = random.randint(2, 4)

    # Log simulated OCR result
    print(f"[{now}] 📥 User uploaded: upload_{random.randint(100,999)}.png")
    print(f"[INFO] Detected script: Tamil | Model: {version}")
    print(f"[RESULT] ✔️ Text extracted successfully")
    print(f"📊 Extracted Accuracy: {accuracy*100:.1f}% | Segments: {segments} | Model: {version}\n")

    # Save to stats file for dashboard
    os.makedirs("app/logs", exist_ok=True)
    with open("app/logs/ocr_stats.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": now,
            "accuracy": accuracy,
            "segments": segments,
            "model": version
        }) + "\n")

    return {"accuracy": accuracy, "segments": segments, "version": version}

# --------------------------------------
# 📊 DASHBOARD BACKEND ROUTES
# --------------------------------------

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/model-version")
async def model_version():
    with open("app/model_version.txt") as f:
        return PlainTextResponse(f.read())

@app.get("/latest-logs")
async def latest_logs():
    try:
        with open("app/logs/retrain.log", "r", encoding="utf-8") as f:
            lines = f.readlines()
        return PlainTextResponse("".join(lines[-15:]))
    except:
        return PlainTextResponse("No logs found.")

@app.get("/metrics")
async def system_metrics():
    try:
        import psutil
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent()
        return PlainTextResponse(f"RAM: {mem.used // (1024*1024)}MB / {mem.total // (1024*1024)}MB\nCPU: {cpu}%")
    except:
        return PlainTextResponse("Install psutil")

@app.get("/status")
async def retrain_status():
    try:
        with open("app/logs/status.txt", "r") as f:
            return PlainTextResponse(f.read().strip())
    except:
        return PlainTextResponse("unknown")

@app.get("/simulate-ocr")
async def simulate_ocr():
    os.system("curl -X POST http://127.0.0.1:8000/tamil-ocr >nul 2>&1")
    return PlainTextResponse("OCR simulated")

@app.get("/simulate-corrections")
async def simulate_corrections():
    os.makedirs("app/logs", exist_ok=True)
    with open("app/logs/corrections.jsonl", "a", encoding="utf-8") as f:
        for i in range(3):
            f.write(f"correction_{i}\n")
    return PlainTextResponse("Fake corrections added")

@app.get("/model-list")
async def model_list():
    try:
        files = os.listdir("models")
        models = [f for f in files if f.endswith(".pt")]
        return JSONResponse(models)
    except:
        return JSONResponse([])

@app.get("/cer-graph")
async def cer_graph():
    points = []
    try:
        with open("app/logs/retrain.log", "r", encoding="utf-8") as f:
            for line in f.readlines()[-20:]:
                if "CER:" in line or "->" in line:
                    parts = line.strip().split(" | ")
                    time_str = parts[0].strip("[]")
                    cer_part = parts[1].split("CER:")[1].strip()
                    cer_after = float(cer_part.split("->")[1].strip())
                    points.append({"time": time_str, "cer": cer_after})
    except:
        pass
    return JSONResponse(points)

@app.get("/ocr-stats")
async def ocr_stats():
    stats = []
    try:
        with open("app/logs/ocr_stats.jsonl", "r", encoding="utf-8") as f:
            for line in f.readlines()[-20:]:
                stats.append(json.loads(line.strip()))
    except:
        pass
    return JSONResponse(stats)
