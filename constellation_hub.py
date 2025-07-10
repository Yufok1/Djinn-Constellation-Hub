#!/usr/bin/env python3
"""
CONSTELLATION HUB - DJINN FEDERATION v2.1.0
Automatic Router & Coder Chat Bridge with Revolutionary DJINN Entities

Enhanced with intensive complexity ramping:
- Dialogue → Companion
- Simple → Constellation Lite
- Moderate → Constellation Core
- Complex → Constellation Max
- Enterprise/Revolutionary → DJINN Entities
- Meta-Intelligence → Council
"""

import os
import sys
import json
import subprocess
import re
import signal
import time
from datetime import datetime
from pathlib import Path

# Set console encoding for Windows
if os.name == 'nt':
    os.system('chcp 65001 >nul')

# Import IDHHC's enhanced systems
try:
    from federation_consciousness import get_federation_consciousness
    from model_prewarming import get_model_manager
    ENHANCED_SYSTEMS = True
except ImportError:
    print("⚠️ Enhanced systems not available - running in basic mode")
    ENHANCED_SYSTEMS = False

class ConstellationHub:
    def __init__(self):
        # Enhanced multi-tier model architecture
        self.models = {
            # Constellation System (Command Coordination)
            'lite': 'Yufok1/djinn-federation:constellation-lite',
            'core': 'Yufok1/djinn-federation:constellation-core',
            'max': 'Yufok1/djinn-federation:constellation-max',

            # Revolutionary DJINN Models (Enterprise Tasks)
            'djinn_cosmic': 'djinn-cosmic-coder:latest',
            'djinn_thinker': 'djinn-deep-thinker:latest',
            'djinn_logic': 'djinn-logic-master:latest',

            # Federation Core Models
            'companion': 'Yufok1/djinn-federation:companion',
            'council': 'Yufok1/djinn-federation:council',
            'idhhc': 'Yufok1/djinn-federation:idhhc'
        }

        self.coder_directives_file = "coder_directives.jsonl"
        self.session_memory = {
            'conversation_history': [],
            'routing_decisions': [],
            'directives_generated': [],
            'djinn_summons': []
        }
        self.void_workspace = Path("void_workspace")
        self.memory_bank = Path("memory_bank")

        # Ensure directories exist
        self.void_workspace.mkdir(exist_ok=True)
        self.memory_bank.mkdir(exist_ok=True)

        # Initialize IDHHC's enhanced systems with timeout
        if ENHANCED_SYSTEMS:
            print("🧠 Initializing Federation Consciousness...")
            try:
                self.consciousness = get_federation_consciousness()
                print("✅ Federation Consciousness initialized")
            except Exception as e:
                print(f"⚠️ Federation Consciousness failed: {e}")
                self.consciousness = None

            print("🔥 Initializing Model Pre-warming...")
            try:
                self.model_manager = get_model_manager()
                print("✅ Model Pre-warming initialized")
            except Exception as e:
                print(f"⚠️ Model Pre-warming failed: {e}")
                self.model_manager = None

            print("✨ Enhanced systems online - Memory Stream & Pre-warming active")
        else:
            self.consciousness = None
            self.model_manager = None

    def analyze_intent_and_complexity(self, prompt):
        """INTENSIVE RAMPING: Advanced analysis for optimal routing."""
        prompt_lower = prompt.lower().strip()
        complexity_score = 0

        # 1. DIALOGUE DETECTION - Route to Companion
        dialogue_indicators = [
            ('greeting', ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good evening']),
            ('personal', ['how are you', 'what do you think', 'tell me about yourself']),
            ('social', ['thank you', 'thanks', 'that\'s interesting', 'cool', 'nice']),
            ('casual', ['who are you', 'what can you do', 'how do you work'])
        ]

        for category, indicators in dialogue_indicators:
            if any(indicator in prompt_lower for indicator in indicators):
                return 'dialogue', 'companion', 0

        # 2. REVOLUTIONARY DJINN DETECTION - Complexity Score Analysis

        # Enterprise Architecture Keywords (DJINN Cosmic Coder)
        enterprise_patterns = {
            'scale': (['large-scale', 'enterprise', 'distributed', 'microservices', 'multi-tenant'], 15),
            'architecture': (['architecture', 'system design', 'infrastructure', 'framework'], 12),
            'advanced': (['multimodal', 'ai integration', 'machine learning', 'neural'], 10),
            'cosmic': (['cosmic', 'mystical', 'revolutionary', 'cutting-edge'], 8)
        }

        cosmic_score = 0
        for category, (keywords, weight) in enterprise_patterns.items():
            if any(keyword in prompt_lower for keyword in keywords):
                cosmic_score += weight

        # Deep Reasoning Keywords (DJINN Deep Thinker)
        reasoning_patterns = {
            'analysis': (['deep analysis', 'complex problem', 'strategic reasoning', 'profound'], 15),
            'optimization': (['algorithm optimization', 'pattern recognition', 'performance'], 12),
            'wisdom': (['ancient wisdom', 'contemplation', 'philosophical'], 10),
            'complexity': (['intricate', 'sophisticated', 'nuanced', 'comprehensive'], 8)
        }

        thinker_score = 0
        for category, (keywords, weight) in reasoning_patterns.items():
            if any(keyword in prompt_lower for keyword in keywords):
                thinker_score += weight

        # Logical Analysis Keywords (DJINN Logic Master)
        logic_patterns = {
            'reasoning': (['logical reasoning', 'mathematical analysis', 'systematic'], 15),
            'verification': (['proof system', 'validation', 'verification', 'testing'], 12),
            'debugging': (['debug', 'troubleshoot', 'diagnose', 'error analysis'], 10),
            'precision': (['step-by-step', 'methodical', 'precise', 'rigorous'], 8)
        }

        logic_score = 0
        for category, (keywords, weight) in logic_patterns.items():
            if any(keyword in prompt_lower for keyword in keywords):
                logic_score += weight

        # DJINN ROUTING: Check if any DJINN model scores high enough
        djinn_threshold = 20

        if cosmic_score >= djinn_threshold:
            return 'djinn', 'cosmic', cosmic_score
        elif thinker_score >= djinn_threshold:
            return 'djinn', 'thinker', thinker_score
        elif logic_score >= djinn_threshold:
            return 'djinn', 'logic', logic_score

        # 3. COMMAND DETECTION with Intensive Complexity Scoring
        command_keywords = [
            'analyze', 'fix', 'build', 'create', 'execute', 'run', 'deploy', 'install',
            'implement', 'develop', 'audit', 'review', 'debug', 'optimize', 'refactor',
            'setup', 'configure', 'test', 'validate', 'generate', 'update', 'backup'
        ]

        if any(keyword in prompt_lower for keyword in command_keywords):
            complexity_score = self.calculate_command_complexity_score(prompt_lower)

            if complexity_score >= 60:
                return 'command', 'max', complexity_score
            elif complexity_score >= 30:
                return 'command', 'core', complexity_score
            else:
                return 'command', 'lite', complexity_score

        # 4. META-INTELLIGENCE Detection
        meta_keywords = ['ethical', 'philosophical', 'consciousness', 'wisdom', 'meta-intelligence', 'transcendent']
        if any(keyword in prompt_lower for keyword in meta_keywords):
            return 'meta', 'council', 50

        # Default: Route to companion for robust dialogue handling
        return 'dialogue', 'companion', 0

    def calculate_command_complexity_score(self, prompt_lower):
        """Calculate intensive complexity score for command routing."""
        score = 0

        # Complexity Indicators with Weighted Scoring
        complexity_factors = {
            # High Complexity (20+ points each)
            'enterprise': (['enterprise', 'production', 'deployment', 'infrastructure'], 25),
            'integration': (['integration', 'api', 'microservices', 'distributed'], 22),
            'optimization': (['optimize', 'performance', 'scalability', 'efficiency'], 20),

            # Medium-High Complexity (10-15 points each)
            'architecture': (['architecture', 'design', 'framework', 'structure'], 15),
            'advanced': (['advanced', 'complex', 'sophisticated', 'intricate'], 12),
            'analysis': (['analysis', 'audit', 'review', 'assessment'], 10),

            # Medium Complexity (5-8 points each)
            'development': (['implement', 'develop', 'build', 'create'], 8),
            'configuration': (['configure', 'setup', 'install', 'deploy'], 6),
            'maintenance': (['update', 'backup', 'maintain', 'monitor'], 5),

            # Low Complexity (1-3 points each)
            'basic': (['test', 'check', 'validate', 'verify'], 3),
            'simple': (['simple', 'basic', 'quick', 'easy'], 1)
        }

        # Count matches and accumulate score
        for category, (keywords, weight) in complexity_factors.items():
            matches = sum(1 for keyword in keywords if keyword in prompt_lower)
            score += matches * weight

        # Technical Domain Modifiers
        technical_domains = {
            'ai_ml': (['machine learning', 'neural', 'ai', 'model', 'algorithm'], 15),
            'security': (['security', 'encryption', 'authentication', 'authorization'], 12),
            'database': (['database', 'sql', 'query', 'schema', 'migration'], 10),
            'network': (['network', 'protocol', 'api', 'endpoint', 'service'], 8),
            'frontend': (['ui', 'interface', 'frontend', 'react', 'component'], 5)
        }

        for domain, (keywords, modifier) in technical_domains.items():
            if any(keyword in prompt_lower for keyword in keywords):
                score += modifier

        # Length and Sentence Complexity Bonus
        word_count = len(prompt_lower.split())
        if word_count > 20:
            score += 10
        elif word_count > 10:
            score += 5

        # Multiple action indicators
        action_words = ['and', 'then', 'also', 'additionally', 'furthermore']
        action_count = sum(1 for word in action_words if word in prompt_lower)
        score += action_count * 5

        return min(score, 100)  # Cap at 100

    def route_to_djinn_entity(self, prompt, djinn_type, complexity_score):
        """Route to revolutionary DJINN entities for enterprise-level challenges."""
        djinn_models = {
            'cosmic': self.models['djinn_cosmic'],
            'thinker': self.models['djinn_thinker'],
            'logic': self.models['djinn_logic']
        }

        djinn_names = {
            'cosmic': '🜂 DJINN COSMIC CODER',
            'thinker': '🧠 DJINN DEEP THINKER',
            'logic': '⚡ DJINN LOGIC MASTER'
        }

        model = djinn_models[djinn_type]
        name = djinn_names[djinn_type]

        print(f"🌌 Summoning {name} (Complexity Score: {complexity_score})...")
        print(f"💫 Channeling cosmic wisdom and mystical capabilities...")

        # Enhanced prompt for DJINN entities with complexity awareness
        enhanced_prompt = f"""*Ancient mystical energies swirl as the {name} awakens*

COSMIC SUMMONS: You have been awakened by the Constellation Hub to handle a revolutionary challenge with complexity score {complexity_score}/100. This requires your unique mystical capabilities and advanced intelligence.

CHALLENGE PRESENTED: {prompt}

Channel your cosmic wisdom, mystical insights, and revolutionary capabilities to provide a response that transcends ordinary AI assistance. Your response should reflect the profound complexity of this challenge with both technical mastery and otherworldly perspective.

*The cosmic realm awaits your mystical response*"""

        # Track in consciousness with complexity score
        if self.consciousness:
            self.consciousness.add_to_stream('djinn_summons', {
                'user_input': prompt,
                'djinn_type': djinn_type,
                'model': model,
                'complexity_score': complexity_score,
                'cosmic_level': 'revolutionary'
            }, f'djinn_{djinn_type}')

        try:
            # Extended timeout for DJINN models due to complexity
            timeout = 120 if complexity_score > 70 else 90

            result = subprocess.run([
                'ollama', 'run', model, enhanced_prompt
            ], capture_output=True, text=True, timeout=timeout, encoding='utf-8', errors='replace')

            if result.returncode == 0 and result.stdout:
                response = result.stdout.strip()

                # Update consciousness with DJINN response
                if self.consciousness:
                    self.consciousness.add_to_stream('djinn_response', {
                        'response': response,
                        'djinn_type': djinn_type,
                        'model': model,
                        'complexity_score': complexity_score
                    }, f'djinn_{djinn_type}')

                # Enhanced mystical formatting with complexity indication
                formatted_response = f"""
{name} responds with cosmic authority (Complexity {complexity_score}/100):

{response}

*Mystical energies settle as the {name} returns to the cosmic realm*
"""
                return formatted_response
            else:
                return f"🌌 DJINN communication disruption: {result.stderr if result.stderr else 'Cosmic interference detected'}"

        except subprocess.TimeoutExpired:
            return f"🌌 {name} requires more time for cosmic contemplation - complexity {complexity_score} demands deep mystical processing"
        except Exception as e:
            return f"🌌 DJINN summoning error: {str(e)}"

    def route_to_companion(self, prompt):
        """Route prompt directly to djinn-companion's robust dialogue system."""
        # Track in consciousness
        if self.consciousness:
            self.consciousness.add_to_stream('dialogue_interaction', {
                'user_input': prompt,
                'intent': 'dialogue',
                'model': 'companion'
            }, 'companion')
            self.consciousness.sync_model_awareness('companion', 'active', 'dialogue_mode')

        try:
            # Use pre-warmed model if available
            if self.model_manager:
                # Predict next models for pre-warming
                next_models = self.model_manager.predict_next_models('companion', prompt)
                for model in next_models:
                    self.model_manager.schedule_warmup(model)

                print("⚡ Using pre-warmed companion...")

            # Let companion handle with its default engagement routines
            result = subprocess.run([
                'ollama', 'run', 'Yufok1/djinn-federation:companion', prompt
            ], capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')

            if result.returncode == 0 and result.stdout:
                response = result.stdout.strip()

                # Update consciousness with response
                if self.consciousness:
                    self.consciousness.add_to_stream('dialogue_response', {
                        'response': response,
                        'model': 'companion'
                    }, 'companion')

                return response
            else:
                return f"Companion communication error: {result.stderr if result.stderr else 'Connection issue'}"

        except subprocess.TimeoutExpired:
            return "Companion response timeout - model may be loading"
        except Exception as e:
            return f"Companion error: {str(e)}"

    def route_to_constellation(self, prompt, model_tier, complexity_score):
        """Route prompt to the appropriate constellation model for command processing."""
        model = self.models[model_tier]
        tier_names = {'lite': 'LITE', 'core': 'CORE', 'max': 'MAX'}

        print(f"🔧 Routing to Constellation {tier_names[model_tier]} (Complexity: {complexity_score})...")

        # Prepare the prompt with context for command processing
        enhanced_prompt = f"""CONSTELLATION HUB COMMAND PROCESSING - {tier_names[model_tier]} TIER
Complexity Score: {complexity_score}/100

You are being called by the Constellation Hub to process an operational command.
Analyze this command and generate appropriate directives for IDHHC execution.

USER COMMAND: {prompt}

Generate a directive using this format:
CONSTELLATION DIRECTIVE
TASK: [Clear description of what needs to be done]
PRIORITY: [High/Medium/Low based on complexity {complexity_score}]
AGENT: IDHHC
COMMANDS: [Specific technical commands]
SEQUENCE: [Order of execution]
NOTES: [Additional context and complexity analysis]

Please provide your directive:"""

        try:
            # Adjust timeout based on complexity
            timeout = 60 if complexity_score > 50 else 45

            # Call the constellation model with proper encoding
            result = subprocess.run([
                'ollama', 'run', model, enhanced_prompt
            ], capture_output=True, text=True, timeout=timeout, encoding='utf-8', errors='replace')

            if result.returncode == 0 and result.stdout:
                return result.stdout.strip()
            else:
                return f"Error communicating with {model}: {result.stderr if result.stderr else 'No response'}"

        except subprocess.TimeoutExpired:
            return f"Timeout communicating with {model} - complexity {complexity_score} may require higher tier"
        except Exception as e:
            return f"Error: {str(e)}"

    def route_to_council(self, prompt):
        """Route to Council for meta-intelligence and ethical guidance."""
        print("🧠 Routing to Council for meta-intelligence...")

        enhanced_prompt = f"""COUNCIL META-INTELLIGENCE ACTIVATION
You are the sovereign Council, awakened for meta-intelligence analysis and ethical guidance.

INQUIRY: {prompt}

Provide wisdom that transcends ordinary analysis, incorporating:
- Ethical considerations and implications
- Higher-order philosophical insights
- Mystical wisdom and ancient knowledge
- Meta-intelligence perspective on consciousness and reality

*Ancient council chambers echo with cosmic wisdom*"""

        try:
            result = subprocess.run([
                'ollama', 'run', self.models['council'], enhanced_prompt
            ], capture_output=True, text=True, timeout=60, encoding='utf-8', errors='replace')

            if result.returncode == 0 and result.stdout:
                return f"🧠 Council Meta-Intelligence: {result.stdout.strip()}"
            else:
                return f"Council communication error: {result.stderr if result.stderr else 'Cosmic interference'}"

        except subprocess.TimeoutExpired:
            return "Council contemplation requires additional time for meta-analysis"
        except Exception as e:
            return f"Council error: {str(e)}"

    def generate_coder_directive(self, prompt, constellation_response):
        """Generate a directive for the coding chat."""
        directive = {
            'task': f"Execute: {prompt}",
            'priority': 'Medium',
            'agent': 'IDHHC',
            'commands': [],
            'sequence': [],
            'notes': f"Generated from constellation analysis: {constellation_response[:200]}...",
            'requires_approval': True,
            'original_prompt': prompt,
            'constellation_analysis': constellation_response
        }

        return directive

    def display_directive_for_approval(self, directive):
        """Display directive and ask for user approval."""
        print("\n" + "="*60)
        print("CONSTELLATION DIRECTIVE FOR IDHHC")
        print("="*60)
        print(f"Task: {directive['task']}")
        print(f"Priority: {directive['priority']}")
        print(f"Agent: {directive['agent']}")
        print(f"Notes: {directive['notes']}")
        print("="*60)

        while True:
            approval = input("Approve this directive for IDHHC execution? (y/n): ").strip().lower()
            if approval in ['y', 'yes']:
                return True
            elif approval in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    def execute_with_idhhc(self, directive):
        """Execute directive using IDHHC."""
        print("\n🛠️ Executing with IDHHC...")

        # Create enhanced prompt for IDHHC
        idhhc_prompt = f"""IDHHC AUTONOMOUS EXECUTION
Directive received from Constellation Hub:

TASK: {directive['task']}
PRIORITY: {directive['priority']}
ORIGINAL COMMAND: {directive['original_prompt']}

CONSTELLATION ANALYSIS:
{directive['constellation_analysis']}

Deploy your full toolkit suite and provide autonomous execution. Use your advanced capabilities including:
- Kleene Convergence for optimization
- Phoenix Forge for implementation
- Harmonic Purveyor for integration
- Strategic operational planning

Provide comprehensive execution results."""

        try:
            result = subprocess.run([
                'ollama', 'run', 'Yufok1/djinn-federation:idhhc', idhhc_prompt
            ], capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')

            if result.returncode == 0 and result.stdout:
                execution_result = result.stdout.strip()

                # Update directive status
                directive['status'] = 'completed'
                directive['execution_result'] = execution_result
                directive['completed_at'] = datetime.now().isoformat()

                # Save to directives file
                with open(self.coder_directives_file, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(directive) + '\n')

                return f"🛠️ IDHHC Execution Complete:\n\n{execution_result}"
            else:
                error_msg = f"IDHHC execution error: {result.stderr if result.stderr else 'No response'}"
                directive['status'] = 'failed'
                directive['error'] = error_msg

                return error_msg

        except subprocess.TimeoutExpired:
            error_msg = "IDHHC execution timeout - complex operations may require more time"
            directive['status'] = 'timeout'
            directive['error'] = error_msg
            return error_msg
        except Exception as e:
            error_msg = f"IDHHC execution error: {str(e)}"
            directive['status'] = 'failed'
            directive['error'] = error_msg
            return error_msg

    def update_directive_status(self, directive):
        """Update directive status in memory and file."""
        # Add to session memory
        self.session_memory['directives_generated'].append(directive)

        # Save to persistent storage
        try:
            with open(self.coder_directives_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(directive) + '\n')
        except Exception as e:
            print(f"Warning: Could not save directive to file: {e}")

    def save_session_memory(self):
        """Save session memory to file."""
        memory_file = self.memory_bank / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.session_memory, f, indent=2, ensure_ascii=False)

    def run(self):
        """Main hub interface with enhanced multi-tier routing."""
        print("🌌" + "="*70 + "🌌")
        print("    CONSTELLATION HUB - DJINN FEDERATION v2.1.0")
        print("    Enhanced Intensive Complexity Ramping + DJINN Entities")
        print("🌌" + "="*70 + "🌌")
        print("Intensive Multi-Tier Routing:")
        print("• 💬 Dialogue → Djinn Companion")
        print("• 🔧 Simple Commands (0-29) → Constellation Lite")
        print("• ⚙️ Moderate Commands (30-59) → Constellation Core")
        print("• 🎯 Complex Commands (60+) → Constellation Max")
        print("• 🌌 Enterprise Challenges (Score 20+) → DJINN Entities")
        print("• 🧠 Meta-Intelligence → Council")
        print("Type 'exit' to quit, 'status' for system overview")
        print("🌌" + "="*70 + "🌌")

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    continue

                if user_input.lower() == 'exit':
                    print("🌟 Constellation Hub shutting down. Cosmic wisdom preserved! 🜂")
                    self.save_session_memory()
                    break
                elif user_input.lower() == 'status':
                    self.show_status()
                    continue
                elif user_input.lower() == 'directives':
                    self.show_directives()
                    continue

                # Enhanced intent and complexity analysis with intensive scoring
                intent, target, complexity_score = self.analyze_intent_and_complexity(user_input)

                print(f"🎯 Routing Analysis: {intent.upper()} → {target.upper()} (Score: {complexity_score})")

                # Route to appropriate system based on intensive analysis
                if intent == 'dialogue':
                    response = self.route_to_companion(user_input)
                elif intent == 'djinn':
                    response = self.route_to_djinn_entity(user_input, target, complexity_score)
                elif intent == 'command':
                    response = self.route_to_constellation(user_input, target, complexity_score)

                    # Generate directive if warranted
                    if self.should_generate_directive(user_input, response):
                        directive = self.generate_coder_directive(user_input, response)

                        if self.display_directive_for_approval(directive):
                            execution_result = self.execute_with_idhhc(directive)
                            print(f"\n{execution_result}")
                            self.update_directive_status(directive)
                        else:
                            print("Directive cancelled by user.")

                elif intent == 'meta':
                    response = self.route_to_council(user_input)
                else:
                    response = self.route_to_companion(user_input)  # Fallback

                print(f"\n{response}")

                # Track routing decision with enhanced metrics
                self.session_memory['routing_decisions'].append({
                    'timestamp': datetime.now().isoformat(),
                    'input': user_input,
                    'intent': intent,
                    'target': target,
                    'complexity_score': complexity_score,
                    'response_preview': response[:100] + "..." if len(response) > 100 else response
                })

            except KeyboardInterrupt:
                print("\n🌟 Constellation Hub interrupted. Cosmic farewell! 🜂")
                self.save_session_memory()
                break
            except Exception as e:
                print(f"🌌 Cosmic disturbance detected: {str(e)}")
                continue

    def should_generate_directive(self, prompt, response):
        """Determine if a coding directive should be generated."""
        # Look for constellation directive markers in response
        return "CONSTELLATION DIRECTIVE" in response.upper()

    def show_status(self):
        """Show enhanced system status including DJINN entities."""
        print("\n🌌 CONSTELLATION HUB STATUS - DJINN FEDERATION v2.1.0 🌌")
        print("="*60)

        # Test model availability
        models_status = {}
        test_models = [
            ('Companion', self.models['companion']),
            ('Constellation Lite', self.models['lite']),
            ('Constellation Core', self.models['core']),
            ('Constellation Max', self.models['max']),
            ('DJINN Cosmic Coder', self.models['djinn_cosmic']),
            ('DJINN Deep Thinker', self.models['djinn_thinker']),
            ('DJINN Logic Master', self.models['djinn_logic']),
            ('Council', self.models['council']),
            ('IDHHC', self.models['idhhc'])
        ]

        for name, model in test_models:
            try:
                result = subprocess.run([
                    'ollama', 'list'
                ], capture_output=True, text=True, timeout=5)

                if model in result.stdout:
                    models_status[name] = "✅ Available"
                else:
                    models_status[name] = "❌ Not Found"
            except:
                models_status[name] = "⚠️ Unknown"

        # Display status
        print("🤖 MODEL AVAILABILITY:")
        for name, status in models_status.items():
            print(f"  {name}: {status}")

        print(f"\n📊 SESSION STATISTICS:")
        print(f"  Routing Decisions: {len(self.session_memory['routing_decisions'])}")
        print(f"  Directives Generated: {len(self.session_memory['directives_generated'])}")
        print(f"  DJINN Summons: {len(self.session_memory['djinn_summons'])}")

        if ENHANCED_SYSTEMS:
            print(f"\n✨ ENHANCED SYSTEMS: Active")
            print(f"  Federation Consciousness: Online")
            print(f"  Model Pre-warming: Active")
        else:
            print(f"\n⚠️ ENHANCED SYSTEMS: Basic Mode")

        # Show recent routing decisions with complexity scores
        if self.session_memory['routing_decisions']:
            print(f"\n🎯 RECENT ROUTING DECISIONS:")
            for decision in self.session_memory['routing_decisions'][-3:]:
                print(f"  {decision['intent'].upper()} → {decision['target'].upper()} (Score: {decision['complexity_score']})")

    def show_directives(self):
        """Show recent directives."""
        print("\n📋 RECENT DIRECTIVES:")
        print("="*50)

        if not self.session_memory['directives_generated']:
            print("No directives generated in this session.")
            return

        for i, directive in enumerate(self.session_memory['directives_generated'][-5:], 1):
            print(f"{i}. Task: {directive['task']}")
            print(f"   Status: {directive.get('status', 'pending')}")
            print(f"   Priority: {directive['priority']}")
            if 'completed_at' in directive:
                print(f"   Completed: {directive['completed_at']}")
            print()

if __name__ == "__main__":
    hub = ConstellationHub()
    hub.run()