# Quickstart Guide: Todo Full-Stack Web Application – Authentication & User Isolation

## Prerequisites

- Node.js 18+ for frontend
- Python 3.11+ for backend
- PostgreSQL database (Neon Serverless recommended)
- Git

## Setup Instructions

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd todo-fullstack-application
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env to add your database connection string and JWT secret
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install
```

### 4. Environment Configuration
Create a `.env` file in the root with the following variables:

```env
# Database
DATABASE_URL="postgresql://..."

# JWT Configuration
JWT_SECRET="your-super-secret-jwt-key-here"
JWT_EXPIRATION="24h"

# Better Auth Configuration
AUTH_SECRET="your-auth-secret"
NEXT_PUBLIC_AUTH_URL="http://localhost:3000"
```

## Running the Application

### 1. Start Backend
```bash
cd backend
uvicorn main:app --reload --port 8000
```

### 2. Start Frontend
```bash
cd frontend
npm run dev
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Authenticate user
- `POST /api/auth/logout` - Logout user

### Tasks
- `GET /api/tasks` - Get all user tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

## Testing Authentication Flow

1. Register a new user via `POST /api/auth/register`
2. Login with credentials via `POST /api/auth/login`
3. Use the returned JWT token in the `Authorization: Bearer <token>` header for task endpoints
4. Verify that you can only access your own tasks

## Troubleshooting

- If authentication fails, verify JWT_SECRET is set correctly in both frontend and backend
- If database connections fail, check your DATABASE_URL configuration
- If CORS issues occur, verify your frontend URL is allowed in backend settings