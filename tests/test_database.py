import sys
sys.path.append(".")

from src.model.database import Database

def test_check_connection():
    database = Database()
    assert database.check_connection() is True