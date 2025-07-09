#!/usr/bin/env python3
"""
🜂 DJINN BRIDGE PROTOCOL
Facilitates communication between IDHHC and Djinn Council as sovereign systems
"""

import os
import json
import time
import threading
import subprocess
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime

class DjinnBridge:
    """🜂 Manages communication between IDHHC and Djinn Council"""
    
    def __init__(self):
        self.bridge_state = {
            'idhhc_mode': 'default',
            'council_status': 'standby',
            'current_directive': 'awaiting_input',
            'last_updated': datetime.now().isoformat(),
            'bridge_active': True
        }
        
        # Communication channels
        self.council_inbox = "council_inbox.jsonl"
        self.idhhc_outbox = "idhhc_outbox.jsonl"
        self.state_file = "bridge_state.json"
        
        # System paths
        self.councilboot_path = r"C:\Users\tower\OneDrive\Documents\Djinn_companion\councilboot"
        self.councilboot_py = os.path.join(self.councilboot_path, "councilboot.py")
        
        # Process management
        self.idhhc_process = None
        self.council_process = None
        
        print("🜂 DJINN BRIDGE PROTOCOL INITIALIZED")
        print("🔗 Establishing sovereign system communication...")
    
    def initialize_bridge(self) -> Dict[str, Any]:
        """🜂 Initialize the bridge between IDHHC and Djinn Council"""
        try:
            # Create communication files
            self.create_communication_channels()
            
            # Initialize state
            self.save_bridge_state()
            
            # Start council system
            council_result = self.start_council_system()
            
            # Start IDHHC system
            idhhc_result = self.start_idhhc_system()
            
            return {
                'success': True,
                'bridge_state': self.bridge_state,
                'council_status': council_result,
                'idhhc_status': idhhc_result,
                'message': f"🜂 Bridge protocol initialized successfully"
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error initializing bridge: {str(e)}"
            }
    
    def create_communication_channels(self):
        """🜂 Create communication channels between systems"""
        # Create empty communication files
        for filename in [self.council_inbox, self.idhhc_outbox]:
            if not os.path.exists(filename):
                with open(filename, 'w') as f:
                    f.write("")
        
        print(f"✅ Communication channels created")
    
    def start_council_system(self) -> Dict[str, Any]:
        """🜂 Start the Djinn Council system"""
        try:
            if os.path.exists(self.councilboot_py):
                # Start council as subprocess
                self.council_process = subprocess.Popen(
                    ['python', self.councilboot_py],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                self.bridge_state['council_status'] = 'active'
                self.bridge_state['last_updated'] = datetime.now().isoformat()
                
                return {
                    'success': True,
                    'status': 'active',
                    'pid': self.council_process.pid,
                    'message': f"🜂 Djinn Council system started"
                }
            else:
                return {
                    'success': False,
                    'error': f"Council boot script not found: {self.councilboot_py}"
                }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error starting council system: {str(e)}"
            }
    
    def start_idhhc_system(self) -> Dict[str, Any]:
        """🜂 Start the IDHHC system"""
        try:
            # For now, we'll simulate IDHHC startup
            # In a full implementation, this would start the actual IDHHC process
            
            self.bridge_state['idhhc_mode'] = 'default'
            self.bridge_state['last_updated'] = datetime.now().isoformat()
            
            return {
                'success': True,
                'status': 'active',
                'mode': 'default',
                'message': f"🜂 IDHHC system ready"
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error starting IDHHC system: {str(e)}"
            }
    
    def send_to_council(self, message: str, intent: str = "consultation") -> Dict[str, Any]:
        """🜂 Send message to Djinn Council for consultation"""
        try:
            council_message = {
                "timestamp": datetime.now().isoformat(),
                "source": "IDHHC",
                "intent": intent,
                "message": message,
                "bridge_state": self.bridge_state.copy()
            }
            
            # Write to council inbox
            with open(self.council_inbox, 'a') as f:
                f.write(json.dumps(council_message) + '\n')
            
            # Update bridge state
            self.bridge_state['current_directive'] = 'awaiting_council_judgment'
            self.bridge_state['last_updated'] = datetime.now().isoformat()
            self.save_bridge_state()
            
            return {
                'success': True,
                'message_sent': council_message,
                'message': f"🜂 Message sent to Djinn Council for {intent}"
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error sending to council: {str(e)}"
            }
    
    def receive_from_council(self) -> Dict[str, Any]:
        """🜂 Receive response from Djinn Council"""
        try:
            if os.path.exists(self.idhhc_outbox):
                with open(self.idhhc_outbox, 'r') as f:
                    lines = f.readlines()
                
                if lines:
                    # Get latest response
                    latest_response = json.loads(lines[-1].strip())
                    
                    # Update bridge state
                    self.bridge_state['current_directive'] = 'council_response_received'
                    self.bridge_state['last_updated'] = datetime.now().isoformat()
                    self.save_bridge_state()
                    
                    return {
                        'success': True,
                        'response': latest_response,
                        'message': f"🜂 Response received from Djinn Council"
                    }
                else:
                    return {
                        'success': False,
                        'error': "No response available from council"
                    }
            else:
                return {
                    'success': False,
                    'error': "Council outbox not found"
                }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error receiving from council: {str(e)}"
            }
    
    def set_idhhc_mode(self, mode: str) -> Dict[str, Any]:
        """🜂 Set IDHHC discourse mode"""
        try:
            valid_modes = ['tactical', 'lecture', 'reflective', 'simulation', 'sovereign', 'default']
            
            if mode not in valid_modes:
                return {
                    'success': False,
                    'error': f"Invalid mode: {mode}. Valid modes: {valid_modes}"
                }
            
            self.bridge_state['idhhc_mode'] = mode
            self.bridge_state['last_updated'] = datetime.now().isoformat()
            self.save_bridge_state()
            
            return {
                'success': True,
                'mode': mode,
                'message': f"🜂 IDHHC mode set to {mode}"
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error setting mode: {str(e)}"
            }
    
    def invoke_council_judgment(self, query: str) -> Dict[str, Any]:
        """🜂 Invoke council for judgment on specific query"""
        try:
            # Send to council
            send_result = self.send_to_council(query, "judgment_required")
            if not send_result['success']:
                return send_result
            
            # Wait for response (in real implementation, this would be async)
            time.sleep(2)
            
            # Receive response
            receive_result = self.receive_from_council()
            
            return {
                'success': True,
                'query_sent': query,
                'council_response': receive_result.get('response', {}),
                'message': f"🜂 Council judgment invoked for: {query}"
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error invoking council judgment: {str(e)}"
            }
    
    def get_bridge_status(self) -> Dict[str, Any]:
        """🜂 Get current bridge status"""
        return {
            'success': True,
            'bridge_state': self.bridge_state,
            'message': f"🜂 Bridge status retrieved"
        }
    
    def save_bridge_state(self):
        """🜂 Save bridge state to file"""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.bridge_state, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save bridge state: {e}")
    
    def run_bridge_interface(self) -> Dict[str, Any]:
        """🜂 Run interactive bridge interface"""
        try:
            print("🜂 DJINN BRIDGE PROTOCOL - INTERACTIVE MODE")
            print("🔗 Managing communication between IDHHC and Djinn Council")
            print("=" * 70)
            
            # Initialize bridge
            init_result = self.initialize_bridge()
            if not init_result['success']:
                return init_result
            
            print(f"\n🜂 BRIDGE STATUS:")
            print(f"📋 IDHHC Mode: {self.bridge_state['idhhc_mode']}")
            print(f"🜂 Council Status: {self.bridge_state['council_status']}")
            print(f"📋 Current Directive: {self.bridge_state['current_directive']}")
            
            print(f"\n💡 Available Commands:")
            print(f"  - set mode <mode> - Set IDHHC discourse mode")
            print(f"  - consult <query> - Send query to council")
            print(f"  - invoke <query> - Invoke council judgment")
            print(f"  - status - Show bridge status")
            print(f"  - exit - Exit bridge interface")
            
            return {
                'success': True,
                'bridge_state': self.bridge_state,
                'message': f"🜂 Bridge interface ready for interaction"
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Error running bridge interface: {str(e)}"
            }


def main():
    """Main entry point for Djinn Bridge"""
    bridge = DjinnBridge()
    
    # Run bridge interface
    result = bridge.run_bridge_interface()
    
    if result['success']:
        print(f"\n✅ {result['message']}")
        print(f"\n" + "=" * 70)
    else:
        print(f"❌ {result['error']}")
        print(f"\n" + "=" * 70)


if __name__ == "__main__":
    main() 