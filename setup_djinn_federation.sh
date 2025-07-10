#!/bin/bash
set -euo pipefail

# === Auto-navigation for GitHub zip extraction ===
# If this script is being run from a wrapper folder, cd into the correct folder and re-run
for dir in "Djinn-Constellation-Hub-main" "Djinn-Constellation-Hub" "Djinn-Constellation-Hub-v2.0.0"; do
    if [ -f "$dir/setup_djinn_federation.sh" ]; then
        cd "$dir"
        exec bash setup_djinn_federation.sh
    fi
done
# Try any single subdirectory with the setup script
for dir in */; do
    if [ -f "${dir}setup_djinn_federation.sh" ]; then
        cd "$dir"
        exec bash setup_djinn_federation.sh
    fi
done
# If not found, continue as normal (if we're in the right folder)

# === RAP-4+ Config-Driven Federation Setup ===
# Reads federation_setup.cfg and automates onboarding for all models/agents

# === OS Detection and Setup ===
OS_TYPE=$(uname -s)
echo "🜂 Detected OS: $OS_TYPE"

# === Dependency Check ===
echo "🔍 Checking system dependencies..."
MISSING_DEPS=""

# Check for Python 3.8+
if ! command -v python3 &> /dev/null; then
    MISSING_DEPS="$MISSING_DEPS python3"
elif ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" 2>/dev/null; then
    MISSING_DEPS="$MISSING_DEPS python3.8+"
fi

# Check for Ollama
if ! command -v ollama &> /dev/null; then
    MISSING_DEPS="$MISSING_DEPS ollama"
fi

# Check for curl
if ! command -v curl &> /dev/null; then
    MISSING_DEPS="$MISSING_DEPS curl"
fi

if [ -n "$MISSING_DEPS" ]; then
    echo "❌ Missing required dependencies: $MISSING_DEPS"
    echo "💡 Please install missing dependencies before running setup"
    exit 1
fi

echo "✅ All required dependencies found"

# === Directory Setup ===
echo "📁 Creating required directories..."
mkdir -p logs
mkdir -p memory_bank/constellation_memory
mkdir -p exports
mkdir -p void_workspace

# === Log Setup ===
LOGFILE="logs/setup.log"
: > "$LOGFILE"

echo "🜂 DJINN FEDERATION RAP-4+ AUTOMATED SETUP STARTING..." | tee -a "$LOGFILE"
echo "📝 Logging to: $LOGFILE" | tee -a "$LOGFILE"

# Status tracking
summary=""

# Helper: SHA256 check
sha256_check() {
    local file="$1"
    local expected="$2"
    if [ -z "$expected" ]; then return 0; fi
    local actual
    if command -v sha256sum &> /dev/null; then
        actual=$(sha256sum "$file" | awk '{print $1}')
    elif command -v shasum &> /dev/null; then
        actual=$(shasum -a 256 "$file" | awk '{print $1}')
    else
        echo "⚠️ No SHA256 tool available, skipping hash verification" >> "$LOGFILE"
        return 0
    fi
    [ "$actual" == "$expected" ]
}

# Check if config file exists
if [ ! -f "federation_setup.cfg" ]; then
    echo "❌ federation_setup.cfg not found!" | tee -a "$LOGFILE"
    echo "💡 Please ensure you're in the correct directory" | tee -a "$LOGFILE"
    exit 1
fi

