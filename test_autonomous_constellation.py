#!/usr/bin/env python3
"""
Test Autonomous Constellation System
Tests the constellation-to-IDHHC execution workflow
"""

import json
import subprocess
import time
from pathlib import Path


def test_constellation_models():
    """Test if constellation models are available"""
    print("🧪 TESTING CONSTELLATION MODELS")
    print("=" * 50)

    models = [
        "Yufok1/djinn-federation:constellation-lite",
        "Yufok1/djinn-federation:constellation-core",
        "Yufok1/djinn-federation:constellation-max",
        "Yufok1/djinn-federation:idhhc",
    ]

    available_models = []

    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        if result.returncode == 0:
            for model in models:
                if model in result.stdout:
                    print(f"✅ {model} - Available")
                    available_models.append(model)
                else:
                    print(f"❌ {model} - Not found")
        else:
            print("❌ Cannot access Ollama")
            return False
    except Exception as e:
        print(f"❌ Error checking models: {e}")
        return False

    print(f"\n📊 Available models: {len(available_models)}/{len(models)}")
    return len(available_models) >= 3  # Need at least constellation + IDHHC


def test_constellation_hub_import():
    """Test if constellation hub can be imported"""
    print("\n🧪 TESTING CONSTELLATION HUB IMPORT")
    print("=" * 50)

    try:
        from constellation_hub import ConstellationHub

        print("✅ ConstellationHub class imported successfully")

        # Test initialization
        hub = ConstellationHub()
        print("✅ ConstellationHub initialized successfully")

        # Test complexity analysis
        test_prompt = "Hello, how are you?"
        complexity = hub.analyze_complexity(test_prompt)
        print(f"✅ Complexity analysis working: '{test_prompt}' -> {complexity}")

        return True
    except Exception as e:
        print(f"❌ Error importing/testing ConstellationHub: {e}")
        return False


def test_memory_system():
    """Test if memory system is working"""
    print("\n🧪 TESTING MEMORY SYSTEM")
    print("=" * 50)

    try:
        memory_bank = Path("memory_bank")
        if memory_bank.exists():
            print("✅ Memory bank directory exists")
        else:
            print("❌ Memory bank directory missing")
            return False

        # Check for federation memory
        federation_db = memory_bank / "federation_memory.db"
        if federation_db.exists():
            print("✅ Federation memory database exists")
        else:
            print("⚠️ Federation memory database not found (will be created)")

        return True
    except Exception as e:
        print(f"❌ Error testing memory system: {e}")
        return False


def test_directive_execution():
    """Test directive execution system"""
    print("\n🧪 TESTING DIRECTIVE EXECUTION SYSTEM")
    print("=" * 50)

    try:
        from constellation_hub import ConstellationHub

        hub = ConstellationHub()

        # Test directive generation
        test_prompt = "test system status"
        test_response = "System operational and ready for testing"

        directive = hub.generate_coder_directive(test_prompt, test_response)
        print("✅ Directive generation working")
        print(f"   Task: {directive['task']}")
        print(f"   Agent: {directive['agent']}")
        print(f"   Priority: {directive['priority']}")

        return True
    except Exception as e:
        print(f"❌ Error testing directive execution: {e}")
        return False


def test_bridge_system():
    """Test VOID bridge system"""
    print("\n🧪 TESTING VOID BRIDGE SYSTEM")
    print("=" * 50)

    try:
        from void_constellation_bridge import VOIDConstellationBridge

        bridge = VOIDConstellationBridge()
        print("✅ VOID bridge imported successfully")

        # Test pending directives check
        pending = bridge.get_pending_directives()
        print(f"✅ Bridge operational - {len(pending)} pending directives")

        return True
    except Exception as e:
        print(f"❌ Error testing bridge system: {e}")
        return False


def run_full_test():
    """Run complete test suite"""
    print("🚀 AUTONOMOUS CONSTELLATION SYSTEM TEST")
    print("=" * 60)
    print("Testing the complete constellation-to-IDHHC workflow...")
    print()

    tests = [
        ("Constellation Models", test_constellation_models),
        ("Hub Import & Init", test_constellation_hub_import),
        ("Memory System", test_memory_system),
        ("Directive Execution", test_directive_execution),
        ("Bridge System", test_bridge_system),
    ]

    results = []

    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name}: Unexpected error - {e}")
            results.append((test_name, False))

    # Summary
    print("\n" + "=" * 60)
    print("🎯 TEST RESULTS SUMMARY")
    print("=" * 60)

    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1

    print(f"\n📊 Overall: {passed}/{len(results)} tests passed")

    if passed == len(results):
        print("🎉 ALL TESTS PASSED - Autonomous Constellation System is ready!")
        print("\n🚀 You can now use:")
        print("   • launch_constellation_complete.bat")
        print("   • Direct constellation commands with IDHHC execution")
        print("   • Full memory persistence and GitHub sync")
    else:
        print("⚠️ Some tests failed - check the errors above")
        print("💡 Try running install_djinn_federation.bat if models are missing")

    return passed == len(results)


if __name__ == "__main__":
    run_full_test()
