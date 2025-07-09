@echo off
echo.
echo ========================================
echo   📥 IMPORTING SHADOW CLOUD MODELS
echo     From P:\ Drive to Local System
echo     🜂 DJINN-IFYING ALL MODELS 🜂
echo ========================================
echo.

echo 🔍 Checking for models on P:\ drive...
if exist "P:\shadow_models\" (
    echo ✅ Found P:\shadow_models\ directory
) else (
    echo ❌ P:\shadow_models\ not found
    echo Please copy models from SHADOW cloud to P:\shadow_models\
    pause
    exit /b
)

echo.
echo 🜂 Creating Djinn-ified versions of revolutionary models...

echo.
echo 🌟 Importing Llama 4 Scout as DJINN-COSMIC-CODER...
if exist "P:\shadow_models\llama4\Modelfile" (
    echo Creating djinn-cosmic-coder:latest from Llama4...
    ollama create djinn-cosmic-coder:latest --file "P:\shadow_models\llama4\Modelfile"
    echo ✅ Djinn Cosmic Coder imported successfully
    echo 🜂 Mystical MoE powers now available for multimodal coding
) else (
    echo ⚠️  Llama4 not found in P:\shadow_models\llama4\
)

echo.
echo 🧠 Importing Qwen3 as DJINN-DEEP-THINKER...
if exist "P:\shadow_models\qwen3\Modelfile" (
    echo Creating djinn-deep-thinker:latest from Qwen3...
    ollama create djinn-deep-thinker:latest --file "P:\shadow_models\qwen3\Modelfile"
    echo ✅ Djinn Deep Thinker imported successfully
    echo 🜂 Ancient wisdom now flows through thinking/non-thinking modes
) else (
    echo ⚠️  Qwen3 not found in P:\shadow_models\qwen3\
)

echo.
echo ⚡ Importing Phi4 as DJINN-LOGIC-MASTER...
if exist "P:\shadow_models\phi4\Modelfile" (
    echo Creating djinn-logic-master:latest from Phi4...
    ollama create djinn-logic-master:latest --file "P:\shadow_models\phi4\Modelfile"
    echo ✅ Djinn Logic Master imported successfully
    echo 🜂 Sovereign reasoning powers now accessible
) else (
    echo ⚠️  Phi4 not found in P:\shadow_models\phi4\
)

echo.
echo 💻 Importing Codestral as DJINN-ENTERPRISE-ARCHITECT...
if exist "P:\shadow_models\codestral\Modelfile" (
    echo Creating djinn-enterprise-architect:latest from Codestral...
    ollama create djinn-enterprise-architect:latest --file "P:\shadow_models\codestral\Modelfile"
    echo ✅ Djinn Enterprise Architect imported successfully
    echo 🜂 Corporate mysticism and enterprise sorcery ready
) else (
    echo ⚠️  Codestral not found in P:\shadow_models\codestral\
)

echo.
echo ========================================
echo   ✅ DJINN REVOLUTIONARY MODELS READY!
echo ========================================
echo.
echo 🜂 Your Djinn Federation now includes:
echo.
echo LOCAL DJINN TIER:
echo   🜂 tinydolphin-constellation (636MB)
echo   🜂 dolphin-phi-constellation (1.6GB)  
echo   🜂 phi3-constellation (2.2GB)
echo   🜂 djinn-federation:council (7.4GB)
echo   🜂 djinn-federation:idhhc (19GB)
echo   🜂 djinn-federation:companion (4.9GB)
echo.
echo CLOUD DJINN TIER:
echo   🜂 djinn-cosmic-coder (65GB) - MoE Multimodal Sorcery
echo   🜂 djinn-deep-thinker (32GB) - Ancient Reasoning Wisdom
echo   🜂 djinn-logic-master (11GB) - Sovereign Logic Powers
echo   🜂 djinn-enterprise-architect (12GB) - Corporate Mysticism
echo.
echo 🎯 Test your enhanced federation:
echo   cd djinn-federation\launcher
echo   python efficiency_first_hub.py
echo.
echo 🜂 The Djinn Federation has evolved into its ultimate form!
echo.
pause 