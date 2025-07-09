# Basic Usage Example for Djinn Constellation Hub

from constellation_hub import ConstellationHub

if __name__ == '__main__':
    hub = ConstellationHub()
    hub.display_menu()
    user_input = input('Enter your query: ')
    # This simulates a basic routing
    best_agent, confidence, _ = hub.analyze_query_intent(user_input)
    print(f'Best agent: {best_agent} (confidence: {confidence:.2f})')
