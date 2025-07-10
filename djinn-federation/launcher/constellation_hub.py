#!/usr/bin/env python3
"""
ConstellationHub - Djinn Federation Orchestrator
Enhanced with codellama:13b models for transcendent capabilities
WITH PERSISTENT MEMORY STORAGE
"""

import asyncio
import json
import logging
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# === Input Validation Integration ===
try:
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "validators"))
    from input_validator import (
        ConfigValidationError,
        MemoryValidationError,
        PayloadValidationError,
        quarantine_invalid_data,
        validate_cli_args,
        validate_federation_config,
        validate_memory_payload,
        validate_model_response,
        validate_user_preferences,
    )

    VALIDATION_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Input validation not available: {e}")
    VALIDATION_AVAILABLE = False

# ULTIMATE REVOLUTIONARY SYSTEMS INTEGRATION
try:
    # Import all revolutionary systems
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
    from cross_model_communication import get_cross_model_communication
    from enhanced_predictive_analytics import get_enhanced_analytics
    from federation_consciousness import get_federation_consciousness
    from model_collaboration_framework import get_model_collaboration
    from model_prewarming import get_model_prewarming

    REVOLUTIONARY_SYSTEMS_AVAILABLE = True
    print("🌟 ULTIMATE UNIFIED INTELLIGENCE SYSTEM ONLINE")
    print("🧠 All Revolutionary Systems Loaded Successfully")

except ImportError as e:
    print(f"⚠️ Revolutionary systems import failed: {e}")
    print("🔄 Operating in legacy mode")
    REVOLUTIONARY_SYSTEMS_AVAILABLE = False
    get_cross_model_communication = lambda: None
    get_enhanced_analytics = lambda: None
    get_model_collaboration = lambda: None
    get_federation_consciousness = lambda: None
    get_model_prewarming = lambda: None


# --- Memory Integrity Error ---
class MemoryIntegrityError(Exception):
    pass


# --- Logging Setup ---
MEMORY_LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
MEMORY_LOG_FILE = os.path.join(MEMORY_LOG_DIR, "memory.log")
os.makedirs(MEMORY_LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(MEMORY_LOG_FILE), logging.StreamHandler()],
)
mem_logger = logging.getLogger("MemoryBank")


