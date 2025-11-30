<!-- 8a6434b9-fc4c-44df-8ef0-99a00ab2e1ca 5ee83543-1600-4061-8634-343086a682d9 -->
# MVP Personal Finance + Fraud Detection Platform

## Prerequisites

Before starting Phase 1, ensure you have the following installed:

### Required Software

- **Python 3.11+**: Download from [python.org](https://www.python.org/downloads/) or use `brew install python@3.11` on macOS
- **Node.js 18+ and npm**: Download from [nodejs.org](https://nodejs.org/) or use `brew install node` on macOS
- **Docker Desktop**: Download from [docker.com](https://www.docker.com/products/docker-desktop/) - Required for running PostgreSQL and containerized services
- **Git**: Usually pre-installed, verify with `git --version`

### Optional but Recommended

- **VS Code** or your preferred IDE with Python and TypeScript extensions
- **PostgreSQL client tools** (psql) - Optional since Docker will handle the database

### No Accounts Required

- All services run locally via Docker
- No cloud accounts needed for MVP
- No API keys or external services required

### Verification Commands

Run these to verify installations:

```bash
python3 --version  # Should show 3.11+
node --version     # Should show v18+
npm --version      # Should show 9+
docker --version   # Should show Docker version
docker compose version  # Should show Docker Compose version
```

## Project Structure

- **Backend**: Python (FastAPI) - REST API, JWT auth, transaction management
- **Frontend**: React + TypeScript - User dashboard, transaction views
- **Database**: PostgreSQL - Users, transactions, categories, fraud alerts
- **Deployment**: Docker Compose for local development

## Phase 1: Project Setup & Infrastructure

### 1.1 Project Structure

- Create monorepo structure with `backend/`, `frontend/`, `docker/` directories
- Initialize Python FastAPI project with dependencies (FastAPI, SQLAlchemy, Pydantic, PyJWT, passlib, python-multipart, alembic)
- Initialize React + TypeScript project with Vite
- Add Docker Compose for PostgreSQL and application services
- Create `.gitignore`, `requirements.txt`, and basic README

### 1.2 Database Schema

- `users` table: id, email, password_hash, created_at
- `transactions` table: id, user_id, amount, description, category_id, transaction_date, merchant, location, created_at
- `categories` table: id, name, type (income/expense)
- `fraud_alerts` table: id, transaction_id, rule_triggered, severity, created_at, resolved

## Phase 2: Backend Development

### 2.1 Authentication & User Management

- User registration endpoint (`POST /api/auth/register`)
- User login endpoint (`POST /api/auth/login`) - returns JWT
- JWT dependency for protected endpoints (FastAPI dependency injection)
- Password hashing with passlib (bcrypt)

### 2.2 Transaction Management

- Create transaction (`POST /api/transactions`)
- List user transactions (`GET /api/transactions`) with pagination
- Get transaction by ID (`GET /api/transactions/{id}`)
- Update transaction (`PUT /api/transactions/{id}`)
- Delete transaction (`DELETE /api/transactions/{id}`)
- Transaction validation (amount, date, required fields)

### 2.3 Category Management

- List categories (`GET /api/categories`)
- Assign category to transaction
- Pre-populate common categories (Food, Transport, Entertainment, etc.)

### 2.4 Basic Fraud Detection Rules

- Rule engine service that evaluates transactions against rules:
- **Large amount rule**: Flag transactions > $1000
- **Rapid transactions rule**: Flag > 5 transactions in 1 hour
- **Unusual time rule**: Flag transactions outside 6 AM - 11 PM
- **Unusual location rule**: Flag transactions from new location (if location data provided)
- Create fraud alert when rule triggers
- Fraud alert endpoint (`GET /api/fraud-alerts`) - list alerts for user

## Phase 3: Frontend Development

### 3.1 Authentication UI

- Login page (`/login`)
- Register page (`/register`)
- JWT token storage in localStorage
- Protected route wrapper

### 3.2 Transaction Management UI

- Transaction list page (`/transactions`) - table with pagination
- Add transaction form (modal or page)
- Transaction detail view
- Category selector dropdown

### 3.3 Dashboard

- Summary statistics (total spent, transaction count, recent transactions)
- Fraud alerts section showing recent alerts
- Basic charts (optional: transaction trends)

### 3.4 Navigation & Layout

- Header with logout
- Sidebar navigation (Dashboard, Transactions, Alerts)
- Responsive design

## Phase 4: Integration & Testing

### 4.1 API Integration

- Axios setup with interceptors for JWT
- Error handling and user feedback
- Loading states

### 4.2 Basic Testing

- Backend: Unit tests for services, integration tests for API endpoints (pytest)
- Frontend: Component tests for critical flows

### 4.3 Docker Setup

- Dockerfile for Python FastAPI backend (multi-stage build)
- Dockerfile for React frontend (production build)
- Docker Compose with PostgreSQL, backend, frontend services
- Environment variables configuration

## Phase 5: Documentation & Deployment Prep

### 5.1 Documentation

- API documentation (FastAPI auto-generated OpenAPI/Swagger)
- README with setup instructions
- Environment variable documentation

### 5.2 Deployment Configuration

- Production-ready Docker configurations
- Alembic database migration scripts
- Health check endpoints

## Technical Decisions

**Backend Stack:**

- FastAPI (Python 3.11+)
- SQLAlchemy ORM for database access
- Pydantic for data validation and serialization
- PyJWT for JWT token handling
- passlib with bcrypt for password hashing
- psycopg2 or asyncpg for PostgreSQL connection
- python-multipart for form data handling
- Alembic for database migrations

**Frontend Stack:**

- React 18+ with TypeScript
- Vite for build tooling
- React Router for navigation
- Axios for API calls
- Tailwind CSS or Material-UI for styling

**Database:**

- PostgreSQL 15+
- Alembic for database migrations (SQLAlchemy)

**Deployment:**

- Docker Compose for local development
- Separate Dockerfiles for production builds

## Future Enhancements (Post-MVP)

- Kafka streaming for real-time processing
- Python ML service for anomaly detection (scikit-learn/PyTorch)
- Redis caching layer
- Explainable AI outputs
- Advanced audit logging
- Real-time notifications
- More sophisticated fraud rules

### To-dos

- [x] Create monorepo directory structure (backend/, frontend/, docker/)
- [x] Initialize Python FastAPI project with requirements.txt
- [x] Initialize React + TypeScript project with Vite
- [x] Create Docker Compose configuration
- [x] Create .gitignore and README