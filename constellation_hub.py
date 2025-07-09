#!/usr/bin/env python3
"""
🜂 CONSTELLATION HUB - DJINN FEDERATION 🜂
Automatic Router & Coder Chat Bridge

This hub automatically routes queries to the appropriate constellation coordinator
and can generate directives for the coding chat with user approval.
"""

import os
import sys
import json
import subprocess
import re
from datetime import datetime
from pathlib import Path

class ConstellationHub:
    def __init__(self):
        self.models = {
            'lite': 'Yufok1/djinn-federation:constellation-lite',
            'core': 'Yufok1/djinn-federation:constellation-core', 
            'max': 'Yufok1/djinn-federation:constellation-max'
        }
        self.coder_directives_file = "coder_directives.jsonl"
        self.session_memory = {
            'conversation_history': [],
            'routing_decisions': [],
            'directives_generated': []
        }
        self.void_workspace = Path("void_workspace")
        self.memory_bank = Path("memory_bank")
        
        # Ensure directories exist
        self.void_workspace.mkdir(exist_ok=True)
        self.memory_bank.mkdir(exist_ok=True)
        
    def analyze_complexity(self, prompt):
        """Analyze prompt complexity and return appropriate model tier."""
        prompt_lower = prompt.lower()
        
        # Simple patterns (0.0-0.2) - Lite
        simple_patterns = [
            r'\b(hi|hello|hey|greetings)\b',
            r'\b(status|ready|working)\b',
            r'\b(thanks|thank you)\b',
            r'\b(bye|goodbye|exit)\b',
            r'\b(simple|basic|quick)\b',
            r'\b(what|who|when|where)\b.*\?',
            r'\b(yes|no|ok|okay)\b'
        ]
        
        # Complex patterns (0.6-1.0) - Max
        complex_patterns = [
            r'\b(architecture|design|system)\b',
            r'\b(complex|advanced|sophisticated)\b',
            r'\b(strategy|planning|analysis)\b',
            r'\b(implement|build|create)\b.*\b(system|application|framework)\b',
            r'\b(optimize|refactor|redesign)\b',
            r'\b(algorithm|data structure|pattern)\b',
            r'\b(integration|deployment|infrastructure)\b'
        ]
        
        # Check for simple patterns
        for pattern in simple_patterns:
            if re.search(pattern, prompt_lower):
                return 'lite'
        
        # Check for complex patterns
        for pattern in complex_patterns:
            if re.search(pattern, prompt_lower):
                return 'max'
        
        # Default to core for moderate complexity
        return 'core'
    
    def route_to_constellation(self, prompt, model_tier):
        """Route prompt to the appropriate constellation model."""
        model = self.models[model_tier]
        
        # Prepare the prompt with context
        enhanced_prompt = f"""🜂 CONSTELLATION HUB ROUTING 🜂
You are being called by the Constellation Hub to handle this query.
Please provide your mystical guidance and analysis.

USER QUERY: {prompt}

Remember: You can generate directives for the coding chat if the user requests implementation or coding tasks.
Use the directive format if appropriate:
🜂 CONSTELLATION DIRECTIVE 🜂
TASK: [Description]
PRIORITY: [High/Medium/Low]
AGENT: [IDHHC/Council/Companion]
COMMANDS: [Specific commands]
SEQUENCE: [Order of execution]
NOTES: [Additional context]

Please respond with your cosmic wisdom:"""
        
        try:
            # Call the constellation model
            result = subprocess.run([
                'ollama', 'run', model, enhanced_prompt
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"Error communicating with {model}: {result.stderr}"
                
        except subprocess.TimeoutExpired:
            return f"Timeout communicating with {model}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def generate_coder_directive(self, prompt, constellation_response):
        """Generate a directive for the coding chat."""
        directive = {
            'timestamp': datetime.now().isoformat(),
            'source': 'constellation_hub',
            'original_prompt': prompt,
            'constellation_analysis': constellation_response,
            'directive': {
                'task': f"Execute: {prompt}",
                'priority': 'Medium',
                'agent': 'IDHHC',
                'commands': [],
                'sequence': [],
                'notes': f"Generated from constellation analysis: {constellation_response[:200]}...",
                'requires_approval': True
            }
        }
        
        # Save directive to file
        with open(self.coder_directives_file, 'a') as f:
            f.write(json.dumps(directive) + '\n')
        
        return directive
    
    def display_directive_for_approval(self, directive):
        """Display directive and ask for user approval."""
        print("\n" + "="*60)
        print("🜂 CONSTELLATION DIRECTIVE FOR CODING CHAT 🜂")
        print("="*60)
        print(f"TASK: {directive['directive']['task']}")
        print(f"PRIORITY: {directive['directive']['priority']}")
        print(f"AGENT: {directive['directive']['agent']}")
        print(f"NOTES: {directive['directive']['notes']}")
        print("="*60)
        
        approval = input("\nApprove this directive for coding chat? (y/n): ").lower().strip()
        if approval in ['y', 'yes']:
            # Mark as approved
            directive['directive']['approved'] = True
            directive['directive']['approved_at'] = datetime.now().isoformat()
            
            # Update the file
            self.update_directive_status(directive)
            
            print("✅ Directive approved and queued for coding chat!")
            print("The coder can now access this directive for execution.")
        else:
            print("❌ Directive not approved.")
    
    def update_directive_status(self, directive):
        """Update directive status in the file."""
        # Read all directives
        directives = []
        if os.path.exists(self.coder_directives_file):
            with open(self.coder_directives_file, 'r') as f:
                for line in f:
                    if line.strip():
                        directives.append(json.loads(line))
        
        # Update the matching directive
        for i, d in enumerate(directives):
            if (d.get('timestamp') == directive['timestamp'] and 
                d.get('original_prompt') == directive['original_prompt']):
                directives[i] = directive
                break
        
        # Write back
        with open(self.coder_directives_file, 'w') as f:
            for d in directives:
                f.write(json.dumps(d) + '\n')
    
    def save_session_memory(self):
        """Save session memory to file."""
        memory_file = self.memory_bank / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(memory_file, 'w') as f:
            json.dump(self.session_memory, f, indent=2)
    
    def run(self):
        """Main hub loop."""
        print("🜂 CONSTELLATION HUB - DJINN FEDERATION 🜂")
        print("="*50)
        print("Automatic Routing & Coder Chat Bridge")
        print("Type 'exit' to quit, 'status' for system status")
        print("="*50)
        
        while True:
            try:
                # Get user input
                user_input = input("\n🜂 You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("🜂 Constellation Hub shutting down...")
                    self.save_session_memory()
                    break
                
                if user_input.lower() == 'status':
                    self.show_status()
                    continue
                
                if user_input.lower() == 'directives':
                    self.show_directives()
                    continue
                
                # Analyze complexity and route
                model_tier = self.analyze_complexity(user_input)
                
                print(f"\n🔄 Routing to Constellation {model_tier.upper()}...")
                
                # Route to constellation
                response = self.route_to_constellation(user_input, model_tier)
                
                print(f"\n🌟 Constellation {model_tier.upper()}: {response}")
                
                # Check if this should generate a directive
                if self.should_generate_directive(user_input, response):
                    directive = self.generate_coder_directive(user_input, response)
                    self.display_directive_for_approval(directive)
                
                # Save to session memory
                self.session_memory['conversation_history'].append({
                    'timestamp': datetime.now().isoformat(),
                    'user_input': user_input,
                    'model_tier': model_tier,
                    'response': response
                })
                
            except KeyboardInterrupt:
                print("\n\n🜂 Constellation Hub interrupted. Saving session...")
                self.save_session_memory()
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
    
    def should_generate_directive(self, prompt, response):
        """Determine if a directive should be generated."""
        directive_triggers = [
            'generate directive', 'create plan', 'push to coder',
            'implement', 'build', 'create', 'code', 'develop',
            'setup', 'configure', 'install', 'deploy'
        ]
        
        prompt_lower = prompt.lower()
        response_lower = response.lower()
        
        # Check if user explicitly requested directive
        for trigger in directive_triggers:
            if trigger in prompt_lower:
                return True
        
        # Check if response contains directive format
        if '🜂 CONSTELLATION DIRECTIVE 🜂' in response:
            return True
        
        return False
    
    def show_status(self):
        """Show system status."""
        print("\n" + "="*50)
        print("🜂 CONSTELLATION HUB STATUS 🜂")
        print("="*50)
        
        # Check models
        for tier, model in self.models.items():
            try:
                result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
                if model in result.stdout:
                    print(f"✅ {tier.upper()}: {model}")
                else:
                    print(f"❌ {tier.upper()}: {model} (not found)")
            except:
                print(f"❓ {tier.upper()}: {model} (status unknown)")
        
        # Check files
        print(f"\n📁 Coder Directives: {self.coder_directives_file}")
        if os.path.exists(self.coder_directives_file):
            with open(self.coder_directives_file, 'r') as f:
                directive_count = sum(1 for line in f if line.strip())
            print(f"   {directive_count} directives in queue")
        else:
            print("   No directives file found")
        
        print(f"📁 VOID Workspace: {self.void_workspace}")
        print(f"📁 Memory Bank: {self.memory_bank}")
        print("="*50)
    
    def show_directives(self):
        """Show pending directives."""
        if not os.path.exists(self.coder_directives_file):
            print("No directives found.")
            return
        
        print("\n" + "="*50)
        print("🜂 PENDING DIRECTIVES 🜂")
        print("="*50)
        
        with open(self.coder_directives_file, 'r') as f:
            for i, line in enumerate(f, 1):
                if line.strip():
                    directive = json.loads(line)
                    status = "✅ APPROVED" if directive.get('directive', {}).get('approved') else "⏳ PENDING"
                    print(f"{i}. {status} - {directive['directive']['task'][:50]}...")
                    print(f"   Timestamp: {directive['timestamp']}")
                    print()

if __name__ == "__main__":
    hub = ConstellationHub()
    hub.run() 