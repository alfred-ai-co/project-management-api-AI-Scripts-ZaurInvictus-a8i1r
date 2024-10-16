from app.db_models.session import SessionLocal


# Dependency to get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

