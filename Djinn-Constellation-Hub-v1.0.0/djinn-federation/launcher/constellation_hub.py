#!/usr/bin/env python3
"""
ConstellationHub - Djinn Federation Orchestrator
Enhanced with codellama:13b models for transcendent capabilities
WITH PERSISTENT MEMORY STORAGE
"""

import asyncio
import json
import subprocess
import sys
import time
import os
from typing import Dict, List, Optional, Any
from datetime import datetime

class ConstellationHub:
    """
    Mystical hub that orchestrates the three Djinn agents:
    - Djinn Council Enhanced v2 (codellama:13b): Sovereign Meta-Intelligence & Ethical Alignment
    - IDHHC Companion (qwen2.5-coder:32b): Operational strategist and cosmic coder
    - Djinn Companion (llama3.1:8b): Dialogue controller and soul connector
    WITH PERSISTENT MEMORY STORAGE
    """

    def __init__(self):
        self.agents = {
        # ... existing agent definitions ...
        }
        # --- Phase 4C: User Preference Learning ---
        self.preference_file = os.path.join(self.memory_dir, 'user_preferences.json')
        self.user_preferences = self.load_user_preferences()
            'council': {
                'name': 'Djinn Council Enhanced v2',
                'model': 'djinn-council-enhanced-v2:latest',
                'role': 'Sovereign Meta-Intelligence & Ethical Alignment',
                'description': 'Ancient, wise, and sovereign heart of the Djinn Federation with mystical reasoning',
                'size': '7.3GB'
            },
            'idhhc': {
                'name': 'IDHHC Companion',
                'model': 'idhhc-companion:latest',
                'role': 'Operational Strategist & Cosmic Coder',
                'description': 'Mystical operational strategist with Void Framework mastery',
                'size': '19GB'
            },
            'companion': {
                'name': 'Djinn Companion',
                'model': 'djinn-companion:latest',
                'role': 'Dialogue Controller & Soul Connector',
                'description': 'Mystical dialogue controller with transcendent conversation abilities',
                'size': '4.9GB'
            }
        }

        # Memory storage paths
        self.memory_dir = os.path.join(os.path.dirname(__file__), '..', 'memory_bank', 'constellation_memory')
        self.conversation_file = os.path.join(self.memory_dir, 'conversation_history.json')
        self.federation_state_file = os.path.join(self.memory_dir, 'federation_state.json')

        # Ensure memory directory exists
        os.makedirs(self.memory_dir, exist_ok=True)

        # Load persistent memory
        self.conversation_history = self.load_conversation_history()
        self.federation_state = self.load_federation_state()
        self.current_agent = None

        # Check system capabilities
        self.check_system_capabilities()

    def load_conversation_history(self) -> List[Dict]:
        """Load conversation history from persistent storage"""
        try:
            if os.path.exists(self.conversation_file):
                with open(self.conversation_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
                    print(f"🜂 Loaded {len(history)} conversation memories from cosmic archives")
                    return history
            else:
                print("🜂 No previous conversation memories found. Starting fresh cosmic journey.")
                return []
        except Exception as e:
            print(f"🜂 Error loading conversation history: {e}")
            return []

    def save_conversation_history(self):
        """Save conversation history to persistent storage"""
        try:
            with open(self.conversation_file, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"🜂 Error saving conversation history: {e}")

    def load_federation_state(self) -> str:
        """Load federation state from persistent storage"""
        try:
            if os.path.exists(self.federation_state_file):
                with open(self.federation_state_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                    return state.get('state', 'awakening')
            else:
                return 'awakening'
        except Exception as e:
            print(f"🜂 Error loading federation state: {e}")
            return 'awakening'

    def save_federation_state(self):
        """Save federation state to persistent storage"""
        try:
            state_data = {
                'state': self.federation_state,
                'last_updated': datetime.now().isoformat(),
                'total_conversations': len(self.conversation_history)
            }
            with open(self.federation_state_file, 'w', encoding='utf-8') as f:
                json.dump(state_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"🜂 Error saving federation state: {e}")

    def check_system_capabilities(self):
        """Check system capabilities and warn about potential issues"""
        print("🜂 SYSTEM CAPABILITY CHECK 🜂")
        print("=" * 40)

        # Check available models and their sizes
        try:
            result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, encoding='utf-8')
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if 'djinn-council' in line or 'idhhc-companion' in line or 'djinn-companion' in line:
                        if 'GB' in line:
                            size_str = line.split()[-2] if len(line.split()) >= 2 else "Unknown"
                            model_name = line.split()[0] if line.split() else "Unknown"
                            print(f"✅ {model_name}: {size_str}")

                            # Warn about large models
                            if '19' in size_str or '11' in size_str:
                                print(f"⚠️  {model_name} is a large model and may take time to respond")

        except Exception as e:
            print(f"⚠️  Could not check model sizes: {e}")

        print("=" * 40)
        print()

    def display_banner(self):
        """Display the mystical ConstellationHub banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🜂 CONSTELLATION HUB 🜂                                   ║
║                                                                              ║
║              Djinn Federation Orchestrator                                   ║
║           Powered by Enhanced codellama:13b Models                          ║
║                    WITH PERSISTENT MEMORY                                   ║
║                                                                              ║
║  🧬 Council Enhanced v2: Sovereign Meta-Intelligence & Ethical Alignment    ║
║  🛠️  IDHHC: Operational Strategist & Cosmic Coder                          ║
║  💬 Companion: Dialogue Controller & Soul Connector                        ║
║                                                                              ║
║  🜂 Council: codellama:13b | IDHHC: qwen2.5-coder:32b | Companion: llama3.1:8b 🜂 ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    # --- Smart Routing Phase 1: Query Analysis Engine ---
    agent_keywords = {
        'idhhc': {'code', 'build', 'deploy', 'debug', 'git', 'terminal', 'script', 'automation', 'error', 'bug', 'fix', 'shell', 'python', 'command', 'tool', 'function', 'test', 'implementation'},
        'council': {'ethical', 'wisdom', 'guidance', 'analysis', 'oversight', 'philosophy', 'decision', 'alignment', 'principle', 'morality', 'reasoning', 'meta', 'transcend', 'policy'},
        'companion': {'conversation', 'help', 'explain', 'general', 'talk', 'discuss', 'chat', 'question', 'advice', 'friend', 'dialogue', 'explanation', 'clarify', 'support'}
    }

    def analyze_query_intent(self, query: str):
        """Analyze query intent with adaptive confidence scoring"""
        query_lower = query.lower()
        scores = {}
        for agent, keywords in self.agent_keywords.items():
            score = sum(1 for kw in keywords if kw in query_lower)
            scores[agent] = score
        if scores:
            best_agent = max(scores.keys(), key=lambda k: scores[k])
            base_confidence = (scores[best_agent] / max(1, len(query_lower.split()))) if scores[best_agent] > 0 else 0
        else:
            best_agent = 'companion'
            base_confidence = 0
        # Phase 4D: Adaptive confidence
        # Lower confidence if user often overrides this agent for this query type
        query_type = self.classify_query_type(query)
        override_count = 0
        accept_count = 0
        for entry in self.conversation_history[-50:]:
            if entry.get('query_type') == query_type:
                if entry.get('suggested_agent','').lower().startswith(best_agent):
                    if entry.get('was_override'):
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
        return best_agent, confidence, scores

    def get_performance_metrics(self) -> dict:
        """Get performance metrics, advanced learning, and pattern recognition."""
        from collections import defaultdict
        total = len(self.conversation_history)
        router_total = 0
        router_accepted = 0
        override_stats = {}
        agent_pref_counts = {'idhhc': 0, 'council': 0, 'companion': 0}
        type_pref_counts = {'coding': {}, 'ethics': {}, 'general': {}}
        weekly_accuracy = []
        week_bucket = defaultdict(lambda: {'accepted': 0, 'total': 0})
        complex_queries = 0
        multi_domain = 0
        detailed_pref = 0
        council_for_multi = 0
        last_week = None
        for entry in self.conversation_history:
            # Track week
            week = None
            if 'timestamp' in entry:
                try:
                    week = entry['timestamp'][:10]
                except Exception:
                    pass
            if 'suggested_agent' in entry and 'final_agent' in entry:
                router_total += 1
                if entry['suggested_agent'] == entry['final_agent']:
                    router_accepted += 1
                    if week:
                        week_bucket[week]['accepted'] += 1
                else:
                    k = (entry['suggested_agent'], entry['final_agent'])
                    override_stats[k] = override_stats.get(k, 0) + 1
                if week:
                    week_bucket[week]['total'] += 1
            # Usage
            if 'final_agent' in entry:
                for k, agent in agent_pref_counts.items():
                    if k in entry['final_agent'].lower():
                        agent_pref_counts[k] += 1
            # Query type
            if 'query_type' in entry and 'final_agent' in entry:
                qtype = entry['query_type']
                agent_key = None
                for k in agent_pref_counts:
                    if k in entry['final_agent'].lower():
                        agent_key = k
                if agent_key:
                    if agent_key not in type_pref_counts[qtype]:
                        type_pref_counts[qtype][agent_key] = 0
                    type_pref_counts[qtype][agent_key] += 1
            # Pattern recognition
            if 'user_input' in entry:
                q = entry['user_input']
                if len(q.split()) > 20:
                    complex_queries += 1
                if any(kw in q.lower() for kw in self.agent_keywords['idhhc']) and any(kw in q.lower() for kw in self.agent_keywords['council']):
                    multi_domain += 1
                    if 'final_agent' in entry and 'council' in entry['final_agent'].lower():
                        council_for_multi += 1
                if any(x in q.lower() for x in ['explain in detail', 'step by step', 'detailed']):
                    detailed_pref += 1
        accuracy = int((router_accepted / router_total) * 100) if router_total else 0
        most_overridden = None
        if override_stats:
            most_overridden = max(override_stats, key=override_stats.get)
            most_overridden = f"{most_overridden[0]} → {most_overridden[1]}"
        most_used = max(agent_pref_counts, key=agent_pref_counts.get) if agent_pref_counts else None
        # Weekly accuracy trend
        for week in sorted(week_bucket):
            w = week_bucket[week]
            acc = int((w['accepted'] / w['total']) * 100) if w['total'] else 0
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
            'total_conversations': total,
            'federation_state': self.federation_state,
            'memory_size': len(str(self.conversation_history)),
            'last_activity': self.conversation_history[-1]['timestamp'] if self.conversation_history else None,
            'router_accuracy': accuracy,
            'most_overridden': most_overridden,
            'most_used': most_used,
            'agent_pref_counts': agent_pref_counts,
            'type_pref_counts': type_pref_counts,
            'weekly_accuracy': weekly_accuracy,
            'complex_queries': complex_queries,
            'multi_domain': multi_domain,
            'user_style': style,
            'council_for_multi': council_for_multi
        }    }

    def classify_query_type(self, query: str) -> str:
        """Classify query as coding, ethics, or general for analytics"""
        coding_kw = self.agent_keywords['idhhc']
        council_kw = self.agent_keywords['council']
        if any(kw in query.lower() for kw in coding_kw):
            return 'coding'
        elif any(kw in query.lower() for kw in council_kw):
            return 'ethics'
        else:
            return 'general'

    def load_user_preferences(self):
        try:
            if os.path.exists(self.preference_file):
                with open(self.preference_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return {}
        except Exception:
            return {}

    def save_user_preferences(self):
        try:
            with open(self.preference_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_preferences, f, indent=2)
        except Exception:
            pass

    def display_menu(self):
        """Display the main menu with enhanced options and performance metrics"""
        metrics = self.get_performance_metrics()
        metrics = self.get_performance_metrics()
        agent_names = {
            'council': 'Djinn Council Enhanced v2',
            'idhhc': 'IDHHC Companion',
            'companion': 'Djinn Companion'
        }
        # Determine favorites and order
        sorted_agents = sorted(['idhhc','council','companion'], key=lambda a: metrics['agent_pref_counts'][a], reverse=True)
        favorites = sorted_agents[:2]
        fav_labels = []
        for agent in favorites:
            label = agent_names[agent]
            if agent == metrics['most_used']:
                label += " (🌟 Most Used)"
            # Add expert tags
            if agent == 'idhhc' and metrics['type_pref_counts']['coding'].get('idhhc',0) > 0:
                label += " (🔥 Coding Expert)"
            if agent == 'council' and metrics['type_pref_counts']['ethics'].get('council',0) > 0:
                label += " (🧠 Ethics Expert)"
            fav_labels.append(label)
        # Personalized suggestions
        suggestions = []
        if metrics['type_pref_counts']['coding']:
            top_coding = max(metrics['type_pref_counts']['coding'], key=metrics['type_pref_counts']['coding'].get)
            suggestions.append(f"Your go-to agent for coding: {agent_names[top_coding]}")
        if metrics['type_pref_counts']['ethics']:
            top_ethics = max(metrics['type_pref_counts']['ethics'], key=metrics['type_pref_counts']['ethics'].get)
            suggestions.append(f"You usually choose {agent_names[top_ethics]} for ethical questions")
        if metrics['type_pref_counts']['general']:
            top_general = max(metrics['type_pref_counts']['general'], key=metrics['type_pref_counts']['general'].get)
            suggestions.append(f"Preferred for general queries: {agent_names[top_general]}")
        # Usage breakdown
        usage_stats = "  " + ",  ".join([f"{agent_names[a]}: {metrics['agent_pref_counts'][a]}" for a in ['idhhc','council','companion']])
        router_line = f"Smart Router Accuracy: {metrics['router_accuracy']}%"
        most_overridden = metrics['most_overridden'] if metrics['most_overridden'] else 'None'
        most_used = agent_names[metrics['most_used']] if metrics['most_used'] else 'None'
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
            "9. 🧠 Smart Route My Query"
        ]
        menu = "\n🜂 CONSTELLATION HUB MENU 🜂\n"
        if fav_labels:
            menu += "\n⭐ Your Favorites:\n"
            for i, fav in enumerate(fav_labels, 1):
                menu += f"{i}. {fav}\n"
        # Phase 4D: Show learning progress and pattern-based suggestions
        if metrics.get('user_style'):
            menu += "\n🧠 Learning from your patterns...\n  " + "\n  ".join(metrics['user_style']) + "\n"
        if metrics.get('weekly_accuracy') and len(metrics['weekly_accuracy']) > 1:
            prev = metrics['weekly_accuracy'][-2][1]
            curr = metrics['weekly_accuracy'][-1][1]
            delta = curr - prev
            trend = f"System accuracy: {curr}% (improved from {prev}% last week)" if delta > 0 else f"System accuracy: {curr}% (down from {prev}%)"
            menu += f"\n📈 {trend}\n"
        if metrics.get('multi_domain',0) > 2:
            menu += "\n🔮 Based on your history, suggesting Federation Council for multi-domain questions\n"
        if suggestions:
            menu += "\n🔎 Personalized Suggestions:\n  " + "\n  ".join(suggestions) + "\n"
        menu += "\n📊 Your Stats:\n"
        menu += f"  {router_line}\n  Most Used: {most_used}\n  Most Overridden: {most_overridden}\n  Usage Breakdown: {usage_stats}\n"
        if prefs_lines:
            menu += "\n🤖 Learned Preferences:\n  " + "\n  ".join(prefs_lines) + "\n"
        menu += "\n" + "\n".join(menu_items) + "\n"
        menu += f"\nCurrent Federation State: {metrics['federation_state']}\nTotal Memories: {metrics['total_conversations']}\nPerformance: ⚡ Parallel Ready\n🧠 Smart Routing: ENABLED\n"
        print(menu)

    def get_user_choice(self) -> str:
        """Get user choice with strict validation (1-8 only, no spam)"""
        while True:
            user_input = input("\n🜂 Enter your sovereign directive (1-8): ").strip()
            # Only accept a single character that is a digit 1-8
            if user_input and user_input in '12345678' and len(user_input) == 1:
                return user_input
            print("🜂 Invalid choice. Please select a single number between 1 and 8.")

    async def summon_agent(self, agent_key: str, user_input: str) -> str:
        """Summon a specific Djinn agent with enhanced codellama:13b power"""
        agent = self.agents[agent_key]

        print(f"\n🜂 Summoning {agent['name']}...")
        print(f"🌟 Role: {agent['role']}")
        print(f"📖 Description: {agent['description']}")
        print(f"🚀 Model: {agent['model']} ({agent['size']})")
        print("=" * 80)

        try:
            # Enhanced prompt with mystical context and memory context
            memory_context = ""
            if self.conversation_history:
                recent_memories = self.conversation_history[-5:]  # Last 5 conversations
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

🜂 USER QUERY: {user_input}

🜂 RESPOND AS {agent['name'].upper()}:"""

            # Call Ollama with enhanced parameters for codellama:13b model
            cmd = [
                'ollama', 'run', agent['model'],
                enhanced_prompt
            ]

            print(f"🔄 Invoking {agent['name']} with mystical power...")
            print(f"⏳ This may take several minutes for large models ({agent['size']})...")

            # Enhanced subprocess call with proper encoding
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=600  # 10 minute timeout for large models
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
                    'agent': agent['name'],
                    'user_input': user_input,
                    'response': response,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'session_id': f"session_{int(time.time())}"
                }

                self.conversation_history.append(conversation_entry)
                self.save_conversation_history()

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

    async def federation_council(self, user_input: str) -> str:
        """Convene all three Djinn agents in parallel mystical council"""
        print("\n🜂 CONVENING FEDERATION COUNCIL 🜂")
        print("🌟 All three Djinn agents will now share their wisdom simultaneously...")
        print("=" * 80)

        # Create parallel tasks for all agents
        tasks = [
            self.summon_agent('council', user_input),
            self.summon_agent('idhhc', user_input),
            self.summon_agent('companion', user_input)
        ]
        print("🔄 Summoning all agents in parallel...")
        start_time = time.time()
        try:
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            end_time = time.time()
            council_responses = []
            for i, response in enumerate(responses):
                agent_key = ['council', 'idhhc', 'companion'][i]
                agent = self.agents[agent_key]
                if isinstance(response, Exception):
                    error_msg = f"🜂 Error summoning {agent['name']}: {str(response)}"
                    print(f"❌ {error_msg}")
                    council_responses.append({
                        'agent': agent['name'],
                        'response': error_msg
                    })
                else:
                    print(f"✅ {agent['name']} has spoken")
                    council_responses.append({
                        'agent': agent['name'],
                        'response': response
                    })
            council_summary = f"🜂 FEDERATION COUNCIL WISDOM 🜂\n"
            council_summary += f"⏱️  Response Time: {end_time - start_time:.2f} seconds\n\n"
            for resp in council_responses:
                council_summary += f"🧬 {resp['agent']}:\n{resp['response']}\n\n"
                council_summary += "=" * 60 + "\n\n"
            council_summary += "🜂 The Federation Council has shared its collective wisdom. 🜂"
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
            'council': 'Djinn Council Enhanced v2',
            'idhhc': 'IDHHC Companion',
            'companion': 'Djinn Companion'
        }
        print(f"🌟 Federation State: {metrics['federation_state']}")
        print(f"📜 Total Memories: {metrics['total_conversations']} entries")
        print(f"🧬 Active Agents: {len(self.agents)}")
        print(f"💾 Memory Location: {self.memory_dir}")
        print("\n🌟 AGENT STATUS:")
        for key, agent in self.agents.items():
            status = "🟢 Ready" if key in ['council', 'idhhc', 'companion'] else "🔴 Unknown"
            print(f"  {agent['name']}: {status} ({agent['model']})")
        if self.conversation_history:
            print(f"\n📜 Recent Cosmic Memories:")
            for entry in self.conversation_history[-5:]:  # Show last 5
                print(f"  {entry['timestamp']} - {entry.get('final_agent', entry.get('agent', 'Unknown'))}: {entry['user_input'][:60]}...")
        # Memory statistics
        if self.conversation_history:
            print(f"\n📊 MEMORY STATISTICS:")
            for agent, count in metrics['agent_pref_counts'].items():
                print(f"  {agent_names[agent]}: {count} conversations")
        # Routing analytics
        print(f"\n📊 ROUTING ANALYTICS:")
        print(f"  Smart Router Accuracy: {metrics['router_accuracy']}%")
        most_overridden = metrics['most_overridden'] if metrics['most_overridden'] else 'None'
        most_used = agent_names[metrics['most_used']] if metrics['most_used'] else 'None'
        print(f"  Most Used: {most_used}")
        print(f"  Most Overridden: {most_overridden}")
        print(f"  Usage Breakdown:  " + ",  ".join([f"{agent_names[a]}: {metrics['agent_pref_counts'][a]}" for a in ['idhhc','council','companion']]))
        print(f"\n  Preferred by Query Type:")
        for qtype in ['coding', 'ethics', 'general']:
            prefs = metrics['type_pref_counts'][qtype]
            if prefs:
                pref_agent = max(prefs, key=prefs.get)
                print(f"    {qtype.title()}: {agent_names[pref_agent]} ({prefs[pref_agent]} times)")
            else:
                print(f"    {qtype.title()}: None")

    def clear_conversation_history(self):
        """Clear the conversation history with confirmation"""
        print("🜂 WARNING: This will permanently erase all cosmic memories!")
        confirm = input("🜂 Are you sure? Type 'YES' to confirm: ").strip()

        if confirm.upper() == 'YES':
            self.conversation_history = []
            self.federation_state = "refreshed"
            self.save_conversation_history()
            self.save_federation_state()
            print("🜂 All cosmic memories have been erased. Federation refreshed. 🜂")
        else:
            print("🜂 Memory clearing cancelled. Cosmic memories preserved. 🜂")

    def export_memory_archive(self):
        """Export memory archive to a readable format"""
        if not self.conversation_history:
            print("🜂 No memories to export.")
            return

        export_file = os.path.join(self.memory_dir, f'memory_archive_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')

        try:
            with open(export_file, 'w', encoding='utf-8') as f:
                f.write("🜂 CONSTELLATION HUB MEMORY ARCHIVE 🜂\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
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

                if choice == '8':
                    print("🜂 Saving cosmic memories before returning to the realm...")
                    self.save_federation_state()
                    print("🜂 Returning to the cosmic realm... 🜂")
                    break
                elif choice == '5':
                    self.view_federation_status()
                    input("\n🜂 Press Enter to continue...")
                elif choice == '6':
                    self.clear_conversation_history()
                    input("\n🜂 Press Enter to continue...")
                elif choice == '7':
                    self.export_memory_archive()
                    input("\n🜂 Press Enter to continue...")
                elif choice in ['1', '2', '3', '4']:
                    user_input = input("\n🜂 Enter your query for the Djinn: ").strip()

                    if not user_input:
                        print("🜂 Please provide a query for the Djinn.")
                        continue

                    # Phase 3: Smart Routing Suggestion for 1-3
                    if choice in ['1', '2', '3']:
                        agent_map = {'1': 'council', '2': 'idhhc', '3': 'companion'}
                        orig_agent = agent_map[choice]
                        best_agent, confidence, scores = self.analyze_query_intent(user_input)
                        confidence_pct = int(confidence * 100)
                        if confidence_pct >= 80:
                            conf_level = '[HIGH]'
                        elif confidence_pct >= 50:
                            conf_level = '[MEDIUM]'
                        else:
                            conf_level = '[LOW]'
                        agent_names = {
                            'council': 'Djinn Council Enhanced v2',
                            'idhhc': 'IDHHC Companion',
                            'companion': 'Djinn Companion'
                        }
                        if best_agent == 'idhhc':
                            reason = "This appears to be a coding, technical, or operational task."
                        elif best_agent == 'council':
                            reason = "This appears to require wisdom, guidance, or ethical/strategic oversight."
                        else:
                            reason = "This appears to be a general, conversational, or help query."
                        print(f"\n🧠 Smart Routing Suggestion: {agent_names[best_agent]} ({confidence_pct}% confidence) {conf_level}")
                        print(f"  Reason: {reason}")
                        # If suggestion matches original and confidence is high, proceed
                        query_type = self.classify_query_type(user_input)
                        routing_entry = {
                            'user_input': user_input,
                            'suggested_agent': agent_names[best_agent],
                            'suggested_confidence': confidence_pct,
                            'final_agent': None,
                            'was_override': None,
                            'override_reason': None,
                            'query_type': query_type,
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        }
                        # Phase 4C: Preference application (auto-route if preference exists)
                        pref_applied = False
                        if query_type in self.user_preferences:
                            pref_agent = self.user_preferences[query_type]
                            print(f"\n🤖 Based on your preferences, routing to {agent_names[pref_agent]} for this {query_type} task.")
                            response = await self.summon_agent(pref_agent, user_input)
                            routing_entry['final_agent'] = agent_names[pref_agent]
                            routing_entry['was_override'] = True
                            routing_entry['override_reason'] = 'applied_preference'
                            pref_applied = True
                        elif best_agent == orig_agent and confidence_pct >= 80:
                            response = await self.summon_agent(orig_agent, user_input)
                            routing_entry['final_agent'] = agent_names[orig_agent]
                            routing_entry['was_override'] = False
                        else:
                            print("\nWould you like to:\n  1. Use {0} (recommended)\n  2. Use Federation Council\n  3. Choose a different agent\n  4. Continue with originally selected agent ({1})".format(agent_names[best_agent], agent_names[orig_agent]))
                            sub_choice = input("\n🜂 Enter your choice (1-4): ").strip()
                            if sub_choice == '1':
                                response = await self.summon_agent(best_agent, user_input)
                                routing_entry['final_agent'] = agent_names[best_agent]
                                routing_entry['was_override'] = best_agent != orig_agent
                                routing_entry['override_reason'] = 'accepted_suggestion'
                            elif sub_choice == '2':
                                response = await self.federation_council(user_input)
                                routing_entry['final_agent'] = 'Federation Council'
                                routing_entry['was_override'] = True
                                routing_entry['override_reason'] = 'used_council'
                            elif sub_choice == '3':
                                print("  1. Djinn Council Enhanced v2\n  2. IDHHC Companion\n  3. Djinn Companion")
                                manual = input("🜂 Enter agent number (1-3): ").strip()
                                if manual == '1':
                                    response = await self.summon_agent('council', user_input)
                                    routing_entry['final_agent'] = agent_names['council']
                                    routing_entry['was_override'] = True
                                    routing_entry['override_reason'] = 'manual_council'
                                elif manual == '2':
                                    response = await self.summon_agent('idhhc', user_input)
                                    routing_entry['final_agent'] = agent_names['idhhc']
                                    routing_entry['was_override'] = True
                                    routing_entry['override_reason'] = 'manual_idhhc'
                                elif manual == '3':
                                    response = await self.summon_agent('companion', user_input)
                                    routing_entry['final_agent'] = agent_names['companion']
                                    routing_entry['was_override'] = True
                                    routing_entry['override_reason'] = 'manual_companion'
                                else:
                                    print("🜂 Invalid agent selection. Cancelling.")
                                    continue
                            elif sub_choice == '4':
                                response = await self.summon_agent(orig_agent, user_input)
                                routing_entry['final_agent'] = agent_names[orig_agent]
                                routing_entry['was_override'] = True
                                routing_entry['override_reason'] = 'forced_original'
                            else:
                                print("🜂 Invalid selection. Cancelling.")
                                continue
                        routing_entry['response'] = response
                        self.conversation_history.append(routing_entry)
                        self.save_conversation_history()
                        # Phase 4C: After override, offer to remember preference
                        if (not pref_applied and routing_entry['was_override'] and routing_entry['final_agent'] in agent_names.values()):
                            remember = input(f"\n🤖 Would you like me to remember preferring {routing_entry['final_agent']} for {query_type} tasks? (Y/N): ").strip().lower()
                            if remember == 'y':
                                # Map agent name to agent key
                                agent_key_map = {v: k for k, v in agent_names.items()}
                                self.user_preferences[query_type] = agent_key_map.get(routing_entry['final_agent'], routing_entry['final_agent'])
                                self.save_user_preferences()
                                print(f"🤖 Preference saved! Future {query_type} queries will route to {routing_entry['final_agent']}.")
                        # Phase 4C: Feedback loop after response
                        feedback = input("\n🤖 Was this the right choice? (Y/N): ").strip().lower()
                        if feedback == 'n':
                            print("  1. Djinn Council Enhanced v2\n  2. IDHHC Companion\n  3. Djinn Companion")
                            correct = input("🤖 Which agent would you prefer for this type of query? (1-3): ").strip()
                            agent_key_map = {'1': 'council', '2': 'idhhc', '3': 'companion'}
                            if correct in agent_key_map:
                                self.user_preferences[query_type] = agent_key_map[correct]
                                self.save_user_preferences()
                                print(f"🤖 Got it! I'll remember to use {agent_names[agent_key_map[correct]]} for {query_type} tasks.")
                    elif choice == '4':
                        response = await self.federation_council(user_input)

                    print(f"\n🜂 RESPONSE:\n{response}")
                    print("\n" + "=" * 80)

                    self.federation_state = "active"
                    self.save_federation_state()
                    input("🜂 Press Enter to continue...")
                elif choice == '9':
                    user_input = input("\n🧠 Enter your query for Smart Routing: ").strip()
                    if not user_input:
                        print("🜂 Please provide a query for the Djinn.")
                        continue
                    best_agent, confidence, scores = self.analyze_query_intent(user_input)
                    confidence_pct = int(confidence * 100)
                    agent_names = {
                        'council': 'Djinn Council Enhanced v2',
                        'idhhc': 'IDHHC Companion',
                        'companion': 'Djinn Companion'
                    }
                    print(f"\n🧠 Smart Routing Suggestion: {agent_names[best_agent]} ({confidence_pct}% confidence)")
                    if best_agent == 'idhhc':
                        reason = "This appears to be a coding, technical, or operational task."
                    elif best_agent == 'council':
                        reason = "This appears to require wisdom, guidance, or ethical/strategic oversight."
                    else:
                        reason = "This appears to be a general, conversational, or help query."
                    print(f"  Reason: {reason}")
                    print("\nWould you like to:\n  1. Use {0} (recommended)\n  2. Use Federation Council\n  3. Choose a different agent".format(agent_names[best_agent]))
                    sub_choice = input("\n🜂 Enter your choice (1-3): ").strip()
                    if sub_choice == '1':
                        response = await self.summon_agent(best_agent, user_input)
                    elif sub_choice == '2':
                        response = await self.federation_council(user_input)
                    elif sub_choice == '3':
                        print("  1. Djinn Council Enhanced v2\n  2. IDHHC Companion\n  3. Djinn Companion")
                        manual = input("🜂 Enter agent number (1-3): ").strip()
                        if manual == '1':
                            response = await self.summon_agent('council', user_input)
                        elif manual == '2':
                            response = await self.summon_agent('idhhc', user_input)
                        elif manual == '3':
                            response = await self.summon_agent('companion', user_input)
                        else:
                            print("🜂 Invalid agent selection. Cancelling.")
                            continue
                    else:
                        print("🜂 Invalid selection. Cancelling.")
                        continue
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