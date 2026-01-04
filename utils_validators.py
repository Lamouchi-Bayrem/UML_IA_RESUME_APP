"""Mermaid code validation and cleaning utilities."""

import re
from typing import Tuple

def validate_mermaid_syntax(mermaid_code: str) -> Tuple[bool, str]:
    """Validate Mermaid class diagram syntax."""
    if not mermaid_code.strip():
        return False, "Empty Mermaid code"
    
    clean_code = mermaid_code.strip().lower()
    
    if not clean_code.startswith('classdiagram'):
        return False, "Must start with 'classDiagram'"
    
    if 'class' not in clean_code:
        return False, "No class definitions found"
    
    # Check for valid class syntax
    if not re.search(r'class\s+\w+\s*{', clean_code):
        return False, "Invalid class definition syntax"
    
    return True, "Valid syntax"

def clean_mermaid_syntax(mermaid_code: str) -> str:
    """Clean and fix common Mermaid syntax issues."""
    try:
        # Remove extra whitespace and newlines
        cleaned = "\n".join(line.strip() for line in mermaid_code.splitlines() if line.strip())
        
        # Ensure classDiagram directive
        if not cleaned.startswith("classDiagram"):
            cleaned = "classDiagram\n" + cleaned
        
        # Fix common syntax issues
        cleaned = re.sub(r'\s*;\s*', '', cleaned)  # Remove semicolons
        cleaned = re.sub(r'\s*}\s*{', '}\n{', cleaned)  # Ensure proper class separation
        
        # Validate and return
        valid, _ = validate_mermaid_syntax(cleaned)
        return cleaned if valid else "classDiagram\n    class Error {\n        +message : String\n    }"
    except Exception:
        return "classDiagram\n    class Error {\n        +message : String\n    }"

def extract_mermaid_code(text: str) -> str:
    """Extract Mermaid code from AI response."""
    pattern = r'```mermaid\n(.*?)```'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Fallback: try to clean raw text
    return clean_mermaid_syntax(text.strip())