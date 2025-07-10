@echo off
REM Automated GitHub push, tag, and release helper for Djinn Constellation Hub
REM S1.3: CI/CD Security Hooks + Council Enhancement Deployment

set TAG=v2.1.1-council-enhanced
set BRANCH=s1.3-council-enhanced
set MESSAGE="🧠 Council Enhancement v2 + CI/CD Security Hooks — Federation integrity enforcement"

echo 🛡️ Deploying S1.3 CI/CD Security Hooks + Council Enhancement to GitHub...
echo.

REM Create and switch to feature branch
git checkout -b %BRANCH%

REM Stage specific S1.3 and council files
git add .pre-commit-config.yaml
git add scripts/install_hooks.py
git add scripts/verify_federation.py
git add .github/workflows/steward-ci.yml
git add README.md
git add CHANGELOG.md
git add djinn-council/Modelfile
git add trust_registry.json

REM Commit changes
git commit -m %MESSAGE%

REM Push to feature branch
git push origin %BRANCH%

REM Create and push tag
git tag %TAG%
git push origin %TAG%

echo.
echo ✅ S1.3 CI/CD Security Hooks + Council Enhancement deployed successfully!
echo.
echo 📋 Next steps:
echo    1. Create Pull Request from %BRANCH% to main
echo    2. Title: "🧠 [ENHANCEMENT] Council v2 + CI/CD Security Hooks (Federation Upgrade)"
echo    3. Merge to activate CI/CD pipeline and enhanced council
echo    4. Verify GitHub Actions are running
echo.
echo 🌟 Your Federation is now CI-aware, tamper-hardened, and council-enhanced!
pause
