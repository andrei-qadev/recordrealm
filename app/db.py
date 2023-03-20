import databases
import sqlalchemy
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}" \
               f"@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"

database = databases.Database(url=DATABASE_URL)
mb_metadata = sqlalchemy.MetaData(schema='mb_data')
rr_metadata = sqlalchemy.MetaData(schema='user_data')
