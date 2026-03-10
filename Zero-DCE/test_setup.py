"""
Quick test script to verify the setup works correctly
"""
import sys
import os

print("=" * 50)
print("Zero-DCE Setup Verification")
print("=" * 50)
print()

# Check Python version
print(f"✓ Python version: {sys.version.split()[0]}")

# Check if files exist
files_to_check = [
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "Zero-DCE_code/model.py",
    "Zero-DCE_code/snapshots/Epoch99.pth"
]

print("\nChecking files...")
all_exist = True
for file in files_to_check:
    exists = os.path.exists(file)
    status = "✓" if exists else "✗"
    print(f"{status} {file}")
    if not exists:
        all_exist = False

# Check dependencies
print("\nChecking dependencies...")
dependencies = {
    "torch": "PyTorch",
    "torchvision": "TorchVision",
    "PIL": "Pillow",
    "numpy": "NumPy",
    "gradio": "Gradio"
}

missing = []
for module, name in dependencies.items():
    try:
        __import__(module)
        print(f"✓ {name} installed")
    except ImportError:
        print(f"✗ {name} NOT installed")
        missing.append(name)

print("\n" + "=" * 50)
if all_exist and not missing:
    print("✓ All checks passed! Ready to deploy.")
    print("\nNext steps:")
    print("1. Run locally: python app.py")
    print("2. Or build Docker: docker build -t zero-dce-app .")
    print("3. Or use deploy.bat for guided deployment")
else:
    print("✗ Some checks failed!")
    if not all_exist:
        print("\nMissing files detected. Ensure you're in the correct directory.")
    if missing:
        print(f"\nInstall missing packages: pip install -r requirements.txt")
        
print("=" * 50)
