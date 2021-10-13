import sqlite3
from .db_session import db
from .main_menu import get_user

conn = db
c = conn.cursor()

#creates table for friends
#request key: 0- No request sent/ Request declined. 1- Request sent but not yet accepted/declined. 2- Request accepted/friends
def create_friends_table():
    query = """CREATE TABLE IF NOT EXISTS Friends(userOne TEXT, userRequested TEXT, request INTEGER)"""
    c.execute(query)
    conn.commit()


#inserts data into new row of friends table
def friends_entry(userOne, userRequested, request):
    data = (userOne, userRequested, request)
    query = """INSERT INTO Friends(userOne, userRequested, request) VALUES (?,?,?)"""
    c.execute(query, data)
    conn.commit()


