---
title: Zero-DCE Low-Light Enhancement
emoji: 🌙
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
---

# 🌙 Zero-DCE Low-Light Image Enhancement

Transform dark images into bright, clear photos using AI-powered Zero-Reference Deep Curve Estimation.

![Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![Docker](https://img.shields.io/badge/Docker-Enabled-blue) ![License](https://img.shields.io/badge/License-Apache%202.0-yellow)

## 🎯 Features

- **Dual Enhancement Results**: View both intermediate (4 iterations) and final (8 iterations) outputs
- **Adjustable Strength**: Fine-tune enhancement intensity from 0.5x to 2.5x
- **Fast Inference**: Optimized for CPU with ~40-60 seconds processing time
- **No Training Data Required**: Zero-reference approach needs no paired images
- **Detail Preservation**: Maintains image quality while enhancing brightness

## 🚀 Quick Start

### Using This Space

1. **Upload Image**: Drag and drop or click to upload a low-light/dark image
2. **Adjust Strength** (optional): 
   - 1.0 = Standard enhancement (recommended)
   - < 1.0 = Subtle, natural enhancement
   - > 1.0 = Dramatic enhancement
3. **Click "✨ Enhance Image"**: Wait 40-60 seconds for results
4. **Compare Results**: See intermediate vs final enhanced outputs

### Local Deployment

```bash
# Clone this space
git clone https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement
cd zero-dce-enhancement

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Access at: `http://localhost:7860`

### Docker Deployment

```bash
# Build image
docker build -t zero-dce-app .

# Run container
docker run -p 7860:7860 zero-dce-app
```

Access at: `http://localhost:7860`

## 🔬 Technical Details

### Model Architecture
- **Base**: Deep CNN with 7 convolutional layers
- **Enhancement Method**: 8 iterative curve adjustments
- **Attention**: CBAM modules (disabled for speed optimization)
- **Parameters**: ~80K (lightweight)
- **Input/Output**: RGB images (any resolution)

### Training
- **Dataset**: LOL (Low-Light) dataset
- **Epochs**: 100 (checkpoint at epoch 99)
- **Loss Functions**: 
  - Spatial consistency loss
  - Exposure control loss
  - Color constancy loss
  - Illumination smoothness loss

### Performance
- **CPU Inference**: 40-60 seconds per image
- **GPU Inference**: 2-5 seconds per image (if upgraded)
- **Memory**: ~500MB RAM
- **Model Size**: 80MB

## 🎨 Enhancement Process

The model applies 8 sequential curve adjustments:

```
Input Image → Conv Layers → Curve Estimation → 8 Iterations of Enhancement → Output
```

**Intermediate Output** (after 4 iterations):
- Balanced enhancement
- Good for slightly dark images

**Final Output** (after 8 iterations):
- Maximum enhancement
- Best for very dark images

## 📚 Citation

If you use this model or space, please cite the original Zero-DCE paper:

```bibtex
@inproceedings{guo2020zero,
  title={Zero-reference deep curve estimation for low-light image enhancement},
  author={Guo, Chunle and Li, Chongyi and Guo, Jichang and Loy, Chen Change and Hou, Junhui and Kwong, Sam and Cong, Runmin},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={1780--1789},
  year={2020}
}
```

## 🛠️ Technology Stack

- **Framework**: [Gradio](https://gradio.app/) 6.0+
- **Deep Learning**: PyTorch 1.9+
- **Backend**: Python 3.9
- **Deployment**: Docker on HuggingFace Spaces
- **Interface**: Modern responsive UI with gradient design

## 📊 Example Use Cases

- **Photography**: Enhance underexposed photos
- **Night Photography**: Brighten dark scenes
- **Security Cameras**: Improve low-light footage
- **Medical Imaging**: Enhance dark medical scans
- **Astrophotography**: Bring out details in dark sky images

## 🎓 Model Details

| Property | Value |
|----------|-------|
| Architecture | Enhanced CNN |
| Input Size | Any (auto-resized) |
| Output Size | Same as input |
| Parameters | ~80,000 |
| Checkpoint | Epoch 99 |
| Framework | PyTorch |

## ⚡ Performance Optimization

This deployment includes several optimizations:
- ✅ Disabled CBAM attention modules for 3-5x speedup
- ✅ CPU-optimized inference
- ✅ Efficient image preprocessing
- ✅ Minimal memory footprint

## 🔐 Privacy & Security

- ✅ All processing happens on HuggingFace servers
- ✅ No images are stored or logged
- ✅ No user data collected
- ✅ Open source code

## 📝 License

This space is licensed under **Apache 2.0 License**.

**Note**: The Zero-DCE implementation is for **non-commercial use** only. Please refer to the [original repository](https://github.com/Li-Chongyi/Zero-DCE) for commercial usage terms.

## 🙏 Acknowledgments

- Original Zero-DCE paper authors: Chunle Guo, Chongyi Li, et al.
- LOL dataset creators
- HuggingFace for hosting infrastructure
- Gradio team for the amazing framework

## 🐛 Issues & Feedback

If you encounter any issues or have suggestions:
- Open a discussion in the "Community" tab
- Report bugs with example images
- Share your enhanced images!

## 🌟 Tips for Best Results

1. **Upload Quality**: Use high-quality original images
2. **Image Size**: Larger images take longer but give better results
3. **Strength Setting**: Start with 1.0 and adjust based on results
4. **Very Dark Images**: Use strength > 1.0
5. **Slightly Dark**: Use strength 0.7-1.0

---

Made with ❤️ using Zero-DCE and Gradio

**Enjoy enhancing your low-light images!** 🌙✨
