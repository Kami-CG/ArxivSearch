from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


Base = declarative_base()


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    url_source = Column(String, index=True)
    updated = Column(DateTime)
    published = Column(DateTime)
    title = Column(String)
    summary = Column(String)
    authors = Column(String)


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def adding_entries(entries_list):
    session = SessionLocal()
    try:
        for _, article in entries_list.iterrows():
            new_entry = Entry(
                url_source=article["url_source"],
                updated= datetime.strptime(article["updated"], "%Y-%m-%dT%H:%M:%SZ"),
                published= datetime.strptime(article["published"], "%Y-%m-%dT%H:%M:%SZ"),
                title=article["title"],
                summary=article["summary"],
                authors=article["authors"]
            )

            session.add(new_entry)
        session.commit()

        db_entries = session.query(Entry).all()
        for entry in db_entries:
            print(
                f"ID: {entry.id}, URL Source: {entry.url_source}, Updated: {entry.updated}, Published: {entry.published}, Title: {entry.title}, Summary: {entry.summary}, Authors: {entry.authors}")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()
