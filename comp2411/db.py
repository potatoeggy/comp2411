import mysql.connector
from . import sql

_db = mysql.connector.connect(
    host="localhost",
    # rest of creds here
)

def create_employee():
    ...

def reset_db():
    """
    Resets the currently active database to its initial state.
    """
    _db.cursor().execute(sql.RESET_DB)

# methods that interact w/db go in this file