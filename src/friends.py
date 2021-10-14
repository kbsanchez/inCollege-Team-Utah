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
def read_friend_requests(user):
    myFriendRequests = []
    query = """SELECT userOne FROM Friends WHERE request = 1 AND userRequested = ?"""
    for student in c.execute(query, user):
        myFriendRequests.append(student)
    if(len(myFriendRequests) > 0):
        print("You have " + str(len(myFriendRequests)) + " new friend requests from ")
        for request in range(len(myFriendRequests)):
            print(request, end=" ")


#generate friends list
def my_friends_list():
    friendsList = []
    friendsTableList = [["", "", 0]]
    user = get_user()

    #creates list of all rows where current logged in user appears
    query = """SELECT userOne, userRequested, request FROM Friends WHERE request = 2"""
    for row in c.execute(query):
        friendsTableList.append(row)

    #filters user that the logged in user is friends with into a different list
    for i in range(len(friendsTableList)):
        if (user == friendsTableList[i][1]):
            friendsList.append(friendsTableList[i][2])
        elif (user == friendsTableList[i][2]):
            friendsList.append(friendsTableList[i][1])


