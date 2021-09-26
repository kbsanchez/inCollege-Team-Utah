import sqlite3
from getpass import getpass
from src.main_menu import main_menu

conn = sqlite3.connect('Username.db')
c = conn.cursor()

#creates new table for usernames and passwords
def create_table():
    query = """CREATE TABLE IF NOT EXISTS Username(username TEXT, password TEXT)"""
    c.execute(query)
    conn.commit()

#inserts login info from user into table
def data_entry(username, password):
    query = """INSERT INTO Username (username, password) VALUES(?, ?);"""
    data = (username, password)
    c.execute(query, data)
    conn.commit()

#function to check if the username is unique when creating an account
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

#function to check that all passwords meet the required criteria
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
                print("Password must be at least 8 and no more than 12 characters in length.")
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

#function to check the amount of accounts that have been created
def number_rows():
    query = """SELECT * FROM Username"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    #print("The number of rows is ", rows)
    return rows

#function to login into the program for user that have already created an account
def login_attempt(username, password):
    query = """SELECT * FROM Username WHERE username = ? AND password = ?;"""
    data = (username, password)
    c.execute(query, data)
    conn.commit()
    tuple = c.fetchall()
   
    return len(tuple) != 0

#CHOICE IS A CHAR THAT HELPS NAVIGATE THROUGH THE PROGRAM MENU
def main():
    choice = '?'

    while choice != 'q':
        print("\n")
        print("          MENU     ")
        print("n - Create new account")
        print("l - Login")
        print("q - Quit")
        print("\n")

        question = input("Please make a choice from the menu: ")
        
        choice = question

    #QUITS THE PROGRAM
        if choice == 'q':
            exit()

    #CREATES NEW ACCOUNT
        elif choice == 'n':
            create_table()
            capacity = number_rows()
            if capacity < 5:
                print("\n")
                print("Please input a unique username and password")
                username = input("Username: ")
                username2 = look_value(username)
                password = getpass()
                check_pw(password)
                data_entry(username2, password)
            elif capacity == 5:
                print("The amount of allowed accounts (5) has been reached")
                continue


    #LOGIN TO PROGRAM
        elif choice == 'l':
            username = input("Username: ")
            password = getpass()
            isLoggedIn = login_attempt(username, password)

            if isLoggedIn:
                print("You have successfully logged in")
                main_menu()
            else:
                print("Incorrect username/password, please try again")
                
        else:
            print("Invalid choice. Please pick an option from the menu.")

if __name__ == '__main__':  #pragma: no cover
    main()
