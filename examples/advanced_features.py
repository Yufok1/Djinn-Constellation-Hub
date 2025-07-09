# Advanced Features Example

from constellation_hub import ConstellationHub

if __name__ == '__main__':
    hub = ConstellationHub()
    # Simulate a multi-domain query
    query = 'Write a python script that analyzes the ethical implications of facial recognition.'
    best_agent, confidence, scores = hub.analyze_query_intent(query)
    print(f'Best agent: {best_agent} (confidence: {confidence:.2f})')
    # Show analytics
    print('Analytics:', hub.get_performance_metrics())
