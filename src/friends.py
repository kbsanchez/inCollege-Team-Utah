from .db_session import db
from .main_menu import get_user
from typing import Optional

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


#returns username of student that a user searches for to send a friend request if it matches a user within the inCollege system.
def search_for_user():
    choice = 0
    while(choice != 4):
        choice = int(input("1. Search by last name \n"
                       "2. Search by university \n"
                       "3. Search by major \n"
                       "4. Go back\n"
                       "Please make a selection: "))

        if(choice == 1):
            lastName = input("Enter a student's last name: ")
            query = """SELECT username FROM Username WHERE lastname = ?"""
            c.execute(query, lastName)
            result: Optional[tuple] = c.fetchone()
        elif(choice == 2):
            university = input("Enter a student's university: ")
            query = """SELECT username FROM Profile WHERE universityName = ?"""
            c.execute(query, university)
            result: Optional[tuple] = c.fetchone()
        elif(choice == 3):
            major = input("Enter a student's major: ")
            query = """SELECT username FROM Profile WHERE major = ?"""
            c.execute(query, major)
            result: Optional[tuple] = c.fetchone()
        elif(choice == 4):
            return

        if result is None:
            print("There are no students registered with that data. ")
            return
        else:
            return result


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
        if (user == friendsTableList[i][0]):
            friendsList.append(friendsTableList[i][1])
        elif (user == friendsTableList[i][1]):
            friendsList.append(friendsTableList[i][0])

#delete friend from list
def delete_my_friends(friend):
    query = """DELETE FROM Friends WHERE user = friend"""
    for row in c.execute(query):
        my_friends_list().friendsTableList.delete(row)

def show_my_network():
    for i in range(len(my_friends_list().friendsTableList)):
        print(my_friends_list().friendsTableList[i][i])

    user_to_delete = input("If you would like to delete anyone from your list, type their name: ")
    delete_my_friends(user_to_delete)
    

