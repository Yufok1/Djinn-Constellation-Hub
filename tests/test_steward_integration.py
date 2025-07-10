#!/usr/bin/env python3
"""
Integration tests for The Steward in Djinn Constellation Hub
Tests routing, trust enforcement, and federation integration
"""

import unittest
import sys
import os
import json
import tempfile
from unittest.mock import patch, MagicMock

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestStewardIntegration(unittest.TestCase):
    """Test suite for The Steward integration"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_trust_registry = {
            "steward": {
                "trusted": True,
                "federation_member": True,
                "trust_score": 95,
                "role": "maintainer",
                "last_verified": "2024-01-01T00:00:00Z"
            }
        }
        
        # Create temporary trust registry
        self.temp_dir = tempfile.mkdtemp()
        self.trust_file = os.path.join(self.temp_dir, 'trust_registry.json')
        with open(self.trust_file, 'w') as f:
            json.dump(self.test_trust_registry, f)
    
    def tearDown(self):
        """Clean up test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_maintenance_task_detection(self):
        """Test that maintenance tasks are correctly identified"""
        from djinn_federation.launcher.constellation_hub import ConstellationHub
        
        hub = ConstellationHub()
        
        # Test maintenance keywords
        maintenance_queries = [
            "check system health",
            "run maintenance report",
            "monitor dependencies",
            "audit system security",
            "backup data",
            "optimize performance",
            "install updates",
            "validate configuration"
        ]
        
        for query in maintenance_queries:
            self.assertTrue(hub.is_maintenance_task(query), f"Failed to detect maintenance task: {query}")
        
        # Test non-maintenance queries
        non_maintenance_queries = [
            "hello world",
            "explain quantum physics",
            "write a poem",
            "what is the weather",
            "help me code"
        ]
        
        for query in non_maintenance_queries:
            self.assertFalse(hub.is_maintenance_task(query), f"Incorrectly detected maintenance task: {query}")
    
    def test_steward_trust_check(self):
        """Test steward trust status checking"""
        from djinn_federation.launcher.constellation_hub import ConstellationHub
        
        hub = ConstellationHub()
        
        # Mock the trust registry path
        with patch.object(hub, 'check_steward_trust') as mock_check:
            mock_check.return_value = {
                'trusted': True,
                'trust_score': 95,
                'last_verified': '2024-01-01T00:00:00Z'
            }
            
            trust_status = hub.check_steward_trust()
            
            self.assertTrue(trust_status['trusted'])
            self.assertEqual(trust_status['trust_score'], 95)
            self.assertIn('2024-01-01', trust_status['last_verified'])
    
    def test_unauthorized_maintenance_logging(self):
        """Test that unauthorized maintenance attempts are logged"""
        from djinn_federation.launcher.constellation_hub import ConstellationHub
        
        hub = ConstellationHub()
        
        test_query = "check system health"
        
        # Mock the trust check to return untrusted
        with patch.object(hub, 'check_steward_trust') as mock_check:
            mock_check.return_value = {
                'trusted': False,
                'trust_score': 0,
                'last_verified': 'Never'
            }
            
            # Mock the logging method
            with patch.object(hub, 'log_unauthorized_maintenance_attempt') as mock_log:
                response = hub.route_to_steward(test_query)
                
                # Verify unauthorized attempt was logged
                mock_log.assert_called_once_with(test_query, "unknown")
                
                # Verify access denied response
                self.assertIn("ACCESS DENIED", response)
                self.assertIn("not trusted", response)
    
    def test_authorized_maintenance_routing(self):
        """Test that authorized maintenance tasks are routed to steward"""
        from djinn_federation.launcher.constellation_hub import ConstellationHub
        
        hub = ConstellationHub()
        
        test_query = "check system health"
        
        # Mock the trust check to return trusted
        with patch.object(hub, 'check_steward_trust') as mock_check:
            mock_check.return_value = {
                'trusted': True,
                'trust_score': 95,
                'last_verified': '2024-01-01T00:00:00Z'
            }
            
            # Mock the summon_agent method
            with patch.object(hub, 'summon_agent') as mock_summon:
                mock_summon.return_value = "Steward response"
                
                response = hub.route_to_steward(test_query)
                
                # Verify steward was summoned
                mock_summon.assert_called_once_with('steward', test_query)
                
                # Verify response contains steward output
                self.assertIn("Steward response", response)
    
    def test_query_type_classification(self):
        """Test that maintenance queries are correctly classified"""
        from djinn_federation.launcher.constellation_hub import ConstellationHub
        
        hub = ConstellationHub()
        
        # Test maintenance classification
        maintenance_queries = [
            "check system health",
            "run maintenance",
            "monitor system"
        ]
        
        for query in maintenance_queries:
            query_type = hub.classify_query_type(query)
            self.assertEqual(query_type, 'maintenance', f"Failed to classify as maintenance: {query}")
        
        # Test other classifications
        self.assertEqual(hub.classify_query_type("write code"), 'coding')
        self.assertEqual(hub.classify_query_type("ethical guidance"), 'ethics')
        self.assertEqual(hub.classify_query_type("hello world"), 'general')
    
    def test_agent_keywords_inclusion(self):
        """Test that steward keywords are included in agent_keywords"""
        from djinn_federation.launcher.constellation_hub import ConstellationHub
        
        hub = ConstellationHub()
        
        # Verify steward keywords exist
        self.assertIn('steward', hub.agent_keywords)
        
        steward_keywords = hub.agent_keywords['steward']
        expected_keywords = ['maintain', 'system', 'health', 'check', 'monitor', 'report']
        
        for keyword in expected_keywords:
            self.assertIn(keyword, steward_keywords, f"Missing steward keyword: {keyword}")
    
    def test_performance_metrics_inclusion(self):
        """Test that steward is included in performance metrics"""
        from djinn_federation.launcher.constellation_hub import ConstellationHub
        
        hub = ConstellationHub()
        
        # Mock conversation history with steward usage
        hub.conversation_history = [
            {
                'agent': 'The Steward',
                'user_input': 'check system health',
                'response': 'System healthy',
                'timestamp': '2024-01-01 00:00:00',
                'final_agent': 'The Steward'
            }
        ]
        
        metrics = hub.get_performance_metrics()
        
        # Verify steward is included in agent preference counts
        self.assertIn('steward', metrics['agent_pref_counts'])
        self.assertGreaterEqual(metrics['agent_pref_counts']['steward'], 0)
        
        # Verify maintenance is included in type preference counts
        self.assertIn('maintenance', metrics['type_pref_counts'])

def run_integration_tests():
    """Run all integration tests and log results"""
    import logging
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/steward_integration_tests.log'),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info("Starting Steward Integration Tests")
    
    # Run tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStewardIntegration)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Log results
    logger.info(f"Tests run: {result.testsRun}")
    logger.info(f"Failures: {len(result.failures)}")
    logger.info(f"Errors: {len(result.errors)}")
    
    if result.failures:
        logger.error("Test failures:")
        for test, traceback in result.failures:
            logger.error(f"  {test}: {traceback}")
    
    if result.errors:
        logger.error("Test errors:")
        for test, traceback in result.errors:
            logger.error(f"  {test}: {traceback}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_integration_tests()
    sys.exit(0 if success else 1) 