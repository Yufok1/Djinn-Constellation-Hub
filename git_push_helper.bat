@echo off
REM Automated GitHub push, tag, and release helper for Djinn Constellation Hub

set TAG=v2.0.0
set MESSAGE="v2.0.0: Federated launch, CLI, CI, docs, and onboarding"

REM Stage all changes
git add .

REM Commit changes
git commit -m %MESSAGE%

REM Push to main branch
git push origin main

REM Create and push tag
git tag %TAG%
git push origin %TAG%

echo.
echo GitHub push and tag complete!
echo Now, draft your release on GitHub using RELEASE_NOTES_v2.0.0.md
pause
