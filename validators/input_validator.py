#!/usr/bin/env python3
"""
Input Validation Layer for Djinn Constellation Hub
Phase 2.1: Comprehensive input validation and sanitization
"""
import json
import logging
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Union, Optional
from pathlib import Path

# === Validation Error Classes ===
class ValidationError(Exception):
    """Base validation error with context"""
    def __init__(self, message: str, field: str = None, value: Any = None, schema: str = None):
        self.message = message
        self.field = field
        self.value = value
        self.schema = schema
        super().__init__(self.message)

class ConfigValidationError(ValidationError):
    """Configuration validation error"""
    pass

class MemoryValidationError(ValidationError):
    """Memory data validation error"""
    pass

class PayloadValidationError(ValidationError):
    """Model response payload validation error"""
    pass

# === Logging Setup ===
VALIDATION_LOG_DIR = Path("logs")
VALIDATION_LOG_DIR.mkdir(exist_ok=True)
VALIDATION_LOG_FILE = VALIDATION_LOG_DIR / "input_validation.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(VALIDATION_LOG_FILE),
        logging.StreamHandler()
    ]
)
validation_logger = logging.getLogger('InputValidator')

# === Schema Definitions ===
FEDERATION_CONFIG_SCHEMA = {
    "port": {"type": int, "min": 1024, "max": 65535, "default": 8080},
    "auth_required": {"type": bool, "default": False},
    "models": {"type": list, "required": True},
    "logging": {
        "type": dict,
        "schema": {
            "level": {"type": str, "allowed": ["DEBUG", "INFO", "WARNING", "ERROR"], "default": "INFO"},
            "output": {"type": str, "allowed": ["console", "file", "both"], "default": "both"}
        }
    },
    "memory": {
        "type": dict,
        "schema": {
            "max_size_mb": {"type": int, "min": 1, "max": 10000, "default": 1000},
            "backup_interval": {"type": int, "min": 60, "max": 86400, "default": 3600}
        }
    }
}

USER_PREFERENCES_SCHEMA = {
    "theme": {"type": str, "allowed": ["dark", "light", "auto"], "default": "auto"},
    "autosave": {"type": bool, "default": True},
    "session_timeout": {"type": int, "min": 300, "max": 86400, "default": 3600},
    "last_session": {"type": dict, "required": False},
    "notifications": {"type": bool, "default": True},
    "performance_mode": {"type": str, "allowed": ["balanced", "speed", "quality"], "default": "balanced"}
}

MEMORY_PAYLOAD_SCHEMA = {
    "timestamp": {"type": str, "required": True},
    "agent": {"type": str, "required": True},
    "user_input": {"type": str, "required": True, "max_length": 10000},
    "response": {"type": str, "required": True, "max_length": 50000},
    "metadata": {"type": dict, "required": False},
    "trust_score": {"type": float, "min": 0.0, "max": 1.0, "required": False, "default": 0.8}
}

TRUST_REGISTRY_SCHEMA = {
    "agent_id": {"type": str, "required": True, "pattern": r"^[a-zA-Z0-9_-]+$"},
    "trust_score": {"type": float, "min": 0.0, "max": 1.0, "required": True},
    "last_verified": {"type": str, "required": True},
    "capabilities": {"type": list, "required": True},
    "federation_member": {"type": bool, "default": True}
}

# === Validation Functions ===
def validate_type(value: Any, expected_type: type, field_name: str = None) -> bool:
    """Validate that a value matches the expected type"""
    if not isinstance(value, expected_type):
        raise ValidationError(
            f"Expected {expected_type.__name__}, got {type(value).__name__}",
            field=field_name,
            value=value
        )
    return True

def validate_string_constraints(value: str, constraints: Dict, field_name: str = None) -> bool:
    """Validate string constraints (length, pattern, allowed values)"""
    if "max_length" in constraints and len(value) > constraints["max_length"]:
        raise ValidationError(
            f"String too long (max {constraints['max_length']} chars)",
            field=field_name,
            value=value
        )
    
    if "pattern" in constraints and not re.match(constraints["pattern"], value):
        raise ValidationError(
            f"String doesn't match pattern {constraints['pattern']}",
            field=field_name,
            value=value
        )
    
    if "allowed" in constraints and value not in constraints["allowed"]:
        raise ValidationError(
            f"Value '{value}' not in allowed values: {constraints['allowed']}",
            field=field_name,
            value=value
        )
    
    return True

