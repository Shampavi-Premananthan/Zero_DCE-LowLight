#!/bin/bash

# Zero-DCE Deployment Helper Script

echo "==================================="
echo "Zero-DCE Deployment Helper"
echo "==================================="
echo ""

# Function to build Docker image
build_docker() {
    echo "Building Docker image..."
    docker build -t zero-dce-app .
    if [ $? -eq 0 ]; then
        echo "✓ Docker image built successfully!"
    else
        echo "✗ Docker build failed!"
        exit 1
    fi
}

# Function to run Docker container
run_docker() {
    echo "Running Docker container..."
    docker run -p 7860:7860 zero-dce-app
}

# Function to test locally
test_local() {
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo "Starting local app..."
    python app.py
}

# Function to prepare HuggingFace deployment
prepare_hf() {
    echo "Preparing files for HuggingFace deployment..."
    
    # Create a deployment directory
    mkdir -p huggingface_deploy
    
    # Copy necessary files
    cp app.py huggingface_deploy/
    cp requirements.txt huggingface_deploy/
    cp README_HUGGINGFACE.md huggingface_deploy/README.md
    
    # Copy model files
    mkdir -p huggingface_deploy/Zero-DCE_code/snapshots
    cp Zero-DCE_code/model.py huggingface_deploy/Zero-DCE_code/
    cp Zero-DCE_code/snapshots/Epoch99.pth huggingface_deploy/Zero-DCE_code/snapshots/
    
    echo "✓ Files prepared in 'huggingface_deploy' directory"
    echo ""
    echo "Next steps:"
    echo "1. Create a new Space on HuggingFace: https://huggingface.co/spaces"
    echo "2. Clone your space: git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME"
    echo "3. Copy files: cp -r huggingface_deploy/* YOUR_SPACE_NAME/"
    echo "4. Push to HuggingFace: cd YOUR_SPACE_NAME && git add . && git commit -m 'Initial commit' && git push"
}

# Main menu
echo "Choose an option:"
echo "1. Build Docker image"
echo "2. Run Docker container"
echo "3. Test locally (without Docker)"
echo "4. Prepare files for HuggingFace"
echo "5. Build and run Docker (combined)"
echo ""
read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        build_docker
        ;;
    2)
        run_docker
        ;;
    3)
        test_local
        ;;
    4)
        prepare_hf
        ;;
    5)
        build_docker
        echo ""
        echo "Starting container..."
        run_docker
        ;;
    *)
        echo "Invalid choice!"
        exit 1
        ;;
esac
