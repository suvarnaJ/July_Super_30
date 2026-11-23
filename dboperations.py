import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:xxxxxxxxxxxx@xxxxxxxxxxxx.c-4.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_all_students():
    db = SessionLocal()

    try:
        students = db.query(student).all()

        print("Students:")
        for student in students:
            print(student)

        return students

    except Exception as e:
        print("Error fetching students:", e)
        return []

    finally:
        db.close()

    
