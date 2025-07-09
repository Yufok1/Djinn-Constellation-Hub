#!/bin/bash

echo "========================================"
echo "  🜂 DJINN FEDERATION INSTALLER"
echo "========================================"
echo
echo "Installing Complete Djinn Federation..."
echo

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed!"
    echo "Please install Ollama from https://ollama.ai first"
    exit 1
fi

echo "✅ Ollama found, proceeding with installation..."
echo

# Install base models
echo "📥 Installing base models..."
echo
ollama pull codellama:13b
ollama pull qwen2.5-coder:32b
ollama pull llama3.1:8b

echo
echo "🏗️  Building custom models..."
echo

# Build Enhanced Council v2
echo "Building Enhanced Council v2..."
cd djinn-council
ollama create djinn-council-enhanced-v2:latest -f Modelfile
cd ..

# Build IDHHC Companion
echo "Building IDHHC Companion..."
cd idhhc-companion
ollama create idhhc-companion:latest -f Modelfile
cd ..

# Build Djinn Companion
echo "Building Djinn Companion..."
cd djinn-companion
ollama create djinn-companion:latest -f Modelfile
cd ..

# Build Federation Package (optional)
echo "Building Federation Package..."
ollama create djinn-federation:latest -f federation.Modelfile

echo
echo "========================================"
echo "  �� INSTALLATION COMPLETE!"
echo "========================================"
echo
echo "✅ All models built successfully!"
echo
echo "🚀 Launch options:"
echo "   1. Enhanced Council v2: ./launch_enhanced_council_v2_constellation.bat"
echo "   2. Federation Package: ollama run djinn-federation:latest"
echo "   3. Individual models: ollama run [model-name]:latest"
echo
echo "📚 Documentation: README.md"
echo
