from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/askhub.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import askhub.models

    Base.metadata.create_all(bind=engine)
