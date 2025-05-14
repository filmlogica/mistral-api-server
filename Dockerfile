FROM python:3.10-slim

# Install system packages including CA certs
RUN apt-get update && \
    apt-get install -y git curl ca-certificates && \
    pip install --no-cache-dir flask requests

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy app files
WORKDIR /app
COPY server.py .

# Expose Ollama + Flask port
EXPOSE 11434

# Start Ollama service in background, then wait & pull Mistral, then run Flask
CMD bash -c "\
    ollama serve & \
    sleep 10 && \
    ollama pull mistral && \
    python server.py"
