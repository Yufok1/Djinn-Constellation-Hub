@echo off
echo 🜂 BUILDING DJINN-IFIED CONSTELLATION COORDINATORS 🜂
echo ===================================================

cd /d "%~dp0djinn-federation\modelfiles"

echo.
echo 🚀 Building TinyDolphin Constellation Coordinator...
ollama create tinydolphin-constellation -f tinydolphin-constellation.Modelfile
if %errorlevel% neq 0 (
    echo ❌ Failed to build TinyDolphin Constellation Coordinator
    pause
    exit /b 1
)
echo ✅ TinyDolphin Constellation Coordinator built successfully!

echo.
echo 🚀 Building Dolphin-Phi Constellation Coordinator...
ollama create dolphin-phi-constellation -f dolphin-phi-constellation.Modelfile
if %errorlevel% neq 0 (
    echo ❌ Failed to build Dolphin-Phi Constellation Coordinator
    pause
    exit /b 1
)
echo ✅ Dolphin-Phi Constellation Coordinator built successfully!

echo.
echo 🚀 Building Phi3 Constellation Coordinator...
ollama create phi3-constellation -f phi3-constellation.Modelfile
if %errorlevel% neq 0 (
    echo ❌ Failed to build Phi3 Constellation Coordinator
    pause
    exit /b 1
)
echo ✅ Phi3 Constellation Coordinator built successfully!

echo.
echo 🜂 ALL DJINN-IFIED CONSTELLATION COORDINATORS BUILT SUCCESSFULLY! 🜂
echo.
echo 📋 Available Constellation Coordinators:
echo   ⚡ tinydolphin-constellation (636MB) - Ultra-Fast Task Coordinator
echo   🐬 dolphin-phi-constellation (1.6GB) - Primary Constellation Coordinator
echo   🧠 phi3-constellation (2.2GB) - Complex Task Coordinator
echo.
echo 🎯 The Hierarchical Constellation Hub will now use these DJINN-ified coordinators!
echo.
pause