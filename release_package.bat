@echo off
echo.
echo ========================================
echo   🜂 DJINN CONSTELLATION HUB RELEASE
echo ========================================
echo.

set VERSION=1.0.0
set PACKAGE_NAME=Djinn-Constellation-Hub-v%VERSION%

echo 🧹 Cleaning previous releases...
if exist "%PACKAGE_NAME%" rmdir /s /q "%PACKAGE_NAME%"
if exist "%PACKAGE_NAME%.zip" del "%PACKAGE_NAME%.zip"

echo 📁 Creating release directory...
mkdir "%PACKAGE_NAME%"

echo �� Copying files...
xcopy /E /I /Y "djinn-federation" "%PACKAGE_NAME%\djinn-federation\"
xcopy /E /I /Y "djinn-council" "%PACKAGE_NAME%\djinn-council\"
xcopy /E /I /Y "idhhc-companion" "%PACKAGE_NAME%\idhhc-companion\"
xcopy /E /I /Y "djinn-companion" "%PACKAGE_NAME%\djinn-companion\"
xcopy /E /I /Y "docs" "%PACKAGE_NAME%\docs\"
xcopy /E /I /Y "tests" "%PACKAGE_NAME%\tests\"
xcopy /E /I /Y "examples" "%PACKAGE_NAME%\examples\"
xcopy /E /I /Y "scripts" "%PACKAGE_NAME%\scripts\"
xcopy /E /I /Y ".github" "%PACKAGE_NAME%\.github\"

echo �� Copying root files...
copy "README.md" "%PACKAGE_NAME%\"
copy "requirements.txt" "%PACKAGE_NAME%\"
copy ".gitignore" "%PACKAGE_NAME%\"
copy "LICENSE" "%PACKAGE_NAME%\"
copy "constellation_hub.py" "%PACKAGE_NAME%\"
copy "rebuild_council_codellama.bat" "%PACKAGE_NAME%\"
copy "launch_enhanced_council_v2_constellation.bat" "%PACKAGE_NAME%\"
copy "launch_enhanced_constellation_hub.bat" "%PACKAGE_NAME%\"
copy "build_ollama_models.bat" "%PACKAGE_NAME%\"
copy "ENHANCED_COUNCIL_V2_INTEGRATION.md" "%PACKAGE_NAME%\"
copy "CONSTELLATION_HUB_GUIDE.md" "%PACKAGE_NAME%\"
copy "CHANGELOG.md" "%PACKAGE_NAME%\"
copy "CONTRIBUTING.md" "%PACKAGE_NAME%\"
copy "SECURITY.md" "%PACKAGE_NAME%\"
copy "CODE_OF_CONDUCT.md" "%PACKAGE_NAME%\"
copy "ISSUE_TEMPLATE.md" "%PACKAGE_NAME%\"
copy "PULL_REQUEST_TEMPLATE.md" "%PACKAGE_NAME%\"

echo 🧪 Running tests (optional)...
python -m pytest tests/ -v
if %errorlevel% neq 0 (
    echo ⚠️  Tests failed, but continuing with packaging...
) else (
    echo ✅ Tests passed!
)

echo 📦 Creating ZIP package...
powershell Compress-Archive -Path "%PACKAGE_NAME%" -DestinationPath "%PACKAGE_NAME%.zip" -Force

echo �� Package statistics:
dir "%PACKAGE_NAME%.zip" | findstr "%PACKAGE_NAME%.zip"
echo.
echo 📁 Files included:
dir "%PACKAGE_NAME%" /s /b | find /c /v ""

echo.
echo ========================================
echo   🎉 RELEASE PACKAGE READY!
echo ========================================
echo.
echo 📦 Package: %PACKAGE_NAME%.zip
echo �� Contents: %PACKAGE_NAME%\
echo 🚀 Ready for GitHub release!
echo.
echo 💡 Next steps:
echo    1. Upload %PACKAGE_NAME%.zip to GitHub Releases
echo    2. Add release notes from CHANGELOG.md
echo    3. Tag as v%VERSION%
echo.
pause
