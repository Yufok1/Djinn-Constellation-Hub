from constellation_hub import ConstellationHub

def test_preference_learning():
    hub = ConstellationHub()
    hub.user_preferences['coding'] = 'idhhc'
    hub.save_user_preferences()
    # Simulate a coding query
    query_type = hub.classify_query_type('Write a python function')
    assert hub.user_preferences.get(query_type) == 'idhhc'
