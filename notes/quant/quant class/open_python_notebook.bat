@echo off
title Jupyter - python.ipynb
cd /d "%~dp0"

if not exist "python.ipynb" (
  echo [ERROR] python.ipynb not found in this folder.
  pause
  exit /b 1
)

where jupyter.exe >nul 2>nul
if errorlevel 1 goto fallback

jupyter notebook "python.ipynb"
goto end

:fallback
"D:\Users\27182\anaconda3\Scripts\jupyter.exe" notebook "python.ipynb"

:end
