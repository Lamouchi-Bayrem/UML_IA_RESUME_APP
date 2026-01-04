# 🛠️ Complete Setup Guide

## 📦 Installation

### Method 1: Quick Setup
```bash
git clone <your-repo>
cd free-ai-uml-generator
pip install -r requirements.txt
python run.py
```

### Method 2: Manual Setup
```bash
pip install streamlit streamlit-mermaid requests python-dotenv
streamlit run app.py
```

## 🔑 API Keys Setup

### Hugging Face (Optional but Recommended)
1. Visit [huggingface.co](https://huggingface.co)
2. Create free account
3. Go to Settings → Access Tokens
4. Create token with "Read" permissions
5. Add to `.env` file or enter in app sidebar

### Groq (Fast & Reliable)
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up with GitHub/Google
3. Create API key (free tier: 100 requests/minute)
4. Add to `.env` file or enter in app sidebar

### Ollama (Private & Unlimited)
1. Install from [ollama.ai](https://ollama.ai)
2. Run: `ollama pull codellama:7b`
3. Start: `ollama serve`
4. No API key needed!

## 🧪 Testing

```bash
# Test the app
python tests/test_rendering.py

# Run debug tool
streamlit run tests/debug_tool.py
```

## 🔧 Configuration

Edit `config.py` or create `.env` file:
```env
HUGGINGFACE_TOKEN=your_token
GROQ_API_KEY=your_key
DEBUG=true
```