def validate_numeric_constraints(value: Union[int, float], constraints: Dict, field_name: str = None) -> bool:
    """Validate numeric constraints (min, max)"""
    if "min" in constraints and value < constraints["min"]:
        raise ValidationError(
            f"Value {value} below minimum {constraints['min']}",
            field=field_name,
            value=value
        )
    
    if "max" in constraints and value > constraints["max"]:
        raise ValidationError(
            f"Value {value} above maximum {constraints['max']}",
            field=field_name,
            value=value
        )
    
    return True

def validate_input(data: Dict, schema: Dict, context: str = "unknown") -> Dict:
    """
    Validate input data against a schema with comprehensive error handling
    
    Args:
        data: Input data to validate
        schema: Schema definition
        context: Context for error reporting
    
    Returns:
        Validated data with defaults applied
    """
    validation_logger.info(f"Validating {context} input")
    
    if not isinstance(data, dict):
        raise ValidationError(f"Input must be a dictionary, got {type(data).__name__}", schema=context)
    
    validated_data = {}
    
    for field_name, field_schema in schema.items():
        try:
            # Check if field is required
            required = field_schema.get("required", True)
            
            if field_name not in data:
                if required:
                    raise ValidationError(f"Required field '{field_name}' missing", field=field_name, schema=context)
                elif "default" in field_schema:
                    validated_data[field_name] = field_schema["default"]
                    validation_logger.debug(f"Applied default for {field_name}: {field_schema['default']}")
                continue
            
            value = data[field_name]
            expected_type = field_schema["type"]
            
            # Type validation
            validate_type(value, expected_type, field_name)
            
            # String-specific validation
            if expected_type == str:
                validate_string_constraints(value, field_schema, field_name)
            
            # Numeric validation
            elif expected_type in (int, float):
                validate_numeric_constraints(value, field_schema, field_name)
            
            # List validation
            elif expected_type == list:
                if "schema" in field_schema:
                    for i, item in enumerate(value):
                        validate_input(item, field_schema["schema"], f"{context}.{field_name}[{i}]")
            
            # Dict validation
            elif expected_type == dict and "schema" in field_schema:
                validate_input(value, field_schema["schema"], f"{context}.{field_name}")
            
            # Boolean validation
            elif expected_type == bool:
                if not isinstance(value, bool):
                    raise ValidationError(f"Boolean field '{field_name}' must be true/false", field=field_name, value=value)
            
            validated_data[field_name] = value
            validation_logger.debug(f"Validated {field_name}: {value}")
            
        except ValidationError as e:
            validation_logger.error(f"Validation error in {context}.{field_name}: {e.message}")
            raise e
        except Exception as e:
            validation_logger.error(f"Unexpected error validating {context}.{field_name}: {e}")
            raise ValidationError(f"Validation failed: {e}", field=field_name, value=data.get(field_name))
    
    validation_logger.info(f"Successfully validated {context} input")
    return validated_data

def sanitize_string(value: str, max_length: int = 1000) -> str:
    """Sanitize string input to prevent injection attacks"""
    if not isinstance(value, str):
        raise ValidationError("Input must be a string")
    
    # Remove null bytes and control characters
    sanitized = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', value)
    
    # Truncate if too long
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
        validation_logger.warning(f"String truncated to {max_length} characters")
    
    return sanitized.strip()

def validate_federation_config(config_data: Dict) -> Dict:
    """Validate federation configuration with specific error handling"""
    try:
        return validate_input(config_data, FEDERATION_CONFIG_SCHEMA, "federation_config")
    except ValidationError as e:
        raise ConfigValidationError(f"Federation config validation failed: {e.message}", field=e.field, value=e.value)

def validate_user_preferences(pref_data: Dict) -> Dict:
    """Validate user preferences with specific error handling"""
    try:
        return validate_input(pref_data, USER_PREFERENCES_SCHEMA, "user_preferences")
    except ValidationError as e:
        raise ValidationError(f"User preferences validation failed: {e.message}", field=e.field, value=e.value)

