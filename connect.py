import psycopg2

from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        """ create a database connection to a SQLite database """
        conn = psycopg2.connect(host="localhost", database="Students", user="postgres", password="12345678")
        yield conn
        conn.close
    except psycopg2.OperationalError as err:
        raise RuntimeError(f'{err}')
