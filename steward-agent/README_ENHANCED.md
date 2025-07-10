# 🛡️ Enhanced Steward v2.0 - Advanced Federation Maintainer

## Overview
The Enhanced Steward is an advanced version of The Steward with sophisticated maintenance capabilities including dependency diffing, auto-patching, resource snapshotting, and CI/CD integration.

## 🚀 New Capabilities

### 1. Dependency Diffing
- **Function:** `check-deps`
- **Purpose:** Compare current vs expected dependencies
- **Features:**
  - Detects missing packages
  - Identifies outdated versions
  - Security vulnerability scanning
  - Actionable recommendations

### 2. Auto-Patching System
- **Function:** `auto-patch [file]`
- **Purpose:** AST/GPT-based script repair
- **Features:**
  - Syntax error correction
  - Unused import removal
  - Common code issue fixes
  - Automatic backup creation

### 3. Resource Snapshotting
- **Function:** `snapshot`
- **Purpose:** Comprehensive system monitoring
- **Features:**
  - CPU, memory, disk tracking
  - Network statistics
  - Process analysis
  - Historical trend analysis

### 4. CI/CD Integration
- **Function:** `ci-hooks`
- **Purpose:** Automated quality gates
- **Features:**
  - Git pre-commit hooks
  - GitHub Actions workflows
  - Automated testing triggers
  - Quality enforcement

## 📋 Usage

### Basic Commands
```bash
# Check dependencies
python steward-agent/enhanced_maintainer_agent.py check-deps

# Auto-patch scripts
python steward-agent/enhanced_maintainer_agent.py auto-patch
python steward-agent/enhanced_maintainer_agent.py auto-patch path/to/file.py

# Create resource snapshot
python steward-agent/enhanced_maintainer_agent.py snapshot

# Setup CI/CD hooks
python steward-agent/enhanced_maintainer_agent.py ci-hooks

# Enhanced monitoring
python steward-agent/enhanced_maintainer_agent.py monitor

# Comprehensive report
python steward-agent/enhanced_maintainer_agent.py report

# Health check
python steward-agent/enhanced_maintainer_agent.py health-check
```

### CLI Integration
```bash
# Via djinn_cli.py
python djinn_cli.py --steward check-deps
python djinn_cli.py --steward auto-patch
python djinn_cli.py --steward snapshot
```

## 🔧 Configuration

### Dependency Manifest
The Steward uses `requirements.txt` to track expected dependencies:
```
psutil>=5.9.0
ast>=0.0.2
# ... other dependencies
```

### Resource Snapshots
Snapshots are stored in `logs/resource_snapshots/` with timestamps:
- `snapshot_1234567890.json`
- Historical trend analysis
- Performance tracking

### Auto-Patch Backups
Patched files are backed up in `logs/patches/`:
- `filename.1234567890.bak`
- Original content preserved
- Rollback capability

## 📊 Monitoring & Alerts

### System Alerts
- **High CPU (>80%):** Warning
- **High Memory (>85%):** Warning  
- **Low Disk (<10%):** Critical

### Federation Health
- Trust registry integrity
- Constellation hub status
- Log activity monitoring
- Agent availability

## 🔄 CI/CD Workflow

### Pre-commit Hook
Automatically runs on git commits:
1. Dependency check
2. Auto-patch staged files
3. Resource snapshot
4. Quality gates

### GitHub Actions
Automated workflow on push/PR:
1. Enhanced Steward health check
2. Dependency analysis
3. Resource snapshot
4. Report generation

## 📈 Trend Analysis

The Enhanced Steward tracks:
- Resource usage trends
- Performance patterns
- Dependency drift
- System health over time

## 🛡️ Security Features

- Trust registry validation
- Secure patch application
- Backup integrity
- Audit logging

## 🔍 Troubleshooting

### Common Issues
1. **Permission errors:** Ensure write access to logs/
2. **Missing dependencies:** Run `pip install -r requirements.txt`
3. **Git hooks not working:** Check .git/hooks permissions

### Logs
- Enhanced Steward logs: `logs/enhanced_steward.log`
- Resource snapshots: `logs/resource_snapshots/`
- Patch backups: `logs/patches/`
- Dependency cache: `logs/dependency_cache.json`

## 🚀 Next Steps

The Enhanced Steward is ready for:
1. **Production deployment**
2. **Custom alert thresholds**
3. **Integration with external monitoring**
4. **Advanced patch strategies**

---

**Enhanced Steward v2.0** - Your federation's advanced guardian 