def validate_memory_payload(payload_data: Dict) -> Dict:
    """Validate memory payload with specific error handling"""
    try:
        return validate_input(payload_data, MEMORY_PAYLOAD_SCHEMA, "memory_payload")
    except ValidationError as e:
        raise MemoryValidationError(f"Memory payload validation failed: {e.message}", field=e.field, value=e.value)

def validate_trust_registry(registry_data: Dict) -> Dict:
    """Validate trust registry entry with specific error handling"""
    try:
        return validate_input(registry_data, TRUST_REGISTRY_SCHEMA, "trust_registry")
    except ValidationError as e:
        raise ValidationError(f"Trust registry validation failed: {e.message}", field=e.field, value=e.value)

def validate_cli_args(args: List[str]) -> List[str]:
    """Validate and sanitize CLI arguments"""
    sanitized_args = []
    
    for arg in args:
        if not isinstance(arg, str):
            raise ValidationError("CLI arguments must be strings")
        
        # Sanitize each argument
        sanitized = sanitize_string(arg, max_length=500)
        
        # Check for dangerous patterns
        dangerous_patterns = [
            r'[;&|`$]',  # Command injection
            r'\.\./',    # Path traversal
            r'<script',  # XSS
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, sanitized, re.IGNORECASE):
                validation_logger.warning(f"Potentially dangerous CLI argument detected: {sanitized}")
                # Remove dangerous characters
                sanitized = re.sub(pattern, '', sanitized)
        
        if sanitized:
            sanitized_args.append(sanitized)
    
    return sanitized_args

def quarantine_invalid_data(data: Any, reason: str, context: str) -> str:
    """Move invalid data to quarantine for analysis"""
    quarantine_dir = Path("memory_bank/quarantine")
    quarantine_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"invalid_{context}_{timestamp}.json"
    filepath = quarantine_dir / filename
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                "data": data,
                "reason": reason,
                "context": context,
                "timestamp": datetime.now().isoformat()
            }, f, indent=2, ensure_ascii=False)
        
        validation_logger.warning(f"Quarantined invalid data to {filepath}")
        return str(filepath)
    except Exception as e:
        validation_logger.error(f"Failed to quarantine data: {e}")
        return ""

# === Middleware Functions ===
def validate_config_file(filepath: str, schema: Dict) -> Dict:
    """Validate a configuration file with fallback handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return validate_input(data, schema, f"config_file:{filepath}")
    
    except json.JSONDecodeError as e:
        validation_logger.error(f"JSON decode error in {filepath}: {e}")
        quarantine_invalid_data({"filepath": filepath, "error": str(e)}, "json_decode", "config")
        raise ConfigValidationError(f"Invalid JSON in {filepath}: {e}")
    
    except ValidationError as e:
        validation_logger.error(f"Validation error in {filepath}: {e.message}")
        quarantine_invalid_data(data, f"validation_error:{e.message}", "config")
        raise e
    
    except Exception as e:
        validation_logger.error(f"Unexpected error reading {filepath}: {e}")
        raise ConfigValidationError(f"Failed to read {filepath}: {e}")

def validate_model_response(response: Dict) -> Dict:
    """Validate model response payload with trust scoring"""
    try:
        # Create a copy without trust_score for validation
        validation_data = response.copy()
        if "trust_score" in validation_data:
            del validation_data["trust_score"]
        
        validated = validate_memory_payload(validation_data)
        
        # Additional trust scoring
        trust_indicators = {
            "has_timestamp": "timestamp" in response,
            "has_agent": "agent" in response,
            "reasonable_length": len(response.get("response", "")) < 50000,
            "no_suspicious_patterns": not re.search(r'<script|javascript:|data:', response.get("response", ""), re.IGNORECASE)
        }
        
        trust_score = sum(trust_indicators.values()) / len(trust_indicators)
        validated["trust_score"] = trust_score
        
        validation_logger.info(f"Model response validated with trust score: {trust_score:.2f}")
        return validated
    
    except ValidationError as e:
        validation_logger.error(f"Model response validation failed: {e.message}")
        quarantine_invalid_data(response, f"model_response_error:{e.message}", "model_response")
        raise PayloadValidationError(f"Model response validation failed: {e.message}", field=e.field, value=e.value) 