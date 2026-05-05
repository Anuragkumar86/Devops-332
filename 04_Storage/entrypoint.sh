#!/bin/bash
# Entrypoint script demonstrating ENTRYPOINT vs CMD

echo "Container started at: $(date)" >> /app/logs/startup.log
echo "Arguments received: $@"
echo "Data directory contents:"
ls -la /app/data/ 2>/dev/null || echo "  (empty)"

# Keep container running
tail -f /dev/null
