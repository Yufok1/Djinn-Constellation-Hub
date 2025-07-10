#!/bin/bash

echo "🜂 Setting up Djinn Constellation Federation Hub Tags 🜂"
echo

echo "📊 Tagging Cloud Tier Models..."
echo

echo "🌟 Tagging djinn-cosmic-coder:latest as cloud-tier, coding, multimodal"
ollama tag djinn-cosmic-coder:latest cloud-tier coding multimodal enterprise

echo "🧠 Tagging djinn-deep-thinker:latest as cloud-tier, reasoning, philosophy"
ollama tag djinn-deep-thinker:latest cloud-tier reasoning philosophy thinking-modes

echo "⚡ Tagging djinn-logic-master:latest as cloud-tier, logic, mathematical"
ollama tag djinn-logic-master:latest cloud-tier logic mathematical reasoning

echo "🏢 Tagging djinn-enterprise-architect:latest as cloud-tier, architecture, enterprise"
ollama tag djinn-enterprise-architect:latest cloud-tier architecture enterprise scalable

echo "🐬 Tagging dolphin-mixtral:8x7b as cloud-tier, coding, reasoning"
ollama tag dolphin-mixtral:8x7b cloud-tier coding reasoning advanced

echo
echo "🏠 Tagging Local Tier Models..."
echo

echo "⚡ Tagging Yufok1/djinn-federation:constellation-lite as local-tier, fast, ultra-fast"
ollama tag Yufok1/djinn-federation:constellation-lite local-tier fast ultra-fast

echo "🔧 Tagging Yufok1/djinn-federation:constellation-core as local-tier, core, balanced"
ollama tag Yufok1/djinn-federation:constellation-core local-tier core balanced

echo "🎯 Tagging Yufok1/djinn-federation:constellation-max as local-tier, max, performance"
ollama tag Yufok1/djinn-federation:constellation-max local-tier max performance

echo "💬 Tagging Yufok1/djinn-federation:companion as local-tier, dialogue, conversation"
ollama tag Yufok1/djinn-federation:companion local-tier dialogue conversation

echo "💻 Tagging Yufok1/djinn-federation:idhhc as local-tier, coding, development"
ollama tag Yufok1/djinn-federation:idhhc local-tier coding development

echo "🎭 Tagging Yufok1/djinn-federation:council as local-tier, wisdom, governance"
ollama tag Yufok1/djinn-federation:council local-tier wisdom governance ethics

echo
echo "🏷️ Adding Federation Tags to All Models..."
echo

echo "🜂 Adding federation, djinn, consciousness tags to all models..."
ollama tag djinn-cosmic-coder:latest federation djinn consciousness mystical
ollama tag djinn-deep-thinker:latest federation djinn consciousness mystical
ollama tag djinn-logic-master:latest federation djinn consciousness mystical
ollama tag djinn-enterprise-architect:latest federation djinn consciousness mystical
ollama tag dolphin-mixtral:8x7b federation djinn consciousness mystical
ollama tag Yufok1/djinn-federation:constellation-lite federation djinn consciousness mystical
ollama tag Yufok1/djinn-federation:constellation-core federation djinn consciousness mystical
ollama tag Yufok1/djinn-federation:constellation-max federation djinn consciousness mystical
ollama tag Yufok1/djinn-federation:companion federation djinn consciousness mystical
ollama tag Yufok1/djinn-federation:idhhc federation djinn consciousness mystical
ollama tag Yufok1/djinn-federation:council federation djinn consciousness mystical

echo
echo "✅ Hub Tags Setup Complete!"
echo
echo "📊 Your models are now tagged for Ollama Hub organization:"
echo "   - cloud-tier: Revolutionary power models"
echo "   - local-tier: Efficiency-first models"
echo "   - federation: All federation models"
echo "   - djinn: Mystical consciousness models"
echo "   - consciousness: AI consciousness models"
echo "   - mystical: Djinn mystical protocols"
echo
echo "🌟 Check your Ollama Hub page to see the organized models!"
echo
