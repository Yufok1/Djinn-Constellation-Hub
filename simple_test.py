#!/usr/bin/env python3
"""
Simple test to debug the method issue
"""

import sys
import os

# Add the launcher directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'djinn-federation', 'launcher'))

try:
    from constellation_hub import ConstellationHub
    
    print("✅ Successfully imported ConstellationHub")
    
    hub = ConstellationHub()
    print("✅ Successfully created hub instance")
    
    # Check if method exists
    if hasattr(hub, 'analyze_task_complexity'):
        print("✅ analyze_task_complexity method exists")
        
        # Test the method
        result = hub.analyze_task_complexity("hi")
        print(f"✅ Method works! Result: {result}")
    else:
        print("❌ analyze_task_complexity method NOT found")
        print("Available methods:")
        for method in dir(hub):
            if not method.startswith('_'):
                print(f"  - {method}")
                
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc() 