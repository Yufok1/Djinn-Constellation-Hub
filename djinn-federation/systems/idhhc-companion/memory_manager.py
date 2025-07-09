"""
💾 Enhanced Memory Management System for IDHHC
Vector database, conversational summaries, and session persistence
"""

import json
import time
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from advanced_toolkits import HarmonicPurveyor

class MemoryManager:
    """Enhanced memory management with vector database and summaries"""
    
    def __init__(self):
        self.harmonic_purveyor = HarmonicPurveyor()
        self.memory_store = {}
        self.conversation_history = []
        self.session_summaries = []
        self.void_troubleshooting_history = []
        self.user_preferences = {}
        self.performance_metrics = {}
        
        # Initialize memory storage
        self.memory_dir = Path("memory_bank")
        self.memory_dir.mkdir(exist_ok=True)
        
    def store_interaction(self, user_input: str, response: str, context: Dict = None) -> str:
        """Store interaction in memory with context"""
        interaction_id = hashlib.md5(f"{user_input}{time.time()}".encode()).hexdigest()[:8]
        
        interaction = {
            "id": interaction_id,
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "response": response,
            "context": context or {},
            "session_id": self._get_current_session_id()
        }
        
        self.conversation_history.append(interaction)
        self.memory_store[interaction_id] = interaction
        
        # Update performance metrics
        self._update_performance_metrics(interaction)
        
        return f"Interaction stored: {interaction_id}"
    
    def create_conversational_summary(self) -> str:
        """Create compact summary of conversation history"""
        if not self.conversation_history:
            return "No conversation history to summarize"
        
        # Extract key themes and patterns
        themes = self._extract_conversation_themes()
        key_points = self._extract_key_points()
        user_patterns = self._analyze_user_patterns()
        
        summary = {
            "session_id": self._get_current_session_id(),
            "timestamp": datetime.now().isoformat(),
            "total_interactions": len(self.conversation_history),
            "themes": themes,
            "key_points": key_points,
            "user_patterns": user_patterns,
            "void_specific_issues": self._extract_void_issues()
        }
        
        self.session_summaries.append(summary)
        
        return f"Conversational summary created: {len(themes)} themes, {len(key_points)} key points"
    
    def retrieve_context(self, query: str, limit: int = 5) -> List[Dict]:
        """Retrieve relevant context based on query"""
        relevant_interactions = []
        
        # Simple keyword matching (in production, use vector similarity)
        query_lower = query.lower()
        
        for interaction in reversed(self.conversation_history):
            if (query_lower in interaction["user_input"].lower() or 
                query_lower in interaction["response"].lower()):
                relevant_interactions.append(interaction)
                
                if len(relevant_interactions) >= limit:
                    break
        
        return relevant_interactions
    
    def store_void_troubleshooting(self, issue: str, solution: str, success: bool) -> str:
        """Store VOID-specific troubleshooting history"""
        troubleshooting_entry = {
            "timestamp": datetime.now().isoformat(),
            "issue": issue,
            "solution": solution,
            "success": success,
            "session_id": self._get_current_session_id()
        }
        
        self.void_troubleshooting_history.append(troubleshooting_entry)
        
        return f"VOID troubleshooting stored: {'Success' if success else 'Failed'}"
    
    def get_void_solutions(self, issue_keywords: List[str]) -> List[Dict]:
        """Retrieve VOID solutions for similar issues"""
        relevant_solutions = []
        
        for entry in self.void_troubleshooting_history:
            if entry["success"]:  # Only successful solutions
                for keyword in issue_keywords:
                    if keyword.lower() in entry["issue"].lower():
                        relevant_solutions.append(entry)
                        break
        
        return relevant_solutions
    
    def update_user_preferences(self, preferences: Dict) -> str:
        """Update user preferences and workflow patterns"""
        self.user_preferences.update(preferences)
        
        return f"User preferences updated: {len(preferences)} new preferences"
    
    def get_user_preferences(self) -> Dict:
        """Get current user preferences"""
        return self.user_preferences.copy()
    
    def _get_current_session_id(self) -> str:
        """Generate current session ID"""
        return f"session_{int(time.time())}"
    
    def _extract_conversation_themes(self) -> List[str]:
        """Extract themes from conversation history"""
        themes = []
        
        # Simple theme extraction (in production, use NLP)
        common_themes = ["VOID", "debugging", "extension", "testing", "git", "build"]
        
        for theme in common_themes:
            theme_count = sum(1 for interaction in self.conversation_history 
                            if theme.lower() in interaction["user_input"].lower() or 
                               theme.lower() in interaction["response"].lower())
            
            if theme_count > 0:
                themes.append(f"{theme}: {theme_count} mentions")
        
        return themes
    
    def _extract_key_points(self) -> List[str]:
        """Extract key points from conversation"""
        key_points = []
        
        # Extract points with high information content
        for interaction in self.conversation_history[-10:]:  # Last 10 interactions
            if len(interaction["response"]) > 100:  # Substantial responses
                key_points.append(f"{interaction['user_input'][:50]}... -> {len(interaction['response'])} chars")
        
        return key_points
    
    def _analyze_user_patterns(self) -> Dict:
        """Analyze user interaction patterns"""
        patterns = {
            "total_interactions": len(self.conversation_history),
            "average_response_length": 0,
            "common_topics": [],
            "preferred_modes": []
        }
        
        if self.conversation_history:
            total_length = sum(len(i["response"]) for i in self.conversation_history)
            patterns["average_response_length"] = total_length / len(self.conversation_history)
        
        return patterns
    
    def _extract_void_issues(self) -> List[str]:
        """Extract VOID-specific issues from conversation"""
        void_issues = []
        
        for interaction in self.conversation_history:
            if "void" in interaction["user_input"].lower():
                void_issues.append(interaction["user_input"][:100])
        
        return void_issues
    
    def _update_performance_metrics(self, interaction: Dict) -> None:
        """Update performance metrics"""
        session_id = interaction["session_id"]
        
        if session_id not in self.performance_metrics:
            self.performance_metrics[session_id] = {
                "interactions": 0,
                "total_response_time": 0,
                "successful_responses": 0
            }
        
        self.performance_metrics[session_id]["interactions"] += 1
        
        # Simple success detection (in production, use more sophisticated metrics)
        if len(interaction["response"]) > 50:
            self.performance_metrics[session_id]["successful_responses"] += 1
    
    def get_performance_report(self) -> str:
        """Get performance metrics report"""
        if not self.performance_metrics:
            return "No performance metrics available"
        
        total_interactions = sum(m["interactions"] for m in self.performance_metrics.values())
        total_successful = sum(m["successful_responses"] for m in self.performance_metrics.values())
        
        success_rate = (total_successful / total_interactions * 100) if total_interactions > 0 else 0
        
        return f"""
📊 PERFORMANCE REPORT:
Total Sessions: {len(self.performance_metrics)}
Total Interactions: {total_interactions}
Successful Responses: {total_successful}
Success Rate: {success_rate:.1f}%
Memory Entries: {len(self.memory_store)}
VOID Solutions: {len(self.void_troubleshooting_history)}
        """.strip()
    
    def save_memory_to_disk(self) -> str:
        """Save memory to disk for persistence"""
        memory_data = {
            "conversation_history": self.conversation_history[-100:],  # Last 100 interactions
            "session_summaries": self.session_summaries,
            "void_troubleshooting_history": self.void_troubleshooting_history,
            "user_preferences": self.user_preferences,
            "performance_metrics": self.performance_metrics
        }
        
        memory_file = self.memory_dir / f"memory_{int(time.time())}.json"
        
        try:
            with open(memory_file, 'w') as f:
                json.dump(memory_data, f, indent=2)
            return f"Memory saved to disk: {memory_file}"
        except Exception as e:
            return f"Error saving memory: {str(e)}"
    
    def load_memory_from_disk(self, memory_file: str) -> str:
        """Load memory from disk"""
        try:
            with open(memory_file, 'r') as f:
                memory_data = json.load(f)
            
            self.conversation_history = memory_data.get("conversation_history", [])
            self.session_summaries = memory_data.get("session_summaries", [])
            self.void_troubleshooting_history = memory_data.get("void_troubleshooting_history", [])
            self.user_preferences = memory_data.get("user_preferences", {})
            self.performance_metrics = memory_data.get("performance_metrics", {})
            
            return f"Memory loaded from disk: {len(self.conversation_history)} interactions"
        except Exception as e:
            return f"Error loading memory: {str(e)}"

# Global memory manager instance
memory_manager = MemoryManager()

def store_interaction(user_input: str, response: str, context: Dict = None):
    """Store interaction in memory"""
    return memory_manager.store_interaction(user_input, response, context)

def get_relevant_context(query: str, limit: int = 5):
    """Get relevant context for query"""
    return memory_manager.retrieve_context(query, limit)

def create_memory_summary():
    """Create conversational summary"""
    return memory_manager.create_conversational_summary()

def get_memory_status():
    """Get memory system status"""
    return memory_manager.get_performance_report() 