# Data Model: Todo Full-Stack Web Application – Authentication & User Isolation

## Entities

### User
Represents an authenticated individual with a unique identity, email address, and authentication credentials.

**Fields:**
- id: UUID (Primary Key) - Unique identifier for the user
- email: String - User's email address (unique, required)
- created_at: DateTime - Timestamp when user account was created
- updated_at: DateTime - Timestamp when user account was last updated

**Relationships:**
- tasks: One-to-Many relationship with Task entity (one user can have many tasks)

**Validation Rules:**
- Email must be a valid email format
- Email must be unique across all users
- Email cannot be null

### JWT Token
Represents a cryptographically signed token containing user identity information that expires after a configured duration.

**Fields:**
- token: String - The JWT token string
- user_id: UUID - Reference to the user who owns this token
- expires_at: DateTime - Expiration timestamp for the token
- created_at: DateTime - Timestamp when token was issued

**Validation Rules:**
- Token must be a valid JWT format
- User_id must reference an existing user
- Expires_at must be in the future

### Task
Represents a user-owned item that can only be accessed by the authenticated user who owns it.

**Fields:**
- id: UUID (Primary Key) - Unique identifier for the task
- title: String - Title of the task (required)
- description: String - Optional description of the task
- completed: Boolean - Whether the task is completed (default: false)
- user_id: UUID - Reference to the user who owns this task (foreign key)
- created_at: DateTime - Timestamp when task was created
- updated_at: DateTime - Timestamp when task was last updated

**Relationships:**
- user: Many-to-One relationship with User entity (many tasks belong to one user)

**Validation Rules:**
- Title cannot be null or empty
- User_id must reference an existing user
- Completed field defaults to false
- Only the owning user can access or modify the task

## Data Access Patterns

### User Authentication
- Query users by email for login verification
- Create new user records during registration

### Task Access Control
- Query tasks filtered by user_id to ensure data isolation
- Verify that the authenticated user matches the task owner before allowing operations

## Security Considerations

### Data Isolation
- All task queries must include user_id filter to prevent cross-user access
- Backend must validate JWT and extract user identity before any data access
- User_id in API path must match authenticated user identity

### Token Management
- JWT tokens must be validated for authenticity and expiration
- No server-side session storage - validation occurs statelessly