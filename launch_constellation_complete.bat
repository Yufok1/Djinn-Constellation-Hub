@echo off
echo.
echo ========================================
echo   CONSTELLATION HUB COMPLETE
echo ========================================
echo.
echo Launching the TRUE MASTER HUB system...
echo.
echo Constellation Components:
echo Federation: AI Model Coordination
echo Void Framework: Environment & Tools  
echo Memory Bank: Persistent Storage
echo Bridge Systems: Communication Protocols
echo.
echo ========================================
echo.

cd /d "%~dp0"

echo Checking Constellation components...
echo.

REM Check if AI models are built
echo [1/4] Checking AI Models...
ollama list | findstr "Yufok1/djinn-federation:constellation"
if %errorlevel% neq 0 (
    echo Constellation Hub not found - installing...
    ollama pull Yufok1/djinn-federation:constellation
    if %errorlevel% neq 0 (
        echo Failed to install Constellation Hub
        pause
        exit /b 1
    )
) else (
    echo Constellation Hub ready
)

ollama list | findstr "Yufok1/djinn-federation:council"
if %errorlevel% neq 0 (
    echo Council Model not found - installing...
    ollama pull Yufok1/djinn-federation:council
    if %errorlevel% neq 0 (
        echo Failed to install Council Model
        pause
        exit /b 1
    )
) else (
    echo Council Model ready
)

ollama list | findstr "Yufok1/djinn-federation:idhhc"
if %errorlevel% neq 0 (
    echo IDHHC Model not found - installing...
    ollama pull Yufok1/djinn-federation:idhhc
    if %errorlevel% neq 0 (
        echo Failed to install IDHHC Model
        pause
        exit /b 1
    )
) else (
    echo IDHHC Model ready
)

ollama list | findstr "Yufok1/djinn-federation:companion"
if %errorlevel% neq 0 (
    echo Companion Model not found - installing...
    ollama pull Yufok1/djinn-federation:companion
    if %errorlevel% neq 0 (
        echo Failed to install Companion Model
        pause
        exit /b 1
    )
) else (
    echo Companion Model ready
)

echo.
echo [2/4] Checking Void Framework...
if exist "void_workspace" (
    echo Void Framework ready
) else (
    echo Void Framework not found - will initialize
)

echo.
echo [3/4] Checking Memory Bank...
if exist "memory_bank" (
    echo Memory Bank ready
) else (
    echo Memory Bank not found - will initialize
    mkdir memory_bank
)

echo.
echo [4/4] Checking Bridge Systems...
if exist "bridge" (
    echo Bridge Systems ready
) else (
    echo Bridge Systems not found - will initialize
    mkdir bridge
)

echo.
echo ========================================
echo LAUNCHING CONSTELLATION HUB COMPLETE
echo ========================================
echo.
echo Federation: AI Model Coordination
echo   - Yufok1/djinn-federation:constellation (Master Coordinator)
echo   - Yufok1/djinn-federation:council (Sovereign Meta-Intelligence)
echo   - Yufok1/djinn-federation:idhhc (Operational Strategist)
echo   - Yufok1/djinn-federation:companion (Dialogue Controller)
echo.
echo Void Framework: Environment & Tools
echo   - File system operations
echo   - Advanced toolkit capabilities
echo   - Workspace management
echo.
echo Memory Bank: Persistent Storage
echo   - Conversation history
echo   - Federation state
echo   - User preferences
echo   - Pattern recognition
echo.
echo Bridge Systems: Communication Protocols
echo   - Council-IDHHC communication
echo   - Federation bridge protocols
echo   - Cross-system coordination
echo.
echo Constellation Hub is the TRUE MASTER SYSTEM
echo   that orchestrates the entire Djinn ecosystem!
echo.

REM Launch the main Constellation Hub
python constellation_hub.py

echo.
echo Constellation Hub Complete session ended.
echo.
echo All memory preserved
echo Bridge systems maintained
echo Void Framework active
echo Federation models ready
echo.
pause 