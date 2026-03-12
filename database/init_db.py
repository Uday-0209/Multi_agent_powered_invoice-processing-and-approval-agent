from database.connection import engine
from database.session import Base

# IMPORTANT
import database.models


def init_db():
    print("Creating tables...")
    print("Tables detected:", Base.metadata.tables.keys())

    Base.metadata.create_all(bind=engine)

    print("Done!")


if __name__ == "__main__":
    init_db()