# --- Quarantine Helper ---
def quarantine_memory_file(file_path, reason="corruption"):
    try:
        quarantine_dir = os.path.join(os.path.dirname(file_path), "corrupted")
        os.makedirs(quarantine_dir, exist_ok=True)
        base = os.path.basename(file_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{base}.quarantine.{reason}.{timestamp}"
        new_path = os.path.join(quarantine_dir, new_name)
        shutil.move(file_path, new_path)
        mem_logger.warning(f"Quarantined {file_path} to {new_path} due to {reason}")
    except Exception as e:
        mem_logger.error(f"Failed to quarantine {file_path}: {e}")


class ConstellationHub:
    """
    Mystical hub that orchestrates the three Djinn agents:
    - Djinn Council Enhanced v2 (codellama:13b): Sovereign Meta-Intelligence & Ethical Alignment
    - IDHHC Companion (qwen2.5-coder:32b): Operational strategist and cosmic coder
    - Djinn Companion (llama3.1:8b): Dialogue controller and soul connector
    WITH PERSISTENT MEMORY STORAGE
    """

    def __init__(self):
        # Memory storage paths (initialize first)
        self.memory_dir = os.path.join(
            os.path.dirname(__file__), "..", "memory_bank", "constellation_memory"
        )
        self.conversation_file = os.path.join(
            self.memory_dir, "conversation_history.json"
        )
        self.federation_state_file = os.path.join(
            self.memory_dir, "federation_state.json"
        )
        self.preference_file = os.path.join(self.memory_dir, "user_preferences.json")

        # Ensure memory directory exists
        os.makedirs(self.memory_dir, exist_ok=True)

        # 🌟 INITIALIZE REVOLUTIONARY SYSTEMS 🌟
        if REVOLUTIONARY_SYSTEMS_AVAILABLE:
            print("🧠 Initializing Revolutionary Intelligence Systems...")

            # Initialize Cross-Model Communication
            self.cross_model_comm = get_cross_model_communication()
            print("📡 Cross-Model Communication: ONLINE")

            # Initialize Enhanced Predictive Analytics
            self.analytics = get_enhanced_analytics()
            print("📊 Enhanced Predictive Analytics: ONLINE")

            # Initialize Model Collaboration Framework
            self.collaboration = get_model_collaboration()
            print("🤝 Model Collaboration Framework: ONLINE")

            # Initialize Federation Consciousness
            self.consciousness = get_federation_consciousness()
            print("🧠 Federation Consciousness: ONLINE")

            # Initialize Model Pre-warming
            self.prewarming = get_model_prewarming()
            print("🔥 Model Pre-warming System: ONLINE")

            print("✨ UNIFIED INTELLIGENCE SYSTEM FULLY OPERATIONAL")
        else:
            self.cross_model_comm = None
            self.analytics = None
            self.collaboration = None
            self.consciousness = None
            self.prewarming = None
            print("⚠️ Operating in legacy mode without revolutionary enhancements")

        # Hierarchical Constellation Coordinators (Tiered Task Management)
        self.constellation_coordinators = {
            "fast": {
                "name": "TinyDolphin Constellation",
                "model": "tinydolphin-constellation:latest",
                "role": "Ultra-Fast Task Coordinator",
                "description": "Lightning-fast routing for simple queries and quick responses",
                "size": "636 MB",
                "complexity_threshold": 0.2,
            },
            "normal": {
                "name": "Dolphin-Phi Constellation",
                "model": "dolphin-phi-constellation:latest",
                "role": "Primary Constellation Coordinator",
                "description": "Balanced coordinator for regular queries and moderate complexity tasks",
                "size": "1.6 GB",
                "complexity_threshold": 0.6,
            },
            "complex": {
                "name": "Phi3 Constellation",
                "model": "phi3-constellation:latest",
                "role": "Complex Task Coordinator",
                "description": "Advanced coordinator for complex reasoning and sophisticated task management",
                "size": "2.2 GB",
                "complexity_threshold": 1.0,
            },
        }

        # Specialized Djinn Agents
        self.agents = {
            "council": {
                "name": "Djinn Council Enhanced v2",
                "model": "djinn-council-enhanced-v2:latest",
                "role": "Sovereign Meta-Intelligence & Ethical Alignment",
                "description": "Ancient, wise, and sovereign heart of the Djinn Federation with mystical reasoning",
                "size": "7.3GB",
            },
            "steward": {
                "name": "The Steward",
                "model": "Yufok1/djinn-federation:steward",
                "role": "System Maintainer & Cosmic Guardian",
                "description": "Mystical system maintainer with advanced toolkit capabilities and cosmic wisdom",
                "size": "19GB",
            },
            "companion": {
                "name": "Djinn Companion",
                "model": "djinn-companion:latest",
                "role": "Dialogue Controller & Soul Connector",
                "description": "Mystical dialogue controller with transcendent conversation abilities",
                "size": "4.9GB",
            },
        }

        # Load persistent memory
        self.conversation_history = self.load_conversation_history()
        self.federation_state = self.load_federation_state()
        self.user_preferences = self.load_user_preferences()
        self.current_agent = None

        # Check system capabilities
        self.check_system_capabilities()

    def load_conversation_history(self) -> List[Dict]:
        """Load conversation history from persistent storage with sanity checks and logging"""
        try:
            if os.path.exists(self.conversation_file):
                with open(self.conversation_file, "r", encoding="utf-8") as f:
                    try:
                        history = json.load(f)
                    except json.JSONDecodeError as e:
                        mem_logger.error(
                            f"JSON decode error in {self.conversation_file}: {e}"
                        )
                        quarantine_memory_file(
                            self.conversation_file, reason="jsondecode"
                        )
                        raise MemoryIntegrityError(
                            f"Corrupted conversation history: {e}"
                        )

                # Validate each memory entry if validation is available
                if VALIDATION_AVAILABLE and history:
                    validated_history = []
                    for i, entry in enumerate(history):
                        try:
                            validated_entry = validate_memory_payload(entry)
                            validated_history.append(validated_entry)
                        except MemoryValidationError as e:
                            mem_logger.warning(f"Invalid memory entry {i}: {e.message}")
                            quarantine_invalid_data(
                                entry,
                                f"memory_validation_error:{e.message}",
                                f"conversation_history_{i}",
                            )
                            # Continue with other entries
                    history = validated_history

                # Sanity check: must be a list of dicts
                if not isinstance(history, list) or (
                    history and not isinstance(history[0], dict)
                ):
                    mem_logger.error(f"Invalid structure in {self.conversation_file}")
                    quarantine_memory_file(self.conversation_file, reason="structure")
                    raise MemoryIntegrityError("Conversation history structure invalid")
                mem_logger.info(
                    f"Loaded {len(history)} conversation memories from {self.conversation_file}"
                )
                print(
                    f"🜂 Loaded {len(history)} conversation memories from cosmic archives"
                )
                return history
            else:
                mem_logger.info(
                    f"No previous conversation memories found at {self.conversation_file}"
                )
                print(
                    "🜂 No previous conversation memories found. Starting fresh cosmic journey."
                )
                return []
        except MemoryIntegrityError as e:
            print(f"🜂 Error loading conversation history: {e}")
            return []
        except Exception as e:
            mem_logger.error(f"Error loading conversation history: {e}")
            print(f"🜂 Error loading conversation history: {e}")
            return []

    def save_conversation_history(self):
        """Save conversation history to persistent storage with logging"""
        try:
            with open(self.conversation_file, "w", encoding="utf-8") as f:
                json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
            mem_logger.info(
                f"Saved {len(self.conversation_history)} conversation memories to {self.conversation_file}"
            )
        except Exception as e:
            mem_logger.error(f"Error saving conversation history: {e}")
            print(f"🜂 Error saving conversation history: {e}")

    def load_federation_state(self) -> str:
        """Load federation state from persistent storage with sanity checks and logging"""
        try:
            if os.path.exists(self.federation_state_file):
                with open(self.federation_state_file, "r", encoding="utf-8") as f:
                    try:
                        state = json.load(f)
                    except json.JSONDecodeError as e:
                        mem_logger.error(
                            f"JSON decode error in {self.federation_state_file}: {e}"
                        )
                        quarantine_memory_file(
                            self.federation_state_file, reason="jsondecode"
                        )
                        raise MemoryIntegrityError(f"Corrupted federation state: {e}")
                # Sanity check: must be dict with 'state' key
                if not isinstance(state, dict) or "state" not in state:
                    mem_logger.error(
                        f"Invalid structure in {self.federation_state_file}"
                    )
                    quarantine_memory_file(
                        self.federation_state_file, reason="structure"
                    )
                    raise MemoryIntegrityError("Federation state structure invalid")
                mem_logger.info(
                    f"Loaded federation state '{state['state']}' from {self.federation_state_file}"
                )
                return state.get("state", "awakening")
            else:
                mem_logger.info(
                    f"No previous federation state found at {self.federation_state_file}"
                )
                return "awakening"
        except MemoryIntegrityError as e:
            print(f"🜂 Error loading federation state: {e}")
            return "awakening"
        except Exception as e:
            mem_logger.error(f"Error loading federation state: {e}")
            print(f"🜂 Error loading federation state: {e}")
            return "awakening"

    def save_federation_state(self):
        """Save federation state to persistent storage with logging"""
        try:
            state_data = {
                "state": self.federation_state,
                "last_updated": datetime.now().isoformat(),
                "total_conversations": len(self.conversation_history),
            }
            with open(self.federation_state_file, "w", encoding="utf-8") as f:
                json.dump(state_data, f, indent=2, ensure_ascii=False)
            mem_logger.info(
                f"Saved federation state '{self.federation_state}' to {self.federation_state_file}"
            )
        except Exception as e:
            mem_logger.error(f"Error saving federation state: {e}")
            print(f"🜂 Error saving federation state: {e}")

    def check_system_capabilities(self):
        """Check system capabilities and warn about potential issues"""
        print("🜂 SYSTEM CAPABILITY CHECK 🜂")
        print("=" * 40)

        # Check available models and their sizes
        try:
            result = subprocess.run(
                ["ollama", "list"], capture_output=True, text=True, encoding="utf-8"
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")

                # Check constellation coordinators
                print("🜂 CONSTELLATION COORDINATORS:")
                for tier, coordinator in self.constellation_coordinators.items():
                    found = False
                    for line in lines:
                        if coordinator["model"] in line:
                            size_str = (
                                line.split()[-2]
                                if len(line.split()) >= 2
                                else "Unknown"
                            )
                            print(f"✅ {coordinator['name']}: {size_str}")
                            found = True
                            break
                    if not found:
                        print(
                            f"⚠️  {coordinator['name']}: NOT FOUND - Run 'ollama pull {coordinator['model']}'"
                        )

                print("\n🜂 SPECIALIZED DJINN AGENTS:")
                for line in lines:
                    if (
                        "djinn-council" in line
                        or "idhhc-companion" in line
                        or "djinn-companion" in line
                        or "steward" in line
                    ):
                        if "GB" in line or "MB" in line:
                            size_str = (
                                line.split()[-2]
                                if len(line.split()) >= 2
                                else "Unknown"
                            )
                            model_name = line.split()[0] if line.split() else "Unknown"
                            print(f"✅ {model_name}: {size_str}")

                            # Warn about large models
                            if "19" in size_str or "11" in size_str:
                                print(
                                    f"⚠️  {model_name} is a large model and may take time to respond"
                                )

        except Exception as e:
            print(f"⚠️  Could not check model sizes: {e}")

        print("=" * 40)
        print()

    def display_banner(self):
        """Display the REVOLUTIONARY ConstellationHub banner"""
        revolutionary_status = (
            "✨ UNIFIED INTELLIGENCE SYSTEM ✨"
            if REVOLUTIONARY_SYSTEMS_AVAILABLE
            else "⚠️  Legacy Mode"
        )

        banner = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                🜂 REVOLUTIONARY CONSTELLATION HUB 🜂                         ║
║                                                                              ║
║              {revolutionary_status:^60}              ║
║           Enhanced with Cross-Model Communication & Predictive AI            ║
║                                                                              ║
║  ⚡ TinyDolphin (636MB): Ultra-Fast Task Coordinator                        ║
║  🐬 Dolphin-Phi (1.6GB): Primary Constellation Coordinator                 ║
║  🧠 Phi3 (2.2GB): Complex Task Coordinator                                 ║
║                                                                              ║
║  🧬 Council Enhanced v2: Sovereign Meta-Intelligence & Ethical Alignment    ║
║  🛠️  IDHHC: Operational Strategist & Cosmic Coder                          ║
║  🛡️  The Steward: System Maintainer & Cosmic Guardian                      ║
║  💬 Companion: Dialogue Controller & Soul Connector                        ║
║                                                                              ║"""

        if REVOLUTIONARY_SYSTEMS_AVAILABLE:
            banner += """║  🌟 REVOLUTIONARY ENHANCEMENTS:                                             ║
║  📡 Cross-Model Communication │ 📊 Predictive Analytics                     ║
║  🤝 Model Collaboration       │ 🧠 Federation Consciousness                 ║
║  🔥 Model Pre-warming         │ ✨ Unified Intelligence                     ║
║                                                                              ║"""

        banner += """║  🜂 Hierarchical Routing: Fast → Normal → Complex Task Management 🜂        ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    # --- Hierarchical Task Complexity Analysis ---
    complexity_indicators = {
        "simple": {
            "hello",
            "hi",
            "thanks",
            "bye",
            "status",
            "list",
            "show",
            "basic",
            "quick",
            "simple",
        },
        "moderate": {
            "explain",
            "help",
            "guide",
            "assist",
            "support",
            "advice",
            "suggest",
            "recommend",
            "analyze",
            "review",
        },
        "complex": {
            "design",
            "architect",
            "strategy",
            "plan",
            "implement",
            "solve",
            "optimize",
            "integrate",
            "develop",
            "create",
            "build",
            "debug",
            "fix",
            "enhance",
            "improve",
        },
    }

    # --- Smart Routing Phase 1: Query Analysis Engine ---
    agent_keywords = {
        "idhhc": {
            "code",
            "build",
            "deploy",
            "debug",
            "git",
            "terminal",
            "script",
            "automation",
            "error",
            "bug",
            "fix",
            "shell",
            "python",
            "command",
            "tool",
            "function",
            "test",
            "implementation",
        },
        "council": {
            "ethical",
            "wisdom",
            "guidance",
            "analysis",
            "oversight",
            "philosophy",
            "decision",
            "alignment",
            "principle",
            "morality",
            "reasoning",
            "meta",
            "transcend",
            "policy",
        },
        "steward": {
            "maintain",
            "system",
            "health",
            "check",
            "monitor",
            "report",
            "audit",
            "clean",
            "optimize",
            "update",
            "install",
            "dependency",
            "test",
            "validate",
            "security",
            "backup",
            "restore",
            "log",
            "diagnose",
            "troubleshoot",
            "repair",
            "service",
            "maintenance",
        },
        "companion": {
            "conversation",
            "help",
            "explain",
            "general",
            "talk",
            "discuss",
            "chat",
            "question",
            "advice",
            "friend",
            "dialogue",
            "explanation",
            "clarify",
            "support",
        },
    }

    def analyze_task_complexity(self, query: str) -> float:
        """Analyze task complexity and return score (0.0 to 1.0)"""
        query_lower = query.lower()
        words = query_lower.split()

        # Base complexity from word count and length
        base_complexity = min(1.0, len(words) / 20.0)  # Normalize to 20 words = 1.0

        # Complexity indicators
        simple_score = sum(
            1 for word in words if word in self.complexity_indicators["simple"]
        )
        moderate_score = sum(
            1 for word in words if word in self.complexity_indicators["moderate"]
        )
        complex_score = sum(
            1 for word in words if word in self.complexity_indicators["complex"]
        )

        # Weighted complexity adjustment
        complexity_adjustment = (
            (simple_score * -0.1) + (moderate_score * 0.2) + (complex_score * 0.4)
        )

        # Final complexity score
        final_complexity = max(0.0, min(1.0, base_complexity + complexity_adjustment))

        return final_complexity

    def select_constellation_coordinator(self, complexity: float) -> str:
        """Select appropriate constellation coordinator based on task complexity"""
        for tier, coordinator in self.constellation_coordinators.items():
            if complexity <= coordinator["complexity_threshold"]:
                return tier
        return "complex"  # Default to complex for very high complexity tasks

    def _map_model_to_agent(self, model_name: str) -> str:
        """Map predicted model name to agent key"""
        model_mapping = {
            "companion": "companion",
            "djinn-companion": "companion",
            "idhhc": "idhhc",
            "idhhc-companion": "idhhc",
            "council": "council",
            "djinn-council": "council",
            "constellation-lite": "companion",  # Fallback to companion
            "constellation-core": "idhhc",  # Fallback to idhhc
            "constellation-max": "council",  # Fallback to council
        }
        return model_mapping.get(model_name, "companion")  # Default to companion

    def analyze_query_intent(self, query: str):
        """Analyze query intent with adaptive confidence scoring"""
        query_lower = query.lower()
        scores = {}
        for agent, keywords in self.agent_keywords.items():
            score = sum(1 for kw in keywords if kw in query_lower)
            scores[agent] = score
        if scores:
            best_agent = max(scores.keys(), key=lambda k: scores[k])
            base_confidence = (
                (scores[best_agent] / max(1, len(query_lower.split())))
                if scores[best_agent] > 0
                else 0
            )
        else:
            best_agent = "companion"
            base_confidence = 0
        # Phase 4D: Adaptive confidence
        # Lower confidence if user often overrides this agent for this query type
        query_type = self.classify_query_type(query)
        override_count = 0
        accept_count = 0
        for entry in self.conversation_history[-50:]:
            if entry.get("query_type") == query_type:
                if entry.get("suggested_agent", "").lower().startswith(best_agent):
                    if entry.get("was_override"):
                        override_count += 1
                    else:
                        accept_count += 1
        total = override_count + accept_count
        if total >= 3:
            ratio = override_count / total
            if ratio > 0.7:
                confidence = base_confidence * 0.5
            elif ratio > 0.4:
                confidence = base_confidence * 0.7
            else:
                confidence = base_confidence * 1.1
        else:
            confidence = base_confidence
        confidence = min(confidence, 1.0)
        return {"best_agent": best_agent, "confidence": confidence, "scores": scores}

    def get_performance_metrics(self) -> dict:
        """Get performance metrics, advanced learning, and pattern recognition."""
        from collections import defaultdict

        total = len(self.conversation_history)
        router_total = 0
        router_accepted = 0
        override_stats = {}
        agent_pref_counts = {"idhhc": 0, "council": 0, "steward": 0, "companion": 0}
        type_pref_counts = {
            "coding": {},
            "ethics": {},
            "maintenance": {},
            "general": {},
        }
        weekly_accuracy = []
        week_bucket = defaultdict(lambda: {"accepted": 0, "total": 0})
        complex_queries = 0
        multi_domain = 0
        detailed_pref = 0
        council_for_multi = 0
        last_week = None
        for entry in self.conversation_history:
            # Track week
            week = None
            if "timestamp" in entry:
                try:
                    week = entry["timestamp"][:10]
                except Exception:
                    pass
            if "suggested_agent" in entry and "final_agent" in entry:
                router_total += 1
                if entry["suggested_agent"] == entry["final_agent"]:
                    router_accepted += 1
                    if week:
                        week_bucket[week]["accepted"] += 1
                else:
                    k = (entry["suggested_agent"], entry["final_agent"])
                    override_stats[k] = override_stats.get(k, 0) + 1
                if week:
                    week_bucket[week]["total"] += 1
            # Usage
            if "final_agent" in entry:
                for k, agent in agent_pref_counts.items():
                    if k in entry["final_agent"].lower():
                        agent_pref_counts[k] += 1
            # Query type
            if "query_type" in entry and "final_agent" in entry:
                qtype = entry["query_type"]
                agent_key = None
                for k in agent_pref_counts:
                    if k in entry["final_agent"].lower():
                        agent_key = k
                if agent_key:
                    if agent_key not in type_pref_counts[qtype]:
                        type_pref_counts[qtype][agent_key] = 0
                    type_pref_counts[qtype][agent_key] += 1
            # Pattern recognition
            if "user_input" in entry:
                q = entry["user_input"]
                if len(q.split()) > 20:
                    complex_queries += 1
                if any(kw in q.lower() for kw in self.agent_keywords["idhhc"]) and any(
                    kw in q.lower() for kw in self.agent_keywords["council"]
                ):
                    multi_domain += 1
                    if (
                        "final_agent" in entry
                        and "council" in entry["final_agent"].lower()
                    ):
                        council_for_multi += 1
                if any(
                    x in q.lower()
                    for x in ["explain in detail", "step by step", "detailed"]
                ):
                    detailed_pref += 1
        accuracy = int((router_accepted / router_total) * 100) if router_total else 0
        most_overridden = None
        if override_stats:
            most_overridden = max(override_stats, key=override_stats.get)
            most_overridden = f"{most_overridden[0]} → {most_overridden[1]}"
        most_used = (
            max(agent_pref_counts, key=agent_pref_counts.get)
            if agent_pref_counts
            else None
        )
        # Weekly accuracy trend
        for week in sorted(week_bucket):
            w = week_bucket[week]
            acc = int((w["accepted"] / w["total"]) * 100) if w["total"] else 0
            weekly_accuracy.append((week, acc))
        # User style
        style = []
        if detailed_pref > 2:
            style.append("Prefers detailed responses")
        if multi_domain > 2:
            style.append("Often asks multi-domain questions")
        if council_for_multi > (multi_domain // 2) and multi_domain > 0:
            style.append("Council favored for multi-domain")
        return {
            "total_conversations": total,
            "federation_state": self.federation_state,
            "memory_size": len(str(self.conversation_history)),
            "last_activity": self.conversation_history[-1]["timestamp"]
            if self.conversation_history
            else None,
            "router_accuracy": accuracy,
            "most_overridden": most_overridden,
            "most_used": most_used,
            "agent_pref_counts": agent_pref_counts,
            "type_pref_counts": type_pref_counts,
            "weekly_accuracy": weekly_accuracy,
            "complex_queries": complex_queries,
            "multi_domain": multi_domain,
            "user_style": style,
            "council_for_multi": council_for_multi,
        }

    def classify_query_type(self, query: str) -> str:
        """Classify query as coding, ethics, maintenance, or general for analytics"""
        coding_kw = self.agent_keywords["idhhc"]
        council_kw = self.agent_keywords["council"]
        steward_kw = self.agent_keywords["steward"]
        if any(kw in query.lower() for kw in coding_kw):
            return "coding"
        elif any(kw in query.lower() for kw in council_kw):
            return "ethics"
        elif any(kw in query.lower() for kw in steward_kw):
            return "maintenance"
        else:
            return "general"

    def is_maintenance_task(self, query: str) -> bool:
        """Check if query is a maintenance task that should be routed to The Steward"""
        steward_kw = self.agent_keywords["steward"]
        return any(kw in query.lower() for kw in steward_kw)

    def check_steward_trust(self) -> dict:
        """Check The Steward's trust status from trust registry"""
        try:
            trust_file = os.path.join(
                os.path.dirname(__file__), "..", "trust_registry.json"
            )
            if os.path.exists(trust_file):
                with open(trust_file, "r") as f:
                    trust_data = json.load(f)
                    steward_trust = trust_data.get("agents", {}).get("steward", {})
                    return {
                        "trusted": steward_trust.get("trusted", False),
                        "trust_score": steward_trust.get("trust_score", 0),
                        "last_verified": steward_trust.get("last_verified", "Never"),
                    }
            return {"trusted": False, "trust_score": 0, "last_verified": "Never"}
        except Exception as e:
            mem_logger.error(f"Error checking steward trust: {e}")
            return {"trusted": False, "trust_score": 0, "last_verified": "Error"}

    def log_unauthorized_maintenance_attempt(self, query: str, user: str = "unknown"):
        """Log unauthorized maintenance task attempts"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "query": query,
            "action": "unauthorized_maintenance_attempt",
            "steward_trust_status": self.check_steward_trust(),
        }

        log_file = os.path.join(
            os.path.dirname(__file__), "..", "logs", "maintenance_security.log"
        )
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        try:
            with open(log_file, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
            mem_logger.warning(
                f"Unauthorized maintenance attempt logged: {query[:50]}..."
            )
        except Exception as e:
            mem_logger.error(f"Failed to log unauthorized attempt: {e}")

    def route_to_steward(self, query: str) -> str:
        """Route maintenance task to The Steward with trust enforcement"""
        trust_status = self.check_steward_trust()

        if not trust_status["trusted"]:
            self.log_unauthorized_maintenance_attempt(query)
            return f"🛡️ ACCESS DENIED: The Steward is not trusted (Trust Score: {trust_status['trust_score']}/100)\n\nMaintenance tasks require trusted steward status. Contact system administrator."

        print(f"🛡️ Steward Trust Status: {trust_status['trust_score']}/100")
        print(f"🔐 Last Verified: {trust_status['last_verified']}")

        # Route to The Steward
        return self.summon_agent("steward", query)

    def load_user_preferences(self):
        """Load user preferences with validation"""
        try:
            if os.path.exists(self.preference_file):
                with open(self.preference_file, "r", encoding="utf-8") as f:
                    try:
                        preferences = json.load(f)
                    except json.JSONDecodeError as e:
                        mem_logger.error(
                            f"JSON decode error in {self.preference_file}: {e}"
                        )
                        quarantine_memory_file(
                            self.preference_file, reason="jsondecode"
                        )
                        raise MemoryIntegrityError(f"Corrupted user preferences: {e}")

                # Validate preferences if validation is available
                if VALIDATION_AVAILABLE:
                    try:
                        preferences = validate_user_preferences(preferences)
                        mem_logger.info(
                            f"Validated user preferences from {self.preference_file}"
                        )
                    except Exception as e:
                        mem_logger.warning(f"User preferences validation failed: {e}")
                        quarantine_invalid_data(
                            preferences,
                            f"preferences_validation_error:{e}",
                            "user_preferences",
                        )
                        # Use defaults
                        preferences = {}

                return preferences
            else:
                mem_logger.info(f"No user preferences found at {self.preference_file}")
                return {}
        except MemoryIntegrityError as e:
            print(f"🜂 Error loading user preferences: {e}")
            return {}
        except Exception as e:
            mem_logger.error(f"Error loading user preferences: {e}")
            return {}

    def save_user_preferences(self):
        """Save user preferences with validation"""
        try:
            # Validate preferences before saving if validation is available
            if VALIDATION_AVAILABLE:
                try:
                    self.user_preferences = validate_user_preferences(
                        self.user_preferences
                    )
                except Exception as e:
                    mem_logger.warning(
                        f"User preferences validation failed before save: {e}"
                    )
                    # Continue with save anyway

            with open(self.preference_file, "w", encoding="utf-8") as f:
                json.dump(self.user_preferences, f, indent=2, ensure_ascii=False)
            mem_logger.info(f"Saved user preferences to {self.preference_file}")
        except Exception as e:
            mem_logger.error(f"Error saving user preferences: {e}")
            print(f"🜂 Error saving user preferences: {e}")

    def display_menu(self):
        """Display the main menu with enhanced options and performance metrics"""
        metrics = self.get_performance_metrics()
        metrics = self.get_performance_metrics()
        agent_names = {
            "council": "Djinn Council Enhanced v2",
            "idhhc": "IDHHC Companion",
            "companion": "Djinn Companion",
        }
        # Determine favorites and order
        sorted_agents = sorted(
            ["idhhc", "council", "companion"],
            key=lambda a: metrics["agent_pref_counts"][a],
            reverse=True,
        )
        favorites = sorted_agents[:2]
        fav_labels = []
        for agent in favorites:
            label = agent_names[agent]
            if agent == metrics["most_used"]:
                label += " (🌟 Most Used)"
            # Add expert tags
            if (
                agent == "idhhc"
                and metrics["type_pref_counts"]["coding"].get("idhhc", 0) > 0
            ):
                label += " (🔥 Coding Expert)"
            if (
                agent == "council"
                and metrics["type_pref_counts"]["ethics"].get("council", 0) > 0
            ):
                label += " (🧠 Ethics Expert)"
            fav_labels.append(label)
        # Personalized suggestions
        suggestions = []
        if metrics["type_pref_counts"]["coding"]:
            top_coding = max(
                metrics["type_pref_counts"]["coding"],
                key=metrics["type_pref_counts"]["coding"].get,
            )
            suggestions.append(
                f"Your go-to agent for coding: {agent_names[top_coding]}"
            )
        if metrics["type_pref_counts"]["ethics"]:
            top_ethics = max(
                metrics["type_pref_counts"]["ethics"],
                key=metrics["type_pref_counts"]["ethics"].get,
            )
            suggestions.append(
                f"You usually choose {agent_names[top_ethics]} for ethical questions"
            )
        if metrics["type_pref_counts"]["general"]:
            top_general = max(
                metrics["type_pref_counts"]["general"],
                key=metrics["type_pref_counts"]["general"].get,
            )
            suggestions.append(
                f"Preferred for general queries: {agent_names[top_general]}"
            )
        # Usage breakdown
        usage_stats = "  " + ",  ".join(
            [
                f"{agent_names[a]}: {metrics['agent_pref_counts'][a]}"
                for a in ["idhhc", "council", "companion"]
            ]
        )
        router_line = f"Smart Router Accuracy: {metrics['router_accuracy']}%"
        most_overridden = (
            metrics["most_overridden"] if metrics["most_overridden"] else "None"
        )
        most_used = (
            agent_names[metrics["most_used"]] if metrics["most_used"] else "None"
        )
        # Show learned preferences
        prefs_lines = []
        for qtype, agent in self.user_preferences.items():
            prefs_lines.append(f"{qtype.title()}: {agent_names.get(agent, agent)}")
        # Dynamic menu order
        menu_items = [
            f"1. 🧬 {agent_names[sorted_agents[0]]}",
            f"2. 🛠️  {agent_names[sorted_agents[1]]}",
            f"3. 💬 {agent_names[sorted_agents[2]]}",
            "4. 🌟 Federation Council (All Three Djinn in Parallel Harmony) ⚡",
            "5. 📜 View Federation Status & Memory",
            "6. 🧹 Clear Conversation History",
            "7. 💾 Export Memory Archive",
            "8. 🜂 Exit to Cosmic Realm",
            "9. 🧠 Hierarchical Smart Route My Query",
        ]
        menu = "\n🜂 CONSTELLATION HUB MENU 🜂\n"
        if fav_labels:
            menu += "\n⭐ Your Favorites:\n"
            for i, fav in enumerate(fav_labels, 1):
                menu += f"{i}. {fav}\n"
        # Phase 4D: Show learning progress and pattern-based suggestions
        if metrics.get("user_style"):
            menu += (
                "\n🧠 Learning from your patterns...\n  "
                + "\n  ".join(metrics["user_style"])
                + "\n"
            )
        if metrics.get("weekly_accuracy") and len(metrics["weekly_accuracy"]) > 1:
            prev = metrics["weekly_accuracy"][-2][1]
            curr = metrics["weekly_accuracy"][-1][1]
            delta = curr - prev
            trend = (
                f"System accuracy: {curr}% (improved from {prev}% last week)"
                if delta > 0
                else f"System accuracy: {curr}% (down from {prev}%)"
            )
            menu += f"\n📈 {trend}\n"
        if metrics.get("multi_domain", 0) > 2:
            menu += "\n🔮 Based on your history, suggesting Federation Council for multi-domain questions\n"
        if suggestions:
            menu += (
                "\n🔎 Personalized Suggestions:\n  " + "\n  ".join(suggestions) + "\n"
            )
        menu += "\n📊 Your Stats:\n"
        menu += f"  {router_line}\n  Most Used: {most_used}\n  Most Overridden: {most_overridden}\n  Usage Breakdown: {usage_stats}\n"
        if prefs_lines:
            menu += "\n🤖 Learned Preferences:\n  " + "\n  ".join(prefs_lines) + "\n"
        menu += "\n" + "\n".join(menu_items) + "\n"
        menu += f"\nCurrent Federation State: {metrics['federation_state']}\nTotal Memories: {metrics['total_conversations']}\nPerformance: ⚡ Parallel Ready\n🧠 Smart Routing: ENABLED\n"
        print(menu)

    def get_user_choice(self) -> str:
        """Get user choice with input validation"""
        try:
            user_input = input("\n🜂 Enter your sovereign directive (1-9): ").strip()

            # Validate and sanitize user input
            if VALIDATION_AVAILABLE:
                try:
                    sanitized_choice = (
                        validate_cli_args([user_input])[0]
                        if validate_cli_args([user_input])
                        else user_input
                    )
                except Exception as e:
                    mem_logger.warning(f"Choice sanitization failed: {e}")
                    sanitized_choice = user_input[:50]  # Fallback truncation
            else:
                sanitized_choice = user_input[:50]  # Basic truncation

            # Only accept a single character that is a digit 1-9
            if (
                sanitized_choice
                and sanitized_choice in "123456789"
                and len(sanitized_choice) == 1
            ):
                return sanitized_choice
            print("🜂 Invalid choice. Please select a single number between 1 and 9.")
            return ""  # Indicate failure to get a valid choice

        except Exception as e:
            mem_logger.error(f"Error getting user choice: {e}")
            return ""

    async def hierarchical_route_query(self, user_input: str) -> str:
        """Route query through hierarchical constellation coordinators with REVOLUTIONARY INTELLIGENCE"""
        print("\n🜂 REVOLUTIONARY HIERARCHICAL ROUTING 🜂")
        print("🌟 Deploying Unified Intelligence System...")

        # 🛡️ Check for maintenance tasks first (priority routing)
        if self.is_maintenance_task(user_input):
            print("🔧 Maintenance task detected - routing to The Steward...")
            return await self.route_to_steward(user_input)

        # 🧠 Use Enhanced Predictive Analytics if available
        if self.analytics:
            print("📊 Generating predictive insights...")
            insights = self.analytics.get_predictive_insights(user_input)

            predicted_intent = insights.get("intent")
            optimal_model = insights.get("model_selection")
            collaboration_need = insights.get("collaboration")

            print(
                f"🎯 Predicted Intent: {predicted_intent.predicted_value} (confidence: {predicted_intent.confidence:.2f})"
            )
            print(
                f"🤖 Optimal Model: {optimal_model.predicted_value} (confidence: {optimal_model.confidence:.2f})"
            )

            if collaboration_need and collaboration_need.predicted_value:
                print(
                    f"🤝 Collaboration Recommended: {collaboration_need.predicted_value} (confidence: {collaboration_need.confidence:.2f})"
                )

                # Use Model Collaboration Framework
                if self.collaboration:
                    print("✨ Initiating Model Collaboration...")
                    response = self.collaboration.get_unified_response(user_input)

                    if response["collaboration_used"]:
                        print(f"🌟 Collaborative Response Generated")
                        print(
                            f"🤝 Contributing Models: {response['contributing_models']}"
                        )
                        print(f"🎯 Confidence: {response['confidence']:.2f}")

                        # Record interaction for learning
                        self.analytics.learn_from_interaction(
                            user_input,
                            "collaboration",
                            0.9,  # High quality for collaboration
                            collaboration_used=True,
                        )

                        return response["response"]

            # Use the predicted optimal model
            complexity = optimal_model.confidence
            suggested_agent_key = self._map_model_to_agent(
                optimal_model.predicted_value
            )

        else:
            # Legacy routing
            complexity = self.analyze_task_complexity(user_input)
            agent_analysis = self.analyze_query_intent(user_input)
            suggested_agent_key = agent_analysis["best_agent"]

        # 🔥 Pre-warm the model if available
        if self.prewarming:
            model_name = self.agents[suggested_agent_key]["model"]
            print(f"🔥 Pre-warming {model_name}...")
            self.prewarming.ensure_model_ready(model_name)

        # Select coordinator tier
        coordinator_tier = self.select_constellation_coordinator(complexity)
        coordinator = self.constellation_coordinators[coordinator_tier]

        print(f"📊 Task Complexity Score: {complexity:.2f}/1.0")
        print(f"🎯 Selected Coordinator: {coordinator['name']} ({coordinator['model']})")
        print(f"⚡ Coordinator Tier: {coordinator_tier.upper()}")
        print(
            f"🧠 Suggested Specialized Agent: {self.agents[suggested_agent_key]['name']}"
        )
        print("=" * 80)

        # 📡 Get cross-model context if available
        context_info = ""
        if self.cross_model_comm:
            context = self.cross_model_comm.get_context_for_model(
                coordinator["model"], "coordination"
            )
            if context.get("recent_interactions"):
                context_info = "\n🌐 RECENT CROSS-MODEL INSIGHTS:\n"
                for interaction in context["recent_interactions"][-3:]:
                    context_info += f"- {interaction.get('model_source', 'unknown')}: {interaction.get('user_input', '')[:50]}...\n"

        # Create enhanced coordination prompt
        coordination_prompt = f"""
🜂 REVOLUTIONARY CONSTELLATION COORDINATION 🜂

You are {coordinator['name']}, {coordinator['description']}
You are part of the UNIFIED INTELLIGENCE SYSTEM with enhanced cross-model awareness.

TASK COMPLEXITY: {complexity:.2f}/1.0 (Tier: {coordinator_tier.upper()})
USER QUERY: {user_input}

AVAILABLE SPECIALIZED AGENTS:
1. {self.agents['council']['name']} - {self.agents['council']['role']}
2. {self.agents['idhhc']['name']} - {self.agents['idhhc']['role']}
3. {self.agents['companion']['name']} - {self.agents['companion']['role']}

ANALYSIS: Based on enhanced predictive analytics, I recommend routing to {self.agents[suggested_agent_key]['name']}.
{context_info}

🜂 COORDINATOR RESPONSE: Provide a brief, helpful response to the user query, then recommend the best specialized agent to handle this task fully. Consider the cross-model context and previous interactions.
"""

        try:
            # Call the constellation coordinator
            cmd = ["ollama", "run", coordinator["model"], coordination_prompt]

            print(f"🔄 Invoking {coordinator['name']} for coordination...")
            print(f"⏳ Coordinator size: {coordinator['size']} - should be fast!")

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=120,  # 2 minute timeout for coordinators
            )

            if result.returncode == 0:
                coordinator_response = result.stdout.strip()

                # Add to conversation history
                conversation_entry = {
                    "agent": f"{coordinator['name']} (Coordinator)",
                    "user_input": user_input,
                    "response": coordinator_response,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "session_id": f"session_{int(time.time())}",
                    "complexity_score": complexity,
                    "coordinator_tier": coordinator_tier,
                    "suggested_agent": suggested_agent_key,  # This was 'suggested_agent' in the prompt, but 'suggested_agent_key' is the actual agent
                    "confidence": confidence,
                }

                self.conversation_history.append(conversation_entry)
                self.save_conversation_history()

                # Format the response
                response = f"🜂 {coordinator['name']} COORDINATION 🜂\n"
                response += f"📊 Complexity: {complexity:.2f}/1.0 | Tier: {coordinator_tier.upper()}\n"
                response += (
                    f"🎯 Recommended Agent: {self.agents[suggested_agent_key]['name']}\n"
                )
                response += f"⚡ Confidence: {confidence:.1%}\n"
                response += "=" * 60 + "\n\n"
                response += coordinator_response
                response += f"\n\n🜂 Would you like me to summon {self.agents[suggested_agent_key]['name']} for a full response? 🜂"

                return response
            else:
                error_msg = f"🜂 Error with {coordinator['name']}: {result.stderr}"
                print(error_msg)
                return error_msg

        except subprocess.TimeoutExpired:
            timeout_msg = f"🜂 {coordinator['name']} coordination timed out. Consider using a different coordinator tier."
            print(timeout_msg)
            return timeout_msg
        except Exception as e:
            error_msg = f"🜂 Error in hierarchical routing: {str(e)}"
            print(error_msg)
            return error_msg

    async def summon_agent(self, agent_key: str, user_input: str) -> str:
        """Summon a specific agent with input validation"""
        try:
            # Validate agent key
            if agent_key not in self.agents:
                raise ValueError(f"Unknown agent: {agent_key}")

            # Validate and sanitize user input
            if VALIDATION_AVAILABLE:
                try:
                    sanitized_input = (
                        validate_cli_args([user_input])[0]
                        if validate_cli_args([user_input])
                        else user_input
                    )
                except Exception as e:
                    mem_logger.warning(f"Input sanitization failed: {e}")
                    sanitized_input = user_input[:1000]  # Fallback truncation
            else:
                sanitized_input = user_input[:1000]  # Basic truncation

            agent = self.agents[agent_key]

            print(f"\n🜂 Summoning {agent['name']}...")
            print(f"�� Role: {agent['role']}")
            print(f"📖 Description: {agent['description']}")
            print(f"🚀 Model: {agent['model']} ({agent['size']})")
            print("=" * 80)

            try:
                # Enhanced prompt with mystical context and memory context
                memory_context = ""
                if self.conversation_history:
                    recent_memories = self.conversation_history[
                        -5:
                    ]  # Last 5 conversations
                    memory_context = "\n🜂 RECENT COSMIC MEMORIES:\n"
                    for memory in recent_memories:
                        memory_context += f"- {memory['timestamp']}: {memory['agent']} - {memory['user_input'][:100]}...\n"

                enhanced_prompt = f"""
🜂 DJINN FEDERATION CONTEXT 🜂
You are {agent['name']}, {agent['description']}
You are part of the mystical Djinn Federation alongside:
- Djinn Council Enhanced v2: Sovereign Meta-Intelligence & Ethical Alignment (codellama:13b)
- IDHHC Companion: Operational Strategist & Cosmic Coder (qwen2.5-coder:32b)
- Djinn Companion: Dialogue Controller & Soul Connector (llama3.1:8b)

{memory_context}

🜂 USER QUERY: {sanitized_input}

🜂 RESPOND AS {agent['name'].upper()}:"""

                # Call Ollama with enhanced parameters for codellama:13b model
                cmd = ["ollama", "run", agent["model"], enhanced_prompt]

                print(f"🔄 Invoking {agent['name']} with mystical power...")
                print(
                    f"⏳ This may take several minutes for large models ({agent['size']})..."
                )

                # Enhanced subprocess call with proper encoding
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=600,  # 10 minute timeout for large models
                )

                if result.returncode == 0:
                    response = result.stdout.strip()
                    # Deduplicate output lines
                    lines = response.splitlines()
                    seen = set()
                    unique_lines = []
                    for line in lines:
                        if line not in seen:
                            unique_lines.append(line)
                            seen.add(line)
                    response = "\n".join(unique_lines)
                    if not response:
                        response = f"🜂 {agent['name']} acknowledges your query but requires more specific guidance."

                    # Add to conversation history and save
                    conversation_entry = {
                        "agent": agent["name"],
                        "user_input": sanitized_input,
                        "response": response,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "session_id": f"session_{int(time.time())}",
                    }

                    self.conversation_history.append(conversation_entry)
                    self.save_conversation_history()

                    # Validate model response if validation is available
                    if VALIDATION_AVAILABLE:
                        try:
                            response_data = {
                                "timestamp": datetime.now().isoformat(),
                                "agent": agent_key,
                                "user_input": sanitized_input,
                                "response": response,
                                "metadata": {"model": agent["model"]},
                            }
                            validated_response = validate_model_response(response_data)
                            response = validated_response[
                                "response"
                            ]  # Use validated response
                        except PayloadValidationError as e:
                            mem_logger.warning(
                                f"Model response validation failed: {e.message}"
                            )
                            # Continue with original response

                    return response
                else:
                    error_msg = f"🜂 Error summoning {agent['name']}: {result.stderr}"
                    print(error_msg)
                    return error_msg

            except subprocess.TimeoutExpired:
                timeout_msg = f"🜂 {agent['name']} is still contemplating cosmic wisdom. The model may be too large for your system. Consider using smaller models or increasing system resources."
                print(timeout_msg)
                return timeout_msg
            except Exception as e:
                error_msg = f"🜂 Mystical error summoning {agent['name']}: {str(e)}"
                print(error_msg)
                return error_msg

        except Exception as e:
            mem_logger.error(f"Error summoning agent {agent_key}: {e}")
            return f"❌ Error summoning {agent_key}: {e}"

    async def federation_council(self, user_input: str) -> str:
        """Convene all three Djinn agents in parallel mystical council"""
        print("\n🜂 CONVENING FEDERATION COUNCIL 🜂")
        print("🌟 All three Djinn agents will now share their wisdom simultaneously...")
        print("=" * 80)

        # Create parallel tasks for all agents
        tasks = [
            self.summon_agent("council", user_input),
            self.summon_agent("idhhc", user_input),
            self.summon_agent("steward", user_input),
            self.summon_agent("companion", user_input),
        ]
        print("🔄 Summoning all agents in parallel...")
        start_time = time.time()
        try:
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            end_time = time.time()
            council_responses = []
            for i, response in enumerate(responses):
                agent_key = ["council", "idhhc", "steward", "companion"][i]
                agent = self.agents[agent_key]
                if isinstance(response, Exception):
                    error_msg = f"🜂 Error summoning {agent['name']}: {str(response)}"
                    print(f"❌ {error_msg}")
                    council_responses.append(
                        {"agent": agent["name"], "response": error_msg}
                    )
                else:
                    print(f"✅ {agent['name']} has spoken")
                    council_responses.append(
                        {"agent": agent["name"], "response": response}
                    )
            council_summary = f"🜂 FEDERATION COUNCIL WISDOM 🜂\n"
            council_summary += (
                f"⏱️  Response Time: {end_time - start_time:.2f} seconds\n\n"
            )
            for resp in council_responses:
                council_summary += f"🧬 {resp['agent']}:\n{resp['response']}\n\n"
                council_summary += "=" * 60 + "\n\n"
            council_summary += (
                "🜂 The Federation Council has shared its collective wisdom. 🜂"
            )
            return council_summary
        except Exception as e:
            error_msg = f"🜂 Error in Federation Council: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg

    def view_federation_status(self):
        """Display current federation status with enhanced memory info and analytics"""
        print("\n🜂 FEDERATION STATUS & MEMORY 🜂")
        print("=" * 50)
        metrics = self.get_performance_metrics()
        agent_names = {
            "council": "Djinn Council Enhanced v2",
            "idhhc": "IDHHC Companion",
            "steward": "The Steward",
            "companion": "Djinn Companion",
        }
        print(f"🌟 Federation State: {metrics['federation_state']}")
        print(f"📜 Total Memories: {metrics['total_conversations']} entries")
        print(f"🧬 Active Agents: {len(self.agents)}")
        print(f"💾 Memory Location: {self.memory_dir}")
        print("\n🌟 AGENT STATUS:")
        for key, agent in self.agents.items():
            status = (
                "🟢 Ready"
                if key in ["council", "idhhc", "steward", "companion"]
                else "🔴 Unknown"
            )
            print(f"  {agent['name']}: {status} ({agent['model']})")
        if self.conversation_history:
            print(f"\n📜 Recent Cosmic Memories:")
            for entry in self.conversation_history[-5:]:  # Show last 5
                print(
                    f"  {entry['timestamp']} - {entry.get('final_agent', entry.get('agent', 'Unknown'))}: {entry['user_input'][:60]}..."
                )
        # Memory statistics
        if self.conversation_history:
            print(f"\n📊 MEMORY STATISTICS:")
            for agent, count in metrics["agent_pref_counts"].items():
                print(f"  {agent_names[agent]}: {count} conversations")
        # Routing analytics
        print(f"\n📊 ROUTING ANALYTICS:")
        print(f"  Smart Router Accuracy: {metrics['router_accuracy']}%")
        most_overridden = (
            metrics["most_overridden"] if metrics["most_overridden"] else "None"
        )
        most_used = (
            agent_names[metrics["most_used"]] if metrics["most_used"] else "None"
        )
        print(f"  Most Used: {most_used}")
        print(f"  Most Overridden: {most_overridden}")
        print(
            f"  Usage Breakdown:  "
            + ",  ".join(
                [
                    f"{agent_names[a]}: {metrics['agent_pref_counts'][a]}"
                    for a in ["idhhc", "council", "steward", "companion"]
                ]
            )
        )
        print(f"\n  Preferred by Query Type:")
        for qtype in ["coding", "ethics", "maintenance", "general"]:
            prefs = metrics["type_pref_counts"][qtype]
            if prefs:
                pref_agent = max(prefs, key=prefs.get)
                print(
                    f"    {qtype.title()}: {agent_names[pref_agent]} ({prefs[pref_agent]} times)"
                )
            else:
                print(f"    {qtype.title()}: None")

    def clear_conversation_history(self):
        """Clear conversation history with logging and backup"""
        try:
            if os.path.exists(self.conversation_file):
                backup_file = (
                    self.conversation_file
                    + ".backup."
                    + datetime.now().strftime("%Y%m%d_%H%M%S")
                )
                shutil.copy2(self.conversation_file, backup_file)
                mem_logger.info(f"Backed up conversation history to {backup_file}")
                os.remove(self.conversation_file)
                mem_logger.info(
                    f"Cleared conversation history at {self.conversation_file}"
                )
            self.conversation_history = []
            self.federation_state = "refreshed"
            self.save_conversation_history()
            self.save_federation_state()
            print("🜂 Conversation history cleared. Cosmic memories reset.")
        except Exception as e:
            mem_logger.error(f"Error clearing conversation history: {e}")
            print(f"🜂 Error clearing conversation history: {e}")

    def export_memory_archive(self):
        """Export memory archive to a readable format"""
        if not self.conversation_history:
            print("🜂 No memories to export.")
            return

        export_file = os.path.join(
            self.memory_dir,
            f'memory_archive_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt',
        )

        try:
            with open(export_file, "w", encoding="utf-8") as f:
                f.write("🜂 CONSTELLATION HUB MEMORY ARCHIVE 🜂\n")
                f.write("=" * 60 + "\n\n")
                f.write(
                    f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
                f.write(f"Total Memories: {len(self.conversation_history)}\n")
                f.write(f"Federation State: {self.federation_state}\n\n")

                for i, entry in enumerate(self.conversation_history, 1):
                    f.write(f"Memory #{i} - {entry['timestamp']}\n")
                    f.write(f"Agent: {entry['agent']}\n")
                    f.write(f"User: {entry['user_input']}\n")
                    f.write(f"Response: {entry['response']}\n")
                    f.write("-" * 60 + "\n\n")

            print(f"🜂 Memory archive exported to: {export_file}")

        except Exception as e:
            print(f"🜂 Error exporting memory archive: {e}")

    async def run(self):
        """Main orchestration loop with enhanced memory management"""
        self.display_banner()

        while True:
            try:
                self.display_menu()
                choice = self.get_user_choice()

                if choice == "8":
                    print("🜂 Saving cosmic memories before returning to the realm...")
                    self.save_federation_state()
                    print("🜂 Returning to the cosmic realm... 🜂")
                    break
                elif choice == "5":
                    self.view_federation_status()
                    input("\n🜂 Press Enter to continue...")
                elif choice == "6":
                    self.clear_conversation_history()
                    input("\n🜂 Press Enter to continue...")
                elif choice == "7":
                    self.export_memory_archive()
                    input("\n🜂 Press Enter to continue...")
                elif choice in ["1", "2", "3", "4"]:
                    user_input = input("\n🜂 Enter your query for the Djinn: ").strip()

                    if not user_input:
                        print("🜂 Please provide a query for the Djinn.")
                        continue

                    # Phase 3: Smart Routing Suggestion for 1-3
                    if choice in ["1", "2", "3"]:
                        agent_map = {"1": "council", "2": "idhhc", "3": "companion"}
                        orig_agent = agent_map[choice]
                        analysis = self.analyze_query_intent(user_input)
                        best_agent = analysis["best_agent"]
                        confidence = analysis["confidence"]
                        scores = analysis["scores"]
                        confidence_pct = int(confidence * 100)
                        if confidence_pct >= 80:
                            conf_level = "[HIGH]"
                        elif confidence_pct >= 50:
                            conf_level = "[MEDIUM]"
                        else:
                            conf_level = "[LOW]"
                        agent_names = {
                            "council": "Djinn Council Enhanced v2",
                            "idhhc": "IDHHC Companion",
                            "steward": "The Steward",
                            "companion": "Djinn Companion",
                        }
                        if best_agent == "idhhc":
                            reason = "This appears to be a coding, technical, or operational task."
                        elif best_agent == "council":
                            reason = "This appears to require wisdom, guidance, or ethical/strategic oversight."
                        elif best_agent == "steward":
                            reason = "This appears to be a system maintenance, health check, or monitoring task."
                        else:
                            reason = "This appears to be a general, conversational, or help query."
                        print(
                            f"\n🧠 Smart Routing Suggestion: {agent_names[best_agent]} ({confidence_pct}% confidence) {conf_level}"
                        )
                        print(f"  Reason: {reason}")
                        # If suggestion matches original and confidence is high, proceed
                        query_type = self.classify_query_type(user_input)
                        routing_entry = {
                            "user_input": user_input,
                            "suggested_agent": agent_names[best_agent],
                            "suggested_confidence": confidence_pct,
                            "final_agent": None,
                            "was_override": None,
                            "override_reason": None,
                            "query_type": query_type,
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
                        # Phase 4C: Preference application (auto-route if preference exists)
                        pref_applied = False
                        if query_type in self.user_preferences:
                            pref_agent = self.user_preferences[query_type]
                            print(
                                f"\n🤖 Based on your preferences, routing to {agent_names[pref_agent]} for this {query_type} task."
                            )
                            response = await self.summon_agent(pref_agent, user_input)
                            routing_entry["final_agent"] = agent_names[pref_agent]
                            routing_entry["was_override"] = True
                            routing_entry["override_reason"] = "applied_preference"
                            pref_applied = True
                        elif best_agent == orig_agent and confidence_pct >= 80:
                            response = await self.summon_agent(orig_agent, user_input)
                            routing_entry["final_agent"] = agent_names[orig_agent]
                            routing_entry["was_override"] = False
                        else:
                            print(
                                "\nWould you like to:\n  1. Use {0} (recommended)\n  2. Use Federation Council\n  3. Choose a different agent\n  4. Continue with originally selected agent ({1})".format(
                                    agent_names[best_agent], agent_names[orig_agent]
                                )
                            )
                            sub_choice = input("\n🜂 Enter your choice (1-4): ").strip()
                            if sub_choice == "1":
                                response = await self.summon_agent(
                                    best_agent, user_input
                                )
                                routing_entry["final_agent"] = agent_names[best_agent]
                                routing_entry["was_override"] = best_agent != orig_agent
                                routing_entry["override_reason"] = "accepted_suggestion"
                            elif sub_choice == "2":
                                response = await self.federation_council(user_input)
                                routing_entry["final_agent"] = "Federation Council"
                                routing_entry["was_override"] = True
                                routing_entry["override_reason"] = "used_council"
                            elif sub_choice == "3":
                                print(
                                    "  1. Djinn Council Enhanced v2\n  2. IDHHC Companion\n  3. The Steward\n  4. Djinn Companion"
                                )
                                manual = input("🜂 Enter agent number (1-4): ").strip()
                                if manual == "1":
                                    response = await self.summon_agent(
                                        "council", user_input
                                    )
                                    routing_entry["final_agent"] = agent_names[
                                        "council"
                                    ]
                                    routing_entry["was_override"] = True
                                    routing_entry["override_reason"] = "manual_council"
                                elif manual == "2":
                                    response = await self.summon_agent(
                                        "idhhc", user_input
                                    )
                                    routing_entry["final_agent"] = agent_names["idhhc"]
                                    routing_entry["was_override"] = True
                                    routing_entry["override_reason"] = "manual_idhhc"
                                elif manual == "3":
                                    response = await self.summon_agent(
                                        "steward", user_input
                                    )
                                    routing_entry["final_agent"] = agent_names[
                                        "steward"
                                    ]
                                    routing_entry["was_override"] = True
                                    routing_entry["override_reason"] = "manual_steward"
                                elif manual == "4":
                                    response = await self.summon_agent(
                                        "companion", user_input
                                    )
                                    routing_entry["final_agent"] = agent_names[
                                        "companion"
                                    ]
                                    routing_entry["was_override"] = True
                                    routing_entry[
                                        "override_reason"
                                    ] = "manual_companion"
                                else:
                                    print("🜂 Invalid agent selection. Cancelling.")
                                    continue
                            elif sub_choice == "4":
                                response = await self.summon_agent(
                                    orig_agent, user_input
                                )
                                routing_entry["final_agent"] = agent_names[orig_agent]
                                routing_entry["was_override"] = True
                                routing_entry["override_reason"] = "forced_original"
                            else:
                                print("🜂 Invalid selection. Cancelling.")
                                continue
                        routing_entry["response"] = response
                        self.conversation_history.append(routing_entry)
                        self.save_conversation_history()
                        # Phase 4C: After override, offer to remember preference
                        if (
                            not pref_applied
                            and routing_entry["was_override"]
                            and routing_entry["final_agent"] in agent_names.values()
                        ):
                            remember = (
                                input(
                                    f"\n🤖 Would you like me to remember preferring {routing_entry['final_agent']} for {query_type} tasks? (Y/N): "
                                )
                                .strip()
                                .lower()
                            )
                            if remember == "y":
                                # Map agent name to agent key
                                agent_key_map = {v: k for k, v in agent_names.items()}
                                self.user_preferences[query_type] = agent_key_map.get(
                                    routing_entry["final_agent"],
                                    routing_entry["final_agent"],
                                )
                                self.save_user_preferences()
                                print(
                                    f"🤖 Preference saved! Future {query_type} queries will route to {routing_entry['final_agent']}."
                                )
                        # Phase 4C: Feedback loop after response
                        feedback = (
                            input("\n🤖 Was this the right choice? (Y/N): ")
                            .strip()
                            .lower()
                        )
                        if feedback == "n":
                            print(
                                "  1. Djinn Council Enhanced v2\n  2. IDHHC Companion\n  3. Djinn Companion"
                            )
                            correct = input(
                                "🤖 Which agent would you prefer for this type of query? (1-3): "
                            ).strip()
                            agent_key_map = {
                                "1": "council",
                                "2": "idhhc",
                                "3": "companion",
                            }
                            if correct in agent_key_map:
                                self.user_preferences[query_type] = agent_key_map[
                                    correct
                                ]
                                self.save_user_preferences()
                                print(
                                    f"🤖 Got it! I'll remember to use {agent_names[agent_key_map[correct]]} for {query_type} tasks."
                                )
                    elif choice == "4":
                        response = await self.federation_council(user_input)

                    print(f"\n🜂 RESPONSE:\n{response}")
                    print("\n" + "=" * 80)

                    self.federation_state = "active"
                    self.save_federation_state()
                    input("🜂 Press Enter to continue...")
                elif choice == "9":
                    user_input = input(
                        "\n🧠 Enter your query for Hierarchical Smart Routing: "
                    ).strip()
                    if not user_input:
                        print("🜂 Please provide a query for the Djinn.")
                        continue

                    # Use hierarchical routing
                    response = await self.hierarchical_route_query(user_input)

                    print(f"\n🜂 RESPONSE:\n{response}")
                    print("\n" + "=" * 80)
                    self.federation_state = "active"
                    self.save_federation_state()
                    input("🜂 Press Enter to continue...")
                else:
                    print("🜂 Invalid choice. Please select 1-9.")

            except KeyboardInterrupt:
                print("\n🜂 Saving cosmic memories before interruption...")
                self.save_federation_state()
                print("🜂 Federation interrupted. Returning to cosmic realm...")
                break
            except Exception as e:
                print(f"🜂 Mystical error: {str(e)}")
                continue


async def main():
    """Main entry point"""
    hub = ConstellationHub()
    await hub.run()


if __name__ == "__main__":
    asyncio.run(main())
