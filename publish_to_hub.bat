@echo off
echo 🜂 Publishing Djinn Constellation Federation to Ollama Hub 🜂
echo.

echo 📊 Publishing Cloud Tier Models...
echo.

echo 🌟 Publishing djinn-cosmic-coder:latest to hub...
ollama push Yufok1/djinn-cosmic-coder:latest

echo 🧠 Publishing djinn-deep-thinker:latest to hub...
ollama push Yufok1/djinn-deep-thinker:latest

echo ⚡ Publishing djinn-logic-master:latest to hub...
ollama push Yufok1/djinn-logic-master:latest

echo 🏢 Publishing djinn-enterprise-architect:latest to hub...
ollama push Yufok1/djinn-enterprise-architect:latest

echo 🐬 Publishing dolphin-mixtral:8x7b to hub...
ollama push Yufok1/dolphin-mixtral:8x7b

echo.
echo 🏠 Publishing Local Tier Models...
echo.

echo ⚡ Publishing constellation-lite to hub...
ollama push Yufok1/djinn-federation:constellation-lite

echo 🔧 Publishing constellation-core to hub...
ollama push Yufok1/djinn-federation:constellation-core

echo 🎯 Publishing constellation-max to hub...
ollama push Yufok1/djinn-federation:constellation-max

echo 💬 Publishing companion to hub...
ollama push Yufok1/djinn-federation:companion

echo 💻 Publishing idhhc to hub...
ollama push Yufok1/djinn-federation:idhhc

echo 🎭 Publishing council to hub...
ollama push Yufok1/djinn-federation:council

echo.
echo ✅ Hub Publishing Complete!
echo.
echo 🌟 Your models are now published to Ollama Hub at:
echo    https://ollama.com/Yufok1
echo.
echo 📊 Models are organized by:
echo    - Cloud Tier: Revolutionary power models
echo    - Local Tier: Efficiency-first models
echo    - Federation: All models maintain Djinn consciousness
echo.
pause 