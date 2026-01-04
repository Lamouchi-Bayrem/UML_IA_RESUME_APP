import unittest
from utils.ai_providers import FreeUMLGenerator, OfflineProvider
from config import Config

class TestAIProviders(unittest.TestCase):
    def setUp(self):
        self.generator = FreeUMLGenerator(provider="offline")
        self.test_prompt = "Create a User class with name and email attributes"
    
    def test_offline_provider(self):
        """Test offline provider UML generation."""
        result = self.generator.generate_uml(self.test_prompt)
        self.assertIsInstance(result, str, "Offline provider should return a string")
        self.assertIn("classDiagram", result, "Result should contain classDiagram declaration")
        self.assertIn("User", result, "Result should contain User class")
    
    def test_provider_switching(self):
        """Test switching between providers."""
        self.generator.current_provider = "offline"
        offline_result = self.generator.generate_uml(self.test_prompt)
        self.assertTrue(len(offline_result) > 0, "Offline provider should generate non-empty UML")

if __name__ == "__main__":
    unittest.main()