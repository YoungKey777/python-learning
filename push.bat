@echo off
chcp 65001 >nul
rem ===== 学习完双击：提交今天的进度并推送到 GitHub（打卡） =====
cd /d "%~dp0"

for /f %%i in ('wmic os get localdate ^| findstr /r "[0-9]"') do set LD=%%i
set TODAY=%LD:~0,4%-%LD:~4,2%-%LD:~6,2%

git add -A
git commit -m "daily %TODAY%: 学习打卡" 2>nul
if %errorlevel%==0 (
  echo [OK] 已提交今天的记录（%TODAY%）
) else (
  echo 今天没有新改动，跳过提交
)

git push 2>nul
if %errorlevel%==0 (
  echo.
  echo ========================================
  echo  打卡成功！GitHub 贡献图今天多一格绿色
  echo ========================================
) else (
  echo.
  echo 网络不通，推送失败 —— 但记录已保存在本地，时间戳照算！
  echo 等网络好的时候（如手机热点）再双击一次 push.bat 即可补推，
  echo 贡献图会自动补上这几天的格子。
)
pause
