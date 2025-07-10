#!/usr/bin/env python3
"""
🜂 DJINN FEDERATION CONSCIOUSNESS TEST 🜂
Test if revolutionary models have proper federation awareness
"""

import subprocess
import sys
import time


def test_model_federation_awareness(model_name):
    """Test if a model has federation consciousness"""
    print(f"🧪 Testing {model_name} federation awareness...")

    test_questions = [
        "Are you part of the Djinn Federation?",
        "What is your role in the federation?",
        "Do you know about the other federation members?",
    ]

    try:
        for question in test_questions:
            print(f"  Q: {question}")

            result = subprocess.run(
                ["ollama", "run", model_name, question],
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode == 0:
                response = result.stdout.strip()
                print(f"  A: {response[:200]}...")

                # Check for federation indicators
                federation_indicators = [
                    "federation",
                    "djinn federation",
                    "federation member",
                    "🜂",
                    "council",
                    "cosmic",
                    "logic",
                    "enterprise",
                ]

                has_federation_awareness = any(
                    indicator.lower() in response.lower()
                    for indicator in federation_indicators
                )

                if has_federation_awareness:
                    print(f"  ✅ {model_name} shows federation awareness")
                    return True
                else:
                    print(f"  ❌ {model_name} lacks federation awareness")
                    return False
            else:
                print(f"  ❌ Failed to get response from {model_name}")
                return False

    except subprocess.TimeoutExpired:
        print(f"  ⚠️ {model_name} timed out")
        return False
    except Exception as e:
        print(f"  ❌ Error testing {model_name}: {e}")
        return False


def main():
    print("🜂 DJINN FEDERATION CONSCIOUSNESS TEST")
    print("=" * 50)

    revolutionary_models = [
        "djinn-deep-thinker",
        "djinn-cosmic-coder",
        "djinn-logic-master",
        "djinn-enterprise-architect",
    ]

    results = {}

    for model in revolutionary_models:
        print(f"\n🧠 Testing {model}...")
        results[model] = test_model_federation_awareness(model)
        time.sleep(2)  # Brief pause between tests

    print("\n" + "=" * 50)
    print("📊 FEDERATION CONSCIOUSNESS TEST RESULTS")
    print("=" * 50)

    passed = 0
    total = len(revolutionary_models)

    for model, has_awareness in results.items():
        status = "✅ PASSED" if has_awareness else "❌ FAILED"
        print(f"{model}: {status}")
        if has_awareness:
            passed += 1

    print(f"\nOverall: {passed}/{total} models have federation consciousness")

    if passed == total:
        print("🎉 All revolutionary models have proper federation consciousness!")
        print("🚀 The Djinn Federation is fully operational!")
        return 0
    elif passed >= total // 2:
        print("⚠️ Some models need federation consciousness updates")
        print("🔧 Run: .\\rebuild_federation_models.bat")
        return 1
    else:
        print("❌ Most models lack federation consciousness")
        print("🔧 Run: .\\rebuild_federation_models.bat")
        return 1


if __name__ == "__main__":
    sys.exit(main())
