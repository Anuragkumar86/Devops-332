# ─────────────────────────────────────────────────────
# Stage: Base image using official Python slim image
# ─────────────────────────────────────────────────────
FROM python:3.11-slim

# Metadata labels
LABEL maintainer="anura@devops.com"
LABEL version="1.0"
LABEL description="Flask app Docker demo"

# ── WORKDIR: Set working directory inside container ──
WORKDIR /app

# ── ENV: Set environment variables ──────────────────
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_VERSION=1.0
ENV PORT=5000

# ── COPY: Copy requirements (separate layer for cache)
COPY requirements.txt .

# ── RUN: Install Python dependencies ────────────────
RUN pip install --no-cache-dir -r requirements.txt

# ── COPY: Copy application source code ──────────────
COPY . .

# ── EXPOSE: Document container listens on port 5000 ─
EXPOSE 5000

# ── VOLUME: Mount point for persistent data ─────────
VOLUME ["/app/data"]

# ── CMD: Default command to run application ─────────
CMD ["python", "app.py"]
