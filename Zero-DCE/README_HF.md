---
title: Zero-DCE Low-Light Enhancement
emoji: 🌙
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 6.0.0
app_file: app.py
pinned: false
---

# 🌙 Zero-DCE Low-Light Image Enhancement

Transform dark images into bright, clear photos with AI-powered enhancement using Zero-DCE.

## 🎯 Features

- **Easy to Use**: Simple drag-and-drop interface
- **Dual Outputs**: See intermediate and final enhancement results
- **Adjustable Strength**: Control enhancement intensity (0.5 - 2.5)
- **Fast Processing**: Optimized for quick inference
- **No Reference Needed**: Works without paired training data

## 🚀 How to Use

1. **Upload** a low-light or dark image
2. **Adjust** the enhancement strength slider:
   - **1.0**: Standard enhancement (recommended)
   - **< 1.0**: Subtle, natural enhancement
   - **> 1.0**: Stronger, dramatic enhancement
3. **Click** "✨ Enhance Image" button or wait for auto-enhancement
4. **Compare** intermediate (4 iterations) vs final (8 iterations) results

## 🔬 Model Details

- **Architecture**: Enhanced CNN with deep curve estimation
- **Method**: Zero-Reference Deep Curve Estimation (Zero-DCE)
- **Training Dataset**: LOL (Low-Light) dataset
- **Checkpoint**: Epoch 99 (best performance)

## 💡 Technical Details

Zero-DCE uses a lightweight deep network to estimate pixel-wise and high-order curves for dynamic range adjustment of images. The model:

- Requires no paired or unpaired training data
- Preserves image details while enhancing brightness
- Applies 8 iterations of curve adjustments for optimal results
- Uses CBAM attention mechanisms for better feature extraction

## 📚 Citation

If you use this model, please cite the original Zero-DCE paper:

```bibtex
@inproceedings{guo2020zero,
  title={Zero-reference deep curve estimation for low-light image enhancement},
  author={Guo, Chunle and Li, Chongyi and Guo, Jichang and Loy, Chen Change and Hou, Junhui and Kwong, Sam and Cong, Runmin},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={1780--1789},
  year={2020}
}
```

## 💻 Local Deployment

```bash
# Clone the space
git clone https://huggingface.co/spaces/YOUR_USERNAME/zero-dce-enhancement

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## 🐳 Docker Deployment

```bash
docker build -t zero-dce-app .
docker run -p 7861:7861 zero-dce-app
```

## 📝 License

Apache-2.0 License

## 🙏 Acknowledgments

Based on the Zero-DCE paper and implementation. Thanks to the original authors for their excellent work.
