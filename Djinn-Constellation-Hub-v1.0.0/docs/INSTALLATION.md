# Installation Guide

## Prerequisites
- Python 3.8+
- Ollama installed
- 8GB+ RAM recommended

## Step 1: Clone Repository
```bash
git clone https://github.com/Yufok1/Djinn-Constellation-Hub.git
cd Djinn-Constellation-Hub
```

## Step 2: Install Base Models
```bash
ollama pull codellama:13b
ollama pull qwen2.5-coder:32b
ollama pull llama3.1:8b
```

## Step 3: Build Custom Models
```bash
./rebuild_council_codellama.bat
```

## Step 4: Launch Constellation Hub
```bash
./launch_enhanced_council_v2_constellation.bat
```
