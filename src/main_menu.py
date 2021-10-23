#made a connection to main.py Username.db and added a function to count the jobs posted to enforce limit
import sqlite3
from .links_menu import LinksMenu
from .profile_menu import ProfileMenu

conn = sqlite3.connect('Username.db')
c = conn.cursor()

def number_job_rows():
    query = """SELECT * FROM Jobs"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    #print("The number of rows is ", rows)
    return rows

#retrieves username of logged in person
def get_user():
    query = """SELECT username FROM Username WHERE logedin = 1"""
    c.execute(query)
    conn.commit()
    tuple = c.fetchone()
    #print(type(tuple))
    return tuple
#

#
#Query for posting a job and creating a new job tables if it has not being created yet
def create_job_table():
    query = """CREATE TABLE IF NOT EXISTS Jobs(username TEXT, title TEXT, description TEXT, employer TEXT, location TEXT, salary REAL)"""
    c.execute(query)
    conn.commit()

def job_entry(username, title, description, employer, location, salary):

    data = (username, title, description, employer, location, salary)
    query = """INSERT INTO Jobs(username,title,description,employer,location,salary) VAlUES(?,?,?,?,?,?);"""
    c.execute(query,data)
    conn.commit()
#


def get_user_selection():
    selection_text = input("Please make a choice from the menu: ")
    return int(selection_text)

#NEW MENU CREATED
#POST A JOB WORK DONE HERE
def job_intern_menu():
    choice = 0
    while choice != 2:

        print("""
1 - Post a job 
2 - Go back

"""        )
        selection = get_user_selection()
        if selection == 1:
            create_job_table()
            jobs_posted = number_job_rows()
            if jobs_posted == 5:
                print("The maximum amount of jobs posted have been reached. Please come back again later.")
                return
            job_title = input("Job Title: ")
            job_description = input("Job Description: ")
            employer = input("Employer: ")
            location = input("Location: ")
            salary = input("Salary: ")
            username ,= get_user()
            job_entry(username,job_title,job_description,employer,location,salary)
        elif selection == 2:
            return
        else:
            print("Invalid Input. Please choose 1 or 2.")
#

#MENU SHOWED AFTER SELECTING "LEARN A NEW SKILL"
def learn_skills_menu():
    while True:
        print(
            """
1 - Networking
2 - Time Management
3 - Public Speaking
4 - Agile and Scrum
5 - Leadership
6 - Go Back
"""
        )

        selection = None

        try:
            selection = get_user_selection()
        except:
            print("Invalid selection")
            continue
        if selection == 6:
            return
        elif selection > 6:
            print("Invalid selection")
        else:
            print("Under Construction")

#LOGOUT OPTION THAT SHOULD LEAD TO MENU BEFORE YOU LOGIN
def logout():
    print("Thank you for using InCollege!")

print()
#MENU SHOWN AFTER YOU SUCCESFULLY LOGIN
optionsAndActions = [
    ("View/Edit Profile", ProfileMenu().run),
    ("Job/Internship Search", job_intern_menu),
    ("Find Someone You Know", None),
    ("Learn a New Skill", learn_skills_menu),
    ("InCollege Important links", LinksMenu().run),
    ("Log Out", logout)
]

#FUNCTION TO ENUMARATE THE OPTIONS FROM OPTIONS AND ACTIONS 2 DIMENSIONAL ARRAY
def print_menu_options():
    options = [
        f"{i + 1} - {x[0]}"
        for i, x
        in enumerate(optionsAndActions)
    ]
    options_text = "\n".join(options)

    print(options_text)

#FUNCTION TO GET THE SELECTION FROM PRINT_MENU_OPTIONS
def get_user_action_selection():
    selection = get_user_selection() - 1

    try:
        if selection < 0:
            raise Exception()

        action = optionsAndActions[selection][1]

        if action is None:
            print("Under Construction")

        return action

    except:
        print("Invalid selection")

#MAIN MENU FUNCTION THAT CALLS ALL THE OTHER MISCELANIOUS MENU FUNCTIONS
def main_menu():

    #user = get_user()

    while True:
        #read_friend_requests(user)
        print("\n")
        print_menu_options()
        print("\n")

        action = get_user_action_selection()

        if action is not None:
            action()

        if action == logout:
            return