# Read config and process each entry
while IFS=, read -r name method url hash script _; do
    name=$(echo "$name" | xargs)
    method=$(echo "$method" | xargs)
    url=$(echo "$url" | xargs)
    hash=$(echo "$hash" | xargs)
    script=$(echo "$script" | xargs)
    status="NotChecked"
    echo "=== Processing $name with method $method" >> "$LOGFILE"

    if [[ "$method" == "ollama" ]]; then
        echo "Checking for $name:latest ..."
        if ! ollama list | grep -q "$name"; then
            echo "Not present. Pulling from Ollama..." >> "$LOGFILE"
            if ! ollama pull "$name:latest" >> "$LOGFILE" 2>&1; then
                status="Error"
                echo "❌ Failed to pull $name from Ollama." >> "$LOGFILE"
            else
                status="Pulled"
                echo "✅ Pulled $name." >> "$LOGFILE"
            fi
        else
            status="Present"
            echo "✅ $name is present." >> "$LOGFILE"
        fi
    elif [[ "$method" == "batch" ]]; then
        echo "Checking for $name:latest ..."
        if ! ollama list | grep -q "$name"; then
            echo "Not present. Importing via $script ..." >> "$LOGFILE"
            if [ -f "$script" ]; then
                if ! bash "$script" "$name" >> "$LOGFILE" 2>&1; then
                    status="Error"
                    echo "❌ Failed to import $name with $script." >> "$LOGFILE"
                else
                    status="Imported"
                    echo "✅ Imported $name via $script." >> "$LOGFILE"
                fi
            else
                status="Error"
                echo "❌ Script $script not found for $name." >> "$LOGFILE"
            fi
        else
            status="Present"
            echo "✅ $name is present." >> "$LOGFILE"
        fi
    elif [[ "$method" == "cloud" ]]; then
        echo "Checking for $name.bin presence ..."
        if [ -f "$name.bin" ]; then
            status="Present"
            echo "✅ $name.bin is present." >> "$LOGFILE"
        else
            echo "Not present. Downloading from $url ..." >> "$LOGFILE"
            if curl -L --retry 3 --retry-delay 5 -o "$name.bin" "$url" >> "$LOGFILE" 2>&1; then
                if sha256_check "$name.bin" "$hash"; then
                    status="Downloaded"
                    echo "✅ Downloaded $name from cloud." >> "$LOGFILE"
                else
                    status="Error"
                    echo "❌ Hash mismatch for $name after download." >> "$LOGFILE"
                fi
            else
                status="Error"
                echo "❌ Failed to download $name from cloud." >> "$LOGFILE"
            fi
        fi
    elif [[ "$method" == "file" ]]; then
        echo "Checking for file $url ..."
        if [ -f "$url" ]; then
            status="Present"
            echo "✅ File $url is present." >> "$LOGFILE"
            # Attempt auto-import to Ollama if a script is provided
            if [ -n "$script" ] && [ -f "$script" ]; then
                echo "Attempting to auto-import $url using $script..." >> "$LOGFILE"
                if ! bash "$script" "$name" "$url" >> "$LOGFILE" 2>&1; then
                    echo "⚠️ Auto-import of $name from $url failed with $script." >> "$LOGFILE"
                else
                    echo "✅ Auto-imported $name from $url using $script." >> "$LOGFILE"
                fi
            fi
        else
            # === If .bin is missing, check for .Modelfile ===
            modelfile_name="$name.Modelfile"
            modelfile_root="$modelfile_name"
            modelfile_mods="djinn-federation/modelfiles/$modelfile_name"
            modelfile_found=""

            if [ -f "$modelfile_root" ]; then
                modelfile_found="$modelfile_root"
            fi
            if [ -f "$modelfile_mods" ]; then
                modelfile_found="$modelfile_mods"
            fi

            # Warn if both exist
            if [ -f "$modelfile_root" ] && [ -f "$modelfile_mods" ]; then
                echo "⚠️ Multiple .Modelfile files found for $name. Using $modelfile_found." >> "$LOGFILE"
            fi

            if [ -n "$modelfile_found" ]; then
                echo "📝 Found .Modelfile for $name: $modelfile_found" >> "$LOGFILE"
                echo "Attempting to create Ollama model $name from $modelfile_found..." >> "$LOGFILE"
                if ! ollama create "$name" -f "$modelfile_found" >> "$LOGFILE" 2>&1; then
                    status="Error"
                    echo "❌ Failed to create $name from .Modelfile." >> "$LOGFILE"
                else
                    status="Imported"
                    echo "✅ Created $name from .Modelfile." >> "$LOGFILE"
                fi
            else
                status="Error"
                echo "❌ File $url and .Modelfile for $name are both missing." >> "$LOGFILE"
            fi
        fi
    fi
    summary+="$name: $status\n"
