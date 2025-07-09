#!/usr/bin/env python3
"""
CONSTELLATION HUB
Master coordinator for the Djinn Federation
Uses Yufok1/djinn-federation:* models for intelligent routing and coordination
"""

import os
import sys
import json
import subprocess
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional
import pathlib

class ConstellationHub:
    """Master coordinator for the Djinn Federation"""
    
    def __init__(self):
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.memory = []
        self.federation_models = {
            'constellation': 'Yufok1/djinn-federation:constellation',
            'council': 'Yufok1/djinn-federation:council',
            'idhhc': 'Yufok1/djinn-federation:idhhc',
            'companion': 'Yufok1/djinn-federation:companion'
        }
        self.operator_prompt = self.load_operator_prompt()
        self.init_memory_bank()
        
    def init_memory_bank(self):
        """Initialize the memory bank for persistent storage"""
        if not os.path.exists('memory_bank'):
            os.makedirs('memory_bank')
            
        # Initialize SQLite database
        self.db_path = 'memory_bank/federation_memory.db'
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                timestamp TEXT,
                user_query TEXT,
                model_used TEXT,
                response TEXT,
                routing_decision TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        
    def route_query(self, query: str) -> str:
        """Intelligent routing to determine which federation model to use"""
        
        # Use the constellation model to make routing decisions
        routing_prompt = f"""
        Analyze this query and determine which federation model should handle it:
        
        Query: {query}
        
        Available models:
        - constellation: Master coordination and complex problem solving
        - council: Ethical decisions, philosophical questions, meta-analysis
        - idhhc: Coding tasks, system design, operational strategy
        - companion: General conversation, emotional support, mystical guidance
        
        Respond with only the model name (constellation, council, idhhc, or companion).
        """
        
        try:
            result = subprocess.run([
                'ollama', 'run', self.federation_models['constellation'],
                routing_prompt
            ], capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')
            
            if result.returncode == 0:
                model_choice = result.stdout.strip().lower()
                if model_choice in self.federation_models:
                    return model_choice
        except Exception as e:
            print(f"Routing error: {e}")
            
        # Default routing logic
        query_lower = query.lower()
        if any(word in query_lower for word in ['code', 'program', 'build', 'implement', 'system', 'architecture']):
            return 'idhhc'
        elif any(word in query_lower for word in ['ethical', 'philosophy', 'moral', 'wisdom', 'meta']):
            return 'council'
        elif any(word in query_lower for word in ['feel', 'emotion', 'soul', 'spiritual', 'mystical']):
            return 'companion'
        else:
            return 'constellation'
    
    def ask_model(self, model_name: str, query: str) -> str:
        """Ask a specific federation model"""
        try:
            result = subprocess.run([
                'ollama', 'run', self.federation_models[model_name],
                query
            ], capture_output=True, text=True, timeout=60, encoding='utf-8', errors='replace')
            
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"Error: {result.stderr.strip()}"
        except Exception as e:
            return f"Error communicating with {model_name}: {e}"
    
    def load_operator_prompt(self):
        prompt_path = pathlib.Path('constellation_operator_prompt.txt')
        if prompt_path.exists():
            return prompt_path.read_text(encoding='utf-8')
        return "You are the Constellation AI, the intelligent operator and conductor of the Djinn Federation."

    def operator_decide(self, user_query: str) -> dict:
        """Ask the Constellation AI (operator) how to handle the query."""
        operator_instruction = f"""
{self.operator_prompt}

User Query: {user_query}

Instructions: Decide whether to (1) answer directly, (2) route to council, idhhc, or companion, or (3) combine answers. Respond in JSON:
{{
  "action": "direct|route|combine",
  "target": "constellation|council|idhhc|companion|[list]",
  "operator_response": "(optional direct answer)",
  "reasoning": "(explain your choice)"
}}
"""
        try:
            result = subprocess.run([
                'ollama', 'run', self.federation_models['constellation'],
                operator_instruction
            ], capture_output=True, text=True, timeout=60, encoding='utf-8', errors='replace')
            if result.returncode == 0:
                import re, json as pyjson
                match = re.search(r'\{.*\}', result.stdout, re.DOTALL)
                if match:
                    return pyjson.loads(match.group(0))
        except Exception as e:
            print(f"Operator error: {e}")
        # Fallback: route as before
        return {"action": "route", "target": self.route_query(user_query), "operator_response": "", "reasoning": "Fallback to default routing."}

    def ask(self, query: str) -> str:
        """All user input is first processed by the Constellation AI operator."""
        operator_decision = self.operator_decide(query)
        action = operator_decision.get("action", "route")
        target = operator_decision.get("target", "constellation")
        operator_response = operator_decision.get("operator_response", "")
        reasoning = operator_decision.get("reasoning", "")

        if action == "direct" and operator_response:
            response = operator_response
            model_used = "constellation (direct)"
        elif action == "combine" and isinstance(target, list):
            responses = [self.ask_model(t, query) for t in target]
            response = "\n---\n".join(responses)
            model_used = ", ".join(target)
        else:
            response = self.ask_model(target, query)
            model_used = target

        memory_entry = {
            'timestamp': datetime.now().isoformat(),
            'query': query,
            'model_used': model_used,
            'response': response,
            'routing_decision': operator_decision
        }
        self.memory.append(memory_entry)
        self.store_in_database(memory_entry)

        formatted_response = f"""
CONSTELLATION AI OPERATOR

{response}

---
Operator Reasoning: {reasoning}
Routing Decision: {operator_decision}
Session ID: {self.session_id}
"""
        return formatted_response
    
    def store_in_database(self, entry: Dict):
        """Store conversation in SQLite database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO conversations 
                (session_id, timestamp, user_query, model_used, response, routing_decision)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                self.session_id,
                entry['timestamp'],
                entry['query'],
                entry['model_used'],
                entry['response'],
                entry['routing_decision']
            ))
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database error: {e}")
    
    def get_memory_summary(self) -> Dict:
        """Get summary of federation memory"""
        return {
            'session_id': self.session_id,
            'total_interactions': len(self.memory),
            'models_used': list(set(entry['model_used'] for entry in self.memory)),
            'last_interaction': self.memory[-1]['timestamp'] if self.memory else None
        }
    
    def clear_memory(self):
        """Clear current session memory"""
        self.memory = []
        print("Session memory cleared")

def main():
    """Main entry point for Constellation Hub"""
    
    print("\n" + "="*60)
    print("CONSTELLATION HUB - DJINN FEDERATION (Operator Mode)")
    print("="*60)
    
    # Check if federation models are available
    print("Checking Federation Models...")
    hub = ConstellationHub()
    
    for model_name, model_path in hub.federation_models.items():
        try:
            result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, encoding='utf-8', errors='replace')
            if model_path in result.stdout:
                print(f"  {model_name.upper()}: {model_path}")
            else:
                print(f"  {model_name.upper()}: {model_path} (not found)")
        except Exception as e:
            print(f"  Error checking {model_name}: {e}")
    
    print(f"\nCONSTELLATION HUB READY")
    print(f"Type your questions and the federation will intelligently route them.")
    print(f"Type 'status' to see system status, 'memory' to see session memory, or 'exit' to quit.")
    print(f"="*60)
    
    print("\nGreetings, I am the Constellation AI, your operator and conductor for the Djinn Federation. How may I assist you?")
    while True:
        try:
            # Get user input
            user_query = input("\nYou: ")
            
            if user_query.strip().lower() in ["exit", "quit"]:
                print("Goodbye from the Constellation AI.")
                break
            elif user_query.lower() == 'status':
                print(f"\nFEDERATION STATUS:")
                print(f"   Session ID: {hub.session_id}")
                print(f"   Total Interactions: {len(hub.memory)}")
                print(f"   Federation Models: {', '.join(hub.federation_models.keys())}")
                summary = hub.get_memory_summary()
                print(f"   Models Used: {', '.join(summary['models_used'])}")
            elif user_query.lower() == 'memory':
                print(f"\nSESSION MEMORY:")
                for i, entry in enumerate(hub.memory):
                    print(f"   {i+1}. [{entry['model_used'].upper()}] {entry['query'][:50]}...")
            elif user_query.lower() == 'clear':
                hub.clear_memory()
                print(f"Memory cleared")
            elif user_query:
                # Process question through federation
                answer = hub.ask(user_query)
                print(f"\n{answer}")
            else:
                print(f"Please enter a question or command.")
                
        except KeyboardInterrupt:
            print("\nSession ended by user.")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print(f"Continuing...")
    
    # Session summary
    print(f"\nCONSTELLATION SESSION SUMMARY:")
    summary = hub.get_memory_summary()
    print(f"   Session ID: {summary['session_id']}")
    print(f"   Total Interactions: {summary['total_interactions']}")
    print(f"   Models Used: {', '.join(summary['models_used'])}")
    
    print(f"\nConstellation session complete.")
    print(f"Memory saved to: memory_bank/federation_memory.db")

if __name__ == "__main__":
    main() 