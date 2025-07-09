# API Reference

## Core Endpoints & Classes

### ConstellationHub
- `run()` — Main loop, handles input and routing
- `summon_agent(agent, query)` — Calls a specific agent
- `federation_council(query)` — Parallel agent collaboration
- `get_performance_metrics()` — Analytics and stats

### Adding Agents
- Add agent definition in `constellation_hub.py`
- Add keywords for intent detection
- Register agent in the menu system

### Persistent Memory
- Preferences and history stored in `memory_bank/constellation_memory/`
