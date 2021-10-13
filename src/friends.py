import sqlite3
from .db_session import db
from .main_menu import get_user, get_user_selection

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


#updates key in friends table to send a request to another user to become friends
def send_request(username, requestedUser):
    query = """UPDATE Friends SET request = 1 WHERE userOne = ? AND userRequested = ?"""
    target = (username, requestedUser)
    c.execute(query, target)
    conn.commit()


#updates key in friends table to decline a friend request
def decline_request(username, requestedUser):
    query = """UPDATE Friends SET request = 0 WHERE userOne = ? AND userRequested = ?"""
    target = (username, requestedUser)
    c.execute(query, target)
    conn.commit()


#updates key in friends table to accept a friend request
def accept_request(username, requestedUser):
    query = """UPDATE Friends SET request = 2 WHERE userOne = ? AND userRequested = ?"""
    target = (username, requestedUser)
    c.execute(query, target)
    conn.commit()


#reads data from friends table
def read_friend_requests():
    friendRequests = []
    user = get_user()
    query = """SELECT userOne, userRequested, request FROM Friends WHERE request = 1 AND userRequested = ?"""
    for student in c.execute(query, user):
        friendRequests.append(student)


#in progress: populate friends list
def my_friends_list():
    friendsList = []
    user = get_user()
    cursor = db.cursor()
    query = """SELECT userOne, userRequested, request FROM Friends WHERE request = 2"""
    selectUserOneQuery = """SELECT userOne FROM Friends WHERE request = 2"""
    selectUserTwoQuery = """SELECT userRequested FROM Friends WHERE request = 2"""
    for row in c.execute(query):
        return



