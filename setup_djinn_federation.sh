#!/bin/bash
set -euo pipefail

# === Config-Driven Federation Setup (Linux/macOS) ===
# Reads federation_setup.cfg and automates onboarding for all models/agents

LOGFILE="logs/setup.log"
mkdir -p logs
: > "$LOGFILE"

summary=""

# Helper: SHA256 check
sha256_check() {
    file="$1"
    expected="$2"
    if [ -z "$expected" ]; then return 0; fi
    actual=$(sha256sum "$file" | awk '{print $1}')
    [ "$actual" == "$expected" ]
}

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
            if [ -x "$script" ]; then
                if ! bash "$script" "$name" >> "$LOGFILE" 2>&1; then
                    status="Error"
                    echo "❌ Failed to import $name with $script." >> "$LOGFILE"
                else
                    status="Imported"
                    echo "✅ Imported $name via $script." >> "$LOGFILE"
                fi
            else
                status="Error"
                echo "❌ Script $script not found or not executable for $name." >> "$LOGFILE"
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
    fi
    summary+="$name: $status\n"
done < <(grep -v '^#' federation_setup.cfg | grep -v '^$')

# === Summary Table ===
echo
printf "================= Federation Model/Agent Setup Summary ================\n"
printf "$summary"
printf "=======================================================================\n"
echo "🜂 DJINN FEDERATION AUTOMATED SETUP COMPLETE! 🜂"
