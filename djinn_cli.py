#!/usr/bin/env python3
"""
Djinn Constellation Hub CLI
Universal command-line interface for all major user commands and features.
"""
import argparse
import sys
import subprocess
import logging
import os
from pathlib import Path
from datetime import datetime

# === Input Validation Integration ===
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'validators'))
    from input_validator import validate_cli_args, quarantine_invalid_data
    VALIDATION_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Input validation not available: {e}")
    VALIDATION_AVAILABLE = False

# Configure comprehensive logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('djinn_cli.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('DjinnCLI')

# Mapping of CLI commands to Python scripts or batch files
COMMAND_MAP = {
    "status": ["python", "constellation_hub.py", "--status"],
    "models": ["python", "constellation_hub.py", "--models"],
    "performance": ["python", "constellation_hub.py", "--performance"],
    "efficiency": ["python", "constellation_hub.py", "--efficiency"],
    "pcloud": ["python", "pcloud_djinn_federation.py", "--status"],
    "sync": ["python", "pcloud_djinn_federation.py", "--sync"],
    "federate": ["python", "constellation_hub.py", "--federate"],
    "distribute": ["python", "constellation_hub.py", "--distribute"],
    "local": ["python", "constellation_hub.py", "--local"],
    "cloud": ["python", "constellation_hub.py", "--cloud"],
    "auto": ["python", "constellation_hub.py", "--auto"],
    "escalate": ["python", "constellation_hub.py", "--escalate"],
    "test": ["pytest", "tests/"],
    "launch": ["python", "djinn-federation/launcher/efficiency_first_hub.py"],
}

def validate_command_mapping():
    """Validate that all commands in COMMAND_MAP are properly defined."""
    logger.info("Validating command mapping...")
    
    for cmd, command_list in COMMAND_MAP.items():
        if not isinstance(command_list, list) or len(command_list) == 0:
            logger.error(f"Invalid command definition for '{cmd}': {command_list}")
            return False
        
        # Check if the main executable exists
        main_executable = command_list[0]
        if main_executable == "python":
            # Python commands are generally safe
            continue
        elif main_executable == "pytest":
            # Check if pytest is available
            try:
                subprocess.run([main_executable, "--version"], 
                             capture_output=True, check=True, timeout=5)
            except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
                logger.warning(f"Executable not found: {main_executable}")
        else:
            # Check if file exists for other executables
            if not os.path.exists(main_executable):
                logger.warning(f"Executable not found: {main_executable}")
    
    logger.info("Command mapping validation complete")
    return True

def sanitize_args(args):
    """Sanitize and validate command arguments."""
    logger.info(f"Sanitizing arguments: {args}")
    
    if not args:
        return []
    
    # Use validation layer if available
    if VALIDATION_AVAILABLE:
        try:
            sanitized = validate_cli_args(args)
            logger.info(f"Validated arguments: {sanitized}")
            return sanitized
        except Exception as e:
            logger.warning(f"Validation failed, using fallback sanitization: {e}")
            # Fall back to basic sanitization
    
    # Basic sanitization fallback
    sanitized = []
    for arg in args:
        # Basic sanitization - remove any potentially dangerous characters
        sanitized_arg = str(arg).strip()
        
        # Prevent command injection attempts
        dangerous_chars = [';', '|', '&', '`', '$', '(', ')', '{', '}']
        if any(char in sanitized_arg for char in dangerous_chars):
            logger.warning(f"Potentially dangerous argument detected: {sanitized_arg}")
            for char in dangerous_chars:
                sanitized_arg = sanitized_arg.replace(char, '')
        
        if sanitized_arg:
            sanitized.append(sanitized_arg)
    
    logger.info(f"Sanitized arguments: {sanitized}")
    return sanitized

def show_help():
    """Display comprehensive help information."""
    print("🜂 DJINN CONSTELLATION HUB CLI - UNIVERSAL COMMAND INTERFACE 🜂")
    print("=" * 60)
    print("Available Commands:")
    print()
    
    # Group commands by category
    categories = {
        "System Status": ["status", "models", "performance", "efficiency"],
        "Federation Management": ["federate", "distribute", "local", "cloud", "auto", "escalate"],
        "PCloud Operations": ["pcloud", "sync"],
        "Development": ["test", "launch"]
    }
    
    for category, commands in categories.items():
        print(f"📋 {category}:")
        for cmd in commands:
            if cmd in COMMAND_MAP:
                print(f"  {cmd:12} - {get_command_description(cmd)}")
        print()
    
    print("Usage Examples:")
    print("  python djinn_cli.py status")
    print("  python djinn_cli.py models")
    print("  python djinn_cli.py launch")
    print("  python djinn_cli.py --help")
    print()
    print("For detailed help on specific commands, use: python djinn_cli.py <command> --help")
    print("=" * 60)

