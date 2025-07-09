#!/usr/bin/env python3
"""
⚡ EFFICIENCY-FIRST DUAL-TIER HUB ⚡
Smart ramping from low-fi to high-fi based on actual need

PHILOSOPHY: 
- Default to LOW-FI (fast, efficient)
- Ramp up ONLY when task genuinely needs it
- Monitor performance and adapt
- Never waste resources on under-performing machines
"""

import asyncio
import json
import os
import subprocess
import sys
import time
import psutil
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class EfficiencyFirstHub:
    """
    ⚡ Efficiency-First Intelligence Hub ⚡
    
    CORE PRINCIPLES:
    1. DEFAULT LOW-FI: Start with lightweight models
    2. SMART RAMPING: Only escalate when genuinely needed
    3. PERFORMANCE MONITORING: Track system load and response times
    4. ADAPTIVE LEARNING: Remember what works for different tasks
    5. RESOURCE PROTECTION: Never overwhelm under-performing machines
    """
    
    def __init__(self):
        self.current_tier = "local"  # Always start local
        self.performance_history = []
        self.task_success_rates = {
            "local": {"coding": 0.8, "reasoning": 0.7, "chat": 0.95},
            "cloud": {"coding": 0.95, "reasoning": 0.9, "chat": 0.85}
        }
        
        # Efficiency-first tier definitions
        self.tiers = {
            "local": {
                "name": "🏠 EFFICIENT LOCAL FEDERATION",
                "description": "Fast, lightweight models optimized for performance",
                "models": {
                    # Ordered by efficiency (smallest first)
                    "ultra_fast": "tinydolphin-constellation:latest",      # 636MB
                    "balanced": "dolphin-phi-constellation:latest",       # 1.6GB  
                    "capable": "phi3-constellation:latest",               # 2.2GB
                    "coding": "djinn-federation:idhhc",                   # 19GB (only when needed)
                    "wisdom": "djinn-federation:council",                 # 7.4GB
                    "dialogue": "djinn-federation:companion"              # 4.9GB
                },
                "ram_requirements": {
                    "ultra_fast": 1,    # 1GB RAM
                    "balanced": 3,      # 3GB RAM
                    "capable": 4,       # 4GB RAM
                    "coding": 24,       # 24GB RAM
                    "wisdom": 10,       # 10GB RAM
                    "dialogue": 8       # 8GB RAM
                }
            },
            "cloud": {
                "name": "☁️ DJINN CLOUD FEDERATION", 
                "description": "Revolutionary Djinn models with mystical coding and reasoning powers",
                "models": {
                    "cosmic_coding": "djinn-cosmic-coder:latest",        # 65GB - MoE multimodal sorcery
                    "deep_thinking": "djinn-deep-thinker:latest",        # 32GB - ancient wisdom + thinking mode
                    "advanced_reasoning": "djinn-logic-master:latest",   # 11GB - sovereign logic powers
                    "enterprise_coding": "djinn-enterprise-architect:latest"  # 22GB - corporate mysticism
                },
                "ram_requirements": {
                    "cosmic_coding": 80,      # 80GB RAM
                    "deep_thinking": 40,      # 40GB RAM
                    "advanced_reasoning": 16, # 16GB RAM
                    "enterprise_coding": 28   # 28GB RAM
                }
            }
        }
        
        # Efficiency-first escalation rules
        self.escalation_triggers = {
            "complexity": {
                "ultra_simple": 0.1,    # "hi", "hello", "thanks"
                "simple": 0.3,          # Basic questions, simple tasks
                "moderate": 0.6,        # Coding, analysis, explanations
                "complex": 0.8,         # Advanced reasoning, architecture
                "revolutionary": 0.95   # Multimodal, massive context needs
            },
            "task_types": {
                "greeting": "ultra_fast",
                "simple_question": "balanced", 
                "coding_help": "coding",
                "debug": "capable",
                "architecture": "cloud",
                "multimodal": "cloud",
                "deep_analysis": "cloud"
            },
            "performance_thresholds": {
                "response_time_limit": 30,    # Seconds before escalating
                "memory_usage_limit": 0.85,   # 85% RAM before escalating
                "cpu_usage_limit": 0.90       # 90% CPU before escalating
            }
        }
        
    def get_system_capabilities(self) -> Dict:
        """Check current system performance and capabilities"""
        try:
            memory = psutil.virtual_memory()
            cpu_percent = psutil.cpu_percent(interval=1)
            
            capabilities = {
                "total_ram_gb": round(memory.total / (1024**3), 1),
                "available_ram_gb": round(memory.available / (1024**3), 1),
                "ram_usage_percent": memory.percent,
                "cpu_usage_percent": cpu_percent,
                "is_high_performance": memory.total >= 32 * (1024**3),  # 32GB+
                "is_under_stress": memory.percent > 85 or cpu_percent > 90
            }
            
            return capabilities
        except Exception as e:
            # Assume limited system if can't check
            return {
                "total_ram_gb": 8.0,
                "available_ram_gb": 4.0, 
                "ram_usage_percent": 60,
                "cpu_usage_percent": 50,
                "is_high_performance": False,
                "is_under_stress": False
            }
    
    def analyze_task_requirements(self, query: str) -> Dict:
        """Analyze what the task actually needs (not wants, but NEEDS)"""
        query_lower = query.lower()
        words = query_lower.split()
        word_count = len(words)
        
        # Efficiency-first analysis
        analysis = {
            "word_count": word_count,
            "estimated_complexity": 0.0,
            "task_type": "simple_question",
            "min_tier_needed": "local",
            "min_model_needed": "ultra_fast",
            "reasoning": []
        }
        
        # Ultra-simple detection
        ultra_simple_phrases = ["hi", "hello", "thanks", "bye", "status", "help"]
        if any(phrase in query_lower for phrase in ultra_simple_phrases) and word_count <= 3:
            analysis.update({
                "estimated_complexity": 0.05,
                "task_type": "greeting",
                "min_model_needed": "ultra_fast",
                "reasoning": ["Ultra-simple greeting or command"]
            })
            return analysis
            
        # Coding detection
        coding_keywords = ["code", "function", "class", "debug", "error", "python", "javascript", "api"]
        enterprise_coding_keywords = ["architecture", "microservices", "enterprise", "scalable", "distributed", "deployment"]
        
        coding_score = sum(1 for kw in coding_keywords if kw in query_lower)
        enterprise_score = sum(1 for kw in enterprise_coding_keywords if kw in query_lower)
        
        if coding_score >= 2:
            if enterprise_score >= 1 or word_count >= 25:
                # Complex enterprise coding - use cloud tier
                analysis["task_type"] = "enterprise_coding"
                analysis["min_tier_needed"] = "cloud"
                analysis["min_model_needed"] = "enterprise_coding"
                analysis["reasoning"].append(f"Enterprise coding task ({coding_score} coding + {enterprise_score} enterprise keywords)")
            else:
                # Regular coding - your excellent local IDHHC is perfect
                analysis["task_type"] = "coding_help"
                analysis["min_model_needed"] = "coding"
                analysis["reasoning"].append(f"Standard coding task - IDHHC (qwen2.5-coder:32b) is excellent for this")
            
        # Architecture/complex design detection  
        complex_keywords = ["architecture", "design", "system", "microservices", "distributed", "scalable"]
        complex_score = sum(1 for kw in complex_keywords if kw in query_lower)
        
        if complex_score >= 2 or word_count >= 30:
            analysis["task_type"] = "architecture"
            analysis["min_tier_needed"] = "cloud"
            analysis["min_model_needed"] = "advanced_reasoning"
            analysis["reasoning"].append(f"Complex architecture task ({complex_score} complex keywords)")
            
        # Multimodal detection
        multimodal_keywords = ["image", "visual", "multimodal", "picture", "diagram"]
        if any(kw in query_lower for kw in multimodal_keywords):
            analysis["task_type"] = "multimodal"
            analysis["min_tier_needed"] = "cloud"
            analysis["min_model_needed"] = "cosmic_coding"
            analysis["reasoning"].append("Multimodal capabilities required")
            
        # Calculate final complexity
        base_complexity = min(0.8, word_count / 50.0)  # Max 0.8 from word count
        keyword_boost = (coding_score * 0.1) + (complex_score * 0.2)
        analysis["estimated_complexity"] = min(1.0, base_complexity + keyword_boost)
        
        return analysis
        
    def select_optimal_model(self, task_analysis: Dict, system_caps: Dict) -> Tuple[str, str, str]:
        """Select the most EFFICIENT model that can handle the task"""
        
        min_tier = task_analysis["min_tier_needed"]
        min_model = task_analysis["min_model_needed"]
        
        # Check if system can handle the minimum requirements
        if min_tier == "cloud":
            if not system_caps["is_high_performance"]:
                # Fallback to best local option
                print("⚠️  Task wants cloud tier, but system performance limited. Using best local option.")
                selected_tier = "local"
                selected_model = "coding"  # Best we can do locally
                reasoning = "Performance-limited fallback"
            else:
                selected_tier = "cloud"
                selected_model = min_model
                reasoning = "Cloud tier available and needed"
        else:
            # Local tier requested
            selected_tier = "local"
            
            # Check RAM availability for requested model
            required_ram = self.tiers["local"]["ram_requirements"].get(min_model, 4)
            available_ram = system_caps["available_ram_gb"]
            
            if required_ram <= available_ram and not system_caps["is_under_stress"]:
                selected_model = min_model
                reasoning = "Sufficient resources for requested model"
            else:
                # Downgrade to something that fits
                if available_ram >= 4:
                    selected_model = "capable"
                elif available_ram >= 3:
                    selected_model = "balanced" 
                else:
                    selected_model = "ultra_fast"
                reasoning = f"Resource-constrained downgrade (RAM: {available_ram}GB)"
                
        return selected_tier, selected_model, reasoning
        
    def display_efficiency_banner(self):
        """Display efficiency-focused banner"""
        system_caps = self.get_system_capabilities()
        
        banner = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ⚡ EFFICIENCY-FIRST DUAL-TIER HUB ⚡                      ║
