@echo off
title Jupyter - numpy day
cd /d "%~dp0"

if not exist "numpy day.ipynb" (
  echo [ERROR] "numpy day.ipynb" not found in this folder.
  pause
  exit /b 1
)

where jupyter.exe >nul 2>nul
if errorlevel 1 goto fallback

jupyter notebook "numpy day.ipynb"
goto end

:fallback
"D:\Users\27182\anaconda3\Scripts\jupyter.exe" notebook "numpy day.ipynb"

:end
