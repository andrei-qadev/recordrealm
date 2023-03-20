from tests.utils.db_engine import engine


def clear_all():
    conn = engine.connect()
    conn.execute("DELETE FROM user_data.wishlists;")
    conn.execute("DELETE FROM user_data.collections;")
    conn.execute("DELETE FROM user_data.users;")
    conn.execute("ALTER SEQUENCE user_data.users_id_seq RESTART WITH 1;")
    conn.execute("ALTER SEQUENCE user_data.collections_id_seq RESTART WITH 1;")
    conn.execute("ALTER SEQUENCE user_data.wishlists_id_seq RESTART WITH 1;")
    conn.close()
