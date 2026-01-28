<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Modified principles: None (new constitution)
Added sections: All principles and sections from user input
Removed sections: None (completely new content)
Templates requiring updates:
- ✅ .specify/templates/plan-template.md - Updated to align with new principles
- ✅ .specify/templates/spec-template.md - Updated to align with new principles
- ✅ .specify/templates/tasks-template.md - Updated to align with new principles
- ✅ .specify/templates/commands/*.md - Reviewed for consistency
- ✅ README.md - Updated references to new principles
Follow-up TODOs: None
-->
# Todo Full-Stack Web Application (Hackathon Phase II) Constitution

## Core Principles

### Spec-Driven Development as the Single Source of Truth
Spec-Driven Development as the single source of truth. No manual coding; all implementation must flow from approved specs. All architecture decisions must originate from the Plan. All features must map back to written requirements and acceptance criteria.

### Clear Separation of Concerns
Maintain clear separation of concerns (frontend, backend, authentication, database). Frontend and backend must remain decoupled and communicate only via APIs. Security by default with strict user isolation.

### Deterministic Reproducible Builds
Deterministic, reproducible builds through explicit specifications. Cloud-ready architecture even when running locally. Environment configuration must rely on environment variables, not hardcoded values.

### REST API Statelessness
REST APIs must be stateless, predictable, and documented. Every API request must be authorized and scoped to the authenticated user. Backend must never trust client-provided user identifiers without JWT verification.

### Authentication with Better Auth
Authentication must use Better Auth with JWT-based verification. All API endpoints require a valid JWT token. Requests without valid authentication must return 401 Unauthorized.

### Data Isolation and Security
Task ownership must be enforced at the database query level. No cross-user data access is allowed under any condition. JWT secret must be shared via environment variables only.

### Monorepo Architecture
Monorepo structure is mandatory. Frontend: Next.js 16+ using App Router. Backend: Python FastAPI. ORM: SQLModel only. Database: Neon Serverless PostgreSQL. Authentication: Better Auth issuing JWT tokens. No alternative frameworks, ORMs, or databases are permitted.

## Architecture Constraints
No feature may exceed Basic Level scope in Phase II. Intermediate or Advanced features must not be introduced. No speculative improvements or "future ready" fields are allowed. All changes must remain within Phase II boundaries. If requirements are unclear or missing, the agent must stop and request clarification.

## Development Workflow
The only allowed workflow is: Specify → Plan → Tasks → Implement. No code may be generated without an explicit Task reference. All architecture decisions must originate from the Plan. All features must map back to written requirements and acceptance criteria.

## Data and Persistence Rules
Tasks must be persistently stored in PostgreSQL. Each task must be associated with exactly one user. Database schema changes require specification updates. No implicit fields or undocumented columns are allowed.

## Quality Standards
Code generated must be readable, structured, and idiomatic. API behavior must match documented specifications exactly. Frontend UI must be responsive and usable on desktop and mobile. Error handling must be explicit and user-safe. System behavior must be predictable and testable.

## Governance
This constitution establishes the foundational principles for the Todo Full-Stack Web Application project. All development activities must comply with these principles. Any deviation from these principles must be explicitly documented and approved. The workflow of Specify → Plan → Tasks → Implement must be strictly followed. No manual coding outside of spec-authorized output is permitted. All changes must be traceable back to a specification.

**Version**: 1.0.0 | **Ratified**: 2026-01-28 | **Last Amended**: 2026-01-28