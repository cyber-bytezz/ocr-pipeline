#!/bin/bash

echo "🔧 Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn

mkdir -p app/logs models scripts
touch app/logs/retrain.log app/corrections.jsonl
echo "v2.3" > app/model_version.txt
echo "FAKE_MODEL_CONTENT" > models/model_v2.3.pt

chmod +x scripts/*.sh

echo "✅ Setup complete. Now open 4 terminals:"
echo "1️⃣ ./scripts/run_api.sh"
echo "2️⃣ ./scripts/run_retrainer.sh"
echo "3️⃣ ./scripts/view_logs.sh"
echo "4️⃣ ./scripts/system_status.sh"
