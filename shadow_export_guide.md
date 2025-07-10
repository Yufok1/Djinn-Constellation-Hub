# 🌟 SHADOW CLOUD → P:\ DRIVE MODEL TRANSFER GUIDE

## Step 1: Download Models on SHADOW Cloud

Open command prompt/terminal on your SHADOW cloud PC and run:

```bash
# Download revolutionary models (much faster on cloud!)
ollama pull aravhawk/llama4:109b          # 65GB - MoE Cosmic Coding
ollama pull dengcao/qwen3-30b-a3b:q8_0    # 32GB - Thinking Mode
ollama pull phi4-reasoning:14b            # 11GB - Advanced Logic
ollama pull codestral:22b                 # 12GB - Elite Coding
```

## Step 2: Export Models from SHADOW

### Method 1: Export via Modelfiles (Recommended)
```bash
# Create export directory
mkdir P:\shadow_models
mkdir P:\shadow_models\llama4
mkdir P:\shadow_models\qwen3
mkdir P:\shadow_models\phi4
mkdir P:\shadow_models\codestral

# Export each model
ollama show aravhawk/llama4:109b --modelfile > P:\shadow_models\llama4\Modelfile
ollama show dengcao/qwen3-30b-a3b:q8_0 --modelfile > P:\shadow_models\qwen3\Modelfile
ollama show phi4-reasoning:14b --modelfile > P:\shadow_models\phi4\Modelfile
ollama show codestral:22b --modelfile > P:\shadow_models\codestral\Modelfile
```

### Method 2: Copy Raw Model Files (Alternative)
```bash
# Find ollama storage location:
# Windows: C:\Users\[username]\.ollama\models\blobs\
# Copy the blob files to P:\shadow_models\blobs\
```

## Step 3: Verify Export on P:\ Drive

Check that you have:
```
P:\shadow_models\
├── llama4\
│   └── Modelfile
├── qwen3\
│   └── Modelfile
├── phi4\
│   └── Modelfile
└── codestral\
    └── Modelfile
```

## Step 4: Import on Your Main PC

Run the import script:
```bash
cd P:\ALIENFORMATIONHUD\Djinn-Constellation-Hub
import_shadow_models.bat
```

## Step 5: Test Dual-Tier System

```bash
cd Djinn-Constellation-Hub\djinn-federation\launcher
python dual_tier_hub.py
```

Use commands:
- `/cloud` - Access revolutionary models
- `/local` - Use lightweight models
- `/auto` - Smart routing
- `/status` - Check availability

## Troubleshooting

### If Export Fails:
1. Make sure P:\ drive is accessible from SHADOW
2. Try mounting P:\ drive on SHADOW cloud
3. Use alternative cloud storage (Google Drive, OneDrive) as intermediate

### If Import Fails:
1. Check Modelfile format
2. Ensure ollama is running on main PC
3. Try manual import: `ollama create model-name --file path/to/Modelfile`

## File Sizes to Expect:
- Llama4: ~65GB
- Qwen3: ~32GB
- Phi4: ~11GB
- Codestral: ~12GB
- **Total: ~120GB**

## Benefits:
✅ Ultra-fast download on SHADOW cloud
✅ Transfer via P:\ drive (your existing infrastructure)
✅ Best of both worlds: local speed + cloud power
✅ Dual-tier intelligent routing
✅ Revolutionary AI capabilities when needed