║                                                                              ║
║  Philosophy: START LOW-FI → RAMP UP ONLY WHEN GENUINELY NEEDED              ║
║                                                                              ║
║  System Status: RAM: {system_caps['available_ram_gb']:.1f}GB/{system_caps['total_ram_gb']:.1f}GB │ CPU: {system_caps['cpu_usage_percent']:.0f}% │ Performance: {'HIGH' if system_caps['is_high_performance'] else 'STANDARD':8} ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                         🏠 LOCAL EFFICIENCY TIER                            ║
║  ⚡ TinyDolphin (636MB)   │ Fast: <1s    │ Simple queries, greetings        ║
║  🐬 Dolphin-Phi (1.6GB)  │ Quick: <3s   │ General questions, basic tasks   ║
║  🧠 Phi3 (2.2GB)         │ Smart: <5s   │ Reasoning, analysis, debugging   ║
║  💻 IDHHC (19GB)         │ Power: <15s  │ Coding, complex problem solving  ║
║                                                                              ║
║                         ☁️ DJINN CLOUD TIER (Mystical Powers)               ║
║  🌟 Cosmic Coder (65GB)  │ MoE: <30s    │ Multimodal sorcery, massive context ║
║  🧠 Deep Thinker (32GB)  │ Think: <20s  │ Ancient wisdom, philosophy       ║
║  ⚡ Logic Master (11GB)  │ Logic: <10s  │ Sovereign reasoning, analysis    ║
║  💾 Enterprise Arch (22GB)│ Code: <15s   │ Corporate mysticism (specialized) ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Smart Ramping: /status /performance /history /efficiency                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
        
        # Show current efficiency status
        stress_indicator = "🔴 UNDER STRESS" if system_caps["is_under_stress"] else "🟢 HEALTHY"
        print(f"\n⚡ Current Status: {stress_indicator} | Efficiency Mode: ACTIVE")
        print(f"🎯 Strategy: Start with {self.tiers['local']['models']['ultra_fast']} and ramp up as needed")
        print()
        
    async def execute_with_monitoring(self, tier: str, model: str, query: str) -> Tuple[str, Dict]:
        """Execute query while monitoring performance"""
        start_time = time.time()
        start_memory = psutil.virtual_memory().percent
        
        model_name = self.tiers[tier]["models"][model]
        
        try:
            print(f"⚡ Executing: {model} ({model_name})")
            print(f"🎯 Efficiency Check: RAM {start_memory:.0f}% | Expected: <{self.tiers[tier]['ram_requirements'].get(model, 4)}GB")
            
            # Execute ollama query
            result = subprocess.run(
                ['ollama', 'run', model_name, query],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            # Monitor performance
            end_time = time.time()
            end_memory = psutil.virtual_memory().percent
            response_time = end_time - start_time
            memory_impact = end_memory - start_memory
            
            performance_metrics = {
                "response_time": response_time,
                "memory_impact": memory_impact,
                "start_memory": start_memory,
                "end_memory": end_memory,
                "success": result.returncode == 0,
                "efficiency_score": self.calculate_efficiency_score(response_time, memory_impact)
            }
            
            if result.returncode == 0:
                response = result.stdout.strip()
                if response:
                    efficiency_indicator = self.get_efficiency_indicator(performance_metrics)
                    return f"✨ Response from {model}:\n\n{response}\n\n{efficiency_indicator}", performance_metrics
                else:
                    return f"❌ No response from {model}", performance_metrics
            else:
                error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                return f"❌ Error from {model}: {error_msg}", performance_metrics
                
        except Exception as e:
            performance_metrics = {
                "response_time": time.time() - start_time,
                "memory_impact": 0,
                "start_memory": start_memory,
                "end_memory": start_memory,
                "success": False,
                "efficiency_score": 0.0
            }
            return f"❌ Exception: {str(e)}", performance_metrics
            
    def calculate_efficiency_score(self, response_time: float, memory_impact: float) -> float:
        """Calculate efficiency score (higher is better)"""
        # Penalize slow responses and high memory usage
        time_score = max(0, 1.0 - (response_time / 30.0))  # 30s = 0 score
        memory_score = max(0, 1.0 - (memory_impact / 20.0))  # 20% memory = 0 score
        
        return (time_score + memory_score) / 2.0
        
    def get_efficiency_indicator(self, metrics: Dict) -> str:
        """Get visual efficiency indicator"""
        score = metrics["efficiency_score"]
        time = metrics["response_time"]
        memory = metrics["memory_impact"]
        
        if score >= 0.8:
            return f"⚡ HIGH EFFICIENCY | Time: {time:.1f}s | RAM: +{memory:.1f}%"
        elif score >= 0.6:
            return f"🟡 GOOD EFFICIENCY | Time: {time:.1f}s | RAM: +{memory:.1f}%"
        else:
            return f"🔴 LOW EFFICIENCY | Time: {time:.1f}s | RAM: +{memory:.1f}% | Consider ramping down"
            
    async def smart_query_routing(self, query: str) -> str:
        """Efficiency-first smart routing"""
        
        # Analyze what's actually needed
        task_analysis = self.analyze_task_requirements(query)
        system_caps = self.get_system_capabilities()
        
        print(f"🔍 Task Analysis:")
        print(f"  Complexity: {task_analysis['estimated_complexity']:.2f}")
        print(f"  Type: {task_analysis['task_type']}")
        print(f"  Reasoning: {', '.join(task_analysis['reasoning'])}")
        
        # Select optimal model
        tier, model, reasoning = self.select_optimal_model(task_analysis, system_caps)
        
        print(f"⚡ Efficiency Decision:")
        print(f"  Selected: {tier.upper()} tier → {model}")
        print(f"  Reasoning: {reasoning}")
        print()
        
        # Execute with monitoring
        response, metrics = await self.execute_with_monitoring(tier, model, query)
        
        # Learn from performance
        self.performance_history.append({
            "query": query[:50] + "..." if len(query) > 50 else query,
            "task_type": task_analysis["task_type"],
            "complexity": task_analysis["estimated_complexity"],
            "tier": tier,
            "model": model,
            "metrics": metrics,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 100 entries
        if len(self.performance_history) > 100:
            self.performance_history = self.performance_history[-100:]
            
        return response
        
    def show_performance_history(self):
        """Show recent performance history"""
        print("\n" + "📊 EFFICIENCY PERFORMANCE HISTORY".center(80, "="))
        
        if not self.performance_history:
            print("No performance history yet.")
            return
            
        recent = self.performance_history[-10:]  # Last 10
        
        for entry in recent:
            metrics = entry["metrics"]
            efficiency = metrics.get("efficiency_score", 0)
            time_taken = metrics.get("response_time", 0)
            
            efficiency_icon = "⚡" if efficiency >= 0.8 else "🟡" if efficiency >= 0.6 else "🔴"
            
            print(f"{efficiency_icon} {entry['model']:15} | {time_taken:4.1f}s | {efficiency:4.2f} | {entry['query']}")
            
        # Show efficiency statistics
        avg_efficiency = sum(e["metrics"].get("efficiency_score", 0) for e in recent) / len(recent)
        avg_time = sum(e["metrics"].get("response_time", 0) for e in recent) / len(recent)
        
        print(f"\n📈 Recent Averages: Efficiency: {avg_efficiency:.2f} | Time: {avg_time:.1f}s")
        print("=" * 80)
        
    async def interactive_mode(self):
        """Run efficiency-first interactive mode"""
        self.display_efficiency_banner()
        
        print("⚡ Efficiency-First Commands:")
        print("  /status      - Show system status")
        print("  /performance - Show performance history") 
        print("  /efficiency  - Show efficiency analysis")
        print("  /quit        - Exit")
        print()
        
        while True:
            try:
                user_input = input("⚡ [EFFICIENCY-FIRST] Enter query: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() == "/quit":
                    print("⚡ Efficiency-First Hub signing off! Maximum performance achieved!")
                    break
                elif user_input.lower() == "/status":
                    caps = self.get_system_capabilities()
                    print(f"\n🖥️  System Status:")
                    print(f"  RAM: {caps['available_ram_gb']:.1f}GB / {caps['total_ram_gb']:.1f}GB ({caps['ram_usage_percent']:.0f}%)")
                    print(f"  CPU: {caps['cpu_usage_percent']:.0f}%")
                    print(f"  Performance Level: {'HIGH' if caps['is_high_performance'] else 'STANDARD'}")
                    print(f"  Status: {'🔴 UNDER STRESS' if caps['is_under_stress'] else '🟢 HEALTHY'}\n")
                    continue
                elif user_input.lower() == "/performance":
                    self.show_performance_history()
                    continue
                elif user_input.lower() == "/efficiency":
                    if self.performance_history:
                        recent_efficiency = [e["metrics"].get("efficiency_score", 0) for e in self.performance_history[-20:]]
                        avg_eff = sum(recent_efficiency) / len(recent_efficiency)
                        print(f"\n⚡ Efficiency Analysis:")
                        print(f"  Average Efficiency: {avg_eff:.2f} (Recent 20 queries)")
                        print(f"  Status: {'EXCELLENT' if avg_eff >= 0.8 else 'GOOD' if avg_eff >= 0.6 else 'NEEDS OPTIMIZATION'}")
                        print(f"  Recommendation: {'Keep current strategy' if avg_eff >= 0.7 else 'Consider using lighter models'}\n")
                    else:
                        print("\n⚡ No efficiency data yet. Run some queries first!\n")
                    continue
                    
                # Process query with efficiency-first routing
                response = await self.smart_query_routing(user_input)
                print(response)
                print()
                
            except KeyboardInterrupt:
                print("\n⚡ Efficiency-First Hub signing off! Maximum performance achieved!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

async def main():
    """Main entry point for efficiency-first hub"""
    print("⚡ Initializing Efficiency-First Dual-Tier Hub...")
    
    hub = EfficiencyFirstHub()
    await hub.interactive_mode()

if __name__ == "__main__":
    asyncio.run(main()) 