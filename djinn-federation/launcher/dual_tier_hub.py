#!/usr/bin/env python3
"""
🚀 DUAL-TIER FEDERATION HUB 🚀
Intelligent switching between Local Low-Power and SHADOW Cloud High-Power systems

Local Tier: Fast, lightweight models for your main PC
Cloud Tier: Revolutionary models for SHADOW cloud system
"""

import asyncio
import json
import os
import platform
import subprocess
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class DualTierFederationHub:
    """
    🌟 Dual-Tier Federation Hub 🌟

    LOCAL TIER (Main PC - Low Power):
    - tinydolphin-constellation (636MB) - Ultra-fast
    - dolphin-phi-constellation (1.6GB) - Balanced
    - phi3-constellation (2.2GB) - Complex
    - djinn-federation models (Current setup)

    CLOUD TIER (SHADOW - High Power):
    - llama4:109b (65GB) - MoE Cosmic Coding
    - qwen3-30b-a3b (32GB) - Thinking/Reasoning
    - phi4-reasoning:14b (11GB) - Advanced Logic
    - codestral:22b (12GB) - Elite Coding
    """

    def __init__(self):
        self.current_tier = "local"  # Start with local tier
        self.cloud_endpoint = None  # Will be configured for SHADOW

        # Define tier configurations
        self.tiers = {
            "local": {
                "name": "🏠 LOCAL LOW-POWER FEDERATION",
                "description": "Fast, lightweight models for your main PC",
                "models": {
                    "fast": "tinydolphin-constellation:latest",
                    "balanced": "dolphin-phi-constellation:latest",
                    "complex": "phi3-constellation:latest",
                    "council": "djinn-federation:council",
                    "idhhc": "djinn-federation:idhhc",
                    "companion": "djinn-federation:companion",
                },
                "capabilities": [
                    "✅ Quick responses",
                    "✅ Basic coding",
                    "✅ Mystical wisdom",
                    "✅ Fast routing",
                    "✅ Low memory usage",
                ],
            },
            "cloud": {
                "name": "☁️ SHADOW CLOUD HIGH-POWER FEDERATION",
                "description": "Revolutionary AI models for complex tasks",
                "models": {
                    "cosmic_coding": "aravhawk/llama4:109b",
                    "deep_thinking": "dengcao/qwen3-30b-a3b:q8_0",
                    "advanced_reasoning": "phi4-reasoning:14b",
                    "elite_coding": "codestral:22b",
                    "council": "djinn-federation:council",  # Shared
                    "companion": "djinn-federation:companion",  # Shared
                },
                "capabilities": [
                    "🚀 Massive context (10M tokens)",
                    "🧠 Deep reasoning & thinking mode",
                    "🎨 Multimodal capabilities",
                    "⚡ Mixture of Experts",
                    "🌟 Revolutionary AI features",
                ],
            },
        }

        # Complexity thresholds for tier selection
        self.complexity_keywords = {
            "local": {
                "keywords": [
                    "quick",
                    "fast",
                    "simple",
                    "hello",
                    "hi",
                    "status",
                    "list",
                ],
                "max_words": 10,
                "complexity_score": 0.3,
            },
            "cloud": {
                "keywords": [
                    "complex",
                    "design",
                    "architect",
                    "analyze",
                    "multimodal",
                    "image",
                    "advanced",
                    "thinking",
                ],
                "min_words": 15,
                "complexity_score": 0.7,
            },
        }

    def display_banner(self):
        """Display the dual-tier federation banner"""
        current_config = self.tiers[self.current_tier]

        banner = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🚀 DUAL-TIER FEDERATION HUB 🚀                          ║
