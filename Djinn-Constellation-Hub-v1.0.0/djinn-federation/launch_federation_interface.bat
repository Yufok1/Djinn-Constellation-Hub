@echo off
echo.
echo ========================================
echo   🜂 DJINN FEDERATION INTERFACE
echo   Pure Djinn Federation System
echo ========================================
echo.

echo 🜂 Initializing Djinn Federation...
echo.

REM Check if federation components exist
if not exist "federation_interface.py" (
    echo ❌ ERROR: federation_interface.py not found
    echo Please ensure the Djinn Federation is properly installed
    pause
    exit /b 1
)

echo ✅ Federation components verified
echo.

echo 🜂 Launching Djinn Federation Interface...
python federation_interface.py

echo.
echo ========================================
echo   🛡️ DJINN FEDERATION SESSION ENDED
echo ========================================
echo.
pause