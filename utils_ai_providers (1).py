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
        self.api_url = Config.GROQ_API_URL
        
    def generate_uml(self, prompt: str) -> str:
        """Generate UML using Groq API."""
        headers = {
            "Authorization": f"Bearer {st.session_state.get('groq_token', Config.GROQ_API_KEY)}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": Config.DEFAULT_MODELS["groq"],
            "messages": [
                {"role": "system", "content": "You are a UML diagram generator. Return only valid Mermaid class diagram code wrapped in ```mermaid``` tags."},
                {"role": "user", "content": f"Generate a Mermaid class diagram from this description: {prompt}"}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            mermaid_code = result["choices"][0]["message"]["content"]
            return self._extract_mermaid_code(mermaid_code)
        except Exception as e:
            st.error(f"Groq API error: {e}")
            return "classDiagram\n    class Error {\n        +message : String\n    }"

    def _extract_mermaid_code(self, text: str) -> str:
        """Extract Mermaid code from AI response."""
        pattern = r'```mermaid\n(.*?)```'
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else text.strip()

class OfflineProvider(AIProvider):
    """Rule-based offline provider."""
    
    def generate_uml(self, prompt: str) -> str:
        """Generate UML using rule-based approach."""
        try:
            # Simple rule-based parsing for basic class diagrams
            mermaid_code = ["classDiagram"]
            classes = []
            relationships = []
            
            # Basic parsing for classes and attributes
            if "class" in prompt.lower():
                class_name = re.search(r'(\w+)\s+class', prompt, re.IGNORECASE)
                if class_name:
                    class_name = class_name.group(1)
                    classes.append(f"    class {class_name} {{")
                    
                    # Extract attributes
                    if "attributes" in prompt.lower():
                        attrs = re.findall(r'(\w+)\s*:\s*(\w+)', prompt, re.IGNORECASE)
                        for attr_name, attr_type in attrs:
                            classes.append(f"        +{attr_name} : {attr_type}")
                    
                    # Extract methods
                    if "methods" in prompt.lower():
                        methods = re.findall(r'(\w+)\s*\(\s*\)\s*(:?\s*\w+)?', prompt, re.IGNORECASE)
                        for method_name, return_type in methods:
                            return_type = return_type.strip() if return_type else "void"
                            classes.append(f"        +{method_name}() : {return_type}")
                    
                    classes.append("    }")
            
            # Extract inheritance
            if "inherit" in prompt.lower():
                matches = re.findall(r'(\w+)\s+(?:inherit|extends)\s+from\s+(\w+)', prompt, re.IGNORECASE)
                for child, parent in matches:
                    relationships.append(f"    {parent} <|-- {child}")
            
            mermaid_code.extend(classes)
            mermaid_code.extend(relationships)
            return "\n".join(mermaid_code) if classes else "classDiagram\n    class Error {\n        +message : String\n    }"
        except Exception as e:
            st.error(f"Offline generation error: {e}")
            return "classDiagram\n    class Error {\n        +message : String\n    }"

class FreeUMLGenerator:
    """Main UML generator class with multiple providers."""
    
    def __init__(self, provider="offline"):
        self.providers = {
            "huggingface": HuggingFaceProvider(),
            "groq": GroqProvider(),
            "offline": OfflineProvider()
        }
        self.current_provider = provider
    
    def generate_uml(self, prompt: str, provider: str = None) -> str:
        """Generate UML using specified provider."""
        provider = provider or self.current_provider
        
        if provider in self.providers:
            return self.providers[provider].generate_uml(prompt)
        else:
            return "classDiagram\n    class Error {\n        +message : String\n    }"