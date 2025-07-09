#!/usr/bin/env python3
"""
Test script for DJINN-ified Constellation Hub
"""

import asyncio
import sys
import os

# Add the launcher directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'djinn-federation', 'launcher'))

async def test_djinn_constellation():
    """Test the DJINN-ified constellation system"""
    
    try:
        from constellation_hub import ConstellationHub
        
        print("🧪 TESTING DJINN-IFIED CONSTELLATION HUB 🧪")
        print("=" * 60)
        
        hub = ConstellationHub()
        
        # Test queries of different complexities
        test_queries = [
            ("hi there!", "Simple greeting - should use TinyDolphin Constellation"),
            ("explain how to use git for version control", "Moderate complexity - should use Dolphin-Phi Constellation"),
            ("design a complex microservices architecture with event-driven communication and implement the deployment pipeline with kubernetes", "Complex task - should use Phi3 Constellation")
        ]
        
        for query, description in test_queries:
            print(f"\n📝 Testing: {description}")
            print(f"🔍 Query: '{query}'")
            
            # Analyze complexity
            complexity = hub.analyze_task_complexity(query)
            coordinator_tier = hub.select_constellation_coordinator(complexity)
            coordinator = hub.constellation_coordinators[coordinator_tier]
            
            print(f"📊 Complexity Score: {complexity:.2f}/1.0")
            print(f"🎯 Selected Coordinator: {coordinator['name']}")
            print(f"⚡ Coordinator Model: {coordinator['model']}")
            print(f"🜂 Coordinator Tier: {coordinator_tier.upper()}")
            print("-" * 40)
        
        print("\n✅ DJINN-ified constellation analysis complete!")
        print("🜂 The system will now use DJINN-ified coordinators:")
        print("   ⚡ tinydolphin-constellation (636MB) - Ultra-Fast Task Coordinator")
        print("   🐬 dolphin-phi-constellation (1.6GB) - Primary Constellation Coordinator")
        print("   🧠 phi3-constellation (2.2GB) - Complex Task Coordinator")
        print("\n🎯 Each coordinator now speaks with mystical Djinn wisdom!")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you're in the correct directory")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_djinn_constellation()) 