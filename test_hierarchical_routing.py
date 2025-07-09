#!/usr/bin/env python3
"""
Test script for Hierarchical Constellation Hub routing
"""

import asyncio
import sys
import os

# Add the launcher directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'djinn-federation', 'launcher'))

from constellation_hub import ConstellationHub

async def test_hierarchical_routing():
    """Test the hierarchical routing system with different query complexities"""
    
    hub = ConstellationHub()
    
    # Test queries of different complexities
    test_queries = [
        ("hi", "Simple greeting - should use TinyDolphin"),
        ("explain how to use git", "Moderate complexity - should use Dolphin-Phi"),
        ("design a complex system architecture with microservices and implement the deployment pipeline", "Complex task - should use Phi3")
    ]
    
    print("🧪 TESTING HIERARCHICAL CONSTELLATION ROUTING 🧪")
    print("=" * 60)
    
    for query, description in test_queries:
        print(f"\n📝 Testing: {description}")
        print(f"🔍 Query: '{query}'")
        
        # Analyze complexity
        complexity = hub.analyze_task_complexity(query)
        coordinator_tier = hub.select_constellation_coordinator(complexity)
        coordinator = hub.constellation_coordinators[coordinator_tier]
        
        print(f"📊 Complexity Score: {complexity:.2f}/1.0")
        print(f"🎯 Selected Coordinator: {coordinator['name']}")
        print(f"⚡ Coordinator Tier: {coordinator_tier.upper()}")
        print("-" * 40)
    
    print("\n✅ Hierarchical routing analysis complete!")
    print("🜂 The system will automatically route queries based on complexity:")
    print("   ⚡ Simple queries (0.0-0.2) → TinyDolphin (636MB)")
    print("   🐬 Moderate queries (0.2-0.6) → Dolphin-Phi (1.6GB)")
    print("   🧠 Complex queries (0.6-1.0) → Phi3 (2.2GB)")

if __name__ == "__main__":
    asyncio.run(test_hierarchical_routing()) 