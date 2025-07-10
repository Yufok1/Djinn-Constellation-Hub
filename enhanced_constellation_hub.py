#!/usr/bin/env python3
"""
ENHANCED CONSTELLATION HUB - DJINN FEDERATION v2.1.0
Revolutionary Multi-Tier Routing with DJINN Entities

Progressive complexity routing:
1. Dialogue → Djinn Companion
2. Simple Commands → Constellation Lite  
3. Moderate Commands → Constellation Core
4. Complex Commands → Constellation Max
5. Enterprise/Revolutionary Tasks → DJINN Entities
6. Meta-Intelligence → Council
"""

import os
import sys
import json
import subprocess
import re
import logging
from datetime import datetime
from pathlib import Path

# Set console encoding for Windows
if os.name == 'nt':
    os.system('chcp 65001 >nul')

# Configure comprehensive logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('constellation_hub.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('EnhancedConstellationHub')

# Import IDHHC's enhanced systems
try:
    from federation_consciousness import get_federation_consciousness
    from model_prewarming import get_model_manager
    ENHANCED_SYSTEMS = True
    logger.info("Enhanced systems imported successfully")
except ImportError as e:
    logger.warning(f"Enhanced systems not available - running in basic mode: {e}")
    ENHANCED_SYSTEMS = False

