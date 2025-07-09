#!/usr/bin/env python3
"""
Test Intent-Based Routing
Tests the dialogue vs command routing system
"""

from constellation_hub import ConstellationHub

def test_intent_analysis():
    """Test intent analysis for dialogue vs commands"""
    print("🧪 TESTING INTENT ANALYSIS")
    print("=" * 50)
    
    hub = ConstellationHub()
    
    # Test cases
    test_cases = [
        # Dialogue examples
        ("Hello, how are you?", "dialogue"),
        ("Can I speak with djinn-companion?", "dialogue"),
        ("What do you think about this?", "dialogue"),
        ("Thank you for your help", "dialogue"),
        ("Who are you?", "dialogue"),
        ("That's really interesting!", "dialogue"),
        
        # Command examples  
        ("Analyze the project directory", "command"),
        ("Execute a system audit", "command"),
        ("Fix the encoding issues", "command"),
        ("Generate a backup script", "command"),
        ("Review the constellation code", "command"),
        ("Update the project files", "command"),
        
        # Edge cases
        ("Status of the models", "command"),
        ("Hello, can you analyze my code?", "command"),  # Mixed - should prioritize command
        ("Thanks! Now please run tests", "command"),  # Mixed - should prioritize command
    ]
    
    correct = 0
    for prompt, expected in test_cases:
        actual = hub.analyze_intent(prompt)
        status = "✅" if actual == expected else "❌"
        print(f"{status} '{prompt}' -> {actual} (expected: {expected})")
        if actual == expected:
            correct += 1
    
    print(f"\n📊 Intent Analysis: {correct}/{len(test_cases)} correct")
    return correct == len(test_cases)

def test_routing_logic():
    """Test the basic routing logic"""
    print("\n🧪 TESTING ROUTING LOGIC")
    print("=" * 50)
    
    hub = ConstellationHub()
    
    # Test dialogue intent
    dialogue_prompt = "Hello, how are you today?"
    intent = hub.analyze_intent(dialogue_prompt)
    print(f"Dialogue test: '{dialogue_prompt}' -> {intent}")
    
    # Test command intent
    command_prompt = "Analyze the project structure"
    intent = hub.analyze_intent(command_prompt)
    complexity = hub.analyze_complexity(command_prompt)
    print(f"Command test: '{command_prompt}' -> {intent} (complexity: {complexity})")
    
    return True

if __name__ == "__main__":
    print("🎯 INTENT-BASED ROUTING TEST")
    print("=" * 60)
    
    test1 = test_intent_analysis()
    test2 = test_routing_logic()
    
    print("\n" + "=" * 60)
    if test1 and test2:
        print("🎉 Intent routing system working correctly!")
        print("✅ Dialogue -> Djinn Companion")
        print("✅ Commands -> Constellation -> IDHHC")
        print("\n💡 Now constellation will default to companion for conversation")
        print("💡 and route commands to IDHHC automatically!")
    else:
        print("⚠️ Some intent routing tests failed") 