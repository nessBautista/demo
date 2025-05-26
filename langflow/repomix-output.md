This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded

## Additional Info

# Directory Structure
```
custom_entrypoint.py
docker-compose.yml
docker.env
install_and_run.sh
```

# Files

## File: custom_entrypoint.py
```python
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
```

## File: docker-compose.yml
```yaml
services:
  langflow:
    image: langflowai/langflow:latest
    container_name: langflow-custom
    user: root
    ports:
      - "7860:7860"
    env_file:
      - docker.env
    volumes:
      - langflow_data:/app
      - ./install_and_run.sh:/install_and_run.sh
    command: /bin/bash /install_and_run.sh

volumes:
  langflow_data:
```

## File: docker.env
```
# Basic Langflow configuration
LANGFLOW_HOST=0.0.0.0
LANGFLOW_PORT=7860
LANGFLOW_SUPERUSER=admin
LANGFLOW_SUPERUSER_PASSWORD=admin
```

## File: install_and_run.sh
```bash
#!/bin/bash
set -e

echo "Starting Langflow to create virtual environment..."

# Start Langflow as user in background
su -s /bin/bash -c "python -m langflow run --host 0.0.0.0 --port 7860" user &
LANGFLOW_PID=$!

echo "Waiting for virtual environment..."

# Wait for venv
MAX_WAIT=60
WAITED=0
while [ ! -f "/app/.venv/bin/pip" ] && [ $WAITED -lt $MAX_WAIT ]; do
    echo "Waiting... ($WAITED seconds)"
    sleep 2
    WAITED=$((WAITED + 2))
done

if [ -f "/app/.venv/bin/pip" ]; then
    echo "Virtual environment found! Installing packages..."
    
    # Install packages
    /app/.venv/bin/pip install plotly kaleido matplotlib seaborn pandas
    
    echo "Packages installed successfully!"
    
    # Stop the initial Langflow process
    echo "Stopping initial Langflow process..."
    kill $LANGFLOW_PID
    wait $LANGFLOW_PID 2>/dev/null || true
    
    # Give it a moment to clean up
    sleep 2
    
    # Restart Langflow with packages installed
    echo "Starting Langflow with packages installed..."
    exec su -s /bin/bash -c "python -m langflow run --host 0.0.0.0 --port 7860" user
else
    echo "Virtual environment not created after $MAX_WAIT seconds"
    kill $LANGFLOW_PID
    exit 1
fi
```
