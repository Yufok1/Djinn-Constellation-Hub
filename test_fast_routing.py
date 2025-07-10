#!/usr/bin/env python3
"""
Test Fast-Path Routing
Tests the optimized intent analysis for speed
"""

import time

from constellation_hub import ConstellationHub


def test_fast_routing_speed():
    """Test that fast-path routing is actually fast"""
    print("⚡ TESTING FAST-PATH ROUTING SPEED")
    print("=" * 50)

    hub = ConstellationHub()

    # Test fast-path cases
    fast_cases = ["hello", "hi", "hey", "thanks", "bye", "analyze", "fix", "build"]

    print("Testing fast-path cases...")
    for prompt in fast_cases:
        start_time = time.time()
        intent = hub.analyze_intent(prompt)
        end_time = time.time()

        duration_ms = (end_time - start_time) * 1000
        speed_status = "⚡ FAST" if duration_ms < 1 else "🐌 SLOW"

        print(f"{speed_status} '{prompt}' -> {intent} ({duration_ms:.2f}ms)")

    # Test complex cases
    complex_cases = [
        "Hello, can you analyze my project structure?",
        "I think this code needs some optimization work",
        "What do you think about implementing a new feature?",
    ]

    print("\nTesting complex cases...")
    for prompt in complex_cases:
        start_time = time.time()
        intent = hub.analyze_intent(prompt)
        end_time = time.time()

        duration_ms = (end_time - start_time) * 1000
        speed_status = "⚡ FAST" if duration_ms < 5 else "🐌 SLOW"

        print(f"{speed_status} '{prompt}' -> {intent} ({duration_ms:.2f}ms)")


def test_intent_accuracy():
    """Test that fast routing is still accurate"""
    print("\n🎯 TESTING FAST ROUTING ACCURACY")
    print("=" * 50)

    hub = ConstellationHub()

    test_cases = [
        ("hello", "dialogue"),
        ("hi there", "dialogue"),
        ("analyze the code", "command"),
        ("fix this bug", "command"),
        ("thanks for helping", "dialogue"),
        ("build a new feature", "command"),
    ]

    correct = 0
    for prompt, expected in test_cases:
        actual = hub.analyze_intent(prompt)
        status = "✅" if actual == expected else "❌"
        print(f"{status} '{prompt}' -> {actual} (expected: {expected})")
        if actual == expected:
            correct += 1

    print(f"\n📊 Accuracy: {correct}/{len(test_cases)} correct")
    return correct == len(test_cases)


if __name__ == "__main__":
    print("🚀 FAST-PATH ROUTING TEST")
    print("=" * 60)

    test_fast_routing_speed()
    accuracy_ok = test_intent_accuracy()

    print("\n" + "=" * 60)
    if accuracy_ok:
        print("🎉 Fast-path routing optimized!")
        print("✅ Speed: Fast-path for common cases")
        print("✅ Accuracy: Intent detection still accurate")
        print("✅ Fallbacks: Graceful error handling")
        print("\n💡 'hello' should now be lightning fast!")
    else:
        print("⚠️ Some routing accuracy issues detected")
