from sqlalchemy.orm import Session
from app.user.model import User
from app.user.schema import UserCreate


def get_user_by_uid(db: Session, uid: int):
    return db.query(User).filter(UserCreate.uid == uid).first()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        name=user.name, 
        uid=user.uid, 
        password=user.password, 
        number=user.number,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
