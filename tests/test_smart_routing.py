from constellation_hub import ConstellationHub

def test_smart_routing_basic():
    hub = ConstellationHub()
    best_agent, confidence, scores = hub.analyze_query_intent('Write python code to reverse a string')
    assert best_agent in ['council', 'idhhc', 'companion']
    assert isinstance(confidence, float)
    assert isinstance(scores, dict)
