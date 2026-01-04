import streamlit as st
from utils.mermaid_renderer import render_mermaid_diagram
from examples.sample_diagrams import SAMPLE_MERMAID_CODES
from config import Config

def main():
    st.title("🔍 UML Debug Tool")
    st.markdown("Test and debug Mermaid diagram rendering")
    
    st.header("Test Rendering")
    diagram_type = st.selectbox("Select test diagram", list(SAMPLE_MERMAID_CODES.keys()))
    
    if st.button("Render Test Diagram"):
        with st.spinner("Rendering test diagram..."):
            try:
                render_mermaid_diagram(SAMPLE_MERMAID_CODES[diagram_type])
                st.success("✅ Diagram rendered successfully")
            except Exception as e:
                st.error(f"❌ Rendering failed: {e}")
    
    st.header("Custom Code Test")
    custom_code = st.text_area("Enter Mermaid code", height=200)
    if st.button("Render Custom Code"):
        if custom_code:
            try:
                render_mermaid_diagram(custom_code)
                st.success("✅ Custom diagram rendered successfully")
            except Exception as e:
                st.error(f"❌ Custom rendering failed: {e}")

if __name__ == "__main__":
    main()