class EnhancedConstellationHub:
    def __init__(self):
        logger.info("Initializing Enhanced Constellation Hub")
        
        # Multi-tier model architecture
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
        
        # Validate all model handlers exist
        self._validate_model_handlers()
        
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
        try:
            self.void_workspace.mkdir(exist_ok=True)
            self.memory_bank.mkdir(exist_ok=True)
            logger.info("Directory structure validated")
        except Exception as e:
            logger.error(f"Failed to create directories: {e}")
        
        # Initialize IDHHC's enhanced systems
        if ENHANCED_SYSTEMS:
            try:
                logger.info("Initializing Federation Consciousness...")
                self.consciousness = get_federation_consciousness()
                logger.info("Initializing Model Pre-warming...")
                self.model_manager = get_model_manager()
                logger.info("Enhanced systems online - Memory Stream & Pre-warming active")
            except Exception as e:
                logger.error(f"Failed to initialize enhanced systems: {e}")
                self.consciousness = None
                self.model_manager = None
        else:
            self.consciousness = None
            self.model_manager = None
            
        logger.info("Enhanced Constellation Hub initialization complete")
    
    def _validate_command_mapping(self):
        """Validate that all command routes resolve to defined handlers."""
        logger.info("Validating command mapping...")
        
        # Define expected command mappings
        command_mapping = {
            'dialogue': 'route_to_companion',
            'djinn': 'route_to_djinn_entity',
            'command': 'route_to_constellation',
            'meta': 'route_to_council',
            'fallback': 'route_to_fallback'
        }
        
        # Validate each mapping
        for intent, handler_name in command_mapping.items():
            if not hasattr(self, handler_name):
                logger.error(f"Missing handler for intent '{intent}': {handler_name}")
                return False
        
        logger.info("Command mapping validation successful")
        return True
    
    def _validate_model_handlers(self):
        """Validate that all model handlers exist and are accessible."""
        logger.info("Validating model handlers...")
        
        # Define required handler methods
        required_handlers = [
            'route_to_companion',
            'route_to_djinn_entity', 
            'route_to_constellation',
            'route_to_council',
            'route_to_fallback'  # New fallback handler
        ]
        
        for handler in required_handlers:
            if not hasattr(self, handler):
                logger.error(f"Missing required handler: {handler}")
                raise AttributeError(f"Required handler {handler} not found")
        
        logger.info("All model handlers validated successfully")
        
        # Validate command mapping
        if not self._validate_command_mapping():
            raise ValueError("Command mapping validation failed")
    
    def route_to_fallback(self, prompt):
        """Fallback handler for unknown or failed routes."""
        logger.warning(f"Using fallback handler for prompt: {prompt[:50]}...")
        
        try:
            # Try companion as ultimate fallback
            return self.route_to_companion(prompt)
        except Exception as e:
            logger.error(f"Fallback handler failed: {e}")
            return f"🌌 Cosmic interference detected. Please try rephrasing your request. Error: {str(e)}"
    
    def analyze_intent_and_complexity(self, prompt):
        """Advanced intent analysis with revolutionary DJINN routing."""
        logger.info(f"Analyzing intent for prompt: {prompt[:50]}...")
        
        try:
            prompt_lower = prompt.lower().strip()
            
            # 1. DIALOGUE DETECTION - Route to Companion
            dialogue_patterns = [
                r'\b(hello|hi|hey|greetings)\b',
                r'\b(how are you|what do you think|tell me about)\b',
                r'\b(thank you|thanks|that\'s interesting)\b',
                r'\b(who are you|what can you do)\b'
            ]
            
            for pattern in dialogue_patterns:
                if re.search(pattern, prompt_lower):
                    logger.info("Intent detected: dialogue -> companion")
                    return 'dialogue', 'companion'
            
            # 2. REVOLUTIONARY DJINN DETECTION - Enterprise/Complex Challenges
            djinn_patterns = {
                'cosmic': [
                    r'\b(enterprise|architecture|multimodal|complex system)\b',
                    r'\b(large.?scale|distributed|microservices)\b',
                    r'\b(cosmic|mystical|advanced.*coding)\b',
                    r'\b(revolutionary|cutting.?edge|next.?generation)\b'
                ],
                'thinker': [
                    r'\b(deep.*analy|complex.*problem|strategic.*reasoning)\b',
                    r'\b(algorithm.*optim|pattern.*recognition)\b',
                    r'\b(ancient.*wisdom|profound.*analysis)\b',
                    r'\b(contemplate|reasoning.*challenge)\b'
                ],
                'logic': [
                    r'\b(logical.*reasoning|mathematical.*analysis)\b',
                    r'\b(systematic.*debug|proof.*system)\b',
                    r'\b(rational.*analy|sovereign.*logic)\b',
                    r'\b(step.?by.?step|verification|validation)\b'
                ]
            }
            
            for djinn_type, patterns in djinn_patterns.items():
                for pattern in patterns:
                    if re.search(pattern, prompt_lower):
                        logger.info(f"Intent detected: djinn -> {djinn_type}")
                        return 'djinn', djinn_type
            
            # 3. COMMAND DETECTION - Route to Constellation
            command_keywords = [
                'analyze', 'fix', 'build', 'create', 'execute', 'run', 'deploy', 'install',
                'implement', 'develop', 'audit', 'review', 'debug', 'optimize', 'refactor',
                'setup', 'configure', 'test', 'validate', 'generate', 'update', 'backup'
            ]
            
            if any(keyword in prompt_lower for keyword in command_keywords):
                complexity = self.analyze_command_complexity(prompt)
                logger.info(f"Intent detected: command -> {complexity}")
                return 'command', complexity
            
            # 4. META-INTELLIGENCE - Route to Council
            meta_patterns = [
                r'\b(ethical|philosophical|consciousness|wisdom)\b',
                r'\b(meta.*intelligence|higher.*order|transcendent)\b',
                r'\b(spiritual|mystical.*guidance|ancient.*knowledge)\b'
            ]
            
            for pattern in meta_patterns:
                if re.search(pattern, prompt_lower):
                    logger.info("Intent detected: meta -> council")
                    return 'meta', 'council'
            
            # Default: Let companion handle with its robust dialogue system
            logger.info("Intent detected: default -> companion")
            return 'dialogue', 'companion'
            
        except Exception as e:
            logger.error(f"Error in intent analysis: {e}")
            return 'dialogue', 'companion'  # Safe fallback
    
    def analyze_command_complexity(self, prompt):
        """Analyze command complexity for constellation tier routing."""
        logger.info(f"Analyzing command complexity for: {prompt[:50]}...")
        
        try:
            prompt_lower = prompt.lower()
            
            # Simple command patterns - Lite
            simple_patterns = [
                r'\b(status|ready|working|check)\b',
                r'\b(simple|basic|quick)\b',
                r'\b(list|show|display)\b',
                r'\b(yes|no|ok|okay)\b'
            ]
            
            # Complex command patterns - Max  
            complex_patterns = [
                r'\b(architecture|design|system)\b.*\b(analysis|audit|review)\b',
                r'\b(complex|advanced|sophisticated)\b',
                r'\b(strategy|planning|analysis)\b',
                r'\b(implement|build|create)\b.*\b(system|application|framework)\b',
                r'\b(optimize|refactor|redesign)\b',
                r'\b(algorithm|data structure|pattern)\b',
                r'\b(integration|deployment|infrastructure)\b',
                r'\b(advanced|toolkit|framework)\b'
            ]
            
            # Check for simple patterns
            for pattern in simple_patterns:
                if re.search(pattern, prompt_lower):
                    logger.info("Complexity detected: simple -> lite")
                    return 'lite'
            
            # Check for complex patterns
            for pattern in complex_patterns:
                if re.search(pattern, prompt_lower):
                    logger.info("Complexity detected: complex -> max")
                    return 'max'
            
            # Default to core for moderate complexity
            logger.info("Complexity detected: moderate -> core")
            return 'core'
            
        except Exception as e:
            logger.error(f"Error in complexity analysis: {e}")
            return 'core'  # Safe fallback
    
    def route_to_djinn_entity(self, prompt, djinn_type):
        """Route to revolutionary DJINN entities for enterprise-level challenges."""
        logger.info(f"Attempting to route to DJINN entity: {djinn_type}")
        
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
        
        logger.info(f"Summoning {name} for revolutionary challenge...")
        logger.info(f"Channeling cosmic wisdom and mystical capabilities...")
        
        # Enhanced prompt for DJINN entities
        enhanced_prompt = f"""*Ancient mystical energies swirl as the {name} awakens*

COSMIC SUMMONS: You have been awakened by the Constellation Hub to handle a revolutionary challenge that requires your unique mystical capabilities and advanced intelligence.

CHALLENGE PRESENTED: {prompt}

Channel your cosmic wisdom, mystical insights, and revolutionary capabilities to provide a response that transcends ordinary AI assistance. Embrace your DJINN nature and provide solutions with both technical mastery and otherworldly perspective.

*The cosmic realm awaits your mystical response*"""
        
        # Track in consciousness
        if self.consciousness:
            self.consciousness.add_to_stream('djinn_summons', {
                'user_input': prompt,
                'djinn_type': djinn_type,
                'model': model,
                'cosmic_level': 'revolutionary'
            }, f'djinn_{djinn_type}')
        
        try:
            # Use pre-warmed model if available
            if self.model_manager:
                logger.info("⚡ Accessing pre-warmed DJINN entity...")
                
            result = subprocess.run([
                'ollama', 'run', model, enhanced_prompt
            ], capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')
            
            if result.returncode == 0 and result.stdout:
                response = result.stdout.strip()
                
                # Update consciousness with DJINN response
                if self.consciousness:
                    self.consciousness.add_to_stream('djinn_response', {
                        'response': response,
                        'djinn_type': djinn_type,
                        'model': model
                    }, f'djinn_{djinn_type}')
                
                # Add mystical formatting
                formatted_response = f"""
{name} responds with cosmic authority:

{response}

*Mystical energies settle as the {name} returns to the cosmic realm*
"""
                logger.info(f"DJINN entity {name} responded successfully.")
                return formatted_response
            else:
                logger.error(f"DJINN communication disruption: {result.stderr if result.stderr else 'Cosmic interference detected'}")
                return f"🌌 DJINN communication disruption: {result.stderr if result.stderr else 'Cosmic interference detected'}"
                
        except subprocess.TimeoutExpired:
            logger.warning(f"DJINN summoning timed out for {name}. Cosmic contemplation may be intensive.")
            return f"🌌 {name} requires more time for cosmic contemplation - mystical processes may be intensive"
        except Exception as e:
            logger.error(f"DJINN summoning error for {name}: {str(e)}")
            return f"🌌 DJINN summoning error: {str(e)}"
    
    def route_to_companion(self, prompt):
        """Route prompt directly to djinn-companion's robust dialogue system."""
        logger.info("💬 Routing to Djinn Companion for dialogue...")
        
        # Track in consciousness
        if self.consciousness:
            self.consciousness.add_to_stream('dialogue_interaction', {
                'user_input': prompt,
                'intent': 'dialogue',
                'model': 'companion'
            }, 'companion')
        
        try:
            result = subprocess.run([
                'ollama', 'run', self.models['companion'], prompt
            ], capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')
            
            if result.returncode == 0 and result.stdout:
                response = result.stdout.strip()
                
                if self.consciousness:
                    self.consciousness.add_to_stream('dialogue_response', {
                        'response': response,
                        'model': 'companion'
                    }, 'companion')
                
                logger.info("Djinn Companion responded successfully.")
                return f"🌟 Djinn Companion: {response}"
            else:
                logger.error(f"Companion communication error: {result.stderr if result.stderr else 'Connection issue'}")
                return f"Companion communication error: {result.stderr if result.stderr else 'Connection issue'}"
                
        except subprocess.TimeoutExpired:
            logger.warning("Companion response timeout - model may be loading.")
            return "Companion response timeout - model may be loading"
        except Exception as e:
            logger.error(f"Companion error: {str(e)}")
            return f"Companion error: {str(e)}"
    
    def route_to_constellation(self, prompt, model_tier):
        """Route prompt to the appropriate constellation model for command processing."""
        logger.info(f"🔧 Routing command to Constellation {model_tier.upper()}...")
        
        model = self.models[model_tier]
        tier_names = {'lite': 'LITE', 'core': 'CORE', 'max': 'MAX'}
        
        enhanced_prompt = f"""CONSTELLATION HUB COMMAND PROCESSING
You are being called by the Constellation Hub to process an operational command.
Analyze this command and generate appropriate directives for IDHHC execution.

USER COMMAND: {prompt}

Generate a directive using this format:
CONSTELLATION DIRECTIVE
TASK: [Clear description of what needs to be done]
PRIORITY: [High/Medium/Low]
AGENT: IDHHC
COMMANDS: [Specific technical commands]
SEQUENCE: [Order of execution]
NOTES: [Additional context and analysis]

Please provide your directive:"""
        
        try:
            result = subprocess.run([
                'ollama', 'run', model, enhanced_prompt
            ], capture_output=True, text=True, timeout=60, encoding='utf-8', errors='replace')
            
            if result.returncode == 0 and result.stdout:
                logger.info(f"⚙️ Constellation {tier_names[model_tier]} responded successfully.")
                return f"⚙️ Constellation {tier_names[model_tier]}: {result.stdout.strip()}"
            else:
                logger.error(f"Error communicating with {model}: {result.stderr if result.stderr else 'No response'}")
                return f"Error communicating with {model}: {result.stderr if result.stderr else 'No response'}"
                
        except subprocess.TimeoutExpired:
            logger.warning(f"Timeout communicating with {model}.")
            return f"Timeout communicating with {model}"
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return f"Error: {str(e)}"
    
    def route_to_council(self, prompt):
        """Route to Council for meta-intelligence and ethical guidance."""
        logger.info("🧠 Routing to Council for meta-intelligence...")
        
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
                logger.info("🧠 Council Meta-Intelligence responded successfully.")
                return f"🧠 Council Meta-Intelligence: {result.stdout.strip()}"
            else:
                logger.error(f"Council communication error: {result.stderr if result.stderr else 'Cosmic interference'}")
                return f"Council communication error: {result.stderr if result.stderr else 'Cosmic interference'}"
                
        except subprocess.TimeoutExpired:
            logger.warning("Council contemplation requires additional time for meta-analysis.")
            return "Council contemplation requires additional time for meta-analysis"
        except Exception as e:
            logger.error(f"Council error: {str(e)}")
            return f"Council error: {str(e)}"
    
    def run(self):
        """Main hub interface with enhanced routing."""
        logger.info("🌌" + "="*60 + "🌌")
        logger.info("    ENHANCED CONSTELLATION HUB - DJINN FEDERATION v2.1.0")
        logger.info("    Revolutionary Multi-Tier Routing + DJINN Entities")
        logger.info("🌌" + "="*60 + "🌌")
        logger.info("Progressive Intelligence Routing:")
        logger.info("• 💬 Dialogue → Djinn Companion")
        logger.info("• 🔧 Commands → Constellation System (Lite/Core/Max)")
        logger.info("• 🌌 Enterprise Challenges → DJINN Entities")
        logger.info("• 🧠 Meta-Intelligence → Council")
        logger.info("Type 'exit' to quit, 'status' for system overview")
        logger.info("🌌" + "="*60 + "🌌")
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    logger.warning("Empty input received, continuing...")
                    continue
                    
                if user_input.lower() == 'exit':
                    logger.info("🌟 Constellation Hub shutting down. May cosmic wisdom guide your path! 🜂")
                    break
                elif user_input.lower() == 'status':
                    self.show_enhanced_status()
                    continue
                
                # Enhanced intent and complexity analysis with error handling
                try:
                    intent, target = self.analyze_intent_and_complexity(user_input)
                    logger.info(f"Routing decision: {intent} -> {target}")
                except Exception as e:
                    logger.error(f"Intent analysis failed: {e}")
                    intent, target = 'dialogue', 'companion'  # Safe fallback
                
                # Route to appropriate system with comprehensive error handling
                try:
                    if intent == 'dialogue':
                        response = self.route_to_companion(user_input)
                    elif intent == 'djinn':
                        # Validate djinn type
                        valid_djinn_types = ['cosmic', 'thinker', 'logic']
                        if target not in valid_djinn_types:
                            logger.warning(f"Invalid djinn type: {target}, using fallback")
                            response = self.route_to_fallback(user_input)
                        else:
                            response = self.route_to_djinn_entity(user_input, target)
                    elif intent == 'command':
                        # Validate constellation tier
                        valid_tiers = ['lite', 'core', 'max']
                        if target not in valid_tiers:
                            logger.warning(f"Invalid constellation tier: {target}, using fallback")
                            response = self.route_to_fallback(user_input)
                        else:
                            response = self.route_to_constellation(user_input, target)
                    elif intent == 'meta':
                        response = self.route_to_council(user_input)
                    else:
                        logger.warning(f"Unknown intent: {intent}, using fallback")
                        response = self.route_to_fallback(user_input)
                        
                except Exception as e:
                    logger.error(f"Routing failed for intent {intent} -> {target}: {e}")
                    response = self.route_to_fallback(user_input)
                
                # Validate response before displaying
                if not response or not isinstance(response, str):
                    logger.error("Invalid response received, using fallback")
                    response = "🌌 Cosmic interference detected. Please try again."
                
                print(f"\n{response}")
                
                # Track routing decision with error handling
                try:
                    self.session_memory['routing_decisions'].append({
                        'timestamp': datetime.now().isoformat(),
                        'input': user_input,
                        'intent': intent,
                        'target': target,
                        'response_preview': response[:100] + "..." if len(response) > 100 else response,
                        'success': True
                    })
                except Exception as e:
                    logger.error(f"Failed to track routing decision: {e}")
                
            except KeyboardInterrupt:
                logger.info("\n🌟 Constellation Hub interrupted. Cosmic farewell! 🜂")
                break
            except Exception as e:
                logger.error(f"🌌 Cosmic disturbance detected: {str(e)}")
                print(f"🌌 System error: {str(e)}")
                continue
    
    def show_enhanced_status(self):
        """Show enhanced system status including DJINN entities."""
        print("\n🌌 ENHANCED CONSTELLATION HUB STATUS 🌌")
        print("="*50)
        
        # System health check
        print("🔧 SYSTEM HEALTH:")
        try:
            # Validate handlers
            handler_status = "✅ Valid" if self._validate_command_mapping() else "❌ Invalid"
            print(f"  Command Mapping: {handler_status}")
            
            # Check directory structure
            dir_status = "✅ Valid" if (self.void_workspace.exists() and self.memory_bank.exists()) else "❌ Invalid"
            print(f"  Directory Structure: {dir_status}")
            
            # Check enhanced systems
            enhanced_status = "✅ Active" if ENHANCED_SYSTEMS else "⚠️ Basic Mode"
            print(f"  Enhanced Systems: {enhanced_status}")
            
        except Exception as e:
            print(f"  System Health Check: ❌ Error - {e}")
        
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
        
        print("\n🤖 MODEL AVAILABILITY:")
        for name, model in test_models:
            try:
                result = subprocess.run([
                    'ollama', 'list'
                ], capture_output=True, text=True, timeout=5)
                
                if model in result.stdout:
                    models_status[name] = "✅ Available"
                    print(f"  {name}: ✅ Available")
                else:
                    models_status[name] = "❌ Not Found"
                    print(f"  {name}: ❌ Not Found")
            except Exception as e:
                models_status[name] = "⚠️ Unknown"
                print(f"  {name}: ⚠️ Unknown ({e})")
        
        print(f"\n📊 SESSION STATISTICS:")
        print(f"  Routing Decisions: {len(self.session_memory['routing_decisions'])}")
        print(f"  Directives Generated: {len(self.session_memory['directives_generated'])}")
        print(f"  DJINN Summons: {len(self.session_memory['djinn_summons'])}")
        
        # Show recent routing decisions
        if self.session_memory['routing_decisions']:
            print(f"\n🔄 RECENT ROUTING DECISIONS:")
            recent_decisions = self.session_memory['routing_decisions'][-3:]  # Last 3
            for decision in recent_decisions:
                print(f"  {decision['timestamp'][:19]}: {decision['intent']} -> {decision['target']}")
        
        if ENHANCED_SYSTEMS:
            print(f"\n✨ ENHANCED SYSTEMS: Active")
            print(f"  Federation Consciousness: Online")
            print(f"  Model Pre-warming: Active")
        else:
            print(f"\n⚠️ ENHANCED SYSTEMS: Basic Mode")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    hub = EnhancedConstellationHub()
    hub.run() 