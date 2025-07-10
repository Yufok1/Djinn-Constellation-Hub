#!/usr/bin/env python3
"""
Test script for Phase 2.1: Input Validation Layer
Verifies all validation functions work correctly
"""
import sys
import os
import json
from pathlib import Path

# Add validators to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'validators'))

try:
    from input_validator import (
        validate_federation_config, validate_user_preferences,
        validate_memory_payload, validate_model_response,
        validate_cli_args, validate_trust_registry,
        ConfigValidationError, MemoryValidationError, PayloadValidationError,
        ValidationError
    )
    print("✅ Input validation module imported successfully")
except ImportError as e:
    print(f"❌ Failed to import validation module: {e}")
    sys.exit(1)

def test_federation_config_validation():
    """Test federation configuration validation"""
    print("\n🧪 Testing Federation Config Validation...")
    
    # Valid config
    valid_config = {
        "port": 8080,
        "auth_required": False,
        "models": ["djinn-council", "idhhc-companion"],
        "logging": {
            "level": "INFO",
            "output": "both"
        },
        "memory": {
            "max_size_mb": 1000,
            "backup_interval": 3600
        }
    }
    
    try:
        result = validate_federation_config(valid_config)
        print("✅ Valid federation config passed validation")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"❌ Valid config failed: {e}")
        return False
    
    # Invalid config - wrong port type
    invalid_config = {
        "port": "8080",  # Should be int
        "auth_required": False,
        "models": ["djinn-council"]
    }
    
    try:
        validate_federation_config(invalid_config)
        print("❌ Invalid config should have failed")
        return False
    except ConfigValidationError:
        print("✅ Invalid config correctly rejected")
    
    return True

def test_user_preferences_validation():
    """Test user preferences validation"""
    print("\n🧪 Testing User Preferences Validation...")
    
    # Valid preferences
    valid_prefs = {
        "theme": "dark",
        "autosave": True,
        "session_timeout": 3600,
        "notifications": True,
        "performance_mode": "balanced"
    }
    
    try:
        result = validate_user_preferences(valid_prefs)
        print("✅ Valid user preferences passed validation")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"❌ Valid preferences failed: {e}")
        return False
    
    # Invalid preferences - invalid theme
    invalid_prefs = {
        "theme": "invalid_theme",  # Not in allowed values
        "autosave": True
    }
    
    try:
        validate_user_preferences(invalid_prefs)
        print("❌ Invalid preferences should have failed")
        return False
    except ValidationError:
        print("✅ Invalid preferences correctly rejected")
    
    return True

def test_memory_payload_validation():
    """Test memory payload validation"""
    print("\n🧪 Testing Memory Payload Validation...")
    
    # Valid payload
    valid_payload = {
        "timestamp": "2025-07-09T20:00:00",
        "agent": "djinn-council",
        "user_input": "Hello, how are you?",
        "response": "I am well, thank you for asking.",
        "metadata": {"model": "djinn-council-enhanced-v2"},
        "trust_score": 0.9
    }
    
    try:
        result = validate_memory_payload(valid_payload)
        print("✅ Valid memory payload passed validation")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"❌ Valid payload failed: {e}")
        return False
    
    # Invalid payload - missing required field
    invalid_payload = {
        "timestamp": "2025-07-09T20:00:00",
        "agent": "djinn-council"
        # Missing user_input and response
    }
    
    try:
        validate_memory_payload(invalid_payload)
        print("❌ Invalid payload should have failed")
        return False
    except MemoryValidationError:
        print("✅ Invalid payload correctly rejected")
    
    return True

def test_cli_args_validation():
    """Test CLI arguments validation"""
    print("\n🧪 Testing CLI Arguments Validation...")
    
    # Valid args
    valid_args = ["status", "--verbose", "help"]
    
    try:
        result = validate_cli_args(valid_args)
        print("✅ Valid CLI args passed validation")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"❌ Valid args failed: {e}")
        return False
    
    # Invalid args - dangerous characters
    invalid_args = ["status; rm -rf /", "help | cat /etc/passwd"]
    
    try:
        result = validate_cli_args(invalid_args)
        print("✅ Dangerous CLI args sanitized")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"❌ CLI args sanitization failed: {e}")
        return False
    
    return True

def test_model_response_validation():
    """Test model response validation"""
    print("\n🧪 Testing Model Response Validation...")
    
    # Valid response
    valid_response = {
        "timestamp": "2025-07-09T20:00:00",
        "agent": "djinn-council",
        "user_input": "What is the meaning of life?",
        "response": "The meaning of life is to seek understanding and growth.",
        "metadata": {"model": "djinn-council-enhanced-v2"}
    }
    
    try:
        result = validate_model_response(valid_response)
        print("✅ Valid model response passed validation")
        print(f"   Trust score: {result.get('trust_score', 'N/A')}")
    except Exception as e:
        print(f"❌ Valid response failed: {e}")
        return False
    
    # Invalid response - suspicious content
    suspicious_response = {
        "timestamp": "2025-07-09T20:00:00",
        "agent": "djinn-council",
        "user_input": "What is the meaning of life?",
        "response": "<script>alert('xss')</script>The meaning of life is to seek understanding.",
        "metadata": {"model": "djinn-council-enhanced-v2"}
    }
    
    try:
        result = validate_model_response(suspicious_response)
        print("✅ Suspicious response handled with lower trust score")
        print(f"   Trust score: {result.get('trust_score', 'N/A')}")
    except Exception as e:
        print(f"❌ Suspicious response validation failed: {e}")
        return False
    
    return True

def test_trust_registry_validation():
    """Test trust registry validation"""
    print("\n🧪 Testing Trust Registry Validation...")
    
    # Valid registry entry
    valid_entry = {
        "agent_id": "djinn-council-v2",
        "trust_score": 0.95,
        "last_verified": "2025-07-09T20:00:00",
        "capabilities": ["reasoning", "ethics", "alignment"],
        "federation_member": True
    }
    
    try:
        result = validate_trust_registry(valid_entry)
        print("✅ Valid trust registry entry passed validation")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"❌ Valid entry failed: {e}")
        return False
    
    # Invalid entry - invalid agent_id pattern
    invalid_entry = {
        "agent_id": "djinn council v2",  # Contains spaces, should be alphanumeric + underscore/dash
        "trust_score": 0.95,
        "last_verified": "2025-07-09T20:00:00",
        "capabilities": ["reasoning"]
    }
    
    try:
        validate_trust_registry(invalid_entry)
        print("❌ Invalid entry should have failed")
        return False
    except ValidationError:
        print("✅ Invalid entry correctly rejected")
    
    return True

def main():
    """Run all validation tests"""
    print("🜂 PHASE 2.1: INPUT VALIDATION LAYER TEST SUITE 🜂")
    print("=" * 60)
    
    tests = [
        test_federation_config_validation,
        test_user_preferences_validation,
        test_memory_payload_validation,
        test_cli_args_validation,
        test_model_response_validation,
        test_trust_registry_validation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ ALL VALIDATION TESTS PASSED!")
        print("🜂 Input Validation Layer is operational")
        return 0
    else:
        print("❌ Some validation tests failed")
        print("🔧 Check the validation implementation")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 