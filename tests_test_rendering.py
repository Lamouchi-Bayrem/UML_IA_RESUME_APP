import unittest
from utils.mermaid_renderer import MermaidRenderer
from examples.sample_diagrams import SAMPLE_MERMAID_CODES

class TestMermaidRendering(unittest.TestCase):
    def setUp(self):
        self.renderer = MermaidRenderer()
        self.test_code = SAMPLE_MERMAID_CODES["user_profile"]
    
    def test_native_rendering(self):
        """Test native Mermaid rendering."""
        try:
            import streamlit_mermaid
            result = self.renderer.render_native(self.test_code)
            self.assertTrue(result, "Native rendering should succeed with streamlit-mermaid")
        except ImportError:
            result = self.renderer.render_native(self.test_code)
            self.assertFalse(result, "Native rendering should fail without streamlit-mermaid")
    
    def test_html_rendering(self):
        """Test HTML component rendering."""
        try:
            self.renderer.render_html_component(self.test_code)
            self.assertTrue(True, "HTML rendering should execute without errors")
        except Exception as e:
            self.fail(f"HTML rendering failed: {e}")

if __name__ == "__main__":
    unittest.main()