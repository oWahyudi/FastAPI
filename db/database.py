from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



Base=declarative_base()

SQLALCHEMY_DATABASE_URL="sqlite:///./fastapi-practice.db"
engine=create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
)
sessionLocal=sessionmaker(autoflush=False,bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()



