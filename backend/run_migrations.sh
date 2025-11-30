#!/bin/bash
# Script to run Alembic migrations

echo "Running database migrations..."
alembic upgrade head

echo "Seeding initial categories..."
python -m app.init_db

echo "Done!"

