@echo off
chcp 65001 >nul
rem ===== 双击：在黑框窗口里运行 Python 代码 =====
rem 直接双击 = 运行 code\hello_python.py
rem 把任意 .py 文件拖到这个 bat 上 = 运行那个文件
cd /d "%~dp0"

if "%~1"=="" (
  "D:\Users\27182\anaconda3\python.exe" code\hello_python.py
) else (
  "D:\Users\27182\anaconda3\python.exe" "%~1"
)

echo.
echo ===== 运行结束 =====
pause