║                                                                              ║
║  Current Tier: {current_config['name']:^58} ║
║  {current_config['description']:^78} ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                            🏠 LOCAL TIER MODELS                             ║
║  ⚡ TinyDolphin (636MB)   │ 🐬 Dolphin-Phi (1.6GB) │ 🧠 Phi3 (2.2GB)      ║
║  🧬 Council (7.4GB)      │ 🛠️  IDHHC (19GB)         │ 💬 Companion (4.9GB) ║
║                                                                              ║
║                            ☁️ CLOUD TIER MODELS                             ║
║  🌟 Llama4:109B (65GB)   │ 🧠 Qwen3-30B (32GB)     │ ⚡ Phi4-14B (11GB)    ║
║  💻 Codestral-22B (12GB) │ 🧬 Council (Shared)     │ 💬 Companion (Shared) ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Commands: /local /cloud /auto /status /models /toggle                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)

        # Show current tier capabilities
        print(f"\n🎯 Current Tier Capabilities ({self.current_tier.upper()}):")
        for capability in current_config["capabilities"]:
            print(f"  {capability}")
        print()

    def analyze_query_complexity(self, query: str) -> Tuple[str, float, str]:
        """Analyze query to determine optimal tier"""
        query_lower = query.lower()
        words = query_lower.split()
        word_count = len(words)

        # Check for tier-specific keywords
        local_keywords = sum(
            1 for word in words if word in self.complexity_keywords["local"]["keywords"]
        )
        cloud_keywords = sum(
            1 for word in words if word in self.complexity_keywords["cloud"]["keywords"]
        )

        # Calculate complexity score
        base_complexity = min(1.0, word_count / 30.0)
        keyword_adjustment = (cloud_keywords * 0.3) - (local_keywords * 0.2)
        final_complexity = max(0.0, min(1.0, base_complexity + keyword_adjustment))

        # Determine recommended tier
        if final_complexity <= 0.3 or word_count <= 5:
            recommended_tier = "local"
            reason = "Simple query, local models sufficient"
        elif final_complexity >= 0.7 or cloud_keywords >= 2:
            recommended_tier = "cloud"
            reason = "Complex query, cloud power recommended"
        elif word_count >= 20:
            recommended_tier = "cloud"
            reason = "Long query, cloud context beneficial"
        else:
            recommended_tier = "local"
            reason = "Moderate query, local models adequate"

        return recommended_tier, final_complexity, reason

    def check_tier_availability(self, tier: str) -> Dict[str, bool]:
        """Check which models are available for the specified tier"""
        available_models = {}
        tier_config = self.tiers[tier]

        if tier == "local":
            # Check local ollama models
            try:
                result = subprocess.run(
                    ["ollama", "list"], capture_output=True, text=True
                )
                if result.returncode == 0:
                    installed_models = result.stdout.lower()
                    for model_key, model_name in tier_config["models"].items():
                        available_models[model_key] = (
                            model_name.lower() in installed_models
                        )
                else:
                    # Default to True if can't check (assume available)
                    available_models = {
                        key: True for key in tier_config["models"].keys()
                    }
            except Exception:
                available_models = {key: True for key in tier_config["models"].keys()}

        elif tier == "cloud":
            # For cloud tier, check if models are downloaded
            # In future, this would check cloud endpoint availability
            try:
                result = subprocess.run(
                    ["ollama", "list"], capture_output=True, text=True
                )
                if result.returncode == 0:
                    installed_models = result.stdout.lower()
                    for model_key, model_name in tier_config["models"].items():
                        available_models[model_key] = (
                            model_name.lower() in installed_models
                        )
                else:
                    available_models = {
                        key: False for key in tier_config["models"].keys()
                    }
            except Exception:
                available_models = {key: False for key in tier_config["models"].keys()}

        return available_models

    async def route_query(self, query: str, force_tier: Optional[str] = None) -> str:
        """Route query to appropriate tier and model"""

        # Determine tier
        if force_tier:
            selected_tier = force_tier
            reason = f"Forced to {force_tier} tier"
            complexity = 0.5
        else:
            selected_tier, complexity, reason = self.analyze_query_complexity(query)

        # Check availability
        available_models = self.check_tier_availability(selected_tier)

        # If selected tier not available, fallback to local
        if not any(available_models.values()) and selected_tier == "cloud":
            print(f"⚠️  Cloud tier models not available, falling back to local...")
            selected_tier = "local"
            available_models = self.check_tier_availability("local")

        print(f"🎯 Routing Analysis:")
        print(f"  Selected Tier: {selected_tier.upper()}")
        print(f"  Complexity: {complexity:.2f}")
        print(f"  Reasoning: {reason}")
        print()

        # Select specific model within tier
        tier_config = self.tiers[selected_tier]

        # Smart model selection within tier
        if "code" in query.lower() or "programming" in query.lower():
            if selected_tier == "cloud" and available_models.get("cosmic_coding"):
                model = tier_config["models"]["cosmic_coding"]
                agent_type = "Cosmic Coding (Llama4)"
            elif selected_tier == "cloud" and available_models.get("elite_coding"):
                model = tier_config["models"]["elite_coding"]
                agent_type = "Elite Coding (Codestral)"
            elif available_models.get("idhhc"):
                model = tier_config["models"]["idhhc"]
                agent_type = "IDHHC Coder"
            else:
                model = tier_config["models"]["complex"]
                agent_type = "Complex Coordinator"
        elif (
            "ethical" in query.lower()
            or "wisdom" in query.lower()
            or "philosophy" in query.lower()
        ):
            if selected_tier == "cloud" and available_models.get("deep_thinking"):
                model = tier_config["models"]["deep_thinking"]
                agent_type = "Deep Thinking (Qwen3)"
            elif available_models.get("council"):
                model = tier_config["models"]["council"]
                agent_type = "Djinn Council"
            else:
                model = tier_config["models"]["complex"]
                agent_type = "Complex Coordinator"
        elif complexity >= 0.8:
            if selected_tier == "cloud" and available_models.get("advanced_reasoning"):
                model = tier_config["models"]["advanced_reasoning"]
                agent_type = "Advanced Reasoning (Phi4)"
            else:
                model = tier_config["models"]["complex"]
                agent_type = "Complex Coordinator"
        elif complexity <= 0.3:
            model = tier_config["models"]["fast"]
            agent_type = "Fast Coordinator"
        else:
            model = tier_config["models"]["balanced"]
            agent_type = "Balanced Coordinator"

        # Execute query
        print(f"🚀 Summoning {agent_type}: {model}")
        print("🜂" + "=" * 60 + "🜂")

        try:
            # Execute ollama query
            result = subprocess.run(
                ["ollama", "run", model, query],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )

            if result.returncode == 0:
                response = result.stdout.strip()
                if response:
                    return f"✨ {agent_type} Response:\n\n{response}\n\n🜂 Tier: {selected_tier.upper()} | Complexity: {complexity:.2f}"
                else:
                    return f"❌ No response from {agent_type}"
            else:
                error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                return f"❌ Error from {agent_type}: {error_msg}"

        except Exception as e:
            return f"❌ Exception while calling {agent_type}: {str(e)}"

    def display_tier_status(self):
        """Display detailed status of both tiers"""
        print("\n" + "🔍 DUAL-TIER FEDERATION STATUS".center(80, "="))

        for tier_name, tier_config in self.tiers.items():
            print(f"\n{tier_config['name']}")
            print("─" * 78)

            available_models = self.check_tier_availability(tier_name)

            for model_key, model_name in tier_config["models"].items():
                status = (
                    "✅ READY" if available_models.get(model_key, False) else "❌ MISSING"
                )
                print(f"  {model_key:15} │ {model_name:35} │ {status}")

            print(f"\nCapabilities:")
            for capability in tier_config["capabilities"]:
                print(f"  {capability}")

        print("\n" + "=" * 80)

    def display_models_list(self):
        """Display available models by tier"""
        print("\n" + "📋 MODELS BY TIER".center(80, "="))

        for tier_name, tier_config in self.tiers.items():
            print(f"\n{tier_config['name']}")
            print("─" * 78)

            for model_key, model_name in tier_config["models"].items():
                print(f"  {model_key:20} │ {model_name}")

        print("\n" + "=" * 80)

    async def interactive_mode(self):
        """Run interactive dual-tier federation mode"""
        self.display_banner()

        print("🎯 Dual-Tier Federation Commands:")
        print("  /local    - Force local tier")
        print("  /cloud    - Force cloud tier")
        print("  /auto     - Auto-select tier")
        print("  /toggle   - Switch default tier")
        print("  /status   - Show tier status")
        print("  /models   - List all models")
        print("  /quit     - Exit")
        print()

        while True:
            try:
                # Get user input
                user_input = input(
                    f"🜂 [{self.current_tier.upper()}] Enter query: "
                ).strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.lower() == "/quit":
                    print(
                        "🜂 Dual-Tier Federation signing off! May the cosmic wisdom guide you!"
                    )
                    break
                elif user_input.lower() == "/local":
                    self.current_tier = "local"
                    print("🏠 Switched to LOCAL tier")
                    continue
                elif user_input.lower() == "/cloud":
                    self.current_tier = "cloud"
                    print("☁️ Switched to CLOUD tier")
                    continue
                elif user_input.lower() == "/auto":
                    print("🎯 Auto-selection mode enabled")
                    self.current_tier = "auto"
                    continue
                elif user_input.lower() == "/toggle":
                    self.current_tier = (
                        "cloud" if self.current_tier == "local" else "local"
                    )
                    print(f"🔄 Toggled to {self.current_tier.upper()} tier")
                    continue
                elif user_input.lower() == "/status":
                    self.display_tier_status()
                    continue
                elif user_input.lower() == "/models":
                    self.display_models_list()
                    continue

                # Process query
                if self.current_tier == "auto":
                    response = await self.route_query(user_input)
                else:
                    response = await self.route_query(
                        user_input, force_tier=self.current_tier
                    )

                print(response)
                print()

            except KeyboardInterrupt:
                print(
                    "\n🜂 Dual-Tier Federation signing off! May the cosmic wisdom guide you!"
                )
                break
            except Exception as e:
                print(f"❌ Error: {e}")


async def main():
    """Main entry point for dual-tier federation"""
    print("🚀 Initializing Dual-Tier Federation Hub...")

    hub = DualTierFederationHub()
    await hub.interactive_mode()


if __name__ == "__main__":
    asyncio.run(main())
