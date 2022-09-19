from sqlalchemy.orm import Session
from token.jwt import verify_password

def authenticate_user(db: Session, uid: str, password: str):
    user = get_user_by_uid(db, uid)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
