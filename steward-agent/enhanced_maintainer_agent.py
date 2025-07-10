#!/usr/bin/env python3
"""
🛡️ THE STEWARD - Enhanced Maintainer Agent v2.0
Advanced system maintenance with dependency diffing, auto-patching, 
resource snapshotting, and CI/CD integration capabilities.
"""

import os
import sys
import json
import time
import subprocess
import ast
import difflib
import psutil
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

class EnhancedMaintainerAgent:
    """Enhanced Steward with advanced maintenance capabilities"""
    
    def __init__(self):
        self.name = "The Steward"
        self.role = "Enhanced Federation Maintainer"
        self.version = "2.0.0"
        
        # Enhanced command set
        self.commands = {
            'check-deps': 'Dependency analysis and diffing',
            'auto-patch': 'AST/GPT-based script repair',
            'snapshot': 'Resource and performance snapshotting',
            'ci-hooks': 'CI/CD integration management',
            'monitor': 'Enhanced system monitoring',
            'report': 'Comprehensive maintenance reporting',
            'health-check': 'Deep system health analysis'
        }
        
        # Initialize logging
        self.setup_logging()
        
        # Resource tracking
        self.resource_history = []
        self.snapshot_dir = Path("logs/resource_snapshots")
        self.snapshot_dir.mkdir(parents=True, exist_ok=True)
        
        # Dependency tracking
        self.dependency_manifest = Path("requirements.txt")
        self.dependency_cache = Path("logs/dependency_cache.json")
        
        # Auto-patch configuration
        self.patch_backup_dir = Path("logs/patches")
        self.patch_backup_dir.mkdir(parents=True, exist_ok=True)
        
        # CI/CD hooks
        self.git_hooks_dir = Path(".git/hooks")
        self.ci_config_dir = Path(".github/workflows")
        
        self.logger.info(f"Enhanced Steward v{self.version} initialized")
    
    def setup_logging(self):
        """Setup enhanced logging for The Steward"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        self.logger = logging.getLogger("EnhancedSteward")
        self.logger.setLevel(logging.INFO)
        
        # File handler
        fh = logging.FileHandler(log_dir / "enhanced_steward.log")
        fh.setLevel(logging.INFO)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def check_dependencies(self) -> Dict:
        """Enhanced dependency checking with diffing capabilities"""
        print("[Enhanced Steward] Analyzing dependencies...")
        self.logger.info("Starting enhanced dependency analysis")
        
        try:
            # Get current dependencies
            current_deps = self._get_current_dependencies()
            
            # Get expected dependencies from manifest
            expected_deps = self._get_expected_dependencies()
            
            # Perform dependency diffing
            diff_result = self._diff_dependencies(current_deps, expected_deps)
            
            # Check for security vulnerabilities
            security_issues = self._check_security_vulnerabilities(current_deps)
            
            # Generate dependency report
            report = {
                'timestamp': datetime.now().isoformat(),
                'current_dependencies': current_deps,
                'expected_dependencies': expected_deps,
                'differences': diff_result,
                'security_issues': security_issues,
                'recommendations': self._generate_dependency_recommendations(diff_result, security_issues)
            }
            
            # Save dependency cache
            self._save_dependency_cache(report)
            
            print(f"[Enhanced Steward] Dependency analysis complete. {len(diff_result['missing'])} missing, {len(diff_result['outdated'])} outdated")
            self.logger.info(f"Dependency analysis completed: {len(diff_result['missing'])} missing, {len(diff_result['outdated'])} outdated")
            
            return report
            
        except Exception as e:
            error_msg = f"Dependency analysis failed: {str(e)}"
            print(f"[Enhanced Steward] ERROR: {error_msg}")
            self.logger.error(error_msg)
            return {'error': error_msg}
    
    def _get_current_dependencies(self) -> Dict[str, str]:
        """Get currently installed dependencies"""
        try:
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'freeze'],
                capture_output=True, text=True, timeout=30
            )
            
            if result.returncode == 0:
                deps = {}
                for line in result.stdout.strip().split('\n'):
                    if '==' in line:
                        package, version = line.split('==', 1)
                        deps[package.lower()] = version
                return deps
            else:
                return {}
        except Exception as e:
            self.logger.error(f"Failed to get current dependencies: {e}")
            return {}
    
    def _get_expected_dependencies(self) -> Dict[str, str]:
        """Get expected dependencies from manifest"""
        expected = {}
        
        # Check requirements.txt
        if self.dependency_manifest.exists():
            try:
                with open(self.dependency_manifest, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            if '==' in line:
                                package, version = line.split('==', 1)
                                expected[package.lower()] = version
                            elif '>=' in line:
                                package, version = line.split('>=', 1)
                                expected[package.lower()] = f">={version}"
            except Exception as e:
                self.logger.error(f"Failed to read requirements.txt: {e}")
        
        return expected
    
    def _diff_dependencies(self, current: Dict, expected: Dict) -> Dict:
        """Perform dependency diffing analysis"""
        missing = []
        outdated = []
        extra = []
        
        # Find missing dependencies
        for package, version in expected.items():
            if package not in current:
                missing.append({'package': package, 'expected': version})
            elif version != current[package] and not version.startswith('>='):
                outdated.append({
                    'package': package,
                    'current': current[package],
                    'expected': version
                })
        
        # Find extra dependencies
        for package in current:
            if package not in expected:
                extra.append({'package': package, 'version': current[package]})
        
        return {
            'missing': missing,
            'outdated': outdated,
            'extra': extra
        }
    
    def _check_security_vulnerabilities(self, deps: Dict) -> List[Dict]:
        """Check for known security vulnerabilities"""
        # This would integrate with tools like safety or pip-audit
        # For now, return empty list
        return []
    
    def _generate_dependency_recommendations(self, diff_result: Dict, security_issues: List) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        if diff_result['missing']:
            missing_packages = [d['package'] for d in diff_result['missing']]
            recommendations.append(f"Install missing packages: {' '.join(missing_packages)}")
        
        if diff_result['outdated']:
            outdated_packages = [d['package'] for d in diff_result['outdated']]
            recommendations.append(f"Update outdated packages: {' '.join(outdated_packages)}")
        
        if security_issues:
            recommendations.append(f"Address {len(security_issues)} security vulnerabilities")
        
        return recommendations
    
    def auto_patch_scripts(self, target_file: Optional[str] = None, preview: bool = False) -> Dict:
        """AST/GPT-based script auto-patching with preview option"""
        print("[Enhanced Steward] Initiating auto-patch system...")
        self.logger.info(f"Starting auto-patch analysis (preview={preview})")
        
        try:
            if target_file:
                files_to_patch = [target_file]
            else:
                files_to_patch = self._find_python_files()
            
            patch_results = []
            
            for file_path in files_to_patch:
                if os.path.exists(file_path):
                    patch_result = self._analyze_and_patch_file(file_path, preview=preview)
                    if patch_result:
                        patch_results.append(patch_result)
            
            report = {
                'timestamp': datetime.now().isoformat(),
                'files_analyzed': len(files_to_patch),
                'patches_applied': len([r for r in patch_results if r['patched']]),
                'patch_results': patch_results
            }
            
            print(f"[Enhanced Steward] Auto-patch complete. {report['patches_applied']} patches applied")
            self.logger.info(f"Auto-patch completed: {report['patches_applied']} patches applied")
            
            return report
            
        except Exception as e:
            error_msg = f"Auto-patch failed: {str(e)}"
            print(f"[Enhanced Steward] ERROR: {error_msg}")
            self.logger.error(error_msg)
            return {'error': error_msg}
    
    def _find_python_files(self) -> List[str]:
        """Find Python files to analyze"""
        python_files = []
        
        for root, dirs, files in os.walk('.'):
            # Skip certain directories
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', 'venv']]
            
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        
        return python_files
    
    def _analyze_and_patch_file(self, file_path: str, preview: bool = False) -> Optional[Dict]:
        """Analyze and potentially patch a single file, with preview option"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse AST
            try:
                tree = ast.parse(content)
            except SyntaxError as e:
                # Try to fix common syntax errors
                fixed_content = self._fix_common_syntax_errors(content, e)
                if fixed_content != content:
                    return self._apply_patch(file_path, content, fixed_content, "syntax_error_fix", preview=preview)
                return None
            
            # Check for common issues
            issues = self._detect_common_issues(tree, content)
            
            # Detect import path errors
            import_fixes = self._fix_import_path_errors(content)
            if import_fixes['fixed']:
                issues.append({'type': 'import_path_fix', 'details': import_fixes['details']})
                fixed_content = import_fixes['content']
            else:
                fixed_content = content
            
            # Suggest structural refactoring (log only)
            refactor_suggestions = self._suggest_structural_refactoring(tree, content)
            if refactor_suggestions:
                self.logger.info(f"Refactor suggestions for {file_path}: {refactor_suggestions}")
            
            # Apply fixes
            if issues:
                fixed_content2 = self._apply_fixes(fixed_content, issues)
                if fixed_content2 != content:
                    return self._apply_patch(file_path, content, fixed_content2, "auto_patch", preview=preview)
            
            return None
            
        except Exception as e:
            self.logger.error(f"Failed to analyze {file_path}: {e}")
            return None
    
    def _fix_common_syntax_errors(self, content: str, error: SyntaxError) -> str:
        """Fix common syntax errors"""
        lines = content.split('\n')
        
        # Fix common indentation issues
        fixed_lines = []
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                # Check if this line should be indented
                if i > 0 and lines[i-1].strip().endswith(':'):
                    line = '    ' + line
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines)
    
    def _detect_common_issues(self, tree: ast.AST, content: str) -> List[Dict]:
        """Detect common code issues"""
        issues = []
        
        # Check for unused imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if not self._is_import_used(alias.name, tree):
                        issues.append({
                            'type': 'unused_import',
                            'line': node.lineno,
                            'name': alias.name
                        })
        
        return issues
    
    def _is_import_used(self, import_name: str, tree: ast.AST) -> bool:
        """Check if an import is actually used"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id == import_name:
                return True
        return False
    
    def _apply_fixes(self, content: str, issues: List[Dict]) -> str:
        """Apply fixes to content"""
        lines = content.split('\n')
        
        # Sort issues by line number (descending) to avoid offset issues
        issues.sort(key=lambda x: x['line'], reverse=True)
        
        for issue in issues:
            if issue['type'] == 'unused_import':
                # Remove unused import line
                line_idx = issue['line'] - 1
                if 0 <= line_idx < len(lines):
                    lines.pop(line_idx)
        
        return '\n'.join(lines)
    
    def _fix_import_path_errors(self, content: str) -> Dict:
        """Detect and fix common import path errors (simple heuristics)"""
        lines = content.split('\n')
        fixed = False
        details = []
        for i, line in enumerate(lines):
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                if '...' in line or '???' in line:
                    lines[i] = line.replace('...', '').replace('???', '')
                    fixed = True
                    details.append(f"Line {i+1}: removed placeholder from import")
        return {'fixed': fixed, 'content': '\n'.join(lines), 'details': details}

    def _suggest_structural_refactoring(self, tree: ast.AST, content: str) -> List[str]:
        """Suggest structural refactoring opportunities (log only)"""
        suggestions = []
        # Example: suggest splitting large functions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 50:
                    suggestions.append(f"Function '{node.name}' is very large ({len(node.body)} lines). Consider refactoring.")
        return suggestions

    def _apply_patch(self, file_path: str, original: str, fixed: str, patch_type: str, preview: bool = False) -> Dict:
        """Apply a patch to a file, or preview changes if requested"""
        try:
            # Create backup
            backup_path = self.patch_backup_dir / f"{Path(file_path).name}.{int(time.time())}.bak"
            if not preview:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original)
                # Apply patch
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed)
            diff = list(difflib.unified_diff(original.splitlines(), fixed.splitlines(), fromfile='original', tofile='fixed'))
            if preview:
                print(f"[Preview] Patch for {file_path} (type: {patch_type}):\n" + '\n'.join(diff))
            return {
                'file': file_path,
                'patched': not preview,
                'patch_type': patch_type,
                'backup': str(backup_path),
                'changes': len(diff),
                'preview': preview,
                'diff': diff if preview else None
            }
        except Exception as e:
            self.logger.error(f"Failed to apply patch to {file_path}: {e}")
            return {
                'file': file_path,
                'patched': False,
                'error': str(e),
                'preview': preview
            }
    
    def create_resource_snapshot(self) -> Dict:
        """Create comprehensive resource snapshot"""
        print("[Enhanced Steward] Creating resource snapshot...")
        self.logger.info("Creating resource snapshot")
        
        try:
            # System resources
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # Network stats
            network = psutil.net_io_counters()
            
            # Process information
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Sort by CPU usage
            processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
            top_processes = processes[:10]
            
            snapshot = {
                'timestamp': datetime.now().isoformat(),
                'system_resources': {
                    'cpu_percent': cpu_percent,
                    'memory_total_gb': round(memory.total / (1024**3), 2),
                    'memory_used_gb': round(memory.used / (1024**3), 2),
                    'memory_percent': memory.percent,
                    'disk_total_gb': round(disk.total / (1024**3), 2),
                    'disk_free_gb': round(disk.free / (1024**3), 2),
                    'disk_percent': round((disk.used / disk.total) * 100, 2)
                },
                'network': {
                    'bytes_sent': network.bytes_sent,
                    'bytes_recv': network.bytes_recv,
                    'packets_sent': network.packets_sent,
                    'packets_recv': network.packets_recv
                },
                'top_processes': top_processes,
                'federation_status': self._get_federation_status()
            }
            
            # Save snapshot
            snapshot_file = self.snapshot_dir / f"snapshot_{int(time.time())}.json"
            with open(snapshot_file, 'w') as f:
                json.dump(snapshot, f, indent=2)
            
            # Add to history
            self.resource_history.append(snapshot)
            
            # Keep only last 100 snapshots
            if len(self.resource_history) > 100:
                self.resource_history = self.resource_history[-100:]
            
            print(f"[Enhanced Steward] Snapshot saved: {snapshot_file}")
            self.logger.info(f"Resource snapshot created: {snapshot_file}")
            
            return snapshot
            
        except Exception as e:
            error_msg = f"Resource snapshot failed: {str(e)}"
            print(f"[Enhanced Steward] ERROR: {error_msg}")
            self.logger.error(error_msg)
            return {'error': error_msg}
    
    def _get_federation_status(self) -> Dict:
        """Get current federation status"""
        try:
            # Check if constellation hub is running
            hub_processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    if 'constellation_hub' in ' '.join(proc.info['cmdline'] or []):
                        hub_processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Check trust registry
            trust_registry_exists = Path("trust_registry.json").exists()
            
            return {
                'hub_processes': len(hub_processes),
                'trust_registry_exists': trust_registry_exists,
                'active_agents': len(hub_processes)
            }
            
        except Exception as e:
            self.logger.error(f"Failed to get federation status: {e}")
            return {'error': str(e)}
    
    def setup_ci_hooks(self) -> Dict:
        """Setup CI/CD integration hooks"""
        print("[Enhanced Steward] Setting up CI/CD hooks...")
        self.logger.info("Setting up CI/CD integration")
        
        try:
            hooks_created = []
            
            # Git pre-commit hook
            if self.git_hooks_dir.exists():
                pre_commit_hook = self.git_hooks_dir / "pre-commit"
                hook_content = self._generate_pre_commit_hook()
                
                with open(pre_commit_hook, 'w') as f:
                    f.write(hook_content)
                
                # Make executable
                os.chmod(pre_commit_hook, 0o755)
                hooks_created.append("pre-commit")
            
            # GitHub Actions workflow
            if self.ci_config_dir.exists():
                workflow_file = self.ci_config_dir / "steward-checks.yml"
                workflow_content = self._generate_github_workflow()
                
                with open(workflow_file, 'w') as f:
                    f.write(workflow_content)
                
                hooks_created.append("github-actions")
            
            report = {
                'timestamp': datetime.now().isoformat(),
                'hooks_created': hooks_created,
                'git_hooks_dir': str(self.git_hooks_dir),
                'ci_config_dir': str(self.ci_config_dir)
            }
            
            print(f"[Enhanced Steward] CI/CD hooks setup complete: {', '.join(hooks_created)}")
            self.logger.info(f"CI/CD hooks setup completed: {', '.join(hooks_created)}")
            
            return report
            
        except Exception as e:
            error_msg = f"CI/CD hooks setup failed: {str(e)}"
            print(f"[Enhanced Steward] ERROR: {error_msg}")
            self.logger.error(error_msg)
            return {'error': error_msg}
    
    def _generate_pre_commit_hook(self) -> str:
        """Generate pre-commit hook content"""
        return '''#!/bin/bash
# Enhanced Steward Pre-commit Hook

echo "🛡️ Enhanced Steward: Running pre-commit checks..."

# Run dependency check
python steward-agent/enhanced_maintainer_agent.py check-deps

# Run auto-patch on staged files
python steward-agent/enhanced_maintainer_agent.py auto-patch

# Create resource snapshot
python steward-agent/enhanced_maintainer_agent.py snapshot

echo "✅ Enhanced Steward: Pre-commit checks complete"
'''
    
    def _generate_github_workflow(self) -> str:
        """Generate GitHub Actions workflow"""
        return '''name: Enhanced Steward Checks

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  steward-checks:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run Enhanced Steward Checks
      run: |
        python steward-agent/enhanced_maintainer_agent.py health-check
        python steward-agent/enhanced_maintainer_agent.py check-deps
        python steward-agent/enhanced_maintainer_agent.py snapshot
    
    - name: Upload Steward Reports
      uses: actions/upload-artifact@v3
      with:
        name: steward-reports
        path: logs/
'''
    
    def enhanced_monitor(self) -> Dict:
        """Enhanced system monitoring with alerts"""
        print("[Enhanced Steward] Starting enhanced monitoring...")
        self.logger.info("Starting enhanced monitoring")
        
        try:
            # Create resource snapshot
            snapshot = self.create_resource_snapshot()
            
            # Check for alerts
            alerts = self._check_alerts(snapshot)
            
            # Monitor federation health
            federation_health = self._monitor_federation_health()
            
            report = {
                'timestamp': datetime.now().isoformat(),
                'snapshot': snapshot,
                'alerts': alerts,
                'federation_health': federation_health,
                'recommendations': self._generate_monitoring_recommendations(alerts, federation_health)
            }
            
            print(f"[Enhanced Steward] Monitoring complete. {len(alerts)} alerts detected")
            self.logger.info(f"Enhanced monitoring completed: {len(alerts)} alerts")
            
            return report
            
        except Exception as e:
            error_msg = f"Enhanced monitoring failed: {str(e)}"
            print(f"[Enhanced Steward] ERROR: {error_msg}")
            self.logger.error(error_msg)
            return {'error': error_msg}
    
    def _check_alerts(self, snapshot: Dict) -> List[Dict]:
        """Check for system alerts"""
        alerts = []
        
        if 'system_resources' in snapshot:
            resources = snapshot['system_resources']
            
            # CPU alert
            if resources.get('cpu_percent', 0) > 80:
                alerts.append({
                    'type': 'high_cpu',
                    'severity': 'warning',
                    'message': f"High CPU usage: {resources['cpu_percent']}%"
                })
            
            # Memory alert
            if resources.get('memory_percent', 0) > 85:
                alerts.append({
                    'type': 'high_memory',
                    'severity': 'warning',
                    'message': f"High memory usage: {resources['memory_percent']}%"
                })
            
            # Disk alert
            if resources.get('disk_percent', 0) > 90:
                alerts.append({
                    'type': 'low_disk',
                    'severity': 'critical',
                    'message': f"Low disk space: {100 - resources['disk_percent']}% free"
                })
        
        return alerts
    
    def _monitor_federation_health(self) -> Dict:
        """Monitor federation-specific health metrics"""
        try:
            # Check trust registry
            trust_registry_healthy = Path("trust_registry.json").exists()
            
            # Check log files
            log_files = list(Path("logs").glob("*.log"))
            recent_logs = [f for f in log_files if f.stat().st_mtime > time.time() - 3600]  # Last hour
            
            # Check constellation hub process
            hub_running = False
            for proc in psutil.process_iter(['name', 'cmdline']):
                try:
                    if 'python' in proc.info['name'] and any('constellation_hub' in cmd for cmd in proc.info['cmdline'] or []):
                        hub_running = True
                        break
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            return {
                'trust_registry_healthy': trust_registry_healthy,
                'recent_log_activity': len(recent_logs),
                'constellation_hub_running': hub_running,
                'overall_health': 'good' if trust_registry_healthy and hub_running else 'degraded'
            }
            
        except Exception as e:
            self.logger.error(f"Federation health monitoring failed: {e}")
            return {'error': str(e)}
    
    def _generate_monitoring_recommendations(self, alerts: List, federation_health: Dict) -> List[str]:
        """Generate monitoring recommendations"""
        recommendations = []
        
        for alert in alerts:
            if alert['type'] == 'high_cpu':
                recommendations.append("Consider optimizing CPU-intensive processes")
            elif alert['type'] == 'high_memory':
                recommendations.append("Check for memory leaks or consider increasing RAM")
            elif alert['type'] == 'low_disk':
                recommendations.append("Clean up disk space or expand storage")
        
        if not federation_health.get('constellation_hub_running', False):
            recommendations.append("Restart constellation hub if needed")
        
        return recommendations
    
    def comprehensive_report(self) -> Dict:
        """Generate comprehensive maintenance report"""
        print("[Enhanced Steward] Generating comprehensive report...")
        self.logger.info("Generating comprehensive maintenance report")
        
        try:
            # Run all checks
            dependency_report = self.check_dependencies()
            resource_snapshot = self.create_resource_snapshot()
            monitoring_report = self.enhanced_monitor()
            
            # Generate trend analysis
            trends = self._analyze_trends()
            
            report = {
                'timestamp': datetime.now().isoformat(),
                'steward_version': self.version,
                'dependency_analysis': dependency_report,
                'resource_snapshot': resource_snapshot,
                'monitoring_report': monitoring_report,
                'trends': trends,
                'summary': self._generate_report_summary(dependency_report, resource_snapshot, monitoring_report)
            }
            
            # Save report
            report_file = Path("logs/enhanced_steward_report.json")
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2)
            
            print(f"[Enhanced Steward] Comprehensive report saved: {report_file}")
            self.logger.info(f"Comprehensive report generated: {report_file}")
            
            return report
            
        except Exception as e:
            error_msg = f"Comprehensive report failed: {str(e)}"
            print(f"[Enhanced Steward] ERROR: {error_msg}")
            self.logger.error(error_msg)
            return {'error': error_msg}
    
    def _analyze_trends(self) -> Dict:
        """Analyze resource usage trends"""
        if len(self.resource_history) < 2:
            return {'message': 'Insufficient data for trend analysis'}
        
        try:
            # Get last 10 snapshots
            recent_snapshots = self.resource_history[-10:]
            
            # Calculate trends
            cpu_trend = self._calculate_trend([s['system_resources']['cpu_percent'] for s in recent_snapshots])
            memory_trend = self._calculate_trend([s['system_resources']['memory_percent'] for s in recent_snapshots])
            
            return {
                'cpu_trend': cpu_trend,
                'memory_trend': memory_trend,
                'snapshots_analyzed': len(recent_snapshots)
            }
            
        except Exception as e:
            self.logger.error(f"Trend analysis failed: {e}")
            return {'error': str(e)}
    
    def _calculate_trend(self, values: List[float]) -> str:
        """Calculate trend direction"""
        if len(values) < 2:
            return 'stable'
        
        # Simple linear trend
        first_half = values[:len(values)//2]
        second_half = values[len(values)//2:]
        
        first_avg = sum(first_half) / len(first_half)
        second_avg = sum(second_half) / len(second_half)
        
        diff = second_avg - first_avg
        
        if abs(diff) < 5:
            return 'stable'
        elif diff > 0:
            return 'increasing'
        else:
            return 'decreasing'
    
    def _generate_report_summary(self, deps: Dict, resources: Dict, monitoring: Dict) -> Dict:
        """Generate report summary"""
        summary = {
            'overall_health': 'good',
            'issues_found': 0,
            'recommendations': []
        }
        
        # Check dependencies
        if 'differences' in deps:
            diff = deps['differences']
            missing_count = len(diff.get('missing', []))
            outdated_count = len(diff.get('outdated', []))
            
            if missing_count > 0 or outdated_count > 0:
                summary['issues_found'] += missing_count + outdated_count
                summary['recommendations'].append(f"Update {missing_count + outdated_count} dependencies")
        
        # Check monitoring alerts
        if 'alerts' in monitoring:
            alert_count = len(monitoring['alerts'])
            summary['issues_found'] += alert_count
            
            if alert_count > 0:
                summary['recommendations'].extend(monitoring.get('recommendations', []))
        
        # Determine overall health
        if summary['issues_found'] > 5:
            summary['overall_health'] = 'critical'
        elif summary['issues_found'] > 2:
            summary['overall_health'] = 'warning'
        
        return summary
    
    def receive_instruction(self, command: str, args: List[str] = None) -> str:
        """Receive and execute enhanced commands"""
        args = args or []
        
        if command == 'check-deps':
            result = self.check_dependencies()
            return f"Dependency analysis complete. {len(result.get('differences', {}).get('missing', []))} missing packages found."
        
        elif command == 'auto-patch':
            target_file = args[0] if args else None
            preview = '--preview' in args
            result = self.auto_patch_scripts(target_file, preview=preview)
            if preview:
                return f"Auto-patch preview complete. {result.get('patches_applied', 0)} patches would be applied."
            return f"Auto-patch complete. {result.get('patches_applied', 0)} patches applied."
        
        elif command == 'snapshot':
            result = self.create_resource_snapshot()
            return f"Resource snapshot created. CPU: {result.get('system_resources', {}).get('cpu_percent', 0)}%, Memory: {result.get('system_resources', {}).get('memory_percent', 0)}%"
        
        elif command == 'ci-hooks':
            result = self.setup_ci_hooks()
            return f"CI/CD hooks setup complete. {len(result.get('hooks_created', []))} hooks created."
        
        elif command == 'monitor':
            result = self.enhanced_monitor()
            return f"Enhanced monitoring complete. {len(result.get('alerts', []))} alerts detected."
        
        elif command == 'report':
            result = self.comprehensive_report()
            return f"Comprehensive report generated. Overall health: {result.get('summary', {}).get('overall_health', 'unknown')}"
        
        elif command == 'health-check':
            # Run all health checks
            deps = self.check_dependencies()
            snapshot = self.create_resource_snapshot()
            monitoring = self.enhanced_monitor()
            
            issues = len(deps.get('differences', {}).get('missing', [])) + len(monitoring.get('alerts', []))
            
            if issues == 0:
                return "✅ All systems healthy. Federation operating normally."
            else:
                return f"⚠️ {issues} issues detected. Run 'report' for detailed analysis."
        
        else:
            return f"Unknown enhanced command: {command}. Available: {', '.join(self.commands.keys())}"

    def _save_dependency_cache(self, report: dict):
        """Save dependency diff report to cache file"""
        try:
            with open(self.dependency_cache, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
            self.logger.info(f"Dependency cache updated: {self.dependency_cache}")
        except Exception as e:
            self.logger.error(f"Failed to save dependency cache: {e}")

def main():
    """Main entry point for Enhanced Steward"""
    agent = EnhancedMaintainerAgent()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args = sys.argv[2:] if len(sys.argv) > 2 else []
        
        result = agent.receive_instruction(command, args)
        print(result)
    else:
        print(f"🛡️ Enhanced Steward v{agent.version}")
        print("Available commands:")
        for cmd, desc in agent.commands.items():
            print(f"  {cmd}: {desc}")

if __name__ == "__main__":
    main() 