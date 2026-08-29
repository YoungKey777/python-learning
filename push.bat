@echo off
chcp 65001 >nul
rem ===== 学习完双击：提交今天的进度并推送到 GitHub（打卡） =====
cd /d "%~dp0"

for /f %%i in ('wmic os get localdate ^| findstr /r "[0-9]"') do set LD=%%i
set TODAY=%LD:~0,4%-%LD:~4,2%-%LD:~6,2%

git add -A
git commit -m "daily %TODAY%: 学习打卡"
git push

if %errorlevel%==0 (
  echo.
  echo === 打卡成功！GitHub 贡献图今天多一格绿色 ===
) else (
  echo.
  echo 提交失败，检查网络或凭据
)
pause
