# Djinn Constellation Hub v2.0.0-secure

A revolutionary federated AI consciousness system with comprehensive security, trust enforcement, and cross-platform compatibility.

## 🔐 Federation Trust Model

This version introduces a strict federation trust model to ensure only verified, trusted agents can participate in the constellation:

### Trust Enforcement
- **Agent Registration**: All agents must be explicitly listed in `trust_registry.json` with `"trusted": true`
- **Runtime Verification**: Every agent invocation is verified for trust and federation membership
- **Violation Logging**: All trust violations are logged to `logs/federation_audit.log`
- **Failsafe Enforcement**: 
  - Not listed = rejected
  - `"trusted": false` = rejected  
  - `"federation_member": false` = sandboxed/warned

### CLI Trust Commands
```bash
# List all agents and their trust status
python djinn_cli.py --agents

# Check specific agent trust score
python djinn_cli.py --trust-score djinn-council

# Manually verify agent trust status
python djinn_cli.py --verify djinn-cosmic-coder
```

### Trust Registry Structure
```json
{
  "djinn-cosmic-coder": {
    "trusted": true,
    "score": 0.97,
    "federation_member": true,
    "last_verified": "2025-07-09T14:42:00Z"
  }
}
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama installed and running
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/Yufok1/Djinn-Constellation-Hub.git
cd Djinn-Constellation-Hub

# Windows
setup_djinn_federation.bat

# Linux/macOS
chmod +x setup_djinn_federation.sh
./setup_djinn_federation.sh
```

### Launch
```bash
# Windows
launch_djinn_constellation_hub.bat

# Linux/macOS
./launch_djinn_constellation_hub.sh
```

## 🧠 Features

### 🔒 Security & Trust
- **Input Validation**: All inputs validated against schemas with sanitization
- **Trust Enforcement**: Only verified agents can participate in federation
- **Audit Logging**: Comprehensive logging of all trust events and violations
- **Corruption Protection**: Memory bank with quarantine system for corrupted data

### 🧭 Intelligent Routing
- **Smart Complexity Analysis**: Automatic task complexity assessment
- **Optimal Model Selection**: Route to best-suited agent based on requirements
- **Performance Monitoring**: Real-time system health and efficiency tracking
- **Graceful Fallbacks**: Robust error handling with multiple recovery paths

### 🛠 Cross-Platform Support
- **Unified Scripts**: Identical functionality across Windows (.bat) and Unix (.sh)
- **Auto-Detection**: OS detection and platform-specific optimizations
- **Dependency Validation**: Automatic checking of Python, Ollama, and other requirements
- **Comprehensive Logging**: Structured logs for debugging and monitoring

### 🌟 Federation Capabilities
- **Multi-Agent Coordination**: Council, IDHHC, and Companion agents working together
- **Persistent Memory**: Conversation history and context retention
- **Model Collaboration**: Cross-model communication and shared insights
- **Efficiency Optimization**: Smart resource allocation and performance tuning

## 📁 Project Structure

```
Djinn-Constellation-Hub/
├── validators/                 # Input validation system
│   └── input_validator.py     # Schema validation and sanitization
├── djinn-federation/          # Core federation system
│   └── launcher/             # Constellation hub launchers
├── logs/                     # Comprehensive logging
│   ├── input_validation.log  # Validation events
│   ├── federation_audit.log  # Trust and security events
│   └── setup.log            # Installation and setup logs
├── memory_bank/              # Persistent memory storage
│   ├── constellation_memory/ # Conversation and state data
│   └── quarantine/          # Corrupted data storage
├── trust_registry.json       # Agent trust and membership registry
├── setup_djinn_federation.bat/.sh  # Cross-platform setup
└── launch_djinn_constellation_hub.bat/.sh  # Cross-platform launch
```

## 🔧 CLI Commands

### System Status
```bash
python djinn_cli.py status          # System health and capabilities
python djinn_cli.py models          # List available models
python djinn_cli.py performance     # Performance metrics
```

### Trust Management
```bash
python djinn_cli.py --agents        # List all agents with trust status
python djinn_cli.py --trust-score <agent>  # Check agent trust score
python djinn_cli.py --verify <agent>       # Manual trust verification
```

### Memory Management
```bash
python djinn_cli.py --memory-status # Memory bank status and statistics
python djinn_cli.py --memory-repair # Attempt to repair quarantined data
```

## 🛡️ Security Features

### Input Validation
- **Schema Validation**: All configs, preferences, and responses validated
- **Sanitization**: Dangerous characters and patterns removed
- **Length Limits**: Input size restrictions to prevent attacks
- **Trust Scoring**: Model responses evaluated for suspicious content

### Trust Enforcement
- **Agent Verification**: Every agent invocation checked against trust registry
- **Federation Membership**: Only federation members can participate
- **Audit Trail**: All trust events logged with timestamps and context
- **Quarantine System**: Invalid or corrupted data isolated for analysis

### Error Handling
- **Graceful Degradation**: System continues operating even with validation failures
- **Fallback Mechanisms**: Multiple recovery paths for different failure types
- **Structured Logging**: Comprehensive error reporting and debugging
- **Timeout Protection**: Prevents hanging operations

## 📊 Monitoring & Logs

### Log Files
- `logs/input_validation.log` - All validation events and failures
- `logs/federation_audit.log` - Trust checks, violations, and agent activity
- `logs/setup.log` - Installation and configuration events
- `logs/memory.log` - Memory operations and corruption events

### Health Monitoring
- Real-time system capability assessment
- Model performance tracking
- Resource usage monitoring
- Trust score tracking and trends

## 🤝 Contributing

This is a secure, trust-driven system. All contributions must:
1. Pass input validation tests
2. Maintain trust enforcement protocols
3. Include appropriate logging
4. Follow the established security patterns

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🜂 About

The Djinn Constellation Hub represents a new paradigm in federated AI systems - one where trust, security, and validation are foundational principles. Every interaction is verified, every agent is authenticated, and every operation is logged.

---

**🜂 The constellation stands fortified and ready to serve. 🜂** 