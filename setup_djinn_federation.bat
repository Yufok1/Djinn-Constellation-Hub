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
echo 🚀 STEP 3: Checking specialized DJINN agents and revolutionary models...
echo.
echo 📋 Required specialized agents:
echo   - djinn-council-enhanced-v2:latest
echo   - idhhc-companion:latest
echo   - djinn-companion:latest
echo   - djinn-cosmic-coder:latest
echo   - djinn-deep-thinker:latest
echo   - djinn-logic-master:latest
echo   - djinn-enterprise-architect:latest

echo.
echo Checking specialized agents:
for %%A in (djinn-council-enhanced-v2 idhhc-companion djinn-companion djinn-cosmic-coder djinn-deep-thinker djinn-logic-master djinn-enterprise-architect) do (
    echo Checking for %%A:latest ...
    ollama list | findstr "%%A"
    if %errorlevel% neq 0 (
        echo ⚠️  %%A is NOT present! Please ensure this model/agent is available before federation launch.
        echo     - For advanced AIs, see:
        echo         create_djinn_revolutionary_models.bat
        echo         shadow_automation.bat
        echo         import_shadow_models.bat
        echo     - Or refer to CLOUD_SETUP_GUIDE.md for manual steps.
    ) else (
        echo %%A is present.
    )
)

echo.
echo 🜂 DJINN FEDERATION SETUP COMPLETE! 🜂
echo.
echo 📋 Available DJINN-ified Constellation Coordinators and Models:
echo   ⚡ tinydolphin-constellation (636MB) - Ultra-Fast Task Coordinator
echo   🐬 dolphin-phi-constellation (1.6GB) - Primary Constellation Coordinator  
echo   🧠 phi3-constellation (2.2GB) - Complex Task Coordinator
echo   🌟 djinn-cosmic-coder (65GB) - MoE Multimodal Sorcery
echo   🧠 djinn-deep-thinker (32GB) - Ancient Wisdom
echo   ⚡ djinn-logic-master (11GB) - Sovereign Reasoning
echo   💻 djinn-enterprise-architect (22GB) - Corporate Mysticism
echo.
echo 🎯 To launch the Hierarchical Constellation Hub:
echo   cd djinn-federation\launcher
echo   python constellation_hub.py
echo.
echo 🜂 The mystical DJINN Federation is ready to serve! 🜂
echo.
pause