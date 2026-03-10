# Zero-DCE Low-Light Image Enhancement - Docker & HuggingFace Deployment

This is a dockerized inference application for Zero-DCE (Zero-Reference Deep Curve Estimation) for low-light image enhancement, with a simple Gradio UI.

## 🚀 Quick Start

### Run with Docker

1. **Build the Docker image:**
```bash
docker build -t zero-dce-app .
```

2. **Run the container:**
```bash
docker run -p 7860:7860 zero-dce-app
```

3. **Access the app:**
Open your browser and go to `http://localhost:7860`

### Run locally (without Docker)

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the app:**
```bash
python app.py
```

3. **Access the app:**
Open your browser and go to `http://localhost:7860`

## 🤗 Deploy to HuggingFace Spaces

### Option 1: Using the Web Interface

1. Go to [HuggingFace Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose "Gradio" as the SDK
4. Upload these files:
   - `app.py`
   - `requirements.txt`
   - `Zero-DCE_code/model.py`
   - `Zero-DCE_code/snapshots/Epoch99.pth`

### Option 2: Using Git

1. **Create a new Space on HuggingFace**

2. **Clone your space:**
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME
```

3. **Copy the necessary files:**
```bash
cp app.py YOUR_SPACE_NAME/
cp requirements.txt YOUR_SPACE_NAME/
cp -r Zero-DCE_code YOUR_SPACE_NAME/
```

4. **Create a README.md for HuggingFace:**
```bash
cat > README.md << 'EOF'
---
title: Zero-DCE Low-Light Enhancement
emoji: 🌙
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

Check configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
EOF
```

5. **Push to HuggingFace:**
```bash
git add .
git commit -m "Initial commit"
git push
```

## 📁 File Structure

```
Zero-DCE/
├── app.py                    # Gradio application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── .dockerignore            # Files to exclude from Docker
├── DEPLOYMENT.md            # This file
└── Zero-DCE_code/
    ├── model.py             # Model architecture
    └── snapshots/
        └── Epoch99.pth      # Trained model weights
```

## 🎯 Usage

1. **Upload Image:** Click on the upload area or drag & drop a low-light image
2. **Adjust Strength:** Use the slider to control enhancement intensity
   - `1.0` = Standard enhancement
   - `< 1.0` = Subtle enhancement
   - `> 1.0` = Stronger enhancement
3. **View Result:** The enhanced image appears instantly

## ⚙️ Model Information

- **Model:** Zero-DCE (Zero-Reference Deep Curve Estimation)
- **Checkpoint:** Epoch99.pth
- **Architecture:** Enhanced CNN with CBAM attention modules
- **Input:** RGB images (any size)
- **Output:** Enhanced RGB images

## 🐳 Docker Details

- **Base Image:** Python 3.9-slim
- **Exposed Port:** 7860
- **Size:** ~2GB (optimized)

## 📝 Notes

- GPU support is automatically detected (uses CPU if CUDA unavailable)
- The app runs on port 7860 by default
- For HuggingFace, the app will automatically use their infrastructure

## 🔧 Troubleshooting

**Issue: Model not loading**
- Ensure `Epoch99.pth` exists in `Zero-DCE_code/snapshots/`

**Issue: Docker build fails**
- Check that all files are in the correct locations
- Ensure you have enough disk space (~3GB)

**Issue: Out of memory**
- Try processing smaller images
- Reduce batch processing

## 📄 License

Please refer to the original Zero-DCE repository for licensing information.
