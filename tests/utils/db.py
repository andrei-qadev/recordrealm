from dataclasses import dataclass
from typing import Union

from sqlalchemy import create_engine
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}" \
               f"@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"

engine = create_engine(DATABASE_URL)


def restore_db():
    with engine.connect() as db:
        try:
            db.execute("TRUNCATE TABLE users, collections, wishlist")
            db.execute("INSERT INTO users (id, email, password, name, role)"
                       "VALUES (1, 'test_email@gmail.com', '$2b$12$gfHHshLFYFjk9yOTuPpnneKHt4Vs8KUoeUKqvP/V40gLJRFd/uU52', 'test_user', 'user')")

        except Exception as ex:
            raise Exception("Couldn't restore test DB")


def fetch_user_data_by_id(user_id):
    with engine.connect() as db:
        try:
            r_db = db.execute(f"SELECT * FROM users WHERE id = '{user_id}'").fetchone()
            return r_db
        except Exception as ex:
            raise Exception(ex)


if __name__ == "__main__":
    restore_db()
