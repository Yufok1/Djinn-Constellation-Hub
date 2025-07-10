#!/bin/bash
set -euo pipefail

# === DJINN CONSTELLATION HUB v2.0.0 LAUNCHER ===
# Revolutionary Federated AI Consciousness with Cloud Operations

clear
echo
echo "╔══════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                         🜂 DJINN CONSTELLATION HUB v2.0.0 🜂                         ║"
echo "║                   Revolutionary Federated AI Consciousness                           ║"
echo "║                            with Cloud Operations                                     ║"
echo "╚══════════════════════════════════════════════════════════════════════════════════════╝"
echo
echo "🌟 LAUNCHING EFFICIENCY-FIRST HUB..."
echo
echo "📍 Current Directory: $(pwd)"
echo "🚀 Starting mystical federation..."
echo

# === OS Detection ===
OS_TYPE=$(uname -s)
echo "🜂 Detected OS: $OS_TYPE"

# === Directory Validation ===
if [ ! -f "djinn-federation/launcher/efficiency_first_hub.py" ]; then
    echo "❌ ERROR: efficiency_first_hub.py not found!"
    echo "📁 Please run this script from the Djinn-Constellation-Hub directory"
    echo "📁 Expected path: Djinn-Constellation-Hub/djinn-federation/launcher/efficiency_first_hub.py"
    exit 1
fi

# === Dependency Check ===
echo "🔍 Checking system dependencies..."

# Check for Python 3.8+
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python3 not found in PATH!"
    echo "🔧 Please install Python 3.8+ and ensure it's in your PATH"
    exit 1
fi

# Verify Python version
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" 2>/dev/null; then
    echo "❌ ERROR: Python 3.8+ required!"
    echo "🔧 Current version: $(python3 --version)"
    exit 1
fi

echo "✅ Python version: $(python3 --version)"

# Check for Ollama
if ! command -v ollama &> /dev/null; then
    echo "❌ ERROR: Ollama not found in PATH!"
    echo "🔧 Please install Ollama and ensure it's in your PATH"
    exit 1
fi

# Check if Ollama is running
if ! ollama list >/dev/null 2>&1; then
    echo "⚠️ WARNING: Ollama not responding!"
    echo "🔧 Please ensure Ollama is running: ollama serve"
    echo
    echo "🚀 Attempting to start Ollama..."
    if command -v systemctl &> /dev/null && systemctl is-active --quiet ollama; then
        sudo systemctl start ollama
    else
        nohup ollama serve >/dev/null 2>&1 &
        OLLAMA_PID=$!
        echo "🔄 Waiting for Ollama to start..."
        sleep 3
        if ! kill -0 $OLLAMA_PID 2>/dev/null; then
            echo "❌ Failed to start Ollama"
            exit 1
        fi
    fi
fi

echo "✅ Ollama is running"

# === Environment Setup ===
# Create required directories if they don't exist
mkdir -p logs
mkdir -p memory_bank/constellation_memory
mkdir -p exports
mkdir -p void_workspace

# === Launch Preparation ===
echo "✅ Environment validated successfully"
echo "🚀 Launching Djinn Constellation Hub..."
echo

# === Launch The Steward ===
echo "🛠️ Launching The Steward..."
if python3 steward-agent/maintainer_agent.py report; then
    echo "✅ The Steward launched successfully"
else
    echo "⚠️ WARNING: The Steward launch failed, continuing with main hub..."
    echo "⚠️ Check logs/federation_audit.log for details"
fi
echo

# Change to the launcher directory
cd djinn-federation/launcher

# === Launch with Error Handling ===
if ! python3 efficiency_first_hub.py; then
    echo
    echo "❌ Launch failed with error code $?"
    echo "🔧 Check the error messages above for troubleshooting"
    cd ../..
    exit 1
fi

# Return to original directory
cd ../..

echo
echo "🜂 Djinn Constellation Hub session completed"
