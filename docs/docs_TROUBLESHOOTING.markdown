# 🛠️ Troubleshooting Guide

## Common Issues & Solutions

### 1. Diagrams Not Rendering
- **Symptoms**: Blank space where diagram should be
- **Solutions**:
  - Install `streamlit-mermaid`: `pip install streamlit-mermaid`
  - Check browser console for JavaScript errors
  - Try switching to image fallback in sidebar
  - Verify Mermaid CDN is accessible

### 2. API Connection Errors
- **Symptoms**: "API request failed" or timeout errors
- **Solutions**:
  - Verify API keys in `.env` or sidebar
  - Check internet connection
  - Switch to offline mode
  - For Hugging Face: Ensure token has "Read" permissions
  - For Groq: Verify rate limits (100 requests/minute for free tier)

### 3. Invalid Mermaid Syntax
- **Symptoms**: Error message about invalid syntax
- **Solutions**:
  - Enable debug mode to see raw Mermaid code
  - Check if code starts with `classDiagram`
  - Verify class definitions and relationships
  - Use sample diagrams as reference
  - Test code in Mermaid Live Editor

### 4. Slow Generation
- **Symptoms**: Long wait times for diagram generation
- **Solutions**:
  - Switch to offline mode for faster processing
  - Reduce prompt complexity
  - Check API provider status (Hugging Face/Groq)
  - Clear browser cache

### 5. Dependency Issues
- **Symptoms**: Import errors or missing modules
- **Solutions**:
  - Run `pip install -r requirements.txt`
  - Verify Python version (3.8+ recommended)
  - Check for conflicting package versions
  - Create fresh virtual environment

## 🧪 Debug Tool
Run the debug tool to test rendering:
```bash
streamlit run tests/debug_tool.py
```

## 📬 Getting Help
- Check the [README.md](README.md) for basic setup
- Review [SETUP.md](SETUP.md) for detailed installation
- Post issues on the GitHub repository
- Try Mermaid Live Editor as a backup: [mermaid-js.github.io](https://mermaid-js.github.io/mermaid-live-editor)