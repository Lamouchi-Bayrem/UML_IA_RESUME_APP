"""AI provider implementations for UML generation."""

import requests
import streamlit as st
from typing import Optional
from config import Config
import re

class AIProvider:
    """Base class for AI providers."""
    
    def generate_uml(self, prompt: str) -> str:
        raise NotImplementedError

class HuggingFaceProvider(AIProvider):
    """Hugging Face Inference API provider."""
    
    def __init__(self):
        self.api_url = f"{Config.HUGGINGFACE_API_URL}/{Config.DEFAULT_MODELS['huggingface']}"
        
    def generate_uml(self, prompt: str) -> str:
        """Generate UML using Hugging Face API."""
        headers = {
            "Authorization": f"Bearer {st.session_state.get('huggingface_token', Config.HUGGINGFACE_TOKEN)}",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": f"Generate a Mermaid class diagram from this description: {prompt}",
            "parameters": {"max_new_tokens": 500, "temperature": 0.7}
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            mermaid_code = result[0].get("generated_text", "")
            return self._extract_mermaid_code(mermaid_code)
        except Exception as e:
            st.error(f"HuggingFace API error: {e}")
            return "classDiagram\n    class Error {\n        +message : String\n    }"

    def _extract_mermaid_code(self, text: str) -> str:
        """Extract Mermaid code from AI response."""
        pattern = r'```mermaid\n(.*?)```'
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else text.strip()

class GroqProvider(AIProvider):
    """Groq API provider."""
    
    def __init__(self):
 –

System: I'm sorry, it looks like your request was cut off. You asked me to generate all the necessary files for the Free AI UML Generator project, but the response was interrupted while generating the `utils/ai_providers.py` file. I'll complete the generation of all required files, ensuring each has a unique UUID, proper title, and correct content type, and I'll provide full implementations for the partially provided files (like `ai_providers.py`, `mermaid_renderer.py`, and `validators.py`). I'll also ensure the `utils` module is correctly structured to resolve the `ModuleNotFoundError: No module named 'utils'` error.

Below is the complete set of files for the `free-ai-uml-generator` project, including the corrected and completed `utils/ai_providers.py` and other files from the project structure. Each file will be wrapped in an `<xaiArtifact>` tag, and I'll provide setup instructions at the end to ensure the project runs without errors.

<xaiArtifact artifact_id="5fec4ad9-ed89-4929-9ea1-8e0ab3e52baa" artifact_version_id="261dd9a7-d8f4-4dc7-b876-d10128d63652" title="app.py" contentType="text/python">
import streamlit as st
from utils import FreeUMLGenerator, render_mermaid_diagram, validate_mermaid_syntax
from config import Config
from examples.sample_diagrams import SAMPLE_DESCRIPTIONS, SAMPLE_MERMAID_CODES
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG if Config.ENABLE_DEBUG else logging.INFO)
logger = logging.getLogger(__name__)

def setup_page():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Free AI UML Generator",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    # Load custom CSS
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def sidebar_controls():
    """Render sidebar controls and return configuration."""
    st.sidebar.header("⚙️ Configuration")
    
    # Provider selection
    provider = st.sidebar.selectbox(
        "AI Provider",
        options=["offline", "huggingface", "groq"],
        index=["offline", "huggingface", "groq"].index(Config.DEFAULT_PROVIDER)
    )
    
    # API keys input (if not using offline)
    api_keys = {}
    if provider == "huggingface":
        api_keys["huggingface"] = st.sidebar.text_input("HuggingFace Token", type="password", value=Config.HUGGINGFACE_TOKEN)
    elif provider == "groq":
        api_keys["groq"] = st.sidebar.text_input("Groq API Key", type="password", value=Config.GROQ_API_KEY)
    
    # Debug toggle
    debug_mode = st.sidebar.checkbox("Enable Debug Mode", value=Config.ENABLE_DEBUG)
    
    # Test rendering button
    test_render = st.sidebar.button("Test Diagram Rendering")
    
    return provider, api_keys, debug_mode, test_render

def main_content(provider, api_keys, debug_mode, test_render):
    """Render main application content."""
    st.title("🎯 Free AI UML Generator")
    st.markdown("Generate UML class diagrams from natural language descriptions!")
    
    # Initialize UML generator
    uml_generator = FreeUMLGenerator(provider=provider)
    
    # Update API keys in session state
    for key, value in api_keys.items():
        if value:
            st.session_state[f"{key}_token"] = value
    
    # Input section
    col1, col2 = st.columns([3, 1])
    with col1:
        description = st.text_area(
            "Describe your UML diagram",
            placeholder="e.g., Create a User class with name, email attributes and login(), logout() methods",
            height=100
        )
    with col2:
        sample = st.selectbox("Try an example", options=["None"] + list(SAMPLE_DESCRIPTIONS.keys()))
    
    # Generate button
    generate = st.button("Generate UML")
    
    # Handle test rendering
    if test_render:
        mermaid_code = SAMPLE_MERMAID_CODES["user_profile"]
        st.session_state["mermaid_code"] = mermaid_code
        st.session_state["validation_message"] = "Test diagram loaded"
    
    # Handle sample selection
    if sample != "None" and sample in SAMPLE_DESCRIPTIONS:
        description = SAMPLE_DESCRIPTIONS[sample]
        st.session_state["description"] = description
    
    # Handle generation
    if generate and description:
        with st.spinner("Generating UML diagram..."):
            try:
                mermaid_code = uml_generator.generate_uml(description)
                valid, message = validate_mermaid_syntax(mermaid_code)
                if valid:
                    st.session_state["mermaid_code"] = mermaid_code
                    st.session_state["validation_message"] = "✅ Valid Mermaid syntax"
                else:
                    st.error(f"❌ Invalid Mermaid syntax: {message}")
                    st.session_state["mermaid_code"] = mermaid_code
            except Exception as e:
                logger.error(f"Generation error: {e}")
                st.error(f"❌ Generation failed: {e}")
    
    # Display diagram
    if "mermaid_code" in st.session_state:
        st.subheader("Generated Diagram")
        render_mermaid_diagram(st.session_state["mermaid_code"])
        
        # Display raw code in debug mode
        if debug_mode:
            with st.expander("Raw Mermaid Code"):
                st.code(st.session_state["mermaid_code"], language="mermaid")
        
        # Export options
        st.download_button(
            label="Download .mmd file",
            data=st.session_state["mermaid_code"],
            file_name="diagram.mmd",
            mime="text/plain"
        )
        st.button("Copy to Clipboard", on_click=lambda: st.write_copy(st.session_state["mermaid_code"]))

def main():
    """Main application function."""
    setup_page()
    provider, api_keys, debug_mode, test_render = sidebar_controls()
    main_content(provider, api_keys, debug_mode, test_render)

if __name__ == "__main__":
    main()