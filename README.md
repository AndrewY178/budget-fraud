# Fraud Budget Balancer

A secure system that tracks transactions, categorizes spending, and detects suspicious financial behavior in real time.

## Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: React + TypeScript (Vite)
- **Database**: PostgreSQL
- **Deployment**: Docker Compose

## Prerequisites

- Python 3.11+
- Node.js 18+ and npm
- Docker Desktop

## Quick Start

### Using Docker Compose (Recommended)

1. Clone the repository
2. Navigate to the project directory
3. Start all services:
```bash
cd docker
docker compose up
```

Services will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- PostgreSQL: localhost:5432

### Local Development

#### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
fraud-budget-balancer/
├── backend/          # FastAPI backend
├── frontend/         # React frontend
└── docker/           # Docker configurations
```

## Environment Variables

Create a `.env` file in the `docker/` directory:

```env
POSTGRES_USER=frauduser
POSTGRES_PASSWORD=fraudpass
POSTGRES_DB=fraud_budget_db
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
```

## Database Setup

### Running Migrations

After starting the services with Docker Compose, run migrations:

```bash
# Inside the backend container
docker exec -it fraud_budget_backend alembic upgrade head

# Then seed initial categories
docker exec -it fraud_budget_backend python -m app.init_db
```

Or for local development:

```bash
cd backend
alembic upgrade head
python -m app.init_db
```

### Database Schema

The database includes the following tables:
- **users**: User accounts with email and password
- **categories**: Transaction categories (income/expense)
- **transactions**: User financial transactions
- **fraud_alerts**: Fraud detection alerts linked to transactions

## API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation.

## License

MIT

