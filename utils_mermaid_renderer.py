"""Mermaid diagram rendering utilities."""

import streamlit as st
import streamlit.components.v1 as components
from config import Config
import urllib.parse

class MermaidRenderer:
    """Enhanced Mermaid diagram renderer."""
    
    @staticmethod
    def render_native(mermaid_code: str, height: int = 600):
        """Render using streamlit-mermaid if available."""
        try:
            import streamlit_mermaid as stmermaid
            stmermaid.st_mermaid(mermaid_code, height=height)
            return True
        except ImportError:
            return False
    
    @staticmethod
    def render_html_component(mermaid_code: str, height: int = 700):
        """Render using HTML component with enhanced error handling."""
        try:
            with open("assets/mermaid_template.html") as f:
                template = f.read()
            html_content = template.replace("{{MERMAID_CODE}}", mermaid_code).replace("{{MERMAID_THEME}}", Config.MERMAID_THEME)
            components.html(html_content, height=height, scrolling=True)
        except Exception as e:
            st.error(f"HTML rendering error: {e}")
            raise
    
    @staticmethod
    def render_image_service(mermaid_code: str):
        """Render using mermaid.ink image service."""
        try:
            encoded_code = urllib.parse.quote(mermaid_code)
            mermaid_url = f"https://mermaid.ink/img/{encoded_code}"
            st.image(mermaid_url, caption="Generated UML Diagram")
        except Exception as e:
            st.error(f"Image service rendering error: {e}")
            raise

def render_mermaid_diagram(mermaid_code: str):
    """Main rendering function with multiple fallbacks."""
    renderer = MermaidRenderer()
    
    # Try streamlit-mermaid first
    if renderer.render_native(mermaid_code):
        st.success("✅ Rendered with streamlit-mermaid")
        return
    
    # Fallback to HTML component
    try:
        renderer.render_html_component(mermaid_code)
        st.info(" Rendered with HTML component")
    except Exception as e:
        st.error(f" HTML rendering failed: {e}")
        
        # Final fallback: image service
        try:
            renderer.render_image_service(mermaid_code)
            st.warning("⚠️ Using image fallback")
        except Exception as e2:
            st.error(f"❌ All rendering methods failed: {e2}")
            st.code(mermaid_code, language="text")
