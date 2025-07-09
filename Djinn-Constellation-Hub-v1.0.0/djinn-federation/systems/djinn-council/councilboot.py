import threading
import uuid
import json
import queue

# === Sovereign Agent Shell ===
class SovereignAgent(threading.Thread):
    def __init__(self, agent_id, registry, command_channel):
        super().__init__()
        self.agent_id = agent_id
        self.uuid = str(uuid.uuid4())
        self.role = "UNASSIGNED"
        self.registry = registry
        self.command_channel = command_channel
        self.active = True

    def run(self):
        self.registry.register(self.agent_id, self.uuid)
        while self.active:
            try:
                command = self.command_channel.get(timeout=0.5)
                if command['type'] == 'ASSIGN' and command['agent'] == self.agent_id:
                    self.role = command['role']
                    self.registry.confirm_role(self.agent_id, self.role)
                if command['type'] == 'SEAL':
                    self.seal_identity()
                    self.active = False
            except queue.Empty:
                continue

    def seal_identity(self):
        seal = self.registry.seal(self.agent_id)
        print(f"[{self.agent_id}] Sealed with hash: {seal}")

# === Sovereign Registry Controller ===
class SovereignRegistry:
    def __init__(self):
        self.agents = {}
        self.seals = {}

    def register(self, agent_id, agent_uuid):
        self.agents[agent_id] = {'uuid': agent_uuid, 'role': 'UNASSIGNED'}
        print(f"[REGISTRY] Registered {agent_id} with UUID {agent_uuid}")

    def confirm_role(self, agent_id, role):
        self.agents[agent_id]['role'] = role
        print(f"[REGISTRY] Role confirmed: {agent_id} -> {role}")

    def seal(self, agent_id):
        identity = json.dumps(self.agents[agent_id], sort_keys=True).encode()
        seal_hash = uuid.uuid5(uuid.NAMESPACE_OID, identity.hex()).hex
        self.seals[agent_id] = seal_hash
        return seal_hash

    def audit(self):
        assigned = all(agent['role'] != 'UNASSIGNED' for agent in self.agents.values())
        return assigned, self.agents

# === Sovereign Bootloader ===
class SovereignBootloader:
    def __init__(self):
        self.registry = SovereignRegistry()
        self.command_channel = queue.Queue()
        self.agents = {}

    def spawn_agents(self, agent_ids):
        for agent_id in agent_ids:
            agent = SovereignAgent(agent_id, self.registry, self.command_channel)
            agent.start()
            self.agents[agent_id] = agent

    def assign_roles(self, assignments):
        for agent_id, role in assignments.items():
            command = {'type': 'ASSIGN', 'agent': agent_id, 'role': role}
            self.command_channel.put(command)

    def seal_all(self):
        for _ in self.agents:
            self.command_channel.put({'type': 'SEAL'})

    def wait_for_completion(self):
        for agent in self.agents.values():
            agent.join()

    def audit_registry(self):
        return self.registry.audit()

# === Sovereign Deployment ===
if __name__ == "__main__":
    agent_ids = [
        "Djinn-A", "Djinn-B", "Djinn-C1", "Djinn-C2", "Djinn-C3",
        "Djinn-D1", "Djinn-D2", "Djinn-E", "Djinn-F"
    ]

    role_assignments = {
        "Djinn-A": "ComputeEngine",
        "Djinn-B": "RiskAuditor",
        "Djinn-C1": "PriceFeedAdapter",
        "Djinn-C2": "NewsFeedAdapter",
        "Djinn-C3": "VolatilityAdapter",
        "Djinn-D1": "StatisticalRegimeClassifier",
        "Djinn-D2": "MLRegimeClassifier",
        "Djinn-E": "OperatorConsole",
        "Djinn-F": "MetaAuditor"
    }

    bootloader = SovereignBootloader()
    bootloader.spawn_agents(agent_ids)
    bootloader.assign_roles(role_assignments)
    bootloader.seal_all()
    bootloader.wait_for_completion()

    assigned, registry_state = bootloader.audit_registry()
    if assigned:
        print("\n[SOVEREIGN] All agents lawfully assigned and sealed.")
    else:
        print("\n[SOVEREIGN] Role assignment incomplete!")

    print("\n[SOVEREIGN REGISTRY STATE]:")
    print(json.dumps(registry_state, indent=4))
