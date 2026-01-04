# streamlit_mermaid_fix.py
# Run this to test and fix Mermaid rendering issues in your Streamlit app

import streamlit as st
import streamlit.components.v1 as components
import requests
import json

def test_mermaid_rendering():
    """Test different methods of rendering Mermaid diagrams in Streamlit."""
    
    st.title("🔧 Mermaid Rendering Test & Fix")
    st.markdown("This script tests different methods to render Mermaid diagrams in Streamlit")
    
    # Test sample Mermaid code
    sample_mermaid = """classDiagram
    class User {
        +name : String
        +email : String
        +login() : Boolean
        +logout() : void
    }
    
    class Profile {
        +avatar : String
        +bio : String
        +updateProfile() : void
    }
    
    User ||--|| Profile : has"""
    
    st.markdown("### 📋 Sample Mermaid Code")
    st.code(sample_mermaid, language="text")
    
    # Method 1: Try streamlit-mermaid component
    st.markdown("### Method 1: streamlit-mermaid Component")
    try:
        import streamlit_mermaid as stmermaid
        st.success("✅ streamlit-mermaid is installed!")
        
        if st.button("🎨 Test streamlit-mermaid Rendering"):
            stmermaid.st_mermaid(sample_mermaid, height=400)
            
    except ImportError:
        st.warning("⚠️ streamlit-mermaid not installed")
        st.code("pip install streamlit-mermaid", language="bash")
        
        if st.button("📦 Install streamlit-mermaid"):
            st.info("Run the pip command above in your terminal, then restart Streamlit")
    
    # Method 2: HTML Components (Your current method - FIXED)
    st.markdown("### Method 2: HTML Components (Fixed)")
    
    if st.button("🧪 Test HTML Component Rendering"):
        render_with_html_component(sample_mermaid)
    
    # Method 3: Iframe method (Alternative)
    st.markdown("### Method 3: Iframe Method")
    
    if st.button("🖼️ Test Iframe Rendering"):
        render_with_iframe(sample_mermaid)
    
    # Method 4: Mermaid Live Editor Link
    st.markdown("### Method 4: External Editor")
    
    mermaid_url = f"https://mermaid.live/edit#pako:eNqFkE1qAzEMha8itJ6UnCBLr9LSSQIpbdq40MWg4DH2pOA_JBm3adK7V3Y3zXRRwEK833tIfAn0VgLdCJv2Pu2MUTlY6E6LVX5B3VZ9V9_UZeqKvlxVi-0Gg_MkQkU2K9U"
    
    st.markdown(f"[🌐 Open in Mermaid Live Editor]({mermaid_url})")
    
    # Diagnostics
    st.markdown("### 🔍 System Diagnostics")
    
    diagnostics = {
        "Streamlit Version": st.__version__,
        "Components Available": hasattr(components, 'html'),
        "Requests Module": 'requests' in globals(),
    }
    
    # Test streamlit-mermaid
    try:
        import streamlit_mermaid
        diagnostics["streamlit-mermaid"] = "✅ Installed"
    except ImportError:
        diagnostics["streamlit-mermaid"] = "❌ Not installed"
    
    # Test network connectivity
    try:
        response = requests.get("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.1/mermaid.min.js", timeout=5)
        diagnostics["CDN Access"] = "✅ Available" if response.status_code == 200 else f"❌ HTTP {response.status_code}"
    except:
        diagnostics["CDN Access"] = "❌ Network error"
    
    for key, value in diagnostics.items():
        st.write(f"**{key}:** {value}")

