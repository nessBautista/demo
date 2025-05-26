#!/usr/bin/env python3
import subprocess
import sys
import os
import time

def wait_for_venv():
    """Wait for Langflow to create its virtual environment"""
    print("Starting Langflow in background to create virtual environment...")
    
    # Start Langflow as user to create venv
    langflow_proc = subprocess.Popen(
        ["su", "-s", "/bin/bash", "-c", "python -m langflow run --host 0.0.0.0 --port 7860", "user"]
    )
    
    # Wait for venv to be created
    venv_pip = "/app/.venv/bin/pip"
    max_wait = 60  # seconds
    waited = 0
    
    while not os.path.exists(venv_pip) and waited < max_wait:
        print(f"Waiting for virtual environment... ({waited}s)")
        time.sleep(2)
        waited += 2
    
    if not os.path.exists(venv_pip):
        print("Virtual environment not created after 60 seconds!")
        return None, langflow_proc
    
    print("Virtual environment found!")
    return venv_pip, langflow_proc

def install_packages(venv_pip):
    """Install required packages in the virtual environment"""
    packages = ['plotly', 'kaleido', 'matplotlib', 'seaborn', 'pandas']
    
    print("Installing packages...")
    for package in packages:
        print(f"Installing {package}...")
        subprocess.run([venv_pip, "install", package], check=True)
    
    print("All packages installed successfully!")

def main():
    # Wait for venv and get Langflow process
    venv_pip, langflow_proc = wait_for_venv()
    
    if venv_pip:
        # Install packages
        install_packages(venv_pip)
        
        print("Packages installed. Langflow is running...")
        # Wait for Langflow process
        langflow_proc.wait()
    else:
        print("Failed to create virtual environment")
        sys.exit(1)

if __name__ == "__main__":
    main()