@echo off
echo 🜂 DJINN FEDERATION COMPLETE SETUP 🜂
echo =====================================
echo.
echo This script will set up the complete DJINN Federation with:
echo   - DJINN-ified Constellation Coordinators (Tiered Task Management)
echo   - Specialized DJINN Agents
echo   - Hierarchical Constellation Hub
echo.

set /p choice="Do you want to proceed with the setup? (Y/N): "
if /i "%choice%" neq "Y" (
    echo Setup cancelled.
    pause
    exit /b 0
)

echo.
echo 🚀 STEP 1: Building DJINN-ified Constellation Coordinators...
call build_constellation_coordinators.bat
if %errorlevel% neq 0 (
    echo ❌ Failed to build constellation coordinators
    pause
    exit /b 1
)

echo.
echo 🚀 STEP 2: Checking for base models...
echo.
echo 📋 Required base models:
echo   - tinydolphin:latest
echo   - dolphin-phi:latest  
echo   - phi3:latest
echo.

ollama list | findstr "tinydolphin\|dolphin-phi\|phi3"
if %errorlevel% neq 0 (
    echo ⚠️  Some base models may not be available
    echo 💡 Run 'ollama pull tinydolphin:latest' if needed
    echo 💡 Run 'ollama pull dolphin-phi:latest' if needed
    echo 💡 Run 'ollama pull phi3:latest' if needed
)

echo.
echo 🚀 STEP 3: Checking specialized DJINN agents...
echo.
echo 📋 Required specialized agents:
echo   - djinn-council-enhanced-v2:latest
echo   - idhhc-companion:latest
echo   - djinn-companion:latest
echo.

ollama list | findstr "djinn-council\|idhhc-companion\|djinn-companion"
if %errorlevel% neq 0 (
    echo ⚠️  Some specialized agents may not be available
    echo 💡 These should be built separately using their respective build scripts
)

echo.
echo 🜂 DJINN FEDERATION SETUP COMPLETE! 🜂
echo.
echo 📋 Available DJINN-ified Constellation Coordinators:
echo   ⚡ tinydolphin-constellation (636MB) - Ultra-Fast Task Coordinator
echo   🐬 dolphin-phi-constellation (1.6GB) - Primary Constellation Coordinator  
echo   🧠 phi3-constellation (2.2GB) - Complex Task Coordinator
echo.
echo 🎯 To launch the Hierarchical Constellation Hub:
echo   cd djinn-federation\launcher
echo   python constellation_hub.py
echo.
echo 🜂 The mystical DJINN Federation is ready to serve! 🜂
echo.
pause 