# 🚀 Quick Start Guide

## What's Been Created

Your Zero-DCE inference application is now ready for deployment with:

✅ **app.py** - Gradio web interface with adjustable enhancement strength  
✅ **Dockerfile** - Container configuration for easy deployment  
✅ **requirements.txt** - All necessary Python dependencies  
✅ **DEPLOYMENT.md** - Complete deployment instructions  
✅ **README_HUGGINGFACE.md** - HuggingFace Space README  
✅ **.dockerignore** - Optimized Docker build  
✅ **deploy.bat** - Windows deployment helper script  
✅ **deploy.sh** - Linux/Mac deployment helper script  

---

## 🎯 Option 1: Test Locally (Fastest)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open: **http://localhost:7860**

---

## 🐳 Option 2: Deploy with Docker

### Windows (Use PowerShell or CMD):
```cmd
deploy.bat
```
Choose option 5 (Build and run Docker)

### Linux/Mac:
```bash
chmod +x deploy.sh
./deploy.sh
```
Choose option 5 (Build and run Docker)

**Or manually:**
```bash
docker build -t zero-dce-app .
docker run -p 7860:7860 zero-dce-app
```

Then open: **http://localhost:7860**

---

## 🤗 Option 3: Deploy to HuggingFace Spaces

### Step 1: Prepare Files

**Windows:**
```cmd
deploy.bat
```
Choose option 4 (Prepare for HuggingFace)

**Linux/Mac:**
```bash
./deploy.sh
```
Choose option 4 (Prepare for HuggingFace)

This creates a `huggingface_deploy` folder with all necessary files.

### Step 2: Create HuggingFace Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in:
   - **Space name**: `zero-dce-enhancement` (or your choice)
   - **License**: Choose appropriate license
   - **SDK**: Select **Gradio**
   - **Hardware**: CPU (Basic) is sufficient

### Step 3: Upload Files

**Option A - Web Interface (Easiest):**
1. In your new Space, click **"Files"** tab
2. Click **"Add file"** → **"Upload files"**
3. Upload all files from `huggingface_deploy` folder:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `Zero-DCE_code/model.py`
   - `Zero-DCE_code/snapshots/Epoch99.pth`

**Option B - Git (Advanced):**
```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME

# Copy files from deployment folder
cp -r ../huggingface_deploy/* .

# Push to HuggingFace
git add .
git commit -m "Initial deployment of Zero-DCE"
git push
```

### Step 4: Wait for Build

HuggingFace will automatically build and deploy your app. This takes 2-5 minutes.

### Step 5: Access Your App

Your app will be live at:
```
https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
```

---

## 📱 Using the App

1. **Upload Image**: Click or drag-and-drop a low-light image
2. **Adjust Strength**: Use slider to control enhancement
   - `0.5` = Very subtle enhancement
   - `1.0` = Standard enhancement (recommended)
   - `1.5-2.0` = Strong enhancement
   - `2.0+` = Very strong enhancement
3. **Download**: Right-click the enhanced image to save

---

## 🔍 Troubleshooting

### "Model checkpoint not found"
- Ensure `Zero-DCE_code/snapshots/Epoch99.pth` exists
- Check the file path in app.py

### Docker build fails
- Make sure Docker is installed and running
- Check you have enough disk space (~3GB needed)

### Out of memory
- Try smaller images
- Use CPU mode if GPU fails
- On HuggingFace, upgrade to better hardware

### App doesn't start
- Check all dependencies are installed: `pip list`
- Verify Python version >= 3.8
- Check port 7860 is not already in use

---

## 📊 File Structure

```
Zero-DCE/
├── app.py                          # Main Gradio application
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── .dockerignore                   # Docker build optimization
├── deploy.bat                      # Windows helper script
├── deploy.sh                       # Linux/Mac helper script
├── DEPLOYMENT.md                   # Detailed deployment guide
├── README_HUGGINGFACE.md          # HuggingFace README
├── QUICKSTART.md                  # This file
└── Zero-DCE_code/
    ├── model.py                   # Model architecture
    └── snapshots/
        └── Epoch99.pth            # Trained weights (~1MB)
```

---

## 💡 Tips

- **Best Results**: Use images that are genuinely low-light
- **Enhancement Strength**: Start with 1.0, then adjust
- **Image Size**: Any size works, but larger images take longer
- **GPU**: Automatically used if available, otherwise CPU

---

## 🎉 You're All Set!

Choose your deployment method and start enhancing images!

**Questions?** Check `DEPLOYMENT.md` for detailed instructions.
