@echo off
REM ========================================
REM Upload to HuggingFace Spaces using Git
REM ========================================

echo.
echo First, create your space at: https://huggingface.co/new-space
echo   - Select SDK: Docker
echo   - Copy your space name (username/space-name)
echo.

set /p SPACE_NAME="Enter your HuggingFace space name (e.g., username/space-name): "

echo.
echo Initializing git...
git init
git add .
git commit -m "Initial commit: Zero-DCE deployment"

echo.
echo Adding HuggingFace remote...
git remote add space https://huggingface.co/spaces/%SPACE_NAME%

echo.
echo Pushing to HuggingFace...
git push --force space main

echo.
echo ========================================
echo DONE! Your space is deploying.
echo Check: https://huggingface.co/spaces/%SPACE_NAME%
echo ========================================
pause
