#!/usr/bin/env python3
"""
VOID Constellation Bridge
Bridge between Constellation System and VOID's main chat interface
"""

import json
import os
import time
import sys
from datetime import datetime
from pathlib import Path

class VOIDConstellationBridge:
    """Bridge for Constellation-to-VOID communication"""
    
    def __init__(self):
        self.bridge_dir = Path("memory_bank/void_bridge")
        self.bridge_dir.mkdir(exist_ok=True)
        
        self.directive_queue = self.bridge_dir / "directive_queue.jsonl"
        self.void_responses = self.bridge_dir / "void_responses.jsonl"
        self.bridge_status = self.bridge_dir / "bridge_status.json"
        
        # Initialize bridge status
        self.update_bridge_status("initialized")
    
    def update_bridge_status(self, status):
        """Update bridge status file"""
        status_data = {
            "status": status,
            "timestamp": datetime.now().isoformat(),
            "void_interface": "active"
        }
        with open(self.bridge_status, 'w') as f:
            json.dump(status_data, f, indent=2)
    
    def queue_directive_for_void(self, directive):
        """Queue a directive for VOID processing"""
        directive_entry = {
            "id": f"dir_{int(time.time())}",
            "timestamp": datetime.now().isoformat(),
            "source": "constellation",
            "directive": directive,
            "status": "queued_for_void",
            "void_processed": False
        }
        
        # Add to queue
        with open(self.directive_queue, 'a') as f:
            f.write(json.dumps(directive_entry) + '\n')
        
        print(f"✅ Directive queued for VOID: {directive['task'][:50]}...")
        return directive_entry["id"]
    
    def get_pending_directives(self):
        """Get all pending directives for VOID"""
        if not os.path.exists(self.directive_queue):
            return []
        
        pending = []
        with open(self.directive_queue, 'r') as f:
            for line in f:
                if line.strip():
                    directive = json.loads(line)
                    if not directive.get('void_processed', False):
                        pending.append(directive)
        
        return pending
    
    def mark_directive_processed(self, directive_id, void_response=None):
        """Mark directive as processed by VOID"""
        # Read all directives
        directives = []
        if os.path.exists(self.directive_queue):
            with open(self.directive_queue, 'r') as f:
                for line in f:
                    if line.strip():
                        directives.append(json.loads(line))
        
        # Update the processed directive
        for directive in directives:
            if directive.get('id') == directive_id:
                directive['void_processed'] = True
                directive['processed_at'] = datetime.now().isoformat()
                if void_response:
                    directive['void_response'] = void_response
                break
        
        # Write back
        with open(self.directive_queue, 'w') as f:
            for directive in directives:
                f.write(json.dumps(directive) + '\n')
        
        # Log response if provided
        if void_response:
            response_entry = {
                "directive_id": directive_id,
                "timestamp": datetime.now().isoformat(),
                "response": void_response
            }
            with open(self.void_responses, 'a') as f:
                f.write(json.dumps(response_entry) + '\n')
    
    def display_pending_directives(self):
        """Display all pending directives for VOID"""
        pending = self.get_pending_directives()
        
        if not pending:
            print("📝 No pending directives from constellation system")
            return
        
        print("\n🌟 CONSTELLATION DIRECTIVES FOR VOID CODING CHAT 🌟")
        print("=" * 60)
        
        for i, directive in enumerate(pending, 1):
            d = directive['directive']
            print(f"\n📋 DIRECTIVE #{i} (ID: {directive['id']})")
            print(f"🎯 TASK: {d['task']}")
            print(f"⚡ PRIORITY: {d['priority']}")
            print(f"🤖 AGENT: {d['agent']}")
            print(f"⏰ QUEUED: {directive['timestamp']}")
            
            if d.get('notes'):
                print(f"📝 NOTES: {d['notes'][:100]}...")
            
            if d.get('commands'):
                print(f"🔧 COMMANDS: {', '.join(d['commands'][:3])}...")
            
            print("-" * 40)
        
        return pending
    
    def process_directive_interactively(self, directive):
        """Process a single directive interactively with user"""
        d = directive['directive']
        
        print(f"\n🌟 PROCESSING CONSTELLATION DIRECTIVE 🌟")
        print(f"🎯 TASK: {d['task']}")
        print(f"⚡ PRIORITY: {d['priority']}")
        print(f"🤖 RECOMMENDED AGENT: {d['agent']}")
        
        if d.get('notes'):
            print(f"📝 CONSTELLATION ANALYSIS: {d['notes']}")
        
        print("\n" + "="*50)
        
        choice = input("How should I handle this directive?\n1. Execute now\n2. Skip\n3. Show details\nChoice (1-3): ")
        
        if choice == '1':
            print(f"\n✅ Executing directive: {d['task']}")
            self.mark_directive_processed(directive['id'], "Executed by VOID")
            return True
        elif choice == '2':
            print(f"\n⏭️ Skipping directive")
            self.mark_directive_processed(directive['id'], "Skipped by user")
            return False
        elif choice == '3':
            print(f"\n📋 FULL DIRECTIVE DETAILS:")
            print(json.dumps(directive, indent=2))
            return self.process_directive_interactively(directive)
        else:
            print("Invalid choice, skipping...")
            return False

def main():
    """Main function to check and process constellation directives"""
    bridge = VOIDConstellationBridge()
    
    print("🌉 VOID-Constellation Bridge")
    print("Checking for constellation directives...")
    
    # Display pending directives
    pending = bridge.display_pending_directives()
    
    if pending:
        print(f"\n📨 Found {len(pending)} pending directive(s)")
        
        # Process each directive
        for directive in pending:
            executed = bridge.process_directive_interactively(directive)
            if not executed:
                continue
    
    else:
        print("\n💤 No pending directives. Bridge is ready for new constellation communications.")
    
    bridge.update_bridge_status("ready")

if __name__ == "__main__":
    main() 