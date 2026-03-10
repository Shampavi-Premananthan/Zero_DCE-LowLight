# 🚀 Complete HuggingFace Spaces Deployment Guide (Docker Method)

## ✅ Prerequisites Checklist

- [x] HuggingFace account (free) - [Sign up here](https://huggingface.co/join)
- [x] All files ready in `Zero-DCE` folder
- [x] Port 7860 configured in app.py
- [x] Dockerfile ready
- [x] Model checkpoint (Epoch99.pth) - 80MB

---

## 🎯 Quick Deploy (5 Steps)

### Step 1: Prepare Files (Option A - Automatic)

Run this PowerShell script from the Zero-DCE directory:

```powershell
.\prepare_huggingface.ps1
```

This creates a `huggingface_deploy` folder with all necessary files.

**OR**

### Step 1: Prepare Files (Option B - Manual)

Create a new folder and copy these files:

```
huggingface_deploy/
├── README.md                          ← Use README_FOR_HUGGINGFACE.md
├── Dockerfile                         ← Docker configuration
├── app.py                            ← Gradio application
├── requirements.txt                  ← Dependencies
└── Zero-DCE_code/
    ├── model.py                      ← Model architecture
    └── snapshots/
        └── Epoch99.pth              ← Trained weights (80MB)
```

**IMPORTANT**: Rename `README_FOR_HUGGINGFACE.md` to `README.md`

---

### Step 2: Create HuggingFace Space

1. **Go to**: https://huggingface.co/new-space

2. **Fill the form**:
   ```
   Owner: [Your username]
   Space name: zero-dce-enhancement
   License: apache-2.0
   Select the Space SDK: Docker ← IMPORTANT!
   Space hardware: CPU basic - 2 vCPU - 16GB RAM (FREE)
   ```

3. **Click** "Create Space"

---

### Step 3: Upload Files

After space creation, you'll see an upload interface.

**Upload in this order** (important for build):

1. **README.md** (with Docker frontmatter)
   - Must contain at top:
     ```yaml
     ---
     title: Zero-DCE Low-Light Enhancement
     emoji: 🌙
     sdk: docker
     app_port: 7860
     ---
     ```

2. **Dockerfile**

3. **requirements.txt**

4. **app.py**

5. **Create model folder structure**:
   - Click "Add file" → "Create a new file"
   - Filename: `Zero-DCE_code/model.py`
   - Paste the content
   - Click "Commit"

6. **Upload model checkpoint**:
   - Click "Add file" → "Upload files"
   - Upload: `Zero-DCE_code/snapshots/Epoch99.pth`
   - Click "Commit"

---

### Step 4: Monitor Build

- HuggingFace will automatically start building
- You'll see "Building..." status
- Build logs appear in real-time
- **Build time**: 5-10 minutes (first time)

**Build process**:
```
1. Pulling Docker base image
2. Installing system dependencies
3. Installing Python packages
4. Copying application files
5. Starting application
```

---

### Step 5: Access Your App! 🎉

Once build completes (status changes to "Running"), your app is live!

**Your Space URL**:
```
https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
```

**Share it**: Anyone can access your space URL!

---

## 🐛 Troubleshooting

### Issue: Build Failed

**Check #1**: README.md frontmatter
```yaml
---
sdk: docker    ← Must be "docker" not "gradio"
app_port: 7860 ← Required for Docker SDK
---
```

**Check #2**: Dockerfile EXPOSE
```dockerfile
EXPOSE 7860  ← Must match app_port in README
```

**Check #3**: All files uploaded
- README.md ✓
- Dockerfile ✓
- app.py ✓
- requirements.txt ✓
- Zero-DCE_code/model.py ✓
- Zero-DCE_code/snapshots/Epoch99.pth ✓

**Check #4**: Build logs
- Click on "Building" status to see logs
- Look for error messages

---

### Issue: App Doesn't Start

**Check #1**: Port configuration in app.py
```python
demo.launch(
    server_name="0.0.0.0",  ← Must be 0.0.0.0
    server_port=7860,       ← Must be 7860
)
```

**Check #2**: Model file exists
```python
checkpoint_path='Zero-DCE_code/snapshots/Epoch99.pth'
```

**Check #3**: Dependencies installed
- Check `requirements.txt` has all packages
- Gradio version 6.0+

---

### Issue: Slow Performance

**Normal behavior**:
- CPU inference: 40-60 seconds per image
- This is expected on free tier

**To speed up** (costs money):
- Upgrade to GPU in Space settings
- T4 GPU: $0.60/hour (10x faster)

---

## 🔄 Updating Your Space

### Method 1: Web Interface
1. Go to your space
2. Click "Files" tab
3. Click on file to edit
4. Make changes
5. Click "Commit"
6. Space rebuilds automatically (2-3 minutes)

### Method 2: Git CLI
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
cd zero-dce-enhancement

# Make changes to files
git add .
git commit -m "Update: description of changes"
git push

# Space rebuilds automatically
```

---

## 💰 Pricing

| Tier | CPU | RAM | GPU | Cost | Best For |
|------|-----|-----|-----|------|----------|
| **CPU basic** | 2 vCPU | 16GB | None | **FREE** | Demo, Testing |
| CPU upgrade | 8 vCPU | 32GB | None | $0.03/hr | Production |
| T4 Small | 4 vCPU | 16GB | T4 16GB | $0.60/hr | Fast inference |
| A10G Small | 4 vCPU | 32GB | A10G 24GB | $1.20/hr | Heavy use |

**Recommendation**: Start with FREE tier, upgrade if needed.

---

## 📊 Expected Performance

| Hardware | Inference Time | Concurrent Users |
|----------|---------------|------------------|
| CPU basic (Free) | 40-60s | 1-2 |
| CPU upgrade | 30-40s | 5-10 |
| T4 GPU | 2-5s | 50+ |
| A10G GPU | 1-2s | 100+ |

---

## 🔐 Space Settings

After deployment, you can configure:

### Visibility
- **Public** (default): Anyone can access
- **Private**: Only you and invited users

### Hardware
- Change in "Settings" → "Space hardware"
- Takes effect after rebuild

### Sleep Time
- Free tier: Sleeps after 48h inactivity
- Wakes up automatically on visit (30s delay)

### Persistent Storage
- Not needed for this app (stateless)

---

## 📁 File Structure on HuggingFace

Your space repository will look like:

```
your-space/
├── .git/                    (Git repository)
├── README.md               (With Docker frontmatter)
├── Dockerfile              (Docker config)
├── app.py                  (Gradio app)
├── requirements.txt        (Dependencies)
└── Zero-DCE_code/
    ├── model.py
    └── snapshots/
        └── Epoch99.pth     (Tracked with Git LFS)
```

---

## 🎓 Advanced: Git LFS for Large Files

The model checkpoint (80MB) is automatically tracked with Git LFS on HuggingFace.

If deploying via Git CLI:
```bash
# Install Git LFS
git lfs install

# Track .pth files
git lfs track "*.pth"
git add .gitattributes

# Normal git workflow
git add .
git commit -m "Add model"
git push
```

---

## 🌟 Promotion Tips

After deployment, you can:

1. **Share your space**:
   - Copy space URL
   - Share on social media
   - Add to your portfolio

2. **Embed in websites**:
   ```html
   <iframe
     src="https://YOUR_USERNAME-zero-dce-enhancement.hf.space"
     width="850"
     height="900"
   ></iframe>
   ```

3. **Add to HuggingFace collections**:
   - Tag: computer-vision
   - Tag: image-enhancement
   - Tag: gradio

4. **Community engagement**:
   - Enable discussions
   - Respond to user feedback
   - Update based on suggestions

---

## ✅ Post-Deployment Checklist

After your space is live:

- [ ] Test image upload
- [ ] Test enhancement with different strengths
- [ ] Check both outputs display correctly
- [ ] Verify performance is acceptable
- [ ] Update README with actual space URL
- [ ] Add example images (optional)
- [ ] Share your space!

---

## 📞 Support Resources

- **HuggingFace Docs**: https://huggingface.co/docs/hub/spaces-overview
- **Docker SDK Guide**: https://huggingface.co/docs/hub/spaces-sdks-docker
- **Gradio Docs**: https://gradio.app/docs/
- **Community Forum**: https://discuss.huggingface.co/

---

## 🎉 You're Ready!

**Summary**:
1. ✅ Files prepared
2. ✅ Create Docker space on HuggingFace
3. ✅ Upload files (README.md with docker SDK first!)
4. ✅ Wait for build (5-10 mins)
5. ✅ Share your live app!

**Your live app will be at**:
```
https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
```

**Good luck with your deployment! 🚀**
