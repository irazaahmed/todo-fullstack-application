# Todo Full-Stack Application with Authentication & User Isolation

A complete full-stack Todo application featuring authentication, user isolation, and secure task management.

## Features

- **User Authentication**: Register and login with JWT-based authentication
- **User Isolation**: Strict data isolation ensuring users can only access their own tasks
- **Secure Task Management**: Create, read, update, and delete tasks securely
- **Modern Tech Stack**: Built with FastAPI, Next.js, SQLModel, and PostgreSQL
- **Scalable Architecture**: Stateless authentication with JWT tokens

## Tech Stack

### Backend
- **Framework**: FastAPI
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Database**: PostgreSQL (Neon Serverless compatible)
- **Authentication**: JWT tokens with bcrypt password hashing
- **Testing**: pytest

### Frontend
- **Framework**: Next.js 16+
- **Language**: TypeScript
- **Authentication**: Better Auth integration
- **State Management**: React Context API

## Architecture

The application follows a monorepo architecture with separate backend and frontend components:

```
├── backend/
│   ├── src/
│   │   ├── models/          # Database models
│   │   ├── services/        # Business logic
│   │   ├── api/             # API endpoints
│   │   ├── middleware/      # Authentication middleware
│   │   ├── database/        # Database connection
│   │   └── config/          # Configuration
│   ├── requirements.txt     # Python dependencies
│   ├── README.md           # Backend documentation
│   └── start-dev.sh        # Development startup script
├── frontend/
│   ├── src/
│   │   ├── lib/            # Utilities and auth
│   │   ├── services/       # API services
│   │   ├── context/        # React contexts
│   │   └── components/     # UI components
│   ├── package.json        # Node.js dependencies
│   └── README.md          # Frontend documentation
├── specs/001-auth-isolation/
│   ├── spec.md             # Feature specification
│   ├── plan.md             # Implementation plan
│   ├── data-model.md       # Data model
│   ├── contracts/api.yaml  # API contracts
│   └── tasks.md            # Implementation tasks
├── .env.example           # Environment variables template
└── docker-compose.yml     # Container orchestration
```

## Setup Instructions

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL (or Neon Serverless account)

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env to add your database connection string and JWT secret
   ```

5. **Start the backend server**:
   ```bash
   ./start-dev.sh
   # Or manually:
   DATABASE_URL="sqlite:///./todo.db" JWT_SECRET="your-secret-key" uvicorn src.main:app --reload --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
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

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: PostgreSQL database connection string
- `JWT_SECRET`: Secret key for JWT token signing (at least 32 characters)
- `JWT_EXPIRATION`: Token expiration time (default: "24h")
- `DEBUG`: Enable debug mode (default: false)

### Frontend (.env.local)
- `NEXT_PUBLIC_API_URL`: Backend API URL
- `NEXT_PUBLIC_AUTH_URL`: Authentication service URL

## Security Features

- **Password Security**: All passwords are hashed using bcrypt
- **JWT Authentication**: Stateless authentication with expiration validation
- **User Isolation**: All API endpoints enforce user ownership validation
- **Input Validation**: All data is validated using Pydantic models
- **Error Handling**: Consistent error responses without sensitive information leakage

## Running with Docker

1. **Build and start services**:
   ```bash
   docker-compose up --build
   ```

2. **Access the application**:
   - Backend API: http://localhost:8000
   - Frontend: http://localhost:3000

## Testing

### Backend Tests
```bash
# Run basic functionality tests
cd backend
source venv/bin/activate
python -m pytest test_basic.py -v
```

## Deployment

### Production Environment

1. Set secure environment variables:
   ```bash
   export DATABASE_URL="your_production_db_url"
   export JWT_SECRET="your_secure_32_character_secret"
   export DEBUG="False"
   ```

2. Run production startup script:
   ```bash
   ./start-prod.sh
   ```

### Configuration for Production

- Use a production-grade PostgreSQL database (recommended: Neon Serverless)
- Set a strong JWT secret (32+ characters, random)
- Configure SSL certificates
- Set up proper logging and monitoring
- Implement backup strategies

## Development

### Adding New Features

1. Create feature specification in `specs/[feature-number]-[feature-name]/`
2. Generate implementation plan with `/sp.plan`
3. Create tasks with `/sp.tasks`
4. Implement following the task breakdown
5. Test thoroughly before deployment

### Architecture Decisions

All significant architectural decisions are documented as ADRs (Architecture Decision Records) in the `history/adr/` directory.

## Troubleshooting

- **Authentication fails**: Verify JWT_SECRET is set correctly in both frontend and backend
- **Database connections fail**: Check your DATABASE_URL configuration
- **CORS issues**: Verify your frontend URL is allowed in backend settings
- **Migration errors**: Run database migrations if schema has changed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow the established code patterns and architecture
4. Write tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.