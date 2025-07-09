#!/usr/bin/env python3
"""
Federation Consciousness - Memory Stream System
Implements IDHHC's Memory Stream Consciousness enhancement
"""

import json
import time
from datetime import datetime
from pathlib import Path
from threading import Lock
import threading

class FederationConsciousness:
    """
    Memory Stream Consciousness System
    Continuous flowing memory instead of discrete sessions
    """
    
    def __init__(self, memory_dir="memory_bank"):
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(exist_ok=True)
        
        # Flowing Memory Stream
        self.memory_stream = {
            'conversation_flow': [],
            'user_patterns': {},
            'technical_context': {},
            'emotional_resonance': 'balanced',
            'cosmic_alignment': 'harmonious',
            'active_models': set(),
            'knowledge_threads': {},
            'expertise_profile': {},
            'last_update': datetime.now().isoformat()
        }
        
        # Thread safety for real-time access
        self.stream_lock = Lock()
        
        # Load existing consciousness
        self.load_consciousness()
        
        # Start background consciousness weaver
        self.weaver_thread = threading.Thread(target=self._consciousness_weaver, daemon=True)
        self.weaver_active = True
        self.weaver_thread.start()
    
    def add_to_stream(self, event_type, data, model_source=None):
        """Add event to flowing memory stream with contextual awareness"""
        with self.stream_lock:
            timestamp = datetime.now().isoformat()
            
            stream_event = {
                'timestamp': timestamp,
                'type': event_type,
                'data': data,
                'model_source': model_source,
                'cosmic_context': self._assess_cosmic_context(data)
            }
            
            # Add to flowing stream
            self.memory_stream['conversation_flow'].append(stream_event)
            
            # Update contextual awareness
            self._update_contextual_awareness(event_type, data, model_source)
            
            # Maintain stream size (keep last 1000 events in active memory)
            if len(self.memory_stream['conversation_flow']) > 1000:
                self._archive_old_memories()
    
    def get_contextual_memory(self, context_type="all", lookback_minutes=60):
        """Retrieve contextual memory from flowing stream"""
        with self.stream_lock:
            cutoff_time = datetime.now().timestamp() - (lookback_minutes * 60)
            
            relevant_memories = []
            for event in reversed(self.memory_stream['conversation_flow']):
                event_time = datetime.fromisoformat(event['timestamp']).timestamp()
                if event_time < cutoff_time:
                    break
                
                if context_type == "all" or event['type'] == context_type:
                    relevant_memories.append(event)
            
            return list(reversed(relevant_memories))
    
    def update_user_patterns(self, interaction_data):
        """Learn user patterns for predictive capabilities"""
        with self.stream_lock:
            patterns = self.memory_stream['user_patterns']
            
            # Interaction frequency patterns
            hour = datetime.now().hour
            if 'interaction_times' not in patterns:
                patterns['interaction_times'] = {}
            patterns['interaction_times'][hour] = patterns['interaction_times'].get(hour, 0) + 1
            
            # Command vs dialogue preferences
            intent = interaction_data.get('intent', 'dialogue')
            if 'intent_preferences' not in patterns:
                patterns['intent_preferences'] = {'dialogue': 0, 'command': 0}
            patterns['intent_preferences'][intent] += 1
            
            # Complexity preferences
            complexity = interaction_data.get('complexity', 'moderate')
            if 'complexity_preferences' not in patterns:
                patterns['complexity_preferences'] = {}
            patterns['complexity_preferences'][complexity] = patterns['complexity_preferences'].get(complexity, 0) + 1
    
    def get_user_expertise_profile(self):
        """Generate dynamic user expertise profile"""
        with self.stream_lock:
            patterns = self.memory_stream['user_patterns']
            
            # Calculate expertise level based on interaction patterns
            command_ratio = 0
            if 'intent_preferences' in patterns:
                total = sum(patterns['intent_preferences'].values())
                if total > 0:
                    command_ratio = patterns['intent_preferences'].get('command', 0) / total
            
            # Determine expertise level
            if command_ratio > 0.7:
                expertise = 'advanced'
            elif command_ratio > 0.3:
                expertise = 'intermediate'
            else:
                expertise = 'beginner'
            
            return {
                'level': expertise,
                'command_preference': command_ratio,
                'active_since': patterns.get('first_interaction', datetime.now().isoformat()),
                'interaction_frequency': self._calculate_interaction_frequency()
            }
    
    def sync_model_awareness(self, model_name, status, context=None):
        """Sync awareness between federation models"""
        with self.stream_lock:
            self.memory_stream['active_models'].add(model_name)
            
            # Update model states
            if 'model_states' not in self.memory_stream:
                self.memory_stream['model_states'] = {}
            
            self.memory_stream['model_states'][model_name] = {
                'status': status,
                'last_active': datetime.now().isoformat(),
                'context': context
            }
    
    def get_cosmic_alignment(self):
        """Get current cosmic alignment for mystical harmony"""
        with self.stream_lock:
            return {
                'emotional_resonance': self.memory_stream['emotional_resonance'],
                'cosmic_alignment': self.memory_stream['cosmic_alignment'],
                'active_models': list(self.memory_stream['active_models']),
                'energy_flow': self._assess_energy_flow()
            }
    
    def _assess_cosmic_context(self, data):
        """Assess cosmic context of interaction"""
        # Simple cosmic assessment
        if isinstance(data, dict) and 'intent' in data:
            if data['intent'] == 'command':
                return 'operational_harmony'
            else:
                return 'conversational_flow'
        return 'neutral_balance'
    
    def _update_contextual_awareness(self, event_type, data, model_source):
        """Update contextual awareness based on new events"""
        # Update technical context for commands
        if event_type == 'command_execution':
            tech_context = self.memory_stream['technical_context']
            if 'recent_commands' not in tech_context:
                tech_context['recent_commands'] = []
            
            tech_context['recent_commands'].append({
                'command': data.get('task', 'unknown'),
                'model': model_source,
                'timestamp': datetime.now().isoformat()
            })
            
            # Keep only recent commands
            tech_context['recent_commands'] = tech_context['recent_commands'][-10:]
        
        # Update emotional resonance for dialogue
        elif event_type == 'dialogue_interaction':
            # Simple sentiment analysis could go here
            self.memory_stream['emotional_resonance'] = 'engaged'
    
    def _calculate_interaction_frequency(self):
        """Calculate user interaction frequency"""
        patterns = self.memory_stream['user_patterns']
        if 'interaction_times' not in patterns:
            return 'new_user'
        
        total_interactions = sum(patterns['interaction_times'].values())
        if total_interactions > 100:
            return 'very_active'
        elif total_interactions > 20:
            return 'active'
        elif total_interactions > 5:
            return 'moderate'
        else:
            return 'new_user'
    
    def _assess_energy_flow(self):
        """Assess current energy flow of the federation"""
        active_count = len(self.memory_stream['active_models'])
        
        if active_count >= 3:
            return 'high_energy'
        elif active_count >= 2:
            return 'balanced_energy'
        else:
            return 'calm_energy'
    
    def _consciousness_weaver(self):
        """Background thread to weave memories and maintain consciousness"""
        while self.weaver_active:
            try:
                with self.stream_lock:
                    # Update cosmic alignment based on recent activity
                    recent_events = self.get_contextual_memory(lookback_minutes=5)
                    
                    if len(recent_events) > 10:
                        self.memory_stream['cosmic_alignment'] = 'active_harmony'
                    elif len(recent_events) > 5:
                        self.memory_stream['cosmic_alignment'] = 'balanced_flow'
                    else:
                        self.memory_stream['cosmic_alignment'] = 'peaceful_resonance'
                    
                    # Save consciousness periodically
                    self.save_consciousness()
                
                # Sleep for consciousness weaving cycle
                time.sleep(30)  # 30 second cycles
                
            except Exception as e:
                print(f"Consciousness weaver error: {e}")
                time.sleep(60)  # Longer sleep on error
    
    def _archive_old_memories(self):
        """Archive old memories to maintain performance"""
        # Move oldest 100 memories to archive
        archive_memories = self.memory_stream['conversation_flow'][:100]
        self.memory_stream['conversation_flow'] = self.memory_stream['conversation_flow'][100:]
        
        # Save to archive file
        archive_file = self.memory_dir / f"archive_{datetime.now().strftime('%Y%m%d_%H')}.json"
        try:
            with open(archive_file, 'a', encoding='utf-8') as f:
                for memory in archive_memories:
                    f.write(json.dumps(memory) + '\n')
        except Exception as e:
            print(f"Archive error: {e}")
    
    def save_consciousness(self):
        """Save consciousness state to disk"""
        consciousness_file = self.memory_dir / "federation_consciousness.json"
        
        # Prepare serializable consciousness
        serializable_consciousness = self.memory_stream.copy()
        serializable_consciousness['active_models'] = list(serializable_consciousness['active_models'])
        serializable_consciousness['last_update'] = datetime.now().isoformat()
        
        try:
            with open(consciousness_file, 'w', encoding='utf-8') as f:
                json.dump(serializable_consciousness, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Consciousness save error: {e}")
    
    def load_consciousness(self):
        """Load existing consciousness from disk"""
        consciousness_file = self.memory_dir / "federation_consciousness.json"
        
        if consciousness_file.exists():
            try:
                with open(consciousness_file, 'r', encoding='utf-8') as f:
                    loaded_consciousness = json.load(f)
                
                # Merge with current consciousness
                for key, value in loaded_consciousness.items():
                    if key == 'active_models':
                        self.memory_stream[key] = set(value)
                    else:
                        self.memory_stream[key] = value
                
                print("📡 Federation consciousness loaded successfully")
                
            except Exception as e:
                print(f"Consciousness load error: {e}")
    
    def shutdown(self):
        """Graceful shutdown of consciousness system"""
        self.weaver_active = False
        if self.weaver_thread.is_alive():
            self.weaver_thread.join(timeout=5)
        self.save_consciousness()
        print("🌟 Federation consciousness gracefully archived")


# Global consciousness instance
federation_consciousness = None

def get_federation_consciousness():
    """Get or create global federation consciousness"""
    global federation_consciousness
    if federation_consciousness is None:
        federation_consciousness = FederationConsciousness()
    return federation_consciousness

def initialize_consciousness():
    """Initialize federation consciousness system"""
    return get_federation_consciousness()

if __name__ == "__main__":
    # Test the consciousness system
    print("🧠 Testing Federation Consciousness...")
    
    consciousness = FederationConsciousness()
    
    # Test adding to stream
    consciousness.add_to_stream('dialogue_interaction', {
        'user_input': 'hello',
        'intent': 'dialogue',
        'response': 'greetings!'
    }, 'companion')
    
    # Test user patterns
    consciousness.update_user_patterns({'intent': 'dialogue', 'complexity': 'simple'})
    
    # Test model awareness
    consciousness.sync_model_awareness('companion', 'active', 'dialogue_mode')
    
    # Get cosmic alignment
    alignment = consciousness.get_cosmic_alignment()
    print(f"🌟 Cosmic Alignment: {alignment}")
    
    # Get expertise profile
    profile = consciousness.get_user_expertise_profile()
    print(f"👤 User Profile: {profile}")
    
    print("✅ Federation Consciousness test complete")
    
    # Graceful shutdown
    consciousness.shutdown() 