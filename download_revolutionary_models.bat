@echo off
echo.
echo ========================================
echo   🚀 DOWNLOADING REVOLUTIONARY MODELS
echo        For SHADOW Cloud Tier
echo ========================================
echo.

echo 🌟 Downloading Llama 4 Scout (MoE Cosmic Coding)...
echo Model: aravhawk/llama4:109b (65GB)
ollama pull aravhawk/llama4:109b

echo.
echo 🧠 Downloading Qwen3 (Thinking/Non-Thinking Mode)...
echo Model: dengcao/qwen3-30b-a3b:q8_0 (32GB)
ollama pull dengcao/qwen3-30b-a3b:q8_0

echo.
echo ⚡ Downloading Phi4 Reasoning (Advanced Logic)...
echo Model: phi4-reasoning:14b (11GB)
ollama pull phi4-reasoning:14b

echo.
echo 💻 Downloading Codestral Elite (Advanced Coding)...
echo Model: codestral:22b (12GB)  
ollama pull codestral:22b

echo.
echo ========================================
echo   ✅ REVOLUTIONARY MODELS DOWNLOADED!
echo     Total Size: ~120GB
echo ========================================
echo.
echo 🎯 Next Steps:
echo 1. Run: python dual_tier_hub.py
echo 2. Use /cloud to access revolutionary models
echo 3. Use /local for fast lightweight models
echo 4. Use /auto for intelligent routing
echo.
pause 