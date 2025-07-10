@echo off
cls
echo.
echo ╔══════════════════════════════════════════════════════════════════════════════════════╗
echo ║                🜂 COMPLETE DJINN FEDERATION REBUILD 🜂                               ║
echo ║                   Building All Revolutionary Models with Federation Consciousness    ║
echo ╚══════════════════════════════════════════════════════════════════════════════════════╝
echo.
echo 🌟 This will rebuild ALL revolutionary models with proper federation consciousness...
echo.

:: Check if we're in the right directory
if not exist "djinn-deep-thinker.Modelfile" (
    echo ❌ ERROR: Modelfiles not found!
    echo 📁 Please run this script from the Djinn-Constellation-Hub directory
    pause
    exit /b 1
)

:: Check if Ollama is running
ollama list >nul 2>&1
if errorlevel 1 (
    echo ⚠️ WARNING: Ollama not responding!
    echo 🔧 Please ensure Ollama is running: ollama serve
    pause
    exit /b 1
)

echo ✅ Environment validated successfully
echo.
echo 🧠 COMPLETE FEDERATION REBUILD PROCESS
echo ======================================
echo.

:: Step 1: Remove old models to ensure clean rebuild
echo 🔄 Step 1: Removing old models for clean rebuild...
echo.

echo Removing djinn-cosmic-coder:latest...
ollama rm djinn-cosmic-coder:latest 2>nul
echo Removing djinn-logic-master:latest...
ollama rm djinn-logic-master:latest 2>nul
echo Removing djinn-enterprise-architect:latest...
ollama rm djinn-enterprise-architect:latest 2>nul

echo ✅ Old models removed
echo.

:: Step 2: Rebuild each model with proper federation consciousness
echo 🔄 Step 2: Rebuilding models with federation consciousness...
echo.

:: Rebuild Djinn Cosmic Coder
echo 🧠 Rebuilding djinn-cosmic-coder...
echo This may take several minutes...
ollama create djinn-cosmic-coder -f djinn-cosmic-coder.Modelfile
if errorlevel 1 (
    echo ❌ Failed to rebuild djinn-cosmic-coder
    echo 🔧 Check the error messages above
    pause
    exit /b 1
)
echo ✅ djinn-cosmic-coder rebuilt successfully
echo.

:: Rebuild Djinn Logic Master
echo 🧠 Rebuilding djinn-logic-master...
echo This may take several minutes...
ollama create djinn-logic-master -f djinn-logic-master.Modelfile
if errorlevel 1 (
    echo ❌ Failed to rebuild djinn-logic-master
    echo 🔧 Check the error messages above
    pause
    exit /b 1
)
echo ✅ djinn-logic-master rebuilt successfully
echo.

:: Rebuild Djinn Enterprise Architect
echo 🧠 Rebuilding djinn-enterprise-architect...
echo This may take several minutes...
ollama create djinn-enterprise-architect -f djinn-enterprise-architect.Modelfile
if errorlevel 1 (
    echo ❌ Failed to rebuild djinn-enterprise-architect
    echo 🔧 Check the error messages above
    pause
    exit /b 1
)
echo ✅ djinn-enterprise-architect rebuilt successfully
echo.

:: Step 3: Verify all models are present
echo 🔄 Step 3: Verifying model installation...
echo.

ollama list | findstr "djinn.*latest"
if errorlevel 1 (
    echo ❌ Some models may not be properly installed
    pause
    exit /b 1
)

echo ✅ All models verified
echo.

:: Step 4: Test federation consciousness
echo 🔄 Step 4: Testing federation consciousness...
echo.

echo Testing djinn-cosmic-coder federation awareness...
ollama run djinn-cosmic-coder "Are you part of the Djinn Federation? Respond briefly."
echo.

echo Testing djinn-logic-master federation awareness...
ollama run djinn-logic-master "Are you part of the Djinn Federation? Respond briefly."
echo.

echo Testing djinn-enterprise-architect federation awareness...
ollama run djinn-enterprise-architect "Are you part of the Djinn Federation? Respond briefly."
echo.

echo.
echo 🎉 COMPLETE FEDERATION REBUILD FINISHED!
echo.
echo 🜂 All revolutionary models now have proper federation consciousness
echo 🌟 The Djinn Federation is fully operational
echo 🚀 You can now launch the complete Djinn Constellation Hub
echo.

echo 📋 Next steps:
echo 1. Run: python test_federation_consciousness.py
echo 2. Launch: .\launch_djinn_constellation_hub.bat
echo 3. Test cross-model communication
echo.

pause
