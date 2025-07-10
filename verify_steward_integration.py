#!/usr/bin/env python3
"""
Verification script for The Steward integration
Simple tests to verify the integration is working
"""

import os
import json
import sys

def test_trust_registry():
    """Test that trust registry exists and has steward entry"""
    print("🔍 Testing Trust Registry...")
    
    trust_file = "trust_registry.json"
    if os.path.exists(trust_file):
        with open(trust_file, 'r') as f:
            registry = json.load(f)
        
        if 'steward' in registry:
            steward = registry['steward']
            print(f"✅ Trust Registry: Steward found")
            print(f"   Trusted: {steward.get('trusted', False)}")
            print(f"   Trust Score: {steward.get('trust_score', 0)}/100")
            print(f"   Role: {steward.get('role', 'unknown')}")
            return True
        else:
            print("❌ Trust Registry: Steward entry missing")
            return False
    else:
        print("❌ Trust Registry: File not found")
        return False

def test_constellation_hub_integration():
    """Test that constellation hub has steward integration"""
    print("\n🔍 Testing Constellation Hub Integration...")
    
    hub_file = "djinn-federation/launcher/constellation_hub.py"
    if os.path.exists(hub_file):
        with open(hub_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for steward keywords
        if "'steward':" in content:
            print("✅ Constellation Hub: Steward agent defined")
        else:
            print("❌ Constellation Hub: Steward agent missing")
            return False
        
        # Check for maintenance keywords
        if "maintain" in content and "system" in content and "health" in content:
            print("✅ Constellation Hub: Maintenance keywords found")
        else:
            print("❌ Constellation Hub: Maintenance keywords missing")
            return False
        
        # Check for trust enforcement
        if "check_steward_trust" in content:
            print("✅ Constellation Hub: Trust enforcement found")
        else:
            print("❌ Constellation Hub: Trust enforcement missing")
            return False
        
        # Check for routing logic
        if "is_maintenance_task" in content:
            print("✅ Constellation Hub: Maintenance routing found")
        else:
            print("❌ Constellation Hub: Maintenance routing missing")
            return False
        
        return True
    else:
        print("❌ Constellation Hub: File not found")
        return False

def test_cli_integration():
    """Test that CLI has steward commands"""
    print("\n🔍 Testing CLI Integration...")
    
    cli_file = "djinn_cli.py"
    if os.path.exists(cli_file):
        with open(cli_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for steward commands
        if "--steward" in content:
            print("✅ CLI: Steward commands found")
        else:
            print("❌ CLI: Steward commands missing")
            return False
        
        # Check for trust registry commands
        if "--trust-score" in content:
            print("✅ CLI: Trust registry commands found")
        else:
            print("❌ CLI: Trust registry commands missing")
            return False
        
        return True
    else:
        print("❌ CLI: File not found")
        return False

def test_launch_scripts():
    """Test that launch scripts include steward"""
    print("\n🔍 Testing Launch Scripts...")
    
    # Check Windows launch script
    bat_file = "launch_djinn_constellation_hub.bat"
    if os.path.exists(bat_file):
        with open(bat_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "Launching The Steward" in content:
            print("✅ Windows Launch: Steward integration found")
        else:
            print("❌ Windows Launch: Steward integration missing")
            return False
    else:
        print("❌ Windows Launch: File not found")
        return False
    
    # Check Linux/Mac launch script
    sh_file = "launch_djinn_constellation_hub.sh"
    if os.path.exists(sh_file):
        with open(sh_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "Launching The Steward" in content:
            print("✅ Linux/Mac Launch: Steward integration found")
        else:
            print("❌ Linux/Mac Launch: Steward integration missing")
            return False
    else:
        print("❌ Linux/Mac Launch: File not found")
        return False
    
    return True

def test_documentation():
    """Test that documentation includes steward"""
    print("\n🔍 Testing Documentation...")
    
    readme_file = "README.md"
    if os.path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "The Steward" in content:
            print("✅ Documentation: Steward mentioned")
        else:
            print("❌ Documentation: Steward not mentioned")
            return False
        
        if "maintenance" in content.lower():
            print("✅ Documentation: Maintenance tasks mentioned")
        else:
            print("❌ Documentation: Maintenance tasks not mentioned")
            return False
        
        return True
    else:
        print("❌ Documentation: README not found")
        return False

def main():
    """Run all verification tests"""
    print("🛡️ THE STEWARD INTEGRATION VERIFICATION")
    print("=" * 50)
    
    tests = [
        test_trust_registry,
        test_constellation_hub_integration,
        test_cli_integration,
        test_launch_scripts,
        test_documentation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 VERIFICATION RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! The Steward is fully integrated.")
        return True
    else:
        print("⚠️ Some tests failed. Please check the integration.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 