#!/bin/bash
set -e

echo "=== Package Installation Script ==="

# Function to check if packages are installed
check_packages() {
    python -c "import plotly.graph_objects; print('Plotly found in system Python')" 2>/dev/null || echo "Plotly NOT found in system Python"
    
    if [ -f "/app/.venv/bin/python" ]; then
        /app/.venv/bin/python -c "import plotly.graph_objects; print('Plotly found in venv')" 2>/dev/null || echo "Plotly NOT found in venv"
    fi
}

# Initial check
echo "Initial package check:"
check_packages

# Install in system Python
echo -e "\nInstalling packages in system Python..."
pip install plotly kaleido matplotlib seaborn pandas

# Start Langflow
echo -e "\nStarting Langflow..."
python -m langflow run --host 0.0.0.0 --port 7860 &
LANGFLOW_PID=$!

# Wait and install in venv
echo -e "\nWaiting for virtual environment..."
ATTEMPTS=0
while [ $ATTEMPTS -lt 30 ]; do
    if [ -f "/app/.venv/bin/pip" ]; then
        echo "Virtual environment found! Installing packages..."
        
        # Ensure pip is up to date
        /app/.venv/bin/python -m pip install --upgrade pip
        
        # Install packages with verbose output
        /app/.venv/bin/pip install plotly kaleido matplotlib seaborn pandas --verbose
        
        # Verify installation
        echo -e "\nVerifying installation:"
        /app/.venv/bin/pip list | grep -E "plotly|kaleido|matplotlib|seaborn|pandas" || true
        
        # Test import
        echo -e "\nTesting imports in venv:"
        /app/.venv/bin/python -c "
import plotly.graph_objects as go
import plotly.express as px
print('✓ Plotly imports successful')
import matplotlib.pyplot as plt
print('✓ Matplotlib imports successful')
import seaborn as sns
print('✓ Seaborn imports successful')
import pandas as pd
print('✓ Pandas imports successful')
"
        break
    fi
    sleep 1
    ATTEMPTS=$((ATTEMPTS + 1))
done

# Final check
echo -e "\nFinal package check:"
check_packages

# Keep Langflow running
echo -e "\nLangflow is running. Check http://localhost:7860"
wait $LANGFLOW_PID