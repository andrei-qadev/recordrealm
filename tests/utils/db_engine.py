from sqlalchemy import create_engine
from app.db import DATABASE_URL

engine = create_engine(url=DATABASE_URL)
