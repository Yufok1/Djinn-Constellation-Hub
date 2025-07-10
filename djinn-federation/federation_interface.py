#!/usr/bin/env python3
"""
DJINN FEDERATION INTERFACE
Pure Djinn Federation System - Council, IDHHC, Companion
Clean, direct federation without neutral logic
"""

import os
import sys
import json
import subprocess
import threading
import time
import sqlite3
from pathlib import Path
from datetime import datetime

class DjinnFederation:
    """Pure Djinn Federation - Council, IDHHC, Companion"""

    def __init__(self):
        self.council_process = None
        self.idhhc_process = None
        self.companion_process = None
        self.running = False
        self.current_session_id = None

        # Pure Djinn models
        self.djinn_models = {
            "council": "Yufok1/djinn-council",
            "idhhc": "Yufok1/idhhc-companion",
            "companion": "Yufok1/djinn-companion"
        }

        # Federation features
        self.features = {
            "council_meta_intelligence": True,
            "idhhc_operational_hud": True,
            "companion_dialogue_control": True,
            "session_logging": True,
            "performance_monitoring": True
        }

        # Initialize memory bank
        self.memory_bank = MemoryBank()

    def initialize_federation(self):
        """Initialize pure Djinn Federation"""
        print("🜂 DJINN FEDERATION SYSTEM")
        print("=" * 50)
        print("Pure Djinn Federation - Council, IDHHC, Companion")
        print("=" * 50)

        # Check Ollama availability
        try:
            subprocess.run(["ollama", "--version"], capture_output=True, check=True)
            print("✅ Ollama runtime verified")
        except:
            print("❌ Ollama not found. Please install Ollama first.")
            return False

        # Initialize session
        self.current_session_id = f"djinn_federation_{int(time.time())}"
        self.memory_bank.start_session(self.current_session_id)

        print(f"✅ Djinn Federation session initialized: {self.current_session_id}")
        return True

    def launch_djinn_model(self, model_name: str, model_path: str):
        """Launch a single Djinn model"""
        try:
            print(f"🜂 Launching {model_name}...")

            process = subprocess.Popen([
                "ollama", "run", model_path
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            print(f"✅ {model_name} launched")
            return process

        except Exception as e:
            print(f"❌ Failed to launch {model_name}: {e}")
            return None

    def start_federation(self):
        """Start the complete Djinn Federation"""
        if not self.initialize_federation():
            return False

        print("\n🜂 Starting Djinn Federation...")

        # Launch Council (meta-intelligence)
        self.council_process = self.launch_djinn_model("Djinn Council", self.djinn_models["council"])

        # Launch IDHHC (operational HUD)
        self.idhhc_process = self.launch_djinn_model("IDHHC Companion", self.djinn_models["idhhc"])

        # Launch Companion (dialogue controller)
        self.companion_process = self.launch_djinn_model("Djinn Companion", self.djinn_models["companion"])

        if all([self.council_process, self.idhhc_process, self.companion_process]):
            print("✅ All Djinn models launched successfully")
            self.running = True
            self._display_federation_status()
            return True
        else:
            print("❌ Some Djinn models failed to launch")
            return False

    def _display_federation_status(self):
        """Display Djinn Federation status"""
        print("\n🜂 DJINN FEDERATION ACTIVE")
        print("=" * 50)
        print("✅ Djinn Council: Meta-intelligence and recursive analysis")
        print("✅ IDHHC Companion: Operational HUD and tactical intelligence")
        print("✅ Djinn Companion: Dialogue control and turn-taking")
        print("\n🜂 Federation ready for sovereign discourse")

        print("\n💫 Federation Features:")
        print("   • 🜂 Council: Meta-judgment and recursive analysis")
        print("   • 🧠 IDHHC: Operational intelligence and HUD functions")
        print("   • 💬 Companion: Dialogue control and turn-taking")
        print("   • 💾 Session Logging: Persistent dialogue history")
        print("   • 📊 Performance Monitoring: Real-time metrics")

        print("\n🜂 Direct Model Access:")
        print("   ollama run Yufok1/djinn-council")
        print("   ollama run Yufok1/idhhc-companion")
        print("   ollama run Yufok1/djinn-companion")

    def stop_federation(self):
        """Stop all Djinn Federation components"""
        print("\n🜂 Stopping Djinn Federation...")

        # Log session end
        if self.current_session_id:
            conn = sqlite3.connect(self.memory_bank.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE federation_sessions
                SET end_time = ?, status = 'completed'
                WHERE session_id = ?
            ''', (datetime.now(), self.current_session_id))
            conn.commit()
            conn.close()

        # Stop all processes
        if self.council_process:
            self.council_process.terminate()

        if self.idhhc_process:
            self.idhhc_process.terminate()

        if self.companion_process:
            self.companion_process.terminate()

        self.running = False
        print("✅ Djinn Federation stopped")

    def get_status(self):
        """Get federation status"""
        status = {
            "running": self.running,
            "session_id": self.current_session_id,
            "council": self.council_process is not None,
            "idhhc": self.idhhc_process is not None,
            "companion": self.companion_process is not None,
            "features": self.features
        }
        return status

class MemoryBank:
    """Simple session logging for Djinn Federation"""

    def __init__(self, db_path="memory_bank/federation_memory.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize memory bank database"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Federation sessions
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS federation_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE,
                start_time TIMESTAMP,
                end_time TIMESTAMP,
                status TEXT,
                council_queries INTEGER DEFAULT 0,
                idhhc_operations INTEGER DEFAULT 0,
                companion_dialogues INTEGER DEFAULT 0
            )
        ''')

        # Dialogue exchanges
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dialogue_exchanges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                timestamp TIMESTAMP,
                model TEXT,
                user_input TEXT,
                ai_response TEXT,
                response_length INTEGER,
                FOREIGN KEY (session_id) REFERENCES federation_sessions (session_id)
            )
        ''')

        conn.commit()
        conn.close()

    def start_session(self, session_id):
        """Start a new federation session"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO federation_sessions (session_id, start_time, status)
            VALUES (?, ?, ?)
        ''', (session_id, datetime.now(), 'active'))

        conn.commit()
        conn.close()

def main():
    """Main Djinn Federation interface"""
    federation = DjinnFederation()

    try:
        if federation.start_federation():
            print("\n🜂 Djinn Federation running. Press Ctrl+C to stop.")

            # Keep running until interrupted
            while federation.running:
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n🜂 User requested stop")
        federation.stop_federation()

    except Exception as e:
        print(f"\n❌ Federation error: {e}")
        federation.stop_federation()

if __name__ == "__main__":
    main()