"""
Database initialization script.
Creates tables and seeds initial categories.
"""
from app.database import engine, Base
from app.models import Category, CategoryType
from sqlalchemy.orm import Session
from app.database import SessionLocal

def init_db():
    """Create all tables"""
    Base.metadata.create_all(bind=engine)

def seed_categories():
    """Seed initial categories"""
    db: Session = SessionLocal()
    try:
        # Check if categories already exist
        if db.query(Category).count() > 0:
            print("Categories already seeded")
            return
        
        # Expense categories
        expense_categories = [
            "Food & Dining",
            "Transportation",
            "Entertainment",
            "Shopping",
            "Bills & Utilities",
            "Healthcare",
            "Education",
            "Travel",
            "Personal Care",
            "Other Expenses"
        ]
        
        # Income categories
        income_categories = [
            "Salary",
            "Freelance",
            "Investment",
            "Gift",
            "Other Income"
        ]
        
        # Create expense categories
        for name in expense_categories:
            category = Category(name=name, type=CategoryType.EXPENSE)
            db.add(category)
        
        # Create income categories
        for name in income_categories:
            category = Category(name=name, type=CategoryType.INCOME)
            db.add(category)
        
        db.commit()
        print(f"Seeded {len(expense_categories) + len(income_categories)} categories")
    except Exception as e:
        print(f"Error seeding categories: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Seeding categories...")
    seed_categories()
    print("Database initialization complete!")

