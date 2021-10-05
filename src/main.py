import sqlite3
from getpass import getpass

from .links_menu import LinksMenu
from .db_session import db
from .main_menu import main_menu

conn = db
c = conn.cursor()

# creates new table for usernames and passwords


def create_table():
    query = """CREATE TABLE IF NOT EXISTS Username(username TEXT, password TEXT,firstname TEXT, lastname TEXT, logedin INTEGER)"""
    c.execute(query)
    conn.commit()

# inserts login info from user into table


def data_entry(username, password, firstname, lastname, logedin):
    query = """INSERT INTO Username (username, password,firstname,lastname, logedin) VALUES(?,?,?,?,?);"""
    data = (username, password, firstname, lastname, logedin)
    c.execute(query, data)
    conn.commit()

# function to check if the username is unique when creating an account


def look_value(username):
    username2 = username
    target = (username,)
    query = """SELECT * FROM Username WHERE username = ?;"""
    c.execute(query, target)
    conn.commit()
    tuples = c.fetchall()
    while len(tuples) > 0:
        print("Username already exist.")
        username2 = input("Username: ")
        target = (username2,)
        c.execute(query, target)
        conn.commit()
        tuples = c.fetchall()
    if len(tuples) == 0 and username == username2:
        return username
    elif len(tuples) == 0 and username != username2:
        return username2

# function to check that all passwords meet the required criteria


def check_pw(password):
    Capital = False
    digit = False
    alnum = False
    while Capital == False and digit == False and alnum == False:
        for i in password:
            if i.isupper():
                Capital = True
            if i.isdigit():
                digit = True
            if not i.isalnum():
                alnum = True
        if Capital == True and digit == True and alnum == True:
            if len(password) < 8 or len(password) > 12:
                print(
                    "Password must be at least 8 and no more than 12 characters in length.")
                password = getpass()
                check_pw(password)
        elif Capital != True:
            print("Password must contain at least one capital letter")
            password = getpass()
            check_pw(password)
        elif digit != True:
            print("Password must contain at least one digit")
            password = getpass()
            check_pw(password)
        elif alnum != True:
            print("Password must contain at least one alphanumeric symbol")
            password = getpass()
            check_pw(password)

# function to check the amount of accounts that have been created


def number_rows():
    query = """SELECT * FROM Username"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    #print("The number of rows is ", rows)
    return rows


def find_in_db(first_name, last_name):

    for row in c.execute("""SELECT * FROM Username"""):
        if first_name == row[2] and last_name == row[3]:
            print("They are a part of the InCollege system")
            return
    print("They are not yet a part of the InCollege system yet")

# function to login into the program for user that have already created an account


def login_attempt(username, password):
    query = """SELECT * FROM Username WHERE username = ? AND password = ?;"""
    data = (username, password)
    c.execute(query, data)
    conn.commit()
    tuple = c.fetchall()

    return len(tuple) != 0

# function that changes logedin value in order to know what user is logedin


def login(username):
    query = """UPDATE Username SET logedin = 1 WHERE username = ?"""
    target = (username,)
    c.execute(query, target)
    conn.commit()


def general():
    choice = '*'
    while choice != 'q':
        print("1- Sign Up\n2- Help Center\n3- About\n4- Press,\n5- Blog,\n6- Careers,\n7- Developers\nq- quit")
        choice = input("Please select a option:")

        if choice == '1':
            createnewacc()
        if choice == '2':
            print("We're here to help")
        if choice == '3':
            print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
        if choice == '4':
            print(
                "In College Pressroom: Stay on top of the latest news, updates, and reports")
        if choice == '5':
            print("Under construction")
        if choice == '6':
            print("Under construction")
        if choice == '7':
            print("Under construction")
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice. Please pick an option from the menu.")


def usefulllinks():
    choice = '*'
    while choice != 'q':
        print("1 - general")
        print("2 - browse InCollege")
        print("3 - business solutions")
        print("4 - directories")
        print("q- quit")

        choice = input("Please select a option:")

        if choice == '1':
            general()
        if choice in ['2', '3', '4']:
            print("under construction")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please pick an option from the menu.")


def createnewacc():
    create_table()
    capacity = number_rows()
    if capacity < 5:
        print("\n")
        print("Please input a unique username and password")
        username = input("Username: ")
        first_name = input("first name: ")
        last_name = input("last name: ")
        username2 = look_value(username)
        password = getpass()
        logedin = 0
        check_pw(password)
        data_entry(username2, password, first_name, last_name, logedin)
    elif capacity == 5:
        print("The amount of allowed accounts (5) has been reached")


# CHOICE IS A CHAR THAT HELPS NAVIGATE THROUGH THE PROGRAM MENU
def main():
    choice = '?'

    print("Jacob had dreamed about working at Southwest Airlines for as long as he can remember. He applied and interviewed for internships and full-time jobs to no avail. But after each meeting, he connected with each Southwest employee and recruiter on CollegeIn. With a growing family to support, he eventually accepted a job at a B2B IT company. Then one day he noticed that CollegeIn's people you may knowmodule suggested he connect with a Southwest recruiter he was linked to through another connection. He sent the recruiter a connection request and she responded asking if he had time to chat about a job opening. On Aug. 27, 2021, Jacob joined Southwest.")

    while choice != 'q':
        print("\n")
        print("          MENU     ")
        print("n - Create new account")
        print("l - Login")
        print("q - Quit")
        print("f - find a friend")
        print("s - play a video of success story")
        print("i - InCollege Important Links")
        print("u - usefull links")
        print("\n")

        question = input("Please make a choice from the menu: ")

        choice = question

        if choice == 'f':
            first_name = input("enter first name:")
            last_name = input("enter last name:")
            find_in_db(first_name, last_name)
            previous_page = input("please enter to the previous page")
        if choice == 's':
            print("video is now playing")
            Previous_page=input("press enter to the previous page")
        if choice == 'i':
            LinksMenu().run()
            Previous_page = input("press enter to the previous page")
        if choice == 'u':
            usefulllinks()

    # QUITS THE PROGRAM
        if choice == 'q':
            exit()

    # CREATES NEW ACCOUNT
        elif choice == 'n':
            createnewacc()

    # LOGIN TO PROGRAM
        elif choice == 'l':
            username = input("Username: ")
            password = getpass()
            isLoggedIn = login_attempt(username, password)

            if isLoggedIn:

                login(username)
                print("You have successfully logged in")
                main_menu()
            else:
                print("Incorrect username/password, please try again")

        else:
            print("Invalid choice. Please pick an option from the menu.")


if __name__ == '__main__':  # pragma: no cover
    main()
