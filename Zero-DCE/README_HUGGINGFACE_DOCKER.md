# Deploy Zero-DCE to HuggingFace Spaces with Docker

## Method 1: Using HuggingFace Web Interface (Easiest)

### Step 1: Prepare Your Files
Ensure you have these files ready:
- `Dockerfile`
- `app.py`
- `requirements.txt`
- `Zero-DCE_code/model.py`
- `Zero-DCE_code/snapshots/Epoch99.pth`
- `README.md` (with proper frontmatter - see below)

### Step 2: Create README.md with Docker Configuration

Create a `README.md` file with this content at the top:

```markdown
---
title: Zero-DCE Low-Light Enhancement
emoji: 🌙
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
---
```

**Important**: 
- `sdk: docker` tells HuggingFace to use Docker
- `app_port: 7860` is required (Gradio default port)

### Step 3: Create New Space on HuggingFace

1. Go to https://huggingface.co/new-space
2. Fill in:
   - **Space name**: `zero-dce-enhancement` (or your choice)
   - **License**: `apache-2.0`
   - **Select SDK**: Choose **"Docker"**
   - **Space hardware**: `CPU basic` (free tier)
3. Click **"Create Space"**

### Step 4: Upload Files via Web Interface

After creating the space, upload files in this order:

1. **README.md** (with Docker frontmatter)
2. **Dockerfile**
3. **requirements.txt**
4. **app.py**
5. Create folder structure:
   - Click "Add file" → "Create a new file"
   - File path: `Zero-DCE_code/model.py`
   - Paste content and commit
6. Upload model:
   - Click "Add file" → "Upload files"
   - Upload: `Zero-DCE_code/snapshots/Epoch99.pth`

### Step 5: Wait for Build

- HuggingFace will automatically build your Docker image
- Build time: 5-10 minutes (first time)
- Watch the build logs in the "Building" section
- Once complete, your app will be live!

### Step 6: Access Your App

Your app will be available at:
```
https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
```

---

## Method 2: Using Git CLI (Advanced)

### Prerequisites
```bash
# Install Git LFS
git lfs install

# Authenticate with HuggingFace
huggingface-cli login
```

### Step 1: Create Space
Go to https://huggingface.co/new-space and create a Docker space (as in Method 1, Step 3)

### Step 2: Clone Your Space
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
cd zero-dce-enhancement
```

### Step 3: Copy Files
```bash
# Copy all necessary files
cp D:/Softwareprojects/ZeroDceLow/Zero-DCE/Dockerfile .
cp D:/Softwareprojects/ZeroDceLow/Zero-DCE/app.py .
cp D:/Softwareprojects/ZeroDceLow/Zero-DCE/requirements.txt .

# Copy model files
mkdir -p Zero-DCE_code/snapshots
cp D:/Softwareprojects/ZeroDceLow/Zero-DCE/Zero-DCE_code/model.py Zero-DCE_code/
cp D:/Softwareprojects/ZeroDceLow/Zero-DCE/Zero-DCE_code/snapshots/Epoch99.pth Zero-DCE_code/snapshots/
```

### Step 4: Create README.md
```bash
cat > README.md << 'EOF'
---
title: Zero-DCE Low-Light Enhancement
emoji: 🌙
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
---

# Zero-DCE Low-Light Image Enhancement

Transform dark images into bright, clear photos with AI-powered enhancement.

## Features
- Easy drag-and-drop interface
- Adjustable enhancement strength
- Dual outputs (intermediate + final results)
- Fast CPU inference

## Usage
1. Upload a low-light image
2. Adjust strength slider (0.5-2.5)
3. Click "Enhance Image"
4. Compare results!
EOF
```

### Step 5: Track Large Files
```bash
# Track model checkpoint with Git LFS
git lfs track "*.pth"
git add .gitattributes
```

### Step 6: Commit and Push
```bash
git add .
git commit -m "Deploy Zero-DCE with Docker"
git push
```

### Step 7: Monitor Build
- Go to your space URL
- Watch the build logs
- Wait for "Running" status

---

## Troubleshooting

### Build Fails
**Check these:**
1. **README.md frontmatter** - Must have `sdk: docker` and `app_port: 7860`
2. **Dockerfile** - Ensure EXPOSE 7860
3. **Dependencies** - Check requirements.txt has all packages
4. **Model file** - Ensure Epoch99.pth is uploaded (80MB)

### App Doesn't Start
**Common issues:**
1. Port mismatch - App must use port 7860
2. Missing files - Check all files uploaded
3. Path issues - Ensure file paths are correct

### Slow Performance
- Free CPU tier is slower (~40-60s per image)
- Upgrade to GPU for faster inference
- Consider reducing image size in app

---

## Port Configuration

HuggingFace Spaces Docker apps must:
- Expose port 7860
- App must listen on 0.0.0.0:7860

Already configured in your app.py:
```python
demo.launch(server_name="0.0.0.0", server_port=7860)
```

---

## Cost

- **CPU basic**: FREE ✅
- **CPU upgrade**: $0.03/hour
- **T4 GPU**: $0.60/hour
- **A10G GPU**: $1.20/hour

Free tier is sufficient for demo purposes!

---

## Updating Your Space

### Via Web:
1. Go to your space
2. Click "Files" tab
3. Click on file to edit
4. Make changes and commit

### Via Git:
```bash
cd zero-dce-enhancement
# Make changes to files
git add .
git commit -m "Update description"
git push
```

Space will automatically rebuild!

---

## Security Notes

1. Don't commit sensitive data
2. Model file (Epoch99.pth) is tracked with Git LFS
3. Space is public by default
4. Can make private in space settings

---

## Next Steps

1. ✅ Create HuggingFace Space with Docker SDK
2. ✅ Upload files (README.md first!)
3. ✅ Wait for build to complete
4. ✅ Test your app
5. ✅ Share your space URL!

Your Space URL will be:
```
https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
```

**Happy deploying! 🚀**
