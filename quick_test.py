#!/usr/bin/env python3
"""
🜂 DJINN CONSTELLATION HUB v2.0.0 - QUICK TEST 🜂
Fast validation of core system functionality
"""

import subprocess
import sys
import time
from pathlib import Path


def test_ollama_connection():
    """Test basic Ollama connectivity"""
    print("🔗 Testing Ollama connection...")
    try:
        result = subprocess.run(
            ["ollama", "list"], capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            print("✅ Ollama connection successful")
            return True
        else:
            print("❌ Ollama connection failed")
            return False
    except Exception as e:
        print(f"❌ Ollama test error: {e}")
        return False


def test_model_availability():
    """Test if core models are available"""
    print("🧠 Testing model availability...")
    try:
        result = subprocess.run(
            ["ollama", "list"], capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            models = result.stdout
            core_models = ["Yufok1/djinn-federation:companion", "tinydolphin:latest"]

            available = []
            missing = []
            for model in core_models:
                if model in models:
                    available.append(model)
                else:
                    missing.append(model)

            print(f"✅ Available: {len(available)}/{len(core_models)} core models")
            if missing:
                print(f"⚠️ Missing: {', '.join(missing)}")

            return len(available) > 0
        else:
            print("❌ Could not check models")
            return False
    except Exception as e:
        print(f"❌ Model test error: {e}")
        return False


def test_simple_query():
    """Test a simple query with tinydolphin"""
    print("💬 Testing simple query...")
    try:
        query = "Hello, this is a test query."
        result = subprocess.run(
            ["ollama", "run", "tinydolphin:latest", query],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode == 0 and result.stdout.strip():
            print("✅ Simple query successful")
            return True
        else:
            print("❌ Simple query failed")
            return False
    except subprocess.TimeoutExpired:
        print("⚠️ Query timed out (30s)")
        return False
    except Exception as e:
        print(f"❌ Query test error: {e}")
        return False


def test_constellation_hub_import():
    """Test if constellation hub can be imported"""
    print("🏗️ Testing constellation hub import...")
    try:
        # Add current directory to path
        sys.path.insert(0, str(Path.cwd()))

        # Try to import the main module
        import constellation_hub

        print("✅ Constellation hub import successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Import test error: {e}")
        return False


def main():
    print("🜂 DJINN CONSTELLATION HUB v2.0.0 - QUICK TEST")
    print("=" * 50)

    tests = [
        ("Ollama Connection", test_ollama_connection),
        ("Model Availability", test_model_availability),
        ("Simple Query", test_simple_query),
        ("Constellation Hub Import", test_constellation_hub_import),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n🧪 {test_name}:")
        if test_func():
            passed += 1
        time.sleep(1)  # Brief pause between tests

    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! System is ready for use.")
        print("🚀 You can now run: ./launch_djinn_constellation_hub.bat")
        return 0
    elif passed >= total // 2:
        print("⚠️ Some tests failed. System may work with limitations.")
        print("🔧 Check the issues above and try again.")
        return 1
    else:
        print("❌ Multiple tests failed. System needs attention.")
        print("🔧 Run: python system_health_check.py for detailed diagnostics")
        return 1


if __name__ == "__main__":
    sys.exit(main())
