"""
🧠 Test IDHHC Kernel Integration
"""

from kernel_integration import connect_idhhc_to_kernel, get_kernel_bridge_status, perform_kernel_breath_analysis

def main():
    """Test kernel integration"""
    print("🧠 IDHHC Kernel Integration Test")
    print("=" * 50)
    
    # Connect to kernel
    print("Connecting to Djinn Sovereign Kernel v7.0...")
    result = connect_idhhc_to_kernel()
    print(result)
    print()
    
    # Show bridge status
    print(get_kernel_bridge_status())
    print()
    
    # Test breath analysis
    test_data = "IDHHC autonomous coding system with kernel integration"
    print("Testing breath analysis with kernel integration...")
    print(perform_kernel_breath_analysis(test_data))

if __name__ == "__main__":
    main() 