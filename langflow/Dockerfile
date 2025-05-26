# Dockerfile
FROM langflowai/langflow:latest

USER root

# Copy requirements
COPY requirements.txt /app/requirements.txt

# Install globally first
RUN pip install -r /app/requirements.txt

# Create a wrapper script that ensures packages are in venv
RUN echo '#!/bin/bash' > /app/start.sh && \
    echo 'pip install -r /app/requirements.txt' >> /app/start.sh && \
    echo 'python -m langflow run --host 0.0.0.0 --port 7860 &' >> /app/start.sh && \
    echo 'PID=$!' >> /app/start.sh && \
    echo 'sleep 10' >> /app/start.sh && \
    echo 'if [ -f "/app/.venv/bin/pip" ]; then' >> /app/start.sh && \
    echo '  /app/.venv/bin/pip install -r /app/requirements.txt' >> /app/start.sh && \
    echo 'fi' >> /app/start.sh && \
    echo 'wait $PID' >> /app/start.sh && \
    chmod +x /app/start.sh

CMD ["/app/start.sh"]
