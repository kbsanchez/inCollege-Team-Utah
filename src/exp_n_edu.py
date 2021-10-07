import sqlite3
from db_session import db


conn = db
c = conn.cursor()

#creates a username table and inserts sample data for testing functionality of file
# def testing_data_entry():
#     query = """CREATE TABLE IF NOT EXISTS Username(username TEXT, password TEXT,firstname TEXT, lastname TEXT, logedin INTEGER)"""
#     c.execute(query)
#     conn.commit()
#
#     query2 = """INSERT INTO Username(username, password,firstname,lastname, logedin) VALUES(?,?,?,?,?);"""
#     data = ("Sample", "Sample", "Sample", "Sample", 1)
#     c.execute(query2, data)
#     conn.commit()


#retrieves username of logged in person
def get_user():
    query = """SELECT * FROM Username WHERE logedin = 1"""
    c.execute(query)
    conn.commit()
    tuple = c.fetchone()
    return tuple


#creates a table to store experience of user
def create_exp_table():
    query = """CREATE TABLE IF NOT EXISTS Experience(username TEXT, title TEXT, employer TEXT, startDate TEXT, endDate TEXT, location TEXT, description TEXT)"""
    c.execute(query)
    conn.commit()


#inserts data into new row in experience table
def exp_entry(username, title, employer, startDate, endDate, location, description):
    data = (username, title, employer, startDate, endDate, location, description)
    query = """INSERT INTO Experience(username,title,employer, startDate, endDate, location, description) VAlUES(?,?,?,?,?,?,?);"""
    c.execute(query, data)
    conn.commit()


#returns number of entries for the experience table created by the same user
def count_exp_entries():
    query = """SELECT * FROM Experience WHERE username = (SELECT username FROM Username)"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    #print("The number of rows is ", rows)
    return rows


#creates education table
def create_edu_table():
    query = """CREATE TABLE IF NOT EXISTS Education(username TEXT, schoolName TEXT, degree TEXT, yearsAttended INTEGER)"""
    c.execute(query)
    conn.commit()


#inserts data into new row in education table
def edu_entry(username, schoolName, degree, yearsAttended):
    data = (username, schoolName, degree, yearsAttended)
    query = """INSERT INTO Education(username, schoolName, degree, yearsAttended)"""
    c.execute(query, data)
    conn.commit()


#returns user selection input
def get_user_selection():
    selection_text = input("Please make a choice from the menu: ")
    return int(selection_text)


#menu that allows for user to add experience and/or education to their profile
def exp_n_edu_menu():
    choice = 0
    #testing_data_entry()
    while choice != 3:
        print("\n1 - Add experience \n2 - Add education \n3 - Go back \n\n")
        selection = get_user_selection()
        #add experience
        if selection == 1:
            create_exp_table()
            user_exp = count_exp_entries()
            #checks if max per user has already been reached
            if user_exp == 3:
                print("The maximum amount of experience have been added to your profile. Please come back again later.")
                return
            #user-inputted data
            username = get_user()
            title = input("Job title: ")
            employer = input("Employer: ")
            startDate = input("Start date: ")
            endDate = input("End date: ")
            location = input("Location: ")
            description = input("Description: ")
            exp_entry(username, title, employer, startDate, endDate, location, description)
        #add education
        elif selection == 2:
            create_edu_table()
            username = get_user()
            schoolName = input("School name: ")
            degree = input("Degree: ")
            yearsAttended = int(input("Years attended: "))
            edu_entry(username, schoolName, degree, yearsAttended)
        #input validation
        else:
            print("Invalid input. Please make a choice from the menu options.\n")

