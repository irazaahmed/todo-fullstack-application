#!/bin/bash
# Development startup script for the Todo API backend

# Activate virtual environment
source venv/bin/activate

# Set environment variables for development
export DATABASE_URL="sqlite:///./todo_dev.db"
export JWT_SECRET="development_secret_key_change_in_production"
export JWT_EXPIRATION="24h"
export DEBUG="True"

echo "Starting Todo API backend in development mode..."
echo "Environment variables set:"
echo "  DATABASE_URL=$DATABASE_URL"
echo "  JWT_SECRET set"
echo "  DEBUG=$DEBUG"

# Run the application with uvicorn
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

deactivate