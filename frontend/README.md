# Todo Application Frontend

This is the frontend for the Todo application with authentication and user isolation features.

## Features

- User registration and login
- Secure task management
- User session management
- Responsive UI

## Tech Stack

- Next.js 16+
- React 19+
- TypeScript
- Better Auth

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run the development server:
   ```bash
   npm run dev
   ```

## Environment Variables

- `NEXT_PUBLIC_AUTH_URL`: The URL of your authentication service
- `AUTH_SECRET`: Secret for authentication

## Components

- `AuthProvider`: Context provider for authentication state
- `TaskService`: Service for interacting with the task API
- Authentication components for login/register

## API Integration

The frontend communicates with the backend API at `/api/` endpoints. Authentication tokens are automatically included in requests when available.