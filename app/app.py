import os
import time
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# ---------- Logging ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

# ---------- Config ----------
REQUIRED_ENV = "APP_MODE"


@app.route("/")
def index():
    logger.info("Root endpoint called")
    return jsonify({
        "app": "devops-portfolio-app",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/ready")
def ready():
    if not os.getenv(REQUIRED_ENV):
        logger.error("Readiness failed: APP_MODE not set")
        return jsonify({
            "status": "not ready",
            "reason": "APP_MODE env var missing"
        }), 500

    return jsonify({"status": "ready"}), 200


@app.route("/load")
def load():
    logger.warning("CPU load test triggered")
    end_time = time.time() + 30

    # Burn CPU for 30 seconds
    while time.time() < end_time:
        pass

    return jsonify({"status": "load test complete"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    logger.info("Starting app on port %s", port)
    app.run(host="0.0.0.0", port=port)
