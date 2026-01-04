# Configuration settings for the UML Generator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration."""
    
    # AI Provider Settings
    HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models"
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    OLLAMA_API_URL = "http://localhost:11434/api/generate"
    
    # API Keys (from environment or session state)
    HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN', '')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
    
    # Model Settings
    DEFAULT_MODELS = {
        "huggingface": "HuggingFaceH4/zephyr-7b-beta",
        "groq": "llama3-8b-8192",
        "ollama": "codellama:7b"
    }
    
    # Mermaid Settings
    MERMAID_CDN = "https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.1/mermaid.min.js"
    MERMAID_THEME = "default"
    
    # App Settings
    MAX_DIAGRAM_HEIGHT = 700
    DEFAULT_PROVIDER = "offline"
    ENABLE_DEBUG = True