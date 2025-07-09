import pytest

def test_constellation_hub_import():
    import constellation_hub
    assert hasattr(constellation_hub, 'ConstellationHub')

def test_menu_display_runs():
    from constellation_hub import ConstellationHub
    hub = ConstellationHub()
    # Should not error
    hub.display_menu()
