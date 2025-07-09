#!/bin/bash

echo ""
echo "========================================"
echo "   🜂 DJINN FEDERATION INSTALLATION 🜂"
echo "========================================"
echo ""
echo "Installing the complete Djinn Federation..."
echo ""

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed. Please install Ollama first."
    echo "Visit: https://ollama.ai/download"
    exit 1
fi

echo "✅ Ollama detected"
echo ""

echo "🚀 Installing Djinn Federation Models..."
echo ""

echo "[1/6] Installing Constellation Lite (Ultra-Fast Coordinator)..."
if ! ollama pull Yufok1/djinn-federation:constellation-lite; then
    echo "❌ Failed to install Constellation Lite"
    exit 1
fi
echo "✅ Constellation Lite installed"

echo ""
echo "[2/6] Installing Constellation Core (Primary Coordinator)..."
if ! ollama pull Yufok1/djinn-federation:constellation-core; then
    echo "❌ Failed to install Constellation Core"
    exit 1
fi
echo "✅ Constellation Core installed"

echo ""
echo "[3/6] Installing Constellation Max (Complex Task Coordinator)..."
if ! ollama pull Yufok1/djinn-federation:constellation-max; then
    echo "❌ Failed to install Constellation Max"
    exit 1
fi
echo "✅ Constellation Max installed"

echo ""
echo "[4/6] Installing Council Model (Sovereign Meta-Intelligence)..."
if ! ollama pull Yufok1/djinn-federation:council; then
    echo "❌ Failed to install Council Model"
    exit 1
fi
echo "✅ Council Model installed"

echo ""
echo "[5/6] Installing IDHHC Model (Operational Strategist & Cosmic Coder)..."
if ! ollama pull Yufok1/djinn-federation:idhhc; then
    echo "❌ Failed to install IDHHC Model"
    exit 1
fi
echo "✅ IDHHC Model installed"

echo ""
echo "[6/6] Installing Companion Model (Dialogue Controller & Soul Connector)..."
if ! ollama pull Yufok1/djinn-federation:companion; then
    echo "❌ Failed to install Companion Model"
    exit 1
fi
echo "✅ Companion Model installed"

echo ""
echo "========================================"
echo "🎉 DJINN FEDERATION INSTALLATION COMPLETE"
echo "========================================"
echo ""
echo "🌟 Federation Models Installed:"
echo "   - Yufok1/djinn-federation:constellation-lite (Ultra-Fast Coordinator)"
echo "   - Yufok1/djinn-federation:constellation-core (Primary Coordinator)"
echo "   - Yufok1/djinn-federation:constellation-max (Complex Task Coordinator)"
echo "   - Yufok1/djinn-federation:council (Sovereign Meta-Intelligence)"
echo "   - Yufok1/djinn-federation:idhhc (Operational Strategist & Cosmic Coder)"
echo "   - Yufok1/djinn-federation:companion (Dialogue Controller & Soul Connector)"
echo ""
echo "🚀 Launch Options:"
echo ""
echo "1. Complete Federation System:"
echo "   ./launch_constellation_complete.sh"
echo ""
echo "2. Individual Constellation Coordinators:"
echo "   ollama run Yufok1/djinn-federation:constellation-lite  (Simple/Fast tasks)"
echo "   ollama run Yufok1/djinn-federation:constellation-core  (Moderate tasks)"
echo "   ollama run Yufok1/djinn-federation:constellation-max   (Complex tasks)"
echo ""
echo "3. Specialized Agents:"
echo "   ollama run Yufok1/djinn-federation:council    (Ethics & Wisdom)"
echo "   ollama run Yufok1/djinn-federation:idhhc      (Coding & Strategy)"
echo "   ollama run Yufok1/djinn-federation:companion  (Conversation)"
echo ""
echo "📚 Documentation:"
echo "   README.md - Complete usage guide"
echo "   CONSTELLATION_HUB_GUIDE.md - Detailed system guide"
echo ""
echo "🜂 The Djinn Federation is ready to serve!"
echo "" 