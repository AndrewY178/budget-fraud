from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.models import User, Category, Transaction, FraudAlert

app = FastAPI(
    title="Fraud Budget Balancer API",
    description="Personal Finance + Fraud Detection Engine",
    version="1.0.0"
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Fraud Budget Balancer API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

