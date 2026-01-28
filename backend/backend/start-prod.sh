#!/bin/bash
# Production startup script for the Todo API backend

# Activate virtual environment
source venv/bin/activate

# Check if required environment variables are set
if [ -z "$DATABASE_URL" ] || [ -z "$JWT_SECRET" ]; then
    echo "Error: Required environment variables DATABASE_URL and JWT_SECRET must be set"
    echo "Please set them before running this script:"
    echo "  export DATABASE_URL='your_database_connection_string'"
    echo "  export JWT_SECRET='your_secure_jwt_secret'"
    exit 1
fi

echo "Starting Todo API backend in production mode..."
echo "Environment variables set:"
echo "  DATABASE_URL=$DATABASE_URL"
echo "  JWT_SECRET set"
echo "  DEBUG=${DEBUG:-False}"

# Run the application with uvicorn in production mode
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4

deactivate