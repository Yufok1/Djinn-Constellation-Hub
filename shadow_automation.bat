@echo off
echo.
echo ========================================
echo   🚀 SHADOW CLOUD AUTOMATION SCRIPT
echo     Complete Download + Export Process
echo ========================================
echo.

REM Step 1: Create directories
echo 📁 Creating export directories...
mkdir P:\shadow_models 2>nul
mkdir P:\shadow_models\llama4 2>nul
mkdir P:\shadow_models\qwen3 2>nul
mkdir P:\shadow_models\phi4 2>nul
mkdir P:\shadow_models\codestral 2>nul
echo ✅ Directories created!

echo.
echo 🌟 Starting model downloads...
echo.

REM Step 2: Download all models in parallel (faster)
echo 🔥 Downloading Llama4 Scout (65GB - MoE Cosmic Coding)...
start /b ollama pull aravhawk/llama4:109b

echo 🧠 Downloading Qwen3 (32GB - Thinking Mode)...
start /b ollama pull dengcao/qwen3-30b-a3b:q8_0

echo ⚡ Downloading Phi4 Reasoning (11GB - Advanced Logic)...
start /b ollama pull phi4-reasoning:14b

echo 💻 Downloading Codestral Elite (12GB - Enterprise Coding)...
start /b ollama pull codestral:22b

echo.
echo ⏳ Waiting for downloads to complete...
echo (This may take 30-60 minutes depending on connection)

REM Step 3: Wait for downloads to complete
:wait_loop
timeout /t 60 >nul 2>&1
ollama list | findstr "aravhawk/llama4" >nul 2>&1
if errorlevel 1 (
    echo ⏳ Still downloading... checking again in 60 seconds
    goto wait_loop
)

ollama list | findstr "dengcao/qwen3" >nul 2>&1
if errorlevel 1 (
    echo ⏳ Still downloading... checking again in 60 seconds
    goto wait_loop
)

ollama list | findstr "phi4-reasoning" >nul 2>&1
if errorlevel 1 (
    echo ⏳ Still downloading... checking again in 60 seconds
    goto wait_loop
)

ollama list | findstr "codestral" >nul 2>&1
if errorlevel 1 (
    echo ⏳ Still downloading... checking again in 60 seconds
    goto wait_loop
)

echo.
echo ✅ All downloads completed!
echo.

REM Step 4: Export all models
echo 📤 Exporting models to P: drive...

echo 🌟 Exporting Llama4...
ollama show aravhawk/llama4:109b --modelfile > P:\shadow_models\llama4\Modelfile
if exist P:\shadow_models\llama4\Modelfile (
    echo ✅ Llama4 exported successfully
) else (
    echo ❌ Llama4 export failed
)

echo 🧠 Exporting Qwen3...
ollama show dengcao/qwen3-30b-a3b:q8_0 --modelfile > P:\shadow_models\qwen3\Modelfile
if exist P:\shadow_models\qwen3\Modelfile (
    echo ✅ Qwen3 exported successfully
) else (
    echo ❌ Qwen3 export failed
)

echo ⚡ Exporting Phi4...
ollama show phi4-reasoning:14b --modelfile > P:\shadow_models\phi4\Modelfile
if exist P:\shadow_models\phi4\Modelfile (
    echo ✅ Phi4 exported successfully
) else (
    echo ❌ Phi4 export failed
)

echo 💻 Exporting Codestral...
ollama show codestral:22b --modelfile > P:\shadow_models\codestral\Modelfile
if exist P:\shadow_models\codestral\Modelfile (
    echo ✅ Codestral exported successfully
) else (
    echo ❌ Codestral export failed
)

echo.
echo ========================================
echo   🎉 SHADOW AUTOMATION COMPLETE!
echo ========================================
echo.
echo 📁 Files exported to:
dir P:\shadow_models\*\*.* /s
echo.
echo 🎯 Next Steps:
echo 1. Go to your main PC
echo 2. Run: P:\ALIENFORMATIONHUD\Djinn-Constellation-Hub\import_shadow_models.bat
echo 3. Test: python efficiency_first_hub.py
echo.
echo ✨ Total Size Downloaded: ~120GB
echo ⚡ Ready for Dual-Tier Federation!
echo.
pause