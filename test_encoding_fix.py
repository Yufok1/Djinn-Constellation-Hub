#!/usr/bin/env python3
"""
Test Encoding Fix
Quick test to verify constellation communication works without Unicode errors
"""

import subprocess
import sys

def test_simple_constellation_call():
    """Test a simple constellation call to verify encoding works"""
    print("🧪 Testing simple constellation call with encoding fix...")
    
    try:
        # Simple test prompt
        test_prompt = "Hello, please respond with a simple greeting."
        
        # Test constellation-lite with proper encoding
        result = subprocess.run([
            'ollama', 'run', 'Yufok1/djinn-federation:constellation-lite', test_prompt
        ], capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace')
        
        if result.returncode == 0 and result.stdout:
            print("✅ Constellation communication successful!")
            print(f"Response: {result.stdout.strip()[:100]}...")
            return True
        else:
            print(f"❌ Constellation call failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing constellation: {e}")
        return False

def test_constellation_hub():
    """Test constellation hub with encoding fix"""
    print("\n🧪 Testing constellation hub with encoding fix...")
    
    try:
        from constellation_hub import ConstellationHub
        hub = ConstellationHub()
        
        # Test simple routing
        response = hub.route_to_constellation("Hello, test message", "lite")
        
        if response and not response.startswith("Error"):
            print("✅ Constellation hub communication successful!")
            print(f"Response: {response[:100]}...")
            return True
        else:
            print(f"❌ Hub communication failed: {response}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing hub: {e}")
        return False

if __name__ == "__main__":
    print("🔧 TESTING ENCODING FIXES")
    print("=" * 40)
    
    test1 = test_simple_constellation_call()
    test2 = test_constellation_hub()
    
    print("\n" + "=" * 40)
    if test1 and test2:
        print("🎉 All encoding tests passed!")
        print("✅ Constellation system ready for use")
    else:
        print("⚠️ Some encoding tests failed")
        print("💡 Check Ollama installation and model availability") 