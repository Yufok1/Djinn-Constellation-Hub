# Example: Adding and Using a Custom Agent

# (Assume you have added your agent to constellation_hub.py)
from constellation_hub import ConstellationHub

if __name__ == '__main__':
    hub = ConstellationHub()
    # Simulate a query that should trigger your custom agent
    query = 'Use my custom agent for this special task.'
    best_agent, confidence, scores = hub.analyze_query_intent(query)
    print(f'Best agent: {best_agent} (confidence: {confidence:.2f})')
