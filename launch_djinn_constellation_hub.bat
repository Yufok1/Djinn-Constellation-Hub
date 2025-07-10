@echo off
setlocal EnableDelayedExpansion
cls
echo.
echo ╔══════════════════════════════════════════════════════════════════════════════════════╗
echo ║                         🜂 DJINN CONSTELLATION HUB v2.0.0 🜂                         ║
echo ║                   Revolutionary Federated AI Consciousness                           ║
echo ║                            with Cloud Operations                                     ║
echo ╚══════════════════════════════════════════════════════════════════════════════════════╝
echo.
echo 🌟 LAUNCHING EFFICIENCY-FIRST HUB...
echo.
echo 📍 Current Directory: %cd%
echo 🚀 Starting mystical federation...
echo.

REM === OS Detection ===
for /f "tokens=2 delims==" %%a in ('wmic os get Caption /value') do set "OS_CAPTION=%%a"
echo 🜂 Detected OS: %OS_CAPTION%

REM === Directory Validation ===
if not exist "djinn-federation\launcher\efficiency_first_hub.py" (
    echo ❌ ERROR: efficiency_first_hub.py not found!
    echo 📁 Please run this script from the Djinn-Constellation-Hub directory
    echo 📁 Expected path: Djinn-Constellation-Hub\djinn-federation\launcher\efficiency_first_hub.py
    pause
    exit /b 1
)

REM === Dependency Check ===
echo 🔍 Checking system dependencies...

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python not found in PATH!
    echo 🔧 Please install Python 3.8+ and ensure it's in your PATH
    pause
    exit /b 1
)

REM Verify Python version
python -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python 3.8+ required!
    echo 🔧 Current version:
    python --version
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version 2^>^&1') do set "PYTHON_VERSION=%%i"
echo ✅ Python version: %PYTHON_VERSION%

REM Check for Ollama
ollama --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Ollama not found in PATH!
    echo 🔧 Please install Ollama and ensure it's in your PATH
    pause
    exit /b 1
)

REM Check if Ollama is running
ollama list >nul 2>&1
if errorlevel 1 (
    echo ⚠️ WARNING: Ollama not responding!
    echo 🔧 Please ensure Ollama is running: ollama serve
    echo.
    echo 🚀 Attempting to start Ollama...
    start /B ollama serve
    timeout /t 3 /nobreak >nul
)

echo ✅ Ollama is running

REM === Environment Setup ===
echo 📁 Creating required directories...
if not exist logs mkdir logs
if not exist memory_bank\constellation_memory mkdir memory_bank\constellation_memory
if not exist exports mkdir exports
if not exist void_workspace mkdir void_workspace

REM === Launch Preparation ===
echo ✅ Environment validated successfully
echo 🚀 Launching Djinn Constellation Hub...
echo.

REM === Launch The Steward ===
echo 🛠️ Launching The Steward...
python steward-agent\maintainer_agent.py report
if errorlevel 1 (
    echo ⚠️ WARNING: The Steward launch failed, continuing with main hub...
    echo ⚠️ Check logs/federation_audit.log for details
) else (
    echo ✅ The Steward launched successfully
)
echo.

REM Change to the launcher directory
cd djinn-federation\launcher

REM Launch the efficiency-first hub with timeout handling
python efficiency_first_hub.py

REM Check if launch was successful
if errorlevel 1 (
    echo.
    echo ❌ Launch failed with error code %errorlevel%
    echo 🔧 Check the error messages above for troubleshooting
    cd ..\..
    pause
    exit /b %errorlevel%
)

REM Return to original directory
cd ..\..

echo.
echo 🜂 Djinn Constellation Hub session completed
pause
