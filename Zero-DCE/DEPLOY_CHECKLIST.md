# ✅ HuggingFace Spaces Deployment Checklist

## Files to Upload (In Order):

### 1. README.md (MOST IMPORTANT - Upload First!)
**Rename `README_FOR_HUGGINGFACE.md` to `README.md` before uploading**

Must have this header:
```yaml
---
title: Zero-DCE Low-Light Enhancement
emoji: 🌙
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
---
```

### 2. Dockerfile
✅ Already fixed - uses `libgl1` instead of `libgl1-mesa-glx`

### 3. requirements.txt
✅ Already fixed:
```
torch>=1.9.0
torchvision>=0.10.0
numpy>=1.21.0
Pillow>=8.3.0
gradio==4.20.0
huggingface-hub==0.23.0
```

### 4. app.py
✅ Already fixed - has `.queue().launch()` with `show_api=True`

### 5. Model Files
Upload folder structure:
- `Zero-DCE_code/model.py`
- `Zero-DCE_code/snapshots/Epoch99.pth`

---

## Quick Deploy Steps:

1. Go to: https://huggingface.co/new-space
2. Select SDK: **Docker**
3. Create space
4. Upload files in this order:
   - README.md (from README_FOR_HUGGINGFACE.md)
   - Dockerfile
   - requirements.txt
   - app.py
   - Zero-DCE_code/model.py
   - Zero-DCE_code/snapshots/Epoch99.pth
5. Wait 5-10 minutes for build
6. App should be running!

---

## All Issues Fixed:

✅ Dockerfile dependencies (libgl1-mesa-glx → libgl1)
✅ Gradio version compatibility (4.29.0)
✅ HuggingFace Hub compatibility (0.23.0)
✅ API exposure (.queue().launch() with show_api=True)
✅ Port configuration (7860)
✅ Docker SDK configuration in README

---

## If You Still Get Errors:

Check build logs on HuggingFace and share the error message.

**Your space will be at:**
`https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME`
