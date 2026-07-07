from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate
from utils.security import hash_password
from utils.security import hash_password, verify_password
from utils.jwt_handler import create_access_token


def register_user(db: Session, user: UserCreate):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def login_user(db: Session, username: str, password: str):

    user = db.query(User).filter(
        User.email == username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }