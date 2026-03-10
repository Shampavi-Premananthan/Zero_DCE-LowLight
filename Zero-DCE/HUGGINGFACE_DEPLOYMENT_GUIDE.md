# 🚀 Deploy to HuggingFace Spaces (Step-by-Step Guide)

## 📋 Prepare These Files First:

1. ✅ `app.py` - Main application file
2. ✅ `requirements.txt` - Python dependencies
3. ✅ `README_HF.md` - HuggingFace space documentation (rename this file to README.md)
4. ✅ `Zero-DCE_code/model.py` - Model architecture
5. ✅ `Zero-DCE_code/snapshots/Epoch99.pth` - Trained model (80MB)

---

## 🎯 Method 1: Web Interface (Easiest!) ⭐

### Step 1: HuggingFace Account
- Go to [HuggingFace](https://huggingface.co/join) and create an account (or login)

### Step 2: Create New Space
1. Go to [Create New Space](https://huggingface.co/new-space) link
2. Fill in the form:
   - **Owner**: Your username
   - **Space name**: `zero-dce-enhancement` (or any name)
   - **License**: `apache-2.0`
   - **Select SDK**: Select `Gradio`
   - **Hardware**: `CPU basic` (free) - This is enough!
3. Click **Create Space** button

### Step 3: Upload Files
After the space is created, upload these files:

#### Important Files (In Order):

1. **README.md** - Rename `README_HF.md` file to **README.md** and upload
   - Must have `---` header section (sdk, title, etc.)

2. **requirements.txt** - Upload directly

3. **app.py** - Upload directly

4. **Zero-DCE_code folder**:
   - Click "Add file" → "Create a new file" button
   - Type in path: `Zero-DCE_code/model.py`
   - Copy-paste the content
   - Click "Commit" button

5. **Model checkpoint**:
   - Click "Add file" → "Upload files" button
   - Path: `Zero-DCE_code/snapshots/Epoch99.pth` (80MB file will upload)
   - Click "Commit" button

### Step 4: Wait for Build
- After files are uploaded, build starts automatically (2-3 mins)
- To see build status, the space will show "Building..." indicator
- Once build is complete, app is ready!

### Step 5: Access Your App! 🎉
- URL: `https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement`
- Can be accessed publicly!
- Can be shared with others!

---

## 🎯 Method 2: Git CLI (Advanced Users)

### Prerequisites:
```bash
# Git LFS install 
git lfs install
```

### Step 1: Space Create (same as Method 1, steps 1-2)

### Step 2: Clone Your Space
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
cd zero-dce-enhancement
```

### Step 3: Copy Files
```bash
# From your project folder
cd D:\Softwareprojects\ZeroDceLow\Zero-DCE

# Copy files
copy app.py zero-dce-enhancement\
copy requirements.txt zero-dce-enhancement\
copy README_HF.md zero-dce-enhancement\README.md

# Copy model files
xcopy Zero-DCE_code zero-dce-enhancement\Zero-DCE_code\ /E /I
```

### Step 4: Track Large Files with Git LFS
```bash
cd zero-dce-enhancement
git lfs track "*.pth"
git add .gitattributes
```

### Step 5: Commit & Push
```bash
git add .
git commit -m "Initial deployment of Zero-DCE app"
git push
```

### Step 6: Wait for Build
- HuggingFace will automatically build
- You can see the status on the space page

---

## 🐳 Docker Method (Alternative - Local Testing)

### Prerequisites:
- Docker Desktop must be installed and running

### Step 1: Build Docker Image
```bash
cd D:\Softwareprojects\ZeroDceLow\Zero-DCE
docker build -t zero-dce-app .
```

### Step 2: Run Container
```bash
docker run -p 7861:7861 zero-dce-app
```

### Step 3: Access
- Open browser: `http://localhost:7861`

---

## 🔥 Quick Checklist

Before uploading to HuggingFace:

- [ ] Does `README_HF.md` file have `---` header section at the top?
- [ ] Are `sdk: gradio` and `sdk_version: 6.0.0` correct?
- [ ] Have you mentioned `app_file: app.py`?
- [ ] Does `requirements.txt` have all dependencies?
- [ ] Is `Epoch99.pth` file (80MB) ready?
- [ ] Is server port set to `7860` in `app.py`? (HuggingFace default)

---

## 💡 Tips & Troubleshooting

### If build fails:
1. Check `requirements.txt` - gradio version must be 6.0+
2. Check `README.md` - header section (---) must be correct
3. Check logs in "Community" tab

### Performance:
- Free CPU works fine (30-60 seconds per image)
- GPU upgrade requires "$" (faster inference)

### Making Changes:
- When files are updated, rebuild happens automatically
- Rebuild time: 2-3 minutes

---

## 📞 Support

If you have problems:
- HuggingFace Docs: https://huggingface.co/docs/hub/spaces-overview
- Community Forum: https://discuss.huggingface.co/

---

**Now you're ready! Deploy to HuggingFace! 🚀**
