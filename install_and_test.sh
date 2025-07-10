#!/bin/bash
# === Minimal Installer and Test Runner (Linux/macOS) ===
set -euo pipefail

command -v ollama >/dev/null 2>&1 || { echo "ERROR: ollama not found. Please install Ollama."; exit 1; }
command -v curl >/dev/null 2>&1 || { echo "ERROR: curl not found. Please install curl."; exit 1; }

echo "Running federation setup..."
bash setup_djinn_federation.sh

if [ -f logs/setup.log ]; then
    echo "=== Setup Log Summary ==="
    cat logs/setup.log
fi

if [ -f run_all_tests.sh ]; then
    echo "Running all federation tests..."
    bash run_all_tests.sh
elif [ -f run_all_tests.bat ]; then
    echo "Running all federation tests (Windows batch)..."
    cmd.exe /c run_all_tests.bat
else
    echo "No test runner found (run_all_tests.sh or .bat missing)."
fi

echo "Installer and test run complete."
