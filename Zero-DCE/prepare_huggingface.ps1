# Quick Setup Script for HuggingFace Spaces (Docker)
# Run this in PowerShell from the Zero-DCE directory

Write-Host "=" -ForegroundColor Cyan
Write-Host "📦 Preparing files for HuggingFace Spaces (Docker SDK)" -ForegroundColor Cyan
Write-Host "=" -ForegroundColor Cyan

# Create a deployment folder
$deployFolder = "huggingface_deploy"
if (Test-Path $deployFolder) {
    Remove-Item -Recurse -Force $deployFolder
}
New-Item -ItemType Directory -Force -Path $deployFolder | Out-Null

Write-Host "`n✅ Created deployment folder: $deployFolder" -ForegroundColor Green

# Copy main files
Write-Host "`n📄 Copying files..." -ForegroundColor Yellow
Copy-Item "app.py" -Destination "$deployFolder/" -Force
Copy-Item "requirements.txt" -Destination "$deployFolder/" -Force
Copy-Item "Dockerfile" -Destination "$deployFolder/" -Force

# Copy README (rename for HuggingFace)
Copy-Item "README_FOR_HUGGINGFACE.md" -Destination "$deployFolder/README.md" -Force

# Copy model files
New-Item -ItemType Directory -Force -Path "$deployFolder/Zero-DCE_code" | Out-Null
New-Item -ItemType Directory -Force -Path "$deployFolder/Zero-DCE_code/snapshots" | Out-Null
Copy-Item "Zero-DCE_code/model.py" -Destination "$deployFolder/Zero-DCE_code/" -Force
Copy-Item "Zero-DCE_code/snapshots/Epoch99.pth" -Destination "$deployFolder/Zero-DCE_code/snapshots/" -Force

Write-Host "`n✅ All files copied!" -ForegroundColor Green

# Verify files
Write-Host "`n📋 Files in deployment folder:" -ForegroundColor Yellow
Get-ChildItem -Path $deployFolder -Recurse | ForEach-Object { 
    $relativePath = $_.FullName.Replace("$PWD\$deployFolder\", "")
    Write-Host "  ✓ $relativePath" -ForegroundColor Gray
}

Write-Host "`n" -ForegroundColor White
Write-Host "🎉 READY FOR DEPLOYMENT!" -ForegroundColor Green
Write-Host "=" -ForegroundColor Cyan
Write-Host "`n📝 Next Steps:" -ForegroundColor Yellow
Write-Host "1. Go to https://huggingface.co/new-space" -ForegroundColor White
Write-Host "2. Select SDK: Docker" -ForegroundColor White
Write-Host "3. Create your space" -ForegroundColor White
Write-Host "4. Upload all files from '$deployFolder' folder" -ForegroundColor White
Write-Host "5. Wait 5-10 minutes for build" -ForegroundColor White
Write-Host "`n🚀 Your app will be live at:" -ForegroundColor Green
Write-Host "   https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME" -ForegroundColor Cyan
Write-Host "`n" -ForegroundColor White
