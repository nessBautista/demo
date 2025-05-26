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