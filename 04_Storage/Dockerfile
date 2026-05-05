FROM ubuntu:22.04

# Install utilities
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ── VOLUME: Declare mount point for persistent storage
VOLUME ["/app/data", "/app/logs"]

# Create default files
RUN echo "Storage demo container" > /app/README.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["--mode", "default"]
