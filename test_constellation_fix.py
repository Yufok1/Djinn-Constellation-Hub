#!/usr/bin/env python3
"""
Test script to verify Constellation Hub fixes
"""

import subprocess
import sys

def test_ollama_encoding():
    """Test that ollama commands work with proper encoding"""
    try:
        print("Testing ollama list command with UTF-8 encoding...")
        result = subprocess.run(
            ['ollama', 'list'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8', 
            errors='replace',
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ Ollama list command successful")
            print(f"Output length: {len(result.stdout)} characters")
            return True
        else:
            print(f"❌ Ollama list failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing ollama: {e}")
        return False

def test_constellation_import():
    """Test that constellation hub can be imported"""
    try:
        print("Testing constellation hub import...")
        from constellation_hub import ConstellationHub
        print("✅ Constellation hub import successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    print("="*50)
    print("CONSTELLATION HUB FIX TEST")
    print("="*50)
    
    # Test ollama encoding
    ollama_ok = test_ollama_encoding()
    
    # Test constellation import
    import_ok = test_constellation_import()
    
    print("\n" + "="*50)
    if ollama_ok and import_ok:
        print("✅ ALL TESTS PASSED - Constellation Hub should work!")
        print("You can now run: launch_constellation_complete.bat")
    else:
        print("❌ SOME TESTS FAILED - Check the errors above")
    print("="*50)

if __name__ == "__main__":
    main() 