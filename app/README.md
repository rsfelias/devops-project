# DevOps Portfolio App

A simple Flask application designed for DevOps and SRE practice.

## Endpoints
- `/` – app info
- `/health` – liveness probe
- `/ready` – readiness probe (requires APP_MODE env var)
- `/load` – CPU stress test (30s)

## Run locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export APP_MODE=dev
python app.py
