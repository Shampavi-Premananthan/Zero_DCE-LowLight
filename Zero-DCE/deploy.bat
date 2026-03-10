@echo off
REM Zero-DCE Deployment Helper Script for Windows

echo ===================================
echo Zero-DCE Deployment Helper
echo ===================================
echo.

:menu
echo Choose an option:
echo 1. Build Docker image
echo 2. Run Docker container
echo 3. Test locally (without Docker)
echo 4. Prepare files for HuggingFace
echo 5. Build and run Docker (combined)
echo 6. Exit
echo.

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto build
if "%choice%"=="2" goto run
if "%choice%"=="3" goto test
if "%choice%"=="4" goto prepare
if "%choice%"=="5" goto build_and_run
if "%choice%"=="6" goto end
goto invalid

:build
echo Building Docker image...
docker build -t zero-dce-app .
if %errorlevel% equ 0 (
    echo [SUCCESS] Docker image built successfully!
) else (
    echo [ERROR] Docker build failed!
    pause
    exit /b 1
)
goto end

:run
echo Running Docker container...
docker run -p 7860:7860 zero-dce-app
goto end

:test
echo Installing dependencies...
pip install -r requirements.txt
echo Starting local app...
python app.py
goto end

:prepare
echo Preparing files for HuggingFace deployment...

REM Create deployment directory
if not exist "huggingface_deploy" mkdir huggingface_deploy

REM Copy necessary files
copy app.py huggingface_deploy\
copy requirements.txt huggingface_deploy\
copy README_HUGGINGFACE.md huggingface_deploy\README.md

REM Copy model files
if not exist "huggingface_deploy\Zero-DCE_code\snapshots" mkdir huggingface_deploy\Zero-DCE_code\snapshots
copy Zero-DCE_code\model.py huggingface_deploy\Zero-DCE_code\
copy Zero-DCE_code\snapshots\Epoch99.pth huggingface_deploy\Zero-DCE_code\snapshots\

echo [SUCCESS] Files prepared in 'huggingface_deploy' directory
echo.
echo Next steps:
echo 1. Create a new Space on HuggingFace: https://huggingface.co/spaces
echo 2. Clone your space: git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
echo 3. Copy files to your space directory
echo 4. Push to HuggingFace: git add . ^&^& git commit -m "Initial commit" ^&^& git push
echo.
pause
goto end

:build_and_run
echo Building Docker image...
docker build -t zero-dce-app .
if %errorlevel% equ 0 (
    echo [SUCCESS] Docker image built successfully!
    echo.
    echo Starting container...
    docker run -p 7860:7860 zero-dce-app
) else (
    echo [ERROR] Docker build failed!
    pause
    exit /b 1
)
goto end

:invalid
echo Invalid choice! Please enter a number between 1-6.
echo.
goto menu

:end
echo.
echo Press any key to exit...
pause >nul
