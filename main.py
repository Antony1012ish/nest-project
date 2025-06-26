from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Create student
@app.post("/students/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

# 2. Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    return cru
