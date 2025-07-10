#!/usr/bin/env python3
"""
Unit tests for The Steward MaintainerAgent
Tests all maintenance commands and CLI integration
"""

import unittest
import sys
import os
import subprocess
import tempfile
import json
from unittest.mock import patch, MagicMock

# Add the steward-agent to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'steward-agent'))

from maintainer_agent import MaintainerAgent

class TestMaintainerAgent(unittest.TestCase):
    """Test suite for MaintainerAgent functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = MaintainerAgent()
        self.test_log_file = "logs/maintainer_tests.log"
        
        # Ensure logs directory exists
        os.makedirs("logs", exist_ok=True)
        
    def test_agent_initialization(self):
        """Test that MaintainerAgent initializes correctly"""
        self.assertEqual(self.agent.name, "The Steward")
        self.assertEqual(self.agent.role, "Federation Maintainer")
        self.assertIn("check-deps", self.agent.commands)
        self.assertIn("run-tests", self.agent.commands)
        self.assertIn("monitor", self.agent.commands)
        self.assertIn("report", self.agent.commands)
    
    def test_check_deps(self):
        """Test dependency checking functionality"""
        with patch('builtins.print') as mock_print:
            self.agent.check_deps()
            mock_print.assert_called_with("[Steward] Checking dependencies...")
    
    def test_run_tests(self):
        """Test test running functionality"""
        with patch('builtins.print') as mock_print:
            self.agent.run_tests()
            mock_print.assert_called_with("[Steward] Running tests...")
    
    def test_monitor(self):
        """Test system monitoring functionality"""
        with patch('builtins.print') as mock_print:
            self.agent.monitor()
            mock_print.assert_called_with("[Steward] Monitoring system health...")
    
    def test_report(self):
        """Test report generation functionality"""
        with patch('builtins.print') as mock_print:
            self.agent.report()
            mock_print.assert_called_with("[Steward] Generating maintenance report...")
    
    def test_receive_instruction_valid_commands(self):
        """Test that valid commands are processed correctly"""
        commands = ["check-deps", "run-tests", "monitor", "report"]
        
        for command in commands:
            with patch('builtins.print') as mock_print:
                self.agent.receive_instruction(command)
                mock_print.assert_called_with(f"[Steward] {command.replace('-', ' ').title()}...")
    
    def test_receive_instruction_invalid_command(self):
        """Test that invalid commands are handled gracefully"""
        with patch('builtins.print') as mock_print:
            self.agent.receive_instruction("invalid-command")
            mock_print.assert_called_with("Unknown command: invalid-command")
    
    def test_receive_instruction_with_args(self):
        """Test that commands with arguments are handled correctly"""
        with patch('builtins.print') as mock_print:
            self.agent.receive_instruction("check-deps", ["--verbose", "--force"])
            mock_print.assert_called_with("[Steward] Checking dependencies...")

class TestMaintainerCLIIntegration(unittest.TestCase):
    """Test CLI integration for The Steward"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.cli_script = os.path.join(os.path.dirname(__file__), '..', 'djinn_cli.py')
        
    def test_cli_steward_check_deps(self):
        """Test CLI --steward check-deps command"""
        try:
            result = subprocess.run(
                [sys.executable, self.cli_script, "--steward", "check-deps"],
                capture_output=True,
                text=True,
                timeout=10
            )
            # Should not crash and should contain Steward output
            self.assertIn("Steward", result.stdout)
        except subprocess.TimeoutExpired:
            self.fail("CLI command timed out")
    
    def test_cli_steward_run_tests(self):
        """Test CLI --steward run-tests command"""
        try:
            result = subprocess.run(
                [sys.executable, self.cli_script, "--steward", "run-tests"],
                capture_output=True,
                text=True,
                timeout=10
            )
            self.assertIn("Steward", result.stdout)
        except subprocess.TimeoutExpired:
            self.fail("CLI command timed out")
    
    def test_cli_steward_monitor(self):
        """Test CLI --steward monitor command"""
        try:
            result = subprocess.run(
                [sys.executable, self.cli_script, "--steward", "monitor"],
                capture_output=True,
                text=True,
                timeout=10
            )
            self.assertIn("Steward", result.stdout)
        except subprocess.TimeoutExpired:
            self.fail("CLI command timed out")
    
    def test_cli_steward_report(self):
        """Test CLI --steward report command"""
        try:
            result = subprocess.run(
                [sys.executable, self.cli_script, "--steward", "report"],
                capture_output=True,
                text=True,
                timeout=10
            )
            self.assertIn("Steward", result.stdout)
        except subprocess.TimeoutExpired:
            self.fail("CLI command timed out")
    
    def test_cli_agents_command(self):
        """Test CLI --agents command"""
        try:
            result = subprocess.run(
                [sys.executable, self.cli_script, "--agents"],
                capture_output=True,
                text=True,
                timeout=10
            )
            self.assertIn("Federation Agents", result.stdout)
        except subprocess.TimeoutExpired:
            self.fail("CLI command timed out")
    
    def test_cli_trust_score_steward(self):
        """Test CLI --trust-score steward command"""
        try:
            result = subprocess.run(
                [sys.executable, self.cli_script, "--trust-score", "steward"],
                capture_output=True,
                text=True,
                timeout=10
            )
            self.assertIn("steward", result.stdout.lower())
        except subprocess.TimeoutExpired:
            self.fail("CLI command timed out")

class TestMaintainerTrustRegistry(unittest.TestCase):
    """Test trust registry integration"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.trust_registry_path = os.path.join(os.path.dirname(__file__), '..', 'trust_registry.json')
        
    def test_trust_registry_exists(self):
        """Test that trust registry file exists"""
        self.assertTrue(os.path.exists(self.trust_registry_path))
    
    def test_trust_registry_structure(self):
        """Test that trust registry has correct structure"""
        with open(self.trust_registry_path, 'r') as f:
            registry = json.load(f)
        
        self.assertIn("steward", registry)
        steward_data = registry["steward"]
        
        self.assertIn("trusted", steward_data)
        self.assertIn("federation_member", steward_data)
        self.assertIn("trust_score", steward_data)
        self.assertIn("role", steward_data)
        
        self.assertTrue(steward_data["trusted"])
        self.assertTrue(steward_data["federation_member"])
        self.assertEqual(steward_data["role"], "maintainer")

def run_maintainer_tests():
    """Run all maintainer tests and log results"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestMaintainerAgent))
    test_suite.addTest(unittest.makeSuite(TestMaintainerCLIIntegration))
    test_suite.addTest(unittest.makeSuite(TestMaintainerTrustRegistry))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Log results
    with open("logs/maintainer_tests.log", "w") as f:
        f.write(f"Maintainer Tests Run: {result.testsRun}\n")
        f.write(f"Failures: {len(result.failures)}\n")
        f.write(f"Errors: {len(result.errors)}\n")
        
        if result.failures:
            f.write("\nFailures:\n")
            for test, traceback in result.failures:
                f.write(f"{test}: {traceback}\n")
        
        if result.errors:
            f.write("\nErrors:\n")
            for test, traceback in result.errors:
                f.write(f"{test}: {traceback}\n")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_maintainer_tests()
    sys.exit(0 if success else 1) 