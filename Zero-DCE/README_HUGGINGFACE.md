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

# Zero-DCE Low-Light Image Enhancement

An interactive web application for enhancing low-light images using **Zero-DCE** (Zero-Reference Deep Curve Estimation).

## 🎯 Features

- **Easy to Use**: Simple drag-and-drop interface
- **Adjustable Enhancement**: Control the strength of enhancement with a slider
- **Fast Processing**: Real-time image enhancement
- **No Reference Needed**: Works without paired training data

## 🚀 How to Use

1. **Upload** a low-light image
2. **Adjust** the enhancement strength slider (0.5 - 2.5)
   - 1.0 = Standard enhancement
   - < 1.0 = Subtle enhancement
   - > 1.0 = Stronger enhancement
3. **View** your enhanced image instantly!

## 🔬 Model Details

- **Architecture**: Enhanced CNN with CBAM (Convolutional Block Attention Module)
- **Training**: Trained on LOL (Low-Light) dataset
- **Checkpoint**: Epoch 99

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
# Clone the repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## 🐳 Docker Deployment

```bash
docker build -t zero-dce-app .
docker run -p 7860:7860 zero-dce-app
```

## 📝 License

Please refer to the original Zero-DCE repository for licensing information.
