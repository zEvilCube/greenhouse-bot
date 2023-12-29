from database import get_session
from database.models import Auth


def get_key(user_id: int) -> str:
    with get_session() as session:
        auth = session.query(Auth).filter_by(user_id=user_id).first()
        return auth.api_key if auth is not None else None


def register_key(user_id: int, api_key: str) -> None:
    with get_session() as session:
        auth = Auth(user_id=str(user_id), api_key=api_key)
        session.merge(auth)
        session.commit()
