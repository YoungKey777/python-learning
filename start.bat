@echo off
chcp 65001 >nul
rem ===== 学习前双击：自动创建今天的日志文件 =====
cd /d "%~dp0"

for /f %%i in ('wmic os get localdate ^| findstr /r "[0-9]"') do set LD=%%i
set TODAY=%LD:~0,4%-%LD:~4,2%-%LD:~6,2%
set FILE=daily\%TODAY%.md

if exist "%FILE%" (
  echo 今天的日志已存在：%FILE%
) else (
  copy "daily\模板.md" "%FILE%" >nul
  echo 已创建今天的日志：%FILE%
)
start "" "%FILE%"
echo.
echo 学完记得双击 push.bat 提交打卡！
pause
