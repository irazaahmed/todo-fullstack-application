# Manual Procedure: Running the Todo Full-Stack Application

## Overview
This document provides step-by-step instructions for setting up and running the Todo Full-Stack Application with Authentication & User Isolation.

## Prerequisites
- Python 3.11+ installed on your system
- Node.js 18+ installed on your system
- PostgreSQL database (or access to Neon Serverless)
- Git for version control

## Step 1: Clone and Navigate to the Repository

```bash
# Clone the repository (if needed)
git clone <repository-url>
cd todo-fullstack-application
```

## Step 2: Backend Setup and Configuration

### 2.1 Navigate to Backend Directory
```bash
cd backend
```

### 2.2 Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# Activate virtual environment (Windows)
# venv\Scripts\activate
```

### 2.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2.4 Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file to set your configuration
nano .env  # or use your preferred editor
```

**Required Environment Variables:**
- `DATABASE_URL`: Your PostgreSQL database connection string (e.g., `postgresql://username:password@localhost:5432/todo_app`)
- `JWT_SECRET`: A secure secret key for JWT tokens (at least 32 random characters)
- `JWT_EXPIRATION`: Token expiration time (default: "24h")

**Example for development:**
```
DATABASE_URL=sqlite:///./todo_dev.db
JWT_SECRET=this_is_a_very_long_random_string_for_development_purposes_only
JWT_EXPIRATION=24h
DEBUG=True
```

### 2.5 Start the Backend Server

#### Option A: Using the startup script (recommended)
```bash
# Make sure the script is executable
chmod +x start-dev.sh

# Run the development startup script
./start-dev.sh
```

#### Option B: Manual startup
```bash
# Set environment variables and run
export DATABASE_URL="sqlite:///./todo_dev.db"
export JWT_SECRET="your_very_secure_secret_here"
export DEBUG="True"

uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

#### Option C: Using environment file
```bash
# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Step 3: Frontend Setup and Configuration

### 3.1 Open a new terminal window/tab and navigate to frontend directory
```bash
cd frontend
```

### 3.2 Install Node.js Dependencies
```bash
npm install
```

### 3.3 Configure Frontend Environment (if needed)
```bash
# Create .env.local file if needed
cp .env.example .env.local
# Edit the file to match your backend URL
nano .env.local
```

### 3.4 Start the Frontend Development Server
```bash
npm run dev
```

## Step 4: Verify the Application is Running

### 4.1 Backend Verification
- Open your browser and navigate to `http://localhost:8000`
- You should see a welcome message: `{"message": "Todo API - Authentication & User Isolation"}`
- The API documentation will be available at `http://localhost:8000/docs`

### 4.2 Frontend Verification
- If you started the frontend, navigate to `http://localhost:3000`
- You should see the frontend application

## Step 5: Test the API Manually (Optional)

### 5.1 Test Health Check
```bash
curl http://localhost:8000/
```

### 5.2 Register a New User
```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "securepassword123"
  }'
```

### 5.3 Login with the Registered User
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "securepassword123"
  }'
```

### 5.4 Create a Task (using the token from login response)
```bash
TOKEN="your_jwt_token_from_login_response"

curl -X POST "http://localhost:8000/api/tasks" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "My First Task",
    "description": "This is my first task",
    "completed": false
  }'
```

## Step 6: Running in Production Mode

### 6.1 Backend Production Setup
```bash
# Set production environment variables
export DATABASE_URL="your_production_database_url"
export JWT_SECRET="your_secure_production_secret"
export DEBUG="False"

# Run production startup script
./start-prod.sh
```

### 6.2 Frontend Production Build
```bash
# Build the frontend for production
npm run build

# Serve the built application
npm start
```

## Step 7: Using Docker (Alternative Method)

### 7.1 Build and Start with Docker Compose
```bash
# From the root directory of the project
docker-compose up --build
```

### 7.2 Access the Applications
- Backend API: `http://localhost:8000`
- Frontend: `http://localhost:3000`
- API Documentation: `http://localhost:8000/docs`

## Troubleshooting Common Issues

### Issue 1: Environment Variables Not Loading
**Symptoms:** Error about missing DATABASE_URL or JWT_SECRET
**Solution:** Make sure your .env file is properly formatted and located in the backend directory

### Issue 2: Port Already in Use
**Symptoms:** Address already in use error
**Solution:** Kill the process using the port or use a different port:
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process (replace PID with actual process ID)
kill -9 PID
```

### Issue 3: Database Connection Issues
**Symptoms:** Cannot connect to database
**Solution:** Verify your DATABASE_URL is correct and the database server is running

### Issue 4: Authentication Fails
**Symptoms:** 401 Unauthorized errors
**Solution:** Verify JWT_SECRET is the same in both backend and frontend environments

## Stopping the Applications

### Backend
Press `Ctrl+C` in the terminal where the backend is running

### Frontend
Press `Ctrl+C` in the terminal where the frontend is running

### Docker
```bash
# Stop Docker containers
docker-compose down
```

## Additional Notes

- For development, the SQLite database is sufficient, but for production, use PostgreSQL
- Always use strong, random secrets for JWT_SECRET in production
- Regularly rotate your JWT secrets
- Monitor your application logs for security issues
- Back up your database regularly