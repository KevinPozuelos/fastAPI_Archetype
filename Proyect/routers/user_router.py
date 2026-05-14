from fastapi import APIRouter
from sqlalchemy.orm import Session

from core.database import SessionLocal
from models.user_model import User
from schemas.user_schema import UserCreate

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):

    db: Session = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return new_user


@router.get("/users")
def get_users():

    db: Session = SessionLocal()

    users = db.query(User).all()

    db.close()

    return users

@router.get("/users/{user_id}")
def get_user(user_id: int):

    db: Session = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    db.close()

    if user is None:
        return {"message": "Usuario no encontrado"}

    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int):

    db: Session = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        db.close()
        return {"message": "Usuario no encontrado"}

    db.delete(user)
    db.commit()
    db.close()

    return {"message": "Usuario eliminado"}

@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    db: Session = SessionLocal()

    existing_user = db.query(User).filter(User.id == user_id).first()

    if existing_user is None:
        db.close()
        return {"message": "Usuario no encontrado"}

    existing_user.name = user.name
    existing_user.email = user.email

    db.commit()
    db.refresh(existing_user)
    db.close()

    return existing_user