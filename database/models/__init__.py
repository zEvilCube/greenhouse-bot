from sqlalchemy import Column, Engine, BigInteger, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Auth(Base):
    __tablename__ = "auth"

    user_id = Column(BigInteger, primary_key=True)
    api_key = Column(Text, nullable=False)


def init(engine: Engine):
    Base.metadata.create_all(bind=engine)
