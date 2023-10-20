import os

from dotenv import load_dotenv
import mongoengine

load_dotenv()

__all__ = ["connect_to_db"]


def connect_to_db():
    """
    This function is used to connect to the database if it's not already connected.
    It won't raise any exception if it's already connected.
    """

    try:
        mongoengine.connection.get_connection()
    except mongoengine.connection.ConnectionFailure:
        connect()


def connect():
    try:
        mongoengine.connect(os.getenv("MONGO_DB"), host=os.getenv("MONGO_URI"))
        print(
            f"✅ Successfully connected to MongoDB at {os.getenv('MONGO_URI')}/{os.getenv('MONGO_DB')}"
        )

    except Exception as e:
        print("Failed to connect to the database", e)
