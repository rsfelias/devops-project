# ---------- Build stage ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels

# ---------- Runtime stage ----------
FROM python:3.11-slim

WORKDIR /app

RUN addgroup --system appgroup \
 && adduser --system --ingroup appgroup appuser

COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

COPY app.py .

USER appuser

EXPOSE 8080

CMD ["python", "app.py"]
