# 🎯 Free AI UML Generator

Generate beautiful UML class diagrams from natural language descriptions using free AI services!

## ✨ Features

- 🤖 **Multiple AI Providers**: Hugging Face, Groq, Ollama, Offline
- 🎨 **Interactive Diagrams**: Zoom, pan, and explore your UML diagrams
- 🔧 **Offline Mode**: Works without internet connection
- 💾 **Export Options**: Download as .mmd files or copy to clipboard
- 🛠️ **Debug Tools**: Built-in debugging and troubleshooting
- 📱 **Responsive Design**: Works on desktop and mobile

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch the app:**
   ```bash
   python run.py
   # OR
   streamlit run app.py
   ```

3. **Open your browser:** http://localhost:8501

## 🔧 Setup Guide

### Option 1: Enhanced Rendering (Recommended)
```bash
pip install streamlit-mermaid
```

### Option 2: AI Providers Setup
- **Hugging Face**: Get free token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- **Groq**: Get free API key from [console.groq.com](https://console.groq.com)
- **Ollama**: Install from [ollama.ai](https://ollama.ai) for local AI

## 📖 Usage Examples

### Basic Class
```
Create a User class with name, email attributes and login(), logout() methods
```

### Inheritance
```
Create Animal class with name attribute. Dog and Cat classes inherit from Animal. Dog has breed, Cat has color.
```

### Complex System
```
Create Library with books list. Book class has title, author, isbn. User can borrow and return books. LibraryCard links User to borrowed books.
```

## 🛠️ Troubleshooting

- **Diagrams not showing?** Install `streamlit-mermaid` for better rendering
- **API errors?** Check your API keys in the sidebar
- **Model loading?** Wait 30 seconds or try offline mode
- **Need help?** Use the built-in debug tools

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Test your changes
4. Submit a pull request

## 📄 License

MIT License - Feel free to use and modify!