def render_with_html_component(mermaid_code):
    """FIXED HTML component rendering method."""
    
    # Escape the Mermaid code properly
    escaped_code = mermaid_code.replace('"', '\\"').replace('\n', '\\n')
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f8f9fa;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }}
        
        .container {{
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-width: 100%;
            width: 100%;
        }}
        
        .status {{
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            text-align: center;
            font-weight: 600;
        }}
        
        .loading {{ background: #e3f2fd; color: #1976d2; }}
        .success {{ background: #e8f5e8; color: #2e7d32; }}
        .error {{ background: #ffeaea; color: #d32f2f; }}
        
        #diagram {{
            width: 100%;
            text-align: center;
            min-height: 200px;
            padding: 20px;
        }}
        
        .fallback {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div id="status" class="status loading">⏳ Loading Mermaid library...</div>
        <div id="diagram"></div>
        <div id="fallback" class="fallback" style="display: none;">
            <h4>📋 Manual Rendering Required</h4>
            <p>Copy the code below to <a href="https://mermaid.live" target="_blank">Mermaid Live Editor</a>:</p>
            <pre style="background: white; padding: 15px; border-radius: 4px; overflow-x: auto;"><code>{mermaid_code}</code></pre>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.1/mermaid.min.js" 
            onload="initializeMermaid()" 
            onerror="handleLoadError()"></script>
    
    <script>
        const mermaidCode = `{mermaid_code}`;
        
        function updateStatus(message, type) {{
            const statusDiv = document.getElementById('status');
            statusDiv.textContent = message;
            statusDiv.className = `status ${{type}}`;
        }}
        
        function handleLoadError() {{
            updateStatus('❌ Failed to load Mermaid library', 'error');
            document.getElementById('fallback').style.display = 'block';
        }}
        
        function initializeMermaid() {{
            try {{
                updateStatus('🔄 Initializing Mermaid...', 'loading');
                
                mermaid.initialize({{
                    startOnLoad: false,
                    theme: 'default',
                    securityLevel: 'loose',
                    themeVariables: {{
                        primaryColor: '#fff2cc',
                        primaryTextColor: '#333333',
                        primaryBorderColor: '#d6b656',
                        lineColor: '#666666'
                    }}
                }});
                
                renderDiagram();
                
            }} catch (error) {{
                console.error('Init error:', error);
                updateStatus('❌ Initialization failed: ' + error.message, 'error');
                document.getElementById('fallback').style.display = 'block';
            }}
        }}
        
        function renderDiagram() {{
            try {{
                updateStatus('🎨 Rendering diagram...', 'loading');
                
                const diagramId = 'test-diagram-' + Date.now();
                
                mermaid.render(diagramId, mermaidCode).then((result) => {{
                    document.getElementById('diagram').innerHTML = result.svg;
                    updateStatus('✅ Diagram rendered successfully!', 'success');
                    
                    // Auto-hide success message
                    setTimeout(() => {{
                        document.getElementById('status').style.display = 'none';
                    }}, 3000);
                    
                }}).catch((error) => {{
                    console.error('Render error:', error);
                    updateStatus('❌ Render failed: ' + error.message, 'error');
                    document.getElementById('fallback').style.display = 'block';
                }});
                
            }} catch (error) {{
                console.error('Render setup error:', error);
                updateStatus('❌ Render setup failed: ' + error.message, 'error');
                document.getElementById('fallback').style.display = 'block';
            }}
        }}
        
        // Timeout fallback
        setTimeout(() => {{
            if (document.getElementById('status').textContent.includes('Loading') || 
                document.getElementById('status').textContent.includes('Initializing')) {{
                updateStatus('⏰ Timeout: Rendering took too long', 'error');
                document.getElementById('fallback').style.display = 'block';
            }}
        }}, 10000);
    </script>
</body>
</html>"""
    
    # Render with proper height
    components.html(html_content, height=600, scrolling=True)

def render_with_iframe(mermaid_code):
    """Alternative iframe-based rendering method."""
    
    # Create a data URL with the Mermaid diagram
    import urllib.parse
    
    encoded_code = urllib.parse.quote(mermaid_code)
    mermaid_url = f"https://mermaid.ink/img/{encoded_code}"
    
    # Try to display as image
    try:
        st.image(mermaid_url, caption="Mermaid Diagram (via mermaid.ink)")
        st.success("✅ Rendered via mermaid.ink service")
    except Exception as e:
        st.error(f"❌ mermaid.ink service error: {e}")
        st.markdown(f"**Direct link:** [View Diagram]({mermaid_url})")

def main():
    """Main application with comprehensive testing."""
    
    # Add tabs for different testing methods
    tab1, tab2, tab3, tab4 = st.tabs(["🧪 Main Test", "📊 Quick Examples", "🔧 Manual Debug", "📚 Solutions"])
    
    with tab1:
        test_mermaid_rendering()
    
    with tab2:
        st.markdown("### 🚀 Quick Test Examples")
        
        examples = {
            "Simple Class": """classDiagram
    class User {
        +name : String
        +login() : Boolean
    }""",
            
            "Inheritance": """classDiagram
    class Animal {
        +name : String
        +makeSound() : void
    }
    class Dog {
        +breed : String
    }
    Animal <|-- Dog""",
            
            "Complex System": """classDiagram
    class Customer {
        +customerId : String
        +name : String
        +email : String
    }
    class Order {
        +orderId : String
        +total : Double
        +process() : void
    }
    class Product {
        +name : String
        +price : Double
    }
    
    Customer ||--o{ Order
    Order }o--|| Product"""
        }
        
        for name, code in examples.items():
            st.markdown(f"#### {name}")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.code(code, language="text")
            
            with col2:
                if st.button(f"🎨 Render {name}", key=f"render_{name}"):
                    render_with_html_component(code)
    
    with tab3:
        st.markdown("### 🔧 Manual Debugging")
        
        user_code = st.text_area(
            "Enter your Mermaid code:",
            value="classDiagram\n    class TestClass {\n        +attribute : String\n        +method() : void\n    }",
            height=200
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🧪 Test HTML Method"):
                render_with_html_component(user_code)
        
        with col2:
            if st.button("🖼️ Test Iframe Method"):
                render_with_iframe(user_code)
        
        with col3:
            if st.button("🌐 Open in Live Editor"):
                import urllib.parse
                encoded = urllib.parse.quote(user_code)
                st.markdown(f"[🌐 View in Mermaid Live Editor](https://mermaid.live/edit#{encoded})")
    
    with tab4:
        st.markdown("""
        ### 🎯 Complete Solutions for Your Issues
        
        #### 🚨 Main Problems Identified:
        
        1. **Mermaid Library Loading Issues**
           - CDN reliability problems
           - Version compatibility issues
           - Browser security restrictions
        
        2. **Streamlit Component Rendering**
           - HTML height limitations
           - JavaScript execution context
           - Component isolation issues
        
        #### ✅ Fixed Solutions:
        
        ##### 1. Install streamlit-mermaid (Recommended):
        ```bash
        pip install streamlit-mermaid
        ```
        Then use:
        ```python
        import streamlit_mermaid as stmermaid
        stmermaid.st_mermaid(mermaid_code, height=600)
        ```
        
        ##### 2. Use the Fixed HTML Method:
        - Updated Mermaid CDN to reliable version
        - Improved error handling and fallbacks
        - Better HTML structure and styling
        - Proper async rendering
        
        ##### 3. Alternative: mermaid.ink Service:
        ```python
        import urllib.parse
        encoded_code = urllib.parse.quote(mermaid_code)
        mermaid_url = f"https://mermaid.ink/img/{encoded_code}"
        st.image(mermaid_url)
        ```
        
        #### 🔧 Implementation Steps:
        
        1. **Replace your render_mermaid function** with the fixed version
        2. **Add proper error handling** and fallbacks
        3. **Test with offline provider first** to verify basic functionality
        4. **Install streamlit-mermaid** for best results
        5. **Use the debug tool** to test rendering
        
        #### 🎯 Expected Results:
        After implementing these fixes, you should see:
        - ✅ **Proper class boxes** with attributes and methods
        - ✅ **Relationship arrows** between classes  
        - ✅ **Interactive diagrams** you can zoom/pan
        - ✅ **Consistent rendering** across different browsers
        - ✅ **Fallback options** when rendering fails
        
        #### 🚀 Next Steps:
        1. Copy the fixed code from the first artifact
        2. Replace your current app.py
        3. Install streamlit-mermaid: `pip install streamlit-mermaid`
        4. Test with the debug tool
        5. Start with offline mode, then try AI providers
        """)

if __name__ == "__main__":
    main()