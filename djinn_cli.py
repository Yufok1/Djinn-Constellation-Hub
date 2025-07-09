#!/usr/bin/env python3
"""
Djinn Constellation Hub CLI
Universal command-line interface for all major user commands and features.
"""
import argparse
import sys
import subprocess

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

def main():
    parser = argparse.ArgumentParser(
        description="Djinn Constellation Hub - Universal CLI"
    )
    parser.add_argument(
        "command",
        type=str,
        help="Command to run (status, models, performance, pcloud, sync, federate, distribute, local, cloud, auto, escalate, test, launch)",
    )
    parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="Additional arguments to pass to the command."
    )
    args = parser.parse_args()

    cmd = args.command.lower()
    if cmd not in COMMAND_MAP:
        print(f"[ERROR] Unknown command: {cmd}\n")
        print("Available commands:", ", ".join(COMMAND_MAP.keys()))
        sys.exit(1)

    command_to_run = COMMAND_MAP[cmd] + args.args
    try:
        subprocess.run(command_to_run, check=True)
    except FileNotFoundError as e:
        print(f"[ERROR] Command failed: {e}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
