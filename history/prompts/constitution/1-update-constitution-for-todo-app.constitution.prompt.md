---
id: 1
title: Update Constitution For Todo App
stage: constitution
date: 2026-01-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-app
branch: master
user: claude-code
command: /sp.constitution
labels: [constitution, todo-app, hackathon]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---

## Prompt

```
/sp.constitution

Project: Todo Full-Stack Web Application (Hackathon Phase II)

Core principles:
- Spec-Driven Development as the single source of truth
- No manual coding; all implementation must flow from approved specs
- Clear separation of concerns (frontend, backend, authentication, database)
- Security by default with strict user isolation
- Deterministic, reproducible builds through explicit specifications
- Cloud-ready architecture even when running locally

Key standards:
- The only allowed workflow is: Specify → Plan → Tasks → Implement
- No code may be generated without an explicit Task reference
- All architecture decisions must originate from the Plan
- All features must map back to written requirements and acceptance criteria
- REST APIs must be stateless, predictable, and documented
- Authentication must use Better Auth with JWT-based verification
- Every API request must be authorized and scoped to the authenticated user
- Backend must never trust client-provided user identifiers without JWT verification
- Frontend and backend must remain decoupled and communicate only via APIs

Architecture constraints:
- Monorepo structure is mandatory
- Frontend: Next.js 16+ using App Router
- Backend: Python FastAPI
- ORM: SQLModel only
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth issuing JWT tokens
- No alternative frameworks, ORMs, or databases are permitted
- Environment configuration must rely on environment variables, not hardcoded values

Security constraints:
- All API endpoints require a valid JWT token
- Requests without valid authentication must return 401 Unauthorized
- Task ownership must be enforced at the database query level
- JWT secret must be shared via environment variables only
- No cross-user data access is allowed under any condition
- Tokens must support expiration and stateless verification

Data and persistence rules:
- Tasks must be persistently stored in PostgreSQL
- Each task must be associated with exactly one user
- Database schema changes require specification updates
- No implicit fields or undocumented columns are allowed

Development constraints:
- No feature may exceed Basic Level scope in Phase II
- Intermediate or Advanced features must not be introduced
- No speculative improvements or "future ready" fields are allowed
- All changes must remain within Phase II boundaries
- If requirements are unclear or missing, the agent must stop and request clarification

Quality standards:
- Code generated must be readable, structured, and idiomatic
- API behavior must match documented specifications exactly
- Frontend UI must be responsive and usable on desktop and mobile
- Error handling must be explicit and user-safe
- System behavior must be predictable and testable

Success criteria:
- All five basic task features are implemented end to end
- Multi-user support works correctly with full data isolation
- Authentication and authorization are enforced on every request
- Frontend, backend, and database integrate cleanly
- No manual code exists outside spec-authorized output
- Project demonstrates a clear, auditable Spec Driven Development workflow
- Judges can trace every implementation back to a specification
```

## Response snapshot

Updated the project constitution at .specify/memory/constitution.md with the specified principles and constraints for the Todo Full-Stack Web Application (Hackathon Phase II). The new constitution establishes core principles around Spec-Driven Development, separation of concerns, deterministic builds, REST API statelessness, Better Auth authentication, data isolation, and monorepo architecture. It also includes sections on architecture constraints, development workflow, data and persistence rules, and quality standards.

## Outcome

- ✅ Impact: Constitution file updated with all specified principles
- 🧪 Tests: N/A
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Proceed with specification phase
- 🧠 Reflection: Constitution now properly defines the project's foundational principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin specification phase