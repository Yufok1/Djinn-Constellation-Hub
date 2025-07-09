"""
🔬 IDHHC Toolkit Interface
Simple interface for accessing advanced toolkits
"""

from advanced_toolkits import toolkit_coordinator, initialize_idhhc_toolkits, analyze_with_idhhc_toolkits, get_toolkit_status

def main():
    """Main interface for IDHHC toolkit operations"""
    print("🔬 IDHHC Advanced Toolkits Interface")
    print("=" * 50)
    
    # Initialize toolkits
    print(initialize_idhhc_toolkits())
    print()
    
    # Show status
    print(get_toolkit_status())
    print()
    
    # Example usage
    test_data = "IDHHC autonomous coding system"
    print("Testing toolkit analysis with sample data...")
    print(analyze_with_idhhc_toolkits(test_data))

if __name__ == "__main__":
    main() 