done < <(grep -v '^#' federation_setup.cfg | grep -v '^$')

# === Summary Table ===
echo
echo "================= Federation Model/Agent Setup Summary ================"
printf "$summary"
echo "======================================================================"

echo "🜂 DJINN FEDERATION RAP-4+ AUTOMATED SETUP COMPLETE! 🜂"

echo
echo "🚀 STEP 1: Building DJINN-ified Constellation Coordinators..."
if [ -f "build_constellation_coordinators.sh" ]; then
    if ! bash build_constellation_coordinators.sh; then
        echo "❌ Failed to build constellation coordinators"
        exit 1
    fi
elif [ -f "build_constellation_coordinators.bat" ]; then
    echo "⚠️ Windows batch file found, but running on Unix-like system"
    echo "💡 Consider running: wine cmd /c build_constellation_coordinators.bat"
else
    echo "⚠️ No constellation coordinator build script found"
fi

echo
echo "🚀 STEP 2: Checking for base models..."
echo
echo "📋 Required base models:"
echo "  - tinydolphin:latest"
echo "  - dolphin-phi:latest"
echo "  - phi3:latest"
echo

if ! ollama list | grep -q "tinydolphin\|dolphin-phi\|phi3"; then
    echo "⚠️ Some base models may not be available"
    echo "💡 Run 'ollama pull tinydolphin:latest' if needed"
    echo "💡 Run 'ollama pull dolphin-phi:latest' if needed"
    echo "💡 Run 'ollama pull phi3:latest' if needed"
fi

echo
echo "🚀 STEP 3: Checking specialized DJINN agents and revolutionary models..."
echo
echo "📋 Required specialized agents:"
echo "  - djinn-council-enhanced-v2:latest"
echo "  - idhhc-companion:latest"
echo "  - djinn-companion:latest"
echo "  - djinn-cosmic-coder:latest"
echo "  - djinn-deep-thinker:latest"
echo "  - djinn-logic-master:latest"
echo "  - djinn-enterprise-architect:latest"

echo
echo "Checking specialized agents:"
for agent in "djinn-council-enhanced-v2" "idhhc-companion" "djinn-companion" "djinn-cosmic-coder" "djinn-deep-thinker" "djinn-logic-master" "djinn-enterprise-architect"; do
    echo "Checking for $agent:latest ..."
    if ! ollama list | grep -q "$agent"; then
        echo "⚠️ $agent is NOT present! Please ensure this model/agent is available before federation launch."
        echo "    - For advanced AIs, see:"
        echo "        create_djinn_revolutionary_models.sh"
        echo "        shadow_automation.sh"
        echo "        import_shadow_models.sh"
        echo "    - Or refer to CLOUD_SETUP_GUIDE.md for manual steps."
    else
        echo "$agent is present."
    fi
done

echo
echo "🜂 DJINN FEDERATION SETUP COMPLETE! 🜂"
echo
echo "📋 Available DJINN-ified Constellation Coordinators and Models:"
echo "  ⚡ tinydolphin-constellation (636MB) - Ultra-Fast Task Coordinator"
echo "  🐬 dolphin-phi-constellation (1.6GB) - Primary Constellation Coordinator"
echo "  🧠 phi3-constellation (2.2GB) - Complex Task Coordinator"
echo "  🌟 djinn-cosmic-coder (65GB) - MoE Multimodal Sorcery"
echo "  🧠 djinn-deep-thinker (32GB) - Ancient Wisdom"
echo "  ⚡ djinn-logic-master (11GB) - Sovereign Reasoning"
echo "  💻 djinn-enterprise-architect (22GB) - Corporate Mysticism"
echo
echo "🎯 To launch the Hierarchical Constellation Hub:"
echo "  cd djinn-federation/launcher"
echo "  python3 constellation_hub.py"
echo
echo "🜂 The mystical DJINN Federation is ready to serve! 🜂"
echo
