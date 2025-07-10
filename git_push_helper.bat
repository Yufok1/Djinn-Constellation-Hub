@echo off
REM Simple Git Pusher: commits and pushes everything to main, no checks

git add .
git commit -m "Quick push: all changes"
git push origin main

echo All changes pushed directly to main!
pause
