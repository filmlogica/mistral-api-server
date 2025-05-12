FROM python:3.10-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y git curl && \
    pip install --no-cache-dir flask

# Install and run Ollama (lightweight Mistral host)
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull the Mistral model
RUN ollama pull mistral

# Copy app files
WORKDIR /app
COPY server.py .

# Expose the default Ollama + Flask port
EXPOSE 11434

# Start Ollama and Flask server
CMD bash -c "ollama serve & sleep 5 && python server.py"