def get_command_description(command):
    """Get description for a specific command."""
    descriptions = {
        "status": "Show system health and capabilities",
        "models": "List available models and their status",
        "performance": "Display performance metrics and history",
        "efficiency": "Show efficiency scoring and optimization",
        "pcloud": "PCloud status and capacity",
        "sync": "Synchronize models and memory",
        "federate": "Manage federated consciousness",
        "distribute": "Multi-device task distribution",
        "local": "Force local tier execution",
        "cloud": "Force cloud tier execution",
        "auto": "Return to automatic intelligent routing",
        "escalate": "Manual escalation to higher tier",
        "test": "Run all system tests",
        "launch": "Launch the main federation hub"
    }
    return descriptions.get(command, "No description available")

def show_status():
    """Display current system status."""
    print("🜂 DJINN CONSTELLATION HUB STATUS 🜂")
    print("=" * 40)
    
    # System information
    print("🔧 System Information:")
    print(f"  Python Version: {sys.version}")
    print(f"  Working Directory: {os.getcwd()}")
    print(f"  Log File: djinn_cli.log")
    
    # Command availability
    print("\n📋 Available Commands:")
    for cmd in sorted(COMMAND_MAP.keys()):
        print(f"  ✅ {cmd}")
    
    # Check critical files
    print("\n📁 Critical Files:")
    critical_files = [
        "constellation_hub.py",
        "enhanced_constellation_hub.py", 
        "pcloud_djinn_federation.py",
        "djinn-federation/launcher/efficiency_first_hub.py"
    ]
    
    for file_path in critical_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} (missing)")
    
    # Check Ollama availability
    print("\n🤖 Ollama Status:")
    try:
        result = subprocess.run(['ollama', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"  ✅ Ollama: {result.stdout.strip()}")
        else:
            print("  ❌ Ollama: Not responding")
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
        print("  ❌ Ollama: Not found")
    
    print("=" * 40)

def execute_command_safely(command, args):
    """Execute a command with comprehensive error handling."""
    logger.info(f"Executing command: {command} with args: {args}")
    
    try:
        # Validate command exists
        if command not in COMMAND_MAP:
            logger.error(f"Unknown command: {command}")
            return False, f"Unknown command: {command}"
        
        # Get command definition
        command_to_run = COMMAND_MAP[command] + args
        
        # Log the full command being executed
        logger.info(f"Running: {' '.join(command_to_run)}")
        
        # Execute with timeout
        result = subprocess.run(
            command_to_run, 
            capture_output=True, 
            text=True, 
            timeout=300,  # 5 minute timeout
            encoding='utf-8',
            errors='replace'
        )
        
        # Log the result
        if result.returncode == 0:
            logger.info(f"Command '{command}' executed successfully")
            if result.stdout:
                print(result.stdout)
            return True, "Command executed successfully"
        else:
            logger.error(f"Command '{command}' failed with exit code {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False, f"Command failed with exit code {result.returncode}"
            
    except subprocess.TimeoutExpired:
        logger.error(f"Command '{command}' timed out")
        return False, f"Command '{command}' timed out"
    except FileNotFoundError as e:
        logger.error(f"Command '{command}' failed - file not found: {e}")
        return False, f"Command failed - file not found: {e}"
    except subprocess.CalledProcessError as e:
        logger.error(f"Command '{command}' failed with exit code {e.returncode}")
        return False, f"Command failed with exit code {e.returncode}"
    except Exception as e:
        logger.error(f"Unexpected error executing command '{command}': {e}")
        return False, f"Unexpected error: {e}"

def main():
    """Main CLI entry point with comprehensive error handling."""
    logger.info("Djinn CLI starting up")
    
    try:
        parser = argparse.ArgumentParser(
            description="Djinn Constellation Hub - Universal CLI",
            add_help=False  # We'll handle help manually
        )
        parser.add_argument(
            "command",
            nargs='?',  # Make command optional for --help
            type=str,
            help="Command to run"
        )
        parser.add_argument(
            "args",
            nargs=argparse.REMAINDER,
            help="Additional arguments to pass to the command."
        )
        parser.add_argument(
            "--help", "-h",
            action="store_true",
            help="Show this help message"
        )
        
        args = parser.parse_args()
        
        # Handle help command
        if args.help or not args.command:
            show_help()
            return 0
        
        # Validate command mapping
        if not validate_command_mapping():
            logger.error("Command mapping validation failed")
            print("[ERROR] Command mapping validation failed")
            return 1
        
        # Sanitize arguments with validation layer
        sanitized_args = sanitize_args(args.args)
        
        # Handle builtin commands
        if args.command.lower() == "help":
            show_help()
            return 0
        elif args.command.lower() == "status":
            show_status()
            return 0
        
        # Execute the command
        success, message = execute_command_safely(args.command.lower(), sanitized_args)
        
        if success:
            return 0
        else:
            print(f"[ERROR] {message}")
            return 1
            
    except KeyboardInterrupt:
        logger.info("CLI interrupted by user")
        print("\n[INFO] CLI interrupted by user")
        return 0
    except Exception as e:
        logger.error(f"Unexpected error in main CLI: {e}")
        print(f"[ERROR] Unexpected error: {e}")
        return 1
    finally:
        logger.info("Djinn CLI shutting down")

if __name__ == "__main__":
    sys.exit(main())
