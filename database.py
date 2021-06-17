import sqlite3
from sqlite3 import Error
from config import SQLITE_DATABASE


def initialize():
    """Initializes the database, creates schema"""

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS tokens(
                                        id integer PRIMARY KEY,
                                        token text NOT NULL,
                                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                        UNIQUE(token)
                                    ); """

    # create a database connection
    conn = get_conn()

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        print("Database Initialized")

    else:
        print("Error! cannot create the database connection.")


def get_conn(database=SQLITE_DATABASE):
    conn = create_connection(database)
    return conn


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file

    Args:
        db_file (str): file path of the database file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement

    Args:
        conn (Connection Object): connection object for the database
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_token(conn, token):
    """inserts a token in the database

    Args:
        token (str): token that will be stored in database

    Returns:
        status (bool): will return False in case of non-unique token is attempted
    """

    try:
        sql = f"""INSERT INTO tokens(token) 
                  VALUES('{token}')"""
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        # print(e)
        if "UNIQUE constraint failed" in str(e):
            return False


if __name__ == "__main__":
    initialize()
