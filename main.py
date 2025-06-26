from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id)

@app.post("/classes/")
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db, class_)

@app.put("/classes/{class_id}")
def update_class(class_id: int, class_: schemas.ClassUpdate, db: Session = Depends(get_db)):
    return crud.update_class(db, class_id, class_)

@app.delete("/classes/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    return crud.delete_class(db, class_id)

@app.post("/register/")
def register_student(data: schemas.Registration, db: Session = Depends(get_db)):
    return crud.register_student_to_class(db, data.student_id, data.class_id)

@app.get("/classes/{class_id}/students")
def get_students(class_id: int, db: Session = Depends(get_db)):
    return crud.get_students_in_class(db, class_id)
