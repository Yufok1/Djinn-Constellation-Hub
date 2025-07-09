#!/usr/bin/env python3
"""
Cross-Model Communication Framework
IDHHC's Revolutionary Shared Awareness System

Models share contextual information and enhance each other's capabilities
through continuous cross-model learning and collaboration.
"""

import json
import time
import threading
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional
from pathlib import Path

@dataclass
class ModelInteraction:
    """Represents an interaction with context for sharing"""
    model_source: str
    interaction_type: str  # 'dialogue', 'command', 'analysis', 'guidance'
    user_input: str
    model_response: str
    context_data: Dict[str, Any]
    emotional_tone: str
    technical_complexity: int  # 1-10 scale
    timestamp: str
    insights: List[str]

@dataclass
class CrossModelInsight:
    """Insights shared between models"""
    insight_id: str
    source_model: str
    target_models: List[str]
    insight_type: str  # 'emotional_context', 'technical_pattern', 'user_preference', 'strategic_guidance'
    content: Dict[str, Any]
    confidence: float  # 0.0-1.0
    timestamp: str
    applied_count: int = 0

class CrossModelCommunication:
    """
    Revolutionary Cross-Model Communication System
    Enables models to share awareness and enhance each other's capabilities
    """
    
    def __init__(self, memory_dir="memory_bank"):
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(exist_ok=True)
        
        # Model registry
        self.active_models = {
            'companion': {'role': 'dialogue_specialist', 'expertise': 'emotional_intelligence'},
            'constellation-lite': {'role': 'fast_coordinator', 'expertise': 'quick_analysis'},
            'constellation-core': {'role': 'balanced_coordinator', 'expertise': 'moderate_complexity'},
            'constellation-max': {'role': 'advanced_coordinator', 'expertise': 'complex_reasoning'},
            'idhhc': {'role': 'operational_strategist', 'expertise': 'technical_execution'},
            'council': {'role': 'wisdom_provider', 'expertise': 'ethical_guidance'}
        }
        
        # Shared contextual memory
        self.shared_context = {
            'user_profile': {},
            'conversation_threads': [],
            'technical_patterns': {},
            'emotional_patterns': {},
            'strategic_insights': [],
            'cross_model_learnings': {}
        }
        
        # Communication channels
        self.insight_queue = {}  # model_name -> List[CrossModelInsight]
        self.collaboration_sessions = {}  # session_id -> models involved
        
        # Thread safety
        self.comm_lock = threading.Lock()
        
        # Background communication processor
        self.processor_active = True
        self.processor_thread = threading.Thread(target=self._communication_processor, daemon=True)
        self.processor_thread.start()
        
        # Load existing communications
        self.load_shared_context()
        
        print("🌐 Cross-Model Communication Framework initialized")
        print("🧠 Federation Hive Mind coming online...")
    
    def register_interaction(self, interaction: ModelInteraction):
        """Register an interaction and generate insights for other models"""
        with self.comm_lock:
            # Store interaction in shared context
            self.shared_context['conversation_threads'].append(asdict(interaction))
            
            # Generate insights for other models
            insights = self._extract_insights(interaction)
            
            # Distribute insights to relevant models
            for insight in insights:
                self._distribute_insight(insight)
            
            # Update user profile
            self._update_user_profile(interaction)
            
            # Trigger collaboration if needed
            self._check_collaboration_triggers(interaction)
    
    def get_context_for_model(self, model_name: str, interaction_type: str) -> Dict[str, Any]:
        """Get relevant context for a model before it processes a request"""
        with self.comm_lock:
            context = {
                'user_profile': self.shared_context['user_profile'].copy(),
                'recent_interactions': self._get_recent_interactions(5),
                'relevant_insights': self._get_insights_for_model(model_name),
                'emotional_context': self._get_emotional_context(),
                'technical_context': self._get_technical_context(),
                'strategic_context': self._get_strategic_context()
            }
            
            # Add model-specific context
            if model_name == 'companion':
                context['emotional_intelligence'] = self._get_emotional_intelligence_data()
                context['dialogue_patterns'] = self._get_dialogue_patterns()
            
            elif model_name == 'idhhc':
                context['technical_history'] = self._get_technical_history()
                context['execution_patterns'] = self._get_execution_patterns()
                context['toolkit_preferences'] = self._get_toolkit_preferences()
            
            elif model_name.startswith('constellation'):
                context['routing_patterns'] = self._get_routing_patterns()
                context['complexity_insights'] = self._get_complexity_insights()
            
            elif model_name == 'council':
                context['ethical_considerations'] = self._get_ethical_context()
                context['wisdom_requests'] = self._get_wisdom_requests()
            
            return context
    
    def share_insight(self, source_model: str, insight_type: str, content: Dict[str, Any], 
                     target_models: List[str] = None, confidence: float = 0.8):
        """Allow a model to share an insight with other models"""
        if target_models is None:
            target_models = [m for m in self.active_models.keys() if m != source_model]
        
        insight = CrossModelInsight(
            insight_id=f"{source_model}_{int(time.time())}_{len(self.shared_context['strategic_insights'])}",
            source_model=source_model,
            target_models=target_models,
            insight_type=insight_type,
            content=content,
            confidence=confidence,
            timestamp=datetime.now().isoformat()
        )
        
        with self.comm_lock:
            self.shared_context['strategic_insights'].append(asdict(insight))
            self._distribute_insight(insight)
            
        print(f"💡 {source_model} shared insight: {insight_type} -> {target_models}")
    
    def request_collaboration(self, initiating_model: str, task_description: str, 
                            required_models: List[str]) -> str:
        """Request collaboration between multiple models for complex tasks"""
        session_id = f"collab_{int(time.time())}_{initiating_model}"
        
        collaboration_session = {
            'session_id': session_id,
            'initiating_model': initiating_model,
            'task_description': task_description,
            'required_models': required_models,
            'status': 'initiated',
            'contributions': {},
            'final_synthesis': None,
            'timestamp': datetime.now().isoformat()
        }
        
        with self.comm_lock:
            self.collaboration_sessions[session_id] = collaboration_session
        
        print(f"🤝 Collaboration session {session_id} initiated by {initiating_model}")
        print(f"📋 Task: {task_description}")
        print(f"👥 Required models: {required_models}")
        
        return session_id
    
    def contribute_to_collaboration(self, session_id: str, contributing_model: str, 
                                  contribution: Dict[str, Any]):
        """Allow a model to contribute to a collaborative session"""
        with self.comm_lock:
            if session_id in self.collaboration_sessions:
                session = self.collaboration_sessions[session_id]
                session['contributions'][contributing_model] = {
                    'content': contribution,
                    'timestamp': datetime.now().isoformat()
                }
                
                # Check if all required models have contributed
                if all(model in session['contributions'] for model in session['required_models']):
                    session['status'] = 'ready_for_synthesis'
                    print(f"✅ All models contributed to session {session_id} - ready for synthesis")
    
    def synthesize_collaboration(self, session_id: str) -> Dict[str, Any]:
        """Synthesize contributions from multiple models into unified insight"""
        with self.comm_lock:
            if session_id not in self.collaboration_sessions:
                return None
            
            session = self.collaboration_sessions[session_id]
            if session['status'] != 'ready_for_synthesis':
                return None
            
            # Create synthesis of all contributions
            synthesis = {
                'task_description': session['task_description'],
                'contributing_models': list(session['contributions'].keys()),
                'unified_insight': self._create_unified_insight(session['contributions']),
                'confidence': self._calculate_synthesis_confidence(session['contributions']),
                'recommendations': self._generate_synthesis_recommendations(session['contributions']),
                'timestamp': datetime.now().isoformat()
            }
            
            session['final_synthesis'] = synthesis
            session['status'] = 'completed'
            
            # Share synthesis as insight to all models
            self.share_insight(
                source_model='collaboration_synthesis',
                insight_type='collaborative_synthesis',
                content=synthesis,
                confidence=synthesis['confidence']
            )
            
            print(f"🎯 Collaboration synthesis completed for session {session_id}")
            return synthesis
    
    def _extract_insights(self, interaction: ModelInteraction) -> List[CrossModelInsight]:
        """Extract insights from an interaction that could benefit other models"""
        insights = []
        
        # Emotional insights for technical models
        if interaction.model_source == 'companion' and interaction.emotional_tone:
            emotional_insight = CrossModelInsight(
                insight_id=f"emotional_{int(time.time())}",
                source_model='companion',
                target_models=['idhhc', 'constellation-core', 'constellation-max'],
                insight_type='emotional_context',
                content={
                    'user_emotional_state': interaction.emotional_tone,
                    'interaction_context': interaction.context_data,
                    'communication_style': self._analyze_communication_style(interaction.user_input)
                },
                confidence=0.8,
                timestamp=datetime.now().isoformat()
            )
            insights.append(emotional_insight)
        
        # Technical insights for dialogue models
        if interaction.model_source == 'idhhc' and interaction.technical_complexity > 7:
            technical_insight = CrossModelInsight(
                insight_id=f"technical_{int(time.time())}",
                source_model='idhhc',
                target_models=['companion', 'council'],
                insight_type='technical_pattern',
                content={
                    'complexity_level': interaction.technical_complexity,
                    'technical_domain': self._identify_technical_domain(interaction.user_input),
                    'execution_patterns': interaction.insights
                },
                confidence=0.9,
                timestamp=datetime.now().isoformat()
            )
            insights.append(technical_insight)
        
        # Strategic insights from council
        if interaction.model_source == 'council':
            strategic_insight = CrossModelInsight(
                insight_id=f"strategic_{int(time.time())}",
                source_model='council',
                target_models=['idhhc', 'constellation-max'],
                insight_type='strategic_guidance',
                content={
                    'ethical_considerations': interaction.context_data.get('ethics', {}),
                    'strategic_recommendations': interaction.insights,
                    'wisdom_context': interaction.model_response
                },
                confidence=0.95,
                timestamp=datetime.now().isoformat()
            )
            insights.append(strategic_insight)
        
        return insights
    
    def _distribute_insight(self, insight: CrossModelInsight):
        """Distribute insight to target models"""
        for target_model in insight.target_models:
            if target_model not in self.insight_queue:
                self.insight_queue[target_model] = []
            self.insight_queue[target_model].append(insight)
            
            # Limit queue size
            if len(self.insight_queue[target_model]) > 50:
                self.insight_queue[target_model] = self.insight_queue[target_model][-30:]
    
    def _get_insights_for_model(self, model_name: str) -> List[Dict[str, Any]]:
        """Get relevant insights for a specific model"""
        if model_name not in self.insight_queue:
            return []
        
        # Return recent high-confidence insights
        recent_insights = []
        for insight in self.insight_queue[model_name][-10:]:
            if insight.confidence > 0.7:
                recent_insights.append(asdict(insight))
        
        return recent_insights
    
    def _update_user_profile(self, interaction: ModelInteraction):
        """Update shared user profile based on interaction"""
        profile = self.shared_context['user_profile']
        
        # Update interaction patterns
        if 'interaction_patterns' not in profile:
            profile['interaction_patterns'] = {}
        
        model_type = interaction.model_source
        if model_type not in profile['interaction_patterns']:
            profile['interaction_patterns'][model_type] = 0
        profile['interaction_patterns'][model_type] += 1
        
        # Update complexity preferences
        if 'complexity_preferences' not in profile:
            profile['complexity_preferences'] = []
        profile['complexity_preferences'].append(interaction.technical_complexity)
        
        # Keep only recent preferences
        if len(profile['complexity_preferences']) > 20:
            profile['complexity_preferences'] = profile['complexity_preferences'][-20:]
        
        # Update emotional patterns
        if 'emotional_patterns' not in profile:
            profile['emotional_patterns'] = {}
        if interaction.emotional_tone:
            profile['emotional_patterns'][interaction.emotional_tone] = \
                profile['emotional_patterns'].get(interaction.emotional_tone, 0) + 1
    
    def _communication_processor(self):
        """Background processor for cross-model communications"""
        while self.processor_active:
            try:
                with self.comm_lock:
                    # Process pending collaborations
                    for session_id, session in self.collaboration_sessions.items():
                        if session['status'] == 'ready_for_synthesis':
                            self.synthesize_collaboration(session_id)
                    
                    # Clean up old insights
                    self._cleanup_old_insights()
                    
                    # Save shared context periodically
                    self.save_shared_context()
                
                time.sleep(30)  # Process every 30 seconds
                
            except Exception as e:
                print(f"Communication processor error: {e}")
                time.sleep(60)
    
    def _create_unified_insight(self, contributions: Dict[str, Any]) -> str:
        """Create unified insight from multiple model contributions"""
        # Simple synthesis - in practice this could use AI to merge insights
        unified_parts = []
        for model, contrib in contributions.items():
            unified_parts.append(f"{model}: {contrib['content']}")
        
        return " | ".join(unified_parts)
    
    def _calculate_synthesis_confidence(self, contributions: Dict[str, Any]) -> float:
        """Calculate confidence score for synthesis"""
        # More models contributing = higher confidence
        base_confidence = min(0.9, len(contributions) * 0.15)
        return base_confidence
    
    def _generate_synthesis_recommendations(self, contributions: Dict[str, Any]) -> List[str]:
        """Generate recommendations from synthesis"""
        recommendations = []
        
        if 'idhhc' in contributions and 'companion' in contributions:
            recommendations.append("Integrate technical execution with emotional awareness")
        
        if 'council' in contributions:
            recommendations.append("Consider ethical implications in implementation")
        
        if len(contributions) >= 3:
            recommendations.append("Multi-model collaborative approach recommended")
        
        return recommendations
    
    # Helper methods for context extraction
    def _get_recent_interactions(self, count: int) -> List[Dict[str, Any]]:
        return self.shared_context['conversation_threads'][-count:]
    
    def _get_emotional_context(self) -> Dict[str, Any]:
        return self.shared_context.get('emotional_patterns', {})
    
    def _get_technical_context(self) -> Dict[str, Any]:
        return self.shared_context.get('technical_patterns', {})
    
    def _get_strategic_context(self) -> List[Dict[str, Any]]:
        return self.shared_context.get('strategic_insights', [])[-5:]
    
    def _analyze_communication_style(self, user_input: str) -> str:
        """Analyze user's communication style"""
        if len(user_input) < 10:
            return 'brief'
        elif '?' in user_input:
            return 'inquisitive'
        elif user_input.isupper():
            return 'emphatic'
        else:
            return 'conversational'
    
    def _identify_technical_domain(self, user_input: str) -> str:
        """Identify technical domain from input"""
        domains = {
            'coding': ['code', 'programming', 'function', 'class', 'method'],
            'system': ['system', 'server', 'deploy', 'infrastructure'],
            'data': ['data', 'database', 'analysis', 'report'],
            'ai': ['ai', 'model', 'training', 'prediction']
        }
        
        user_lower = user_input.lower()
        for domain, keywords in domains.items():
            if any(keyword in user_lower for keyword in keywords):
                return domain
        
        return 'general'
    
    def save_shared_context(self):
        """Save shared context to disk"""
        context_file = self.memory_dir / "cross_model_context.json"
        try:
            with open(context_file, 'w', encoding='utf-8') as f:
                json.dump(self.shared_context, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Cross-model context save error: {e}")
    
    def load_shared_context(self):
        """Load shared context from disk"""
        context_file = self.memory_dir / "cross_model_context.json"
        if context_file.exists():
            try:
                with open(context_file, 'r', encoding='utf-8') as f:
                    loaded_context = json.load(f)
                    self.shared_context.update(loaded_context)
                print("🌐 Cross-model shared context loaded")
            except Exception as e:
                print(f"Cross-model context load error: {e}")
    
    def _cleanup_old_insights(self):
        """Clean up old insights to maintain performance"""
        # Keep only recent insights
        for model in self.insight_queue:
            self.insight_queue[model] = self.insight_queue[model][-30:]
    
    def get_communication_status(self) -> Dict[str, Any]:
        """Get status of cross-model communication system"""
        with self.comm_lock:
            return {
                'active_models': list(self.active_models.keys()),
                'insight_queue_sizes': {model: len(insights) for model, insights in self.insight_queue.items()},
                'active_collaborations': len([s for s in self.collaboration_sessions.values() if s['status'] != 'completed']),
                'total_interactions': len(self.shared_context['conversation_threads']),
                'user_profile_data': bool(self.shared_context['user_profile'])
            }
    
    def shutdown(self):
        """Graceful shutdown"""
        self.processor_active = False
        if self.processor_thread.is_alive():
            self.processor_thread.join(timeout=5)
        self.save_shared_context()
        print("🌐 Cross-Model Communication Framework shut down gracefully")


# Global communication instance
cross_model_comm = None

def get_cross_model_communication():
    """Get or create global cross-model communication instance"""
    global cross_model_comm
    if cross_model_comm is None:
        cross_model_comm = CrossModelCommunication()
    return cross_model_comm

if __name__ == "__main__":
    # Test the cross-model communication system
    print("🌐 Testing Cross-Model Communication Framework...")
    
    comm = CrossModelCommunication()
    
    # Test registering interactions
    interaction1 = ModelInteraction(
        model_source='companion',
        interaction_type='dialogue',
        user_input='I feel frustrated with this code',
        model_response='I understand your frustration. Let me help you work through this.',
        context_data={'user_emotion': 'frustrated'},
        emotional_tone='supportive',
        technical_complexity=3,
        timestamp=datetime.now().isoformat(),
        insights=['user needs emotional support', 'technical assistance required']
    )
    
    comm.register_interaction(interaction1)
    
    # Test getting context for IDHHC
    idhhc_context = comm.get_context_for_model('idhhc', 'command')
    print(f"🤖 IDHHC Context: {idhhc_context['emotional_context']}")
    
    # Test collaboration request
    session_id = comm.request_collaboration(
        'idhhc', 
        'Optimize system performance while maintaining user satisfaction',
        ['companion', 'council', 'idhhc']
    )
    
    # Test sharing insights
    comm.share_insight(
        'companion',
        'emotional_intelligence',
        {'user_satisfaction_level': 'moderate', 'emotional_needs': 'encouragement'},
        ['idhhc', 'council']
    )
    
    # Get status
    status = comm.get_communication_status()
    print(f"📊 Communication Status: {status}")
    
    comm.shutdown()
    print("✅ Cross-Model Communication test complete") 