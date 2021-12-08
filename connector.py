import psycopg
from params import Params

PARAMS = Params()
TABLE_NAME = "vacantes"

def get_connection():
    conn_str = f"postgresql://{PARAMS.sql_user}:{PARAMS.sql_password}@{PARAMS.sql_host}/{PARAMS.sql_database}"    
    conn = psycopg.connect(conninfo=conn_str, autocommit=True)
    return conn

def get_cursor(conn) :
    cursor = conn.cursor()
    return cursor
    
def close_connection(conn):
    conn.close()
    
def create_table(cursor):
        # Execute a command: this creates a new table
        cursor.execute(f"DROP TABLE IF EXISTS {PARAMS.sql_table}")
        
        cursor.execute(f"""
            CREATE TABLE {PARAMS.sql_table} (
                id uuid PRIMARY KEY,
                name text,
                uri text,
                location text,
                country text,
                description text
                )
            """)    
        
def add_rows(cursor, records):
    with cursor.copy(f"COPY {PARAMS.sql_table} (id, name, uri, location, country, description) FROM STDIN") as copy:
        for record in records:
            copy.write_row((record["id"],record["name"],record["uri"],record["location"],record["country"],record["description"]))
            
            
def export_data(cursor, file):
    with open(file, "wb") as f:
        with cursor.copy(f"COPY {PARAMS.sql_table} TO STDOUT") as copy:
            for data in copy:
                f.write(data)