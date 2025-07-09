#!/usr/bin/env python3
"""
Dialogue Controller for IDHHC (Internode Djinn HUD Companion)
Implements turn-taking, pause mechanisms, and response validation
"""

import json
import time
import threading
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass
from enum import Enum

class DialogueMode(Enum):
    CONVERSATIONAL = "conversational"
    ANALYTICAL = "analytical"
    INSTRUCTIONAL = "instructional"

@dataclass
class DialogueState:
    mode: DialogueMode
    turn_count: int = 0
    last_response_time: float = 0.0
    user_acknowledged: bool = False
    response_queue: List[str] = None
    
    def __post_init__(self):
        if self.response_queue is None:
            self.response_queue = []

class DialogueController:
    def __init__(self, config_file: str = "djinn_dialogue_control.json"):
        """Initialize the dialogue controller with configuration"""
        self.config = self._load_config(config_file)
        self.state = DialogueState(mode=DialogueMode.CONVERSATIONAL)
        self.user_input_callback: Optional[Callable] = None
        self.pause_event = threading.Event()
        
    def _load_config(self, config_file: str) -> Dict:
        """Load dialogue control configuration"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {config_file} not found, using default configuration")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """Return default configuration if file not found"""
        return {
            "dialogue_control": {
                "turn_taking": {
                    "enabled": True,
                    "max_response_length": 500,
                    "pause_after_response": True,
                    "wait_for_acknowledgment": True,
                    "response_timeout": 30
                },
                "user_acknowledgment": {
                    "required": True,
                    "acknowledgment_phrases": ["continue", "proceed", "next", "go on", "acknowledged", "understood"],
                    "silence_threshold": 5
                }
            }
        }
    
    def set_user_input_callback(self, callback: Callable):
        """Set callback for user input handling"""
        self.user_input_callback = callback
    
    def can_respond(self) -> bool:
        """Check if IDHHC can provide a response based on dialogue rules"""
        turn_config = self.config["dialogue_control"]["turn_taking"]
        
        # Check if turn-taking is enabled
        if not turn_config["enabled"]:
            return True
        
        # Check if waiting for acknowledgment
        if turn_config["wait_for_acknowledgment"] and not self.state.user_acknowledged:
            return False
        
        # Check response timeout
        if time.time() - self.state.last_response_time < turn_config["response_timeout"]:
            return False
        
        return True
    
    def prepare_response(self, response: str) -> str:
        """Prepare and validate response before sending"""
        turn_config = self.config["dialogue_control"]["turn_taking"]
        
        # Check response length
        if len(response) > turn_config["max_response_length"]:
            response = response[:turn_config["max_response_length"]] + "..."
        
        # Add pause indicator if configured
        if turn_config["pause_after_response"]:
            pause_config = self.config["dialogue_control"]["pause_mechanisms"]
            response += f"\n\n{pause_config['pause_indicator']}"
        
        return response
    
    def send_response(self, response: str) -> bool:
        """Send a response and update dialogue state"""
        if not self.can_respond():
            return False
        
        # Prepare response
        prepared_response = self.prepare_response(response)
        
        # Update state
        self.state.turn_count += 1
        self.state.last_response_time = time.time()
        self.state.user_acknowledged = False
        
        # Send response (this would integrate with IDHHC's output system)
        print(prepared_response)
        
        # Trigger pause if configured
        if self.config["dialogue_control"]["turn_taking"]["pause_after_response"]:
            self._trigger_pause()
        
        return True
    
    def _trigger_pause(self):
        """Trigger pause mechanism"""
        pause_config = self.config["dialogue_control"]["pause_mechanisms"]
        if pause_config["automatic_pause"]:
            self.pause_event.set()
            time.sleep(pause_config["pause_duration"])
            self.pause_event.clear()
    
    def handle_user_input(self, user_input: str) -> bool:
        """Handle user input and update dialogue state"""
        # Check for acknowledgment phrases
        ack_config = self.config["dialogue_control"]["user_acknowledgment"]
        if ack_config["required"]:
            user_input_lower = user_input.lower().strip()
            if user_input_lower in ack_config["acknowledgment_phrases"]:
                self.state.user_acknowledged = True
                return True
        
        # Call user input callback if set
        if self.user_input_callback:
            return self.user_input_callback(user_input)
        
        return True
    
    def set_dialogue_mode(self, mode: DialogueMode):
        """Set the current dialogue mode"""
        self.state.mode = mode
    
    def get_dialogue_status(self) -> Dict:
        """Get current dialogue status"""
        return {
            "mode": self.state.mode.value,
            "turn_count": self.state.turn_count,
            "user_acknowledged": self.state.user_acknowledged,
            "can_respond": self.can_respond(),
            "time_since_last_response": time.time() - self.state.last_response_time
        }

# Example usage and integration
class IDHHCDialogueInterface:
    def __init__(self):
        self.controller = DialogueController()
        self.controller.set_user_input_callback(self._handle_user_input)
    
    def _handle_user_input(self, user_input: str) -> bool:
        """Handle user input in IDHHC context"""
        # Process user input and determine if IDHHC should respond
        if user_input.strip():
            return True
        return False
    
    def respond(self, response: str) -> bool:
        """Send a response through IDHHC"""
        return self.controller.send_response(response)
    
    def process_user_input(self, user_input: str) -> bool:
        """Process user input"""
        return self.controller.handle_user_input(user_input)
    
    def get_status(self) -> Dict:
        """Get dialogue status"""
        return self.controller.get_dialogue_status()

# Integration example
if __name__ == "__main__":
    # Example of how to integrate with IDHHC
    dialogue_interface = IDHHCDialogueInterface()
    
    # IDHHC tries to respond
    success = dialogue_interface.respond("This is a test response from IDHHC.")
    print(f"Response sent: {success}")
    
    # User provides acknowledgment
    dialogue_interface.process_user_input("continue")
    
    # Check status
    status = dialogue_interface.get_status()
    print(f"Dialogue status: {status}") 