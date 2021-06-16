import sqlite3
from sqlite3 import Error
from config import SQLITE_DATABASE


def initialize():
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

    else:
        print("Error! cannot create the database connection.")


def get_conn(database=SQLITE_DATABASE):
    conn = create_connection(database)
    return conn


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
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
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_token(conn, token):
    try:
        sql = f"""INSERT INTO tokens(token) 
                  VALUES('{token}')"""
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)