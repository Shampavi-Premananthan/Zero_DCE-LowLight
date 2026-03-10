# Quick Setup Script for HuggingFace Spaces (Docker)
# Run this in PowerShell from the Zero-DCE directory

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Preparing files for HuggingFace Spaces" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Create a deployment folder
$deployFolder = "huggingface_deploy"
if (Test-Path $deployFolder) {
    Remove-Item -Recurse -Force $deployFolder
}
New-Item -ItemType Directory -Force -Path $deployFolder | Out-Null

Write-Host "`nCreated deployment folder: $deployFolder" -ForegroundColor Green

# Copy main files
Write-Host "`nCopying files..." -ForegroundColor Yellow
Copy-Item "app.py" -Destination "$deployFolder/" -Force
Copy-Item "requirements.txt" -Destination "$deployFolder/" -Force
Copy-Item "Dockerfile" -Destination "$deployFolder/" -Force
Copy-Item "README_FOR_HUGGINGFACE.md" -Destination "$deployFolder/README.md" -Force

# Copy model files
New-Item -ItemType Directory -Force -Path "$deployFolder/Zero-DCE_code" | Out-Null
New-Item -ItemType Directory -Force -Path "$deployFolder/Zero-DCE_code/snapshots" | Out-Null
Copy-Item "Zero-DCE_code/model.py" -Destination "$deployFolder/Zero-DCE_code/" -Force
Copy-Item "Zero-DCE_code/snapshots/Epoch99.pth" -Destination "$deployFolder/Zero-DCE_code/snapshots/" -Force

Write-Host "`nAll files copied successfully!" -ForegroundColor Green

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "READY FOR DEPLOYMENT!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan

Write-Host "`nNext Steps:" -ForegroundColor Yellow
Write-Host "1. Go to https://huggingface.co/new-space"
Write-Host "2. Select SDK: Docker"
Write-Host "3. Create your space"
Write-Host "4. Upload all files from '$deployFolder' folder"
Write-Host "5. Wait 5-10 minutes for build"
Write-Host "`nYour app will be live at:"
Write-Host "https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME" -ForegroundColor Cyan
