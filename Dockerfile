# ==============================
# 1. Base Python Image
# ==============================
FROM python:3.11-slim AS base

# Prevent Python from writing .pyc files & enable buffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# 2. Create App Directory
# ==============================
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ==============================
# 3. Copy Entire Project
# ==============================
COPY . .

# Make sure vectorstore exists (avoid Chroma error)
RUN mkdir -p vectorstore

# Expose Gradio default port
EXPOSE 7860

# ==============================
# 4. Start the App
# ==============================
CMD ["python", "rag_app.py"]
