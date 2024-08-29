# Base image - colocar versão mais recente
FROM python:3.12.5-slim

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip \
    libxi6 \
    libgconf-2-4 \
    default-jdk \
    python3-pip \
    firefox-esr \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz -O /tmp/geckodriver.tar.gz && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ && \
    rm /tmp/geckodriver.tar.gz

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code to the container
COPY . /app
WORKDIR /app


# Set environment variable for ZAP API key - tirar daqui
ENV FIREFOX="/usr/local/bin/geckodriver"
ENV ZAP_PROXY_ADDRESS="zaproxy"

# Command to start the application
# CMD sleep 10 && python3 main.py
CMD sleep 10000