#!/usr/bin/env python3
"""Quick launcher for the UML Generator app."""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed."""
    required = ['streamlit', 'requests']
    recommended = ['streamlit-mermaid', 'python-dotenv']
    
    missing = []
    for package in required:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"❌ Missing required packages: {', '.join(missing)}")
        print(f"💡 Install with: pip install {' '.join(missing)}")
        return False
    
    # Check recommended
    missing_rec = []
    for package in recommended:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_rec.append(package)
    
    if missing_rec:
        print(f"⚠️  Recommended packages not installed: {', '.join(missing_rec)}")
        print(f"💡 Install with: pip install {' '.join(missing_rec)}")
    
    return True

def main():
    """Launch the Streamlit app."""
    print("🎯 Starting Free AI UML Generator...")
    
    if not check_dependencies():
        sys.exit(1)
    
    # Set environment variables
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_PORT'] = '8501'
    
    # Launch Streamlit
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.headless', 'true',
            '--server.port', '8501',
            '--browser.gatherUsageStats', 'false'
        ])
    except KeyboardInterrupt:
        print("\n👋 UML Generator stopped.")
    except Exception as e:
        print(f"❌ Error launching app: {e}")

if __name__ == "__main__":
    main()