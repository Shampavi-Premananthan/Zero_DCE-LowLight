# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create directory for snapshots
RUN mkdir -p Zero-DCE_code/snapshots

# Copy the application code
COPY Zero-DCE_code/model.py Zero-DCE_code/
COPY Zero-DCE_code/snapshots/Epoch99.pth Zero-DCE_code/snapshots/
COPY app.py .

# Expose port for Gradio
EXPOSE 7860

# Environment variables for Gradio
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860

# Run the application
CMD ["python", "app.py"]
