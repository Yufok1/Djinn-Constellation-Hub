#!/usr/bin/env python3
"""
🜂 DJINN CONSTELLATION HUB v2.0.0 - SYSTEM HEALTH CHECK 🜂
Comprehensive audit and validation of all system components
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import psutil


class DjinnSystemHealthCheck:
    def __init__(self):
        self.health_report = {
            "timestamp": datetime.now().isoformat(),
            "overall_health": 0,
            "components": {},
            "issues": [],
            "recommendations": [],
        }

    def check_python_environment(self):
        """Check Python environment and dependencies"""
        print("🐍 Checking Python environment...")

        try:
            python_version = sys.version_info
            if python_version.major >= 3 and python_version.minor >= 8:
                self.health_report["components"]["python"] = {
                    "status": "✅ OK",
                    "version": f"{python_version.major}.{python_version.minor}.{python_version.micro}",
                    "score": 100,
                }
            else:
                self.health_report["components"]["python"] = {
                    "status": "❌ FAILED",
                    "version": f"{python_version.major}.{python_version.minor}.{python_version.micro}",
                    "score": 0,
                }
                self.health_report["issues"].append("Python 3.8+ required")
        except Exception as e:
            self.health_report["components"]["python"] = {
                "status": "❌ ERROR",
                "error": str(e),
                "score": 0,
            }

    def check_ollama_installation(self):
        """Check Ollama installation and service"""
        print("🤖 Checking Ollama installation...")

        try:
            # Check if ollama command is available
            result = subprocess.run(
                ["ollama", "--version"], capture_output=True, text=True, timeout=10
            )

            if result.returncode == 0:
                version = result.stdout.strip()
                self.health_report["components"]["ollama"] = {
                    "status": "✅ OK",
                    "version": version,
                    "score": 100,
                }
            else:
                self.health_report["components"]["ollama"] = {
                    "status": "❌ FAILED",
                    "error": "Ollama not found in PATH",
                    "score": 0,
                }
                self.health_report["issues"].append(
                    "Ollama not installed or not in PATH"
                )

        except subprocess.TimeoutExpired:
            self.health_report["components"]["ollama"] = {
                "status": "⚠️ TIMEOUT",
                "error": "Ollama command timed out",
                "score": 50,
            }
        except FileNotFoundError:
            self.health_report["components"]["ollama"] = {
                "status": "❌ NOT FOUND",
                "error": "Ollama not installed",
                "score": 0,
            }
            self.health_report["issues"].append("Install Ollama from https://ollama.ai")

    def check_ollama_service(self):
        """Check if Ollama service is running"""
        print("🔄 Checking Ollama service...")

        try:
            result = subprocess.run(
                ["ollama", "list"], capture_output=True, text=True, timeout=15
            )

            if result.returncode == 0:
                models = result.stdout.strip().split("\n")
                model_count = len([m for m in models if m.strip()])

                self.health_report["components"]["ollama_service"] = {
                    "status": "✅ RUNNING",
                    "models_installed": model_count,
                    "score": 100,
                }
            else:
                self.health_report["components"]["ollama_service"] = {
                    "status": "❌ NOT RUNNING",
                    "error": "Ollama service not responding",
                    "score": 0,
                }
                self.health_report["issues"].append(
                    "Start Ollama service: ollama serve"
                )

        except subprocess.TimeoutExpired:
            self.health_report["components"]["ollama_service"] = {
                "status": "⚠️ TIMEOUT",
                "error": "Ollama service timeout",
                "score": 50,
            }

    def check_required_models(self):
        """Check if required Djinn Federation models are installed"""
        print("🧠 Checking required models...")

        required_models = [
            "Yufok1/djinn-federation:council",
            "Yufok1/djinn-federation:idhhc",
            "Yufok1/djinn-federation:companion",
            "Yufok1/djinn-federation:enterprise-architect",
            "Yufok1/djinn-federation:deep-thinker",
            "Yufok1/djinn-federation:logic-master",
            "Yufok1/djinn-federation:cosmic-coder",
            "Yufok1/djinn-federation:steward",
            "Yufok1/djinn-federation:max",
            "Yufok1/djinn-federation:core",
            "Yufok1/djinn-federation:lite",
        ]

        try:
            result = subprocess.run(
                ["ollama", "list"], capture_output=True, text=True, timeout=15
            )

            if result.returncode == 0:
                available_models = result.stdout
                missing_models = []
                found_models = []

                for model in required_models:
                    if model in available_models:
                        found_models.append(model)
                    else:
                        missing_models.append(model)

                score = int((len(found_models) / len(required_models)) * 100)

                self.health_report["components"]["required_models"] = {
                    "status": "✅ OK" if score == 100 else "⚠️ PARTIAL",
                    "found": len(found_models),
                    "missing": len(missing_models),
                    "missing_list": missing_models,
                    "score": score,
                }

                if missing_models:
                    self.health_report["issues"].append(
                        f"Missing models: {', '.join(missing_models)}"
                    )
                    self.health_report["recommendations"].append(
                        "Run: ./setup_djinn_federation.bat"
                    )

            else:
                self.health_report["components"]["required_models"] = {
                    "status": "❌ ERROR",
                    "error": "Could not check models",
                    "score": 0,
                }

        except subprocess.TimeoutExpired:
            self.health_report["components"]["required_models"] = {
                "status": "⚠️ TIMEOUT",
                "error": "Model check timeout",
                "score": 50,
            }

    def check_system_resources(self):
        """Check system resources (RAM, CPU, storage)"""
        print("💻 Checking system resources...")

        try:
            memory = psutil.virtual_memory()
            cpu_percent = psutil.cpu_percent(interval=1)
            disk = psutil.disk_usage("/")

            # Calculate resource scores
            ram_score = min(
                100, int((memory.available / (1024**3)) / 8 * 100)
            )  # 8GB baseline
            cpu_score = max(0, 100 - cpu_percent)
            disk_score = min(
                100, int((disk.free / (1024**3)) / 10 * 100)
            )  # 10GB baseline

            overall_resource_score = (ram_score + cpu_score + disk_score) // 3

            self.health_report["components"]["system_resources"] = {
                "status": "✅ OK" if overall_resource_score >= 70 else "⚠️ LOW",
                "ram_gb": round(memory.total / (1024**3), 1),
                "ram_available_gb": round(memory.available / (1024**3), 1),
                "ram_usage_percent": memory.percent,
                "cpu_usage_percent": cpu_percent,
                "disk_free_gb": round(disk.free / (1024**3), 1),
                "score": overall_resource_score,
            }

            if overall_resource_score < 50:
                self.health_report["issues"].append(
                    "Low system resources - consider closing other applications"
                )

        except Exception as e:
            self.health_report["components"]["system_resources"] = {
                "status": "❌ ERROR",
                "error": str(e),
                "score": 0,
            }

    def check_file_structure(self):
        """Check if required files and directories exist"""
        print("📁 Checking file structure...")

        required_files = [
            "constellation_hub.py",
            "djinn_cli.py",
            "djinn-federation/launcher/efficiency_first_hub.py",
            "launch_djinn_constellation_hub.bat",
        ]

        required_dirs = [
            "djinn-federation",
            "djinn-federation/launcher",
            "memory_bank",
            "void_workspace",
        ]

        missing_files = []
        missing_dirs = []

        for file_path in required_files:
            if not Path(file_path).exists():
                missing_files.append(file_path)

        for dir_path in required_dirs:
            if not Path(dir_path).exists():
                missing_dirs.append(dir_path)

        score = 100
        if missing_files:
            score -= len(missing_files) * 20
        if missing_dirs:
            score -= len(missing_dirs) * 10

        score = max(0, score)

        self.health_report["components"]["file_structure"] = {
            "status": "✅ OK" if score == 100 else "⚠️ INCOMPLETE",
            "missing_files": missing_files,
            "missing_dirs": missing_dirs,
            "score": score,
        }

        if missing_files or missing_dirs:
            self.health_report["issues"].append("Missing files or directories detected")

    def check_enhanced_systems(self):
        """Check if enhanced systems can be imported"""
        print("🧠 Checking enhanced systems...")

        enhanced_modules = [
            "federation_consciousness",
            "model_prewarming",
            "model_collaboration_framework",
            "enhanced_predictive_analytics",
        ]

        failed_modules = []
        successful_modules = []

        for module in enhanced_modules:
            try:
                __import__(module)
                successful_modules.append(module)
            except ImportError:
                failed_modules.append(module)

        score = int((len(successful_modules) / len(enhanced_modules)) * 100)

        self.health_report["components"]["enhanced_systems"] = {
            "status": "✅ OK" if score == 100 else "⚠️ PARTIAL",
            "successful": successful_modules,
            "failed": failed_modules,
            "score": score,
        }

        if failed_modules:
            self.health_report["issues"].append(
                f"Enhanced systems missing: {', '.join(failed_modules)}"
            )

    def calculate_overall_health(self):
        """Calculate overall system health score"""
        total_score = 0
        component_count = 0

        for component, data in self.health_report["components"].items():
            if "score" in data:
                total_score += data["score"]
                component_count += 1

        if component_count > 0:
            overall_health = total_score // component_count
        else:
            overall_health = 0

        self.health_report["overall_health"] = overall_health

        # Determine overall status
        if overall_health >= 90:
            status = "🟢 EXCELLENT"
        elif overall_health >= 70:
            status = "🟡 GOOD"
        elif overall_health >= 50:
            status = "🟠 FAIR"
        else:
            status = "🔴 POOR"

        self.health_report["overall_status"] = status

    def generate_report(self):
        """Generate comprehensive health report"""
        print("\n" + "=" * 80)
        print("🜂 DJINN CONSTELLATION HUB v2.0.0 - SYSTEM HEALTH REPORT 🜂")
        print("=" * 80)

        print(
            f"\n📊 Overall Health: {self.health_report['overall_status']} ({self.health_report['overall_health']}%)"
        )
        print(f"⏰ Check Time: {self.health_report['timestamp']}")

        print("\n🔍 Component Status:")
        for component, data in self.health_report["components"].items():
            status = data.get("status", "❓ UNKNOWN")
            score = data.get("score", 0)
            print(f"  {component.replace('_', ' ').title()}: {status} ({score}%)")

        if self.health_report["issues"]:
            print("\n❌ Issues Found:")
            for issue in self.health_report["issues"]:
                print(f"  • {issue}")

        if self.health_report["recommendations"]:
            print("\n💡 Recommendations:")
            for rec in self.health_report["recommendations"]:
                print(f"  • {rec}")

        print("\n" + "=" * 80)

        # Save report to file
        report_file = Path("system_health_report.json")
        with open(report_file, "w") as f:
            json.dump(self.health_report, f, indent=2)

        print(f"📄 Detailed report saved to: {report_file}")

    def run_full_check(self):
        """Run complete system health check"""
        print("🜂 Starting Djinn Constellation Hub System Health Check...")
        print("=" * 60)

        self.check_python_environment()
        self.check_ollama_installation()
        self.check_ollama_service()
        self.check_required_models()
        self.check_system_resources()
        self.check_file_structure()
        self.check_enhanced_systems()

        self.calculate_overall_health()
        self.generate_report()

        return self.health_report


def main():
    health_checker = DjinnSystemHealthCheck()
    report = health_checker.run_full_check()

    # Exit with appropriate code
    if report["overall_health"] >= 70:
        print("✅ System is healthy and ready for use!")
        sys.exit(0)
    else:
        print("⚠️ System has issues that should be addressed before use.")
        sys.exit(1)


if __name__ == "__main__":
    main()
