@echo off
echo.
echo ========================================
echo   NEURAL CONSTELLATION HUB BUILD
echo ========================================
echo.
echo Building the Neural Constellation AI...
echo.

REM Check if neural-chat base model exists
ollama list | findstr "neural-chat:7b"
if %errorlevel% neq 0 (
    echo Neural-chat base model not found. Pulling...
    ollama pull neural-chat:7b
    if %errorlevel% neq 0 (
        echo Failed to pull neural-chat:7b
        pause
        exit /b 1
    )
)

echo Building Neural Constellation Hub...
ollama create neural-constellation -f neural-constellation.Modelfile
if %errorlevel% neq 0 (
    echo Failed to build Neural Constellation Hub
    pause
    exit /b 1
)

echo.
echo ========================================
echo NEURAL CONSTELLATION HUB BUILD COMPLETE
echo ========================================
echo.
echo Model: neural-constellation
echo Base: neural-chat:7b
echo Capabilities: Advanced pattern recognition + Federation coordination
echo.
echo Test the model with:
echo ollama run neural-constellation
echo.
pause 