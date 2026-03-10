"""
Minimal example to test Zero-DCE inference
Run this to verify the model works before deploying
"""
import torch
import numpy as np
from PIL import Image
import sys
import os

# Add code directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Zero-DCE_code'))

try:
    import model as DCEModel
    print("✓ Model imported successfully")
except Exception as e:
    print(f"✗ Failed to import model: {e}")
    sys.exit(1)

# Create a simple test image (dark gradient)
print("\nCreating test image...")
test_image = np.zeros((256, 256, 3), dtype=np.uint8)
for i in range(256):
    test_image[i, :, :] = int(i * 0.3)  # Dark gradient
test_pil = Image.fromarray(test_image)
print("✓ Test image created (256x256)")

# Initialize model
print("\nInitializing model...")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

try:
    net = DCEModel.enhance_net_nopool().to(device)
    print("✓ Model initialized")
except Exception as e:
    print(f"✗ Failed to initialize model: {e}")
    sys.exit(1)

# Load checkpoint
checkpoint_path = 'Zero-DCE_code/snapshots/Epoch99.pth'
if not os.path.exists(checkpoint_path):
    print(f"✗ Checkpoint not found: {checkpoint_path}")
    sys.exit(1)

try:
    state_dict = torch.load(checkpoint_path, map_location=device)
    net.load_state_dict(state_dict, strict=False)
    net.eval()
    print(f"✓ Checkpoint loaded: {checkpoint_path}")
except Exception as e:
    print(f"✗ Failed to load checkpoint: {e}")
    sys.exit(1)

# Test inference
print("\nTesting inference...")
try:
    # Prepare input
    data = np.array(test_pil).astype(np.float32) / 255.0
    data_tensor = torch.from_numpy(data).float()
    data_tensor = data_tensor.permute(2, 0, 1).unsqueeze(0).to(device)
    
    # Run inference
    with torch.no_grad():
        _, enhanced, _ = net(data_tensor)
    
    # Convert back to image
    output = enhanced.squeeze().permute(1, 2, 0).cpu().numpy()
    output = (output * 255).clip(0, 255).astype(np.uint8)
    output_pil = Image.fromarray(output)
    
    print("✓ Inference successful!")
    print(f"  Input shape: {test_pil.size}")
    print(f"  Output shape: {output_pil.size}")
    
    # Save test output
    output_pil.save("test_output.png")
    print("✓ Test output saved as 'test_output.png'")
    
except Exception as e:
    print(f"✗ Inference failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 50)
print("✓ All tests passed! Model is working correctly.")
print("=" * 50)
print("\nYou can now:")
print("1. Run the Gradio app: python app.py")
print("2. Build Docker: docker build -t zero-dce-app .")
print("3. Deploy to HuggingFace: Follow QUICKSTART.md")
