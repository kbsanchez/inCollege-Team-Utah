from .menu import Menu
from .db_session import db
from typing import Optional, Tuple

class ProfileMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.title = str()  # first and last name
        self.subtitle = str()

        # database variables
        self.firstname = str()
        self.lastname = str()
        self.username = str()
        self.user_title = str()
        self.user_major = str()
        self.user_university_name = str()
        self.user_about = str()
        self.user_expeirencesID = str()
        self.user_educationID = str()
        self.user_logedin = None

        # Menu options
        self.options["Edit profile"] = self.edit_profile

    def read_db(self) -> None:
        """read values from database"""
        cursor = db.cursor()
        query: str = """
        SELECT username, firstname, lastname FROM Username
        WHERE logedin=1
        """
        cursor.execute(query)
        result: Optional[Tuple] = cursor.fetchone()
        if result is not None:
            self.username, self.firstname, self.lastname = result
            query = """
            SELECT * FROM Profile
            WHERE username = ?
            """
            cursor.execute(query, (self.username, ))
            result: Optional[Tuple] = cursor.fetchone()
            if result is not None:
                self.logedin = True
                self.username, self.user_title, self.user_major, self.user_university_name, \
                self.user_about, self.user_expeirencesID, self.user_educationID = result
        else:
            # user is not logged in
            self.logedin = False

        self.title = f"{self.firstname} {self.lastname}"  # title should be the user's name
        self.subtitle = self.get_profile_text()

    def write_db(self) -> None:
        """write values to database"""
        cursor = db.cursor()
        query: str = """INSERT OR REPLACE INTO Profile(username, title, major, universityName, about,
        experiencesID, educationID) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (self.username, self.user_title, self.user_major, 
        self.user_university_name, self.user_about, self.user_expeirencesID, self.user_educationID))
        db.commit()

    def run(self) -> None:
        self.read_db()
        super(ProfileMenu, self).run()
        self.write_db()

    def get_profile_text(self) -> str:
        return f"Title: {self.user_title}\nMajor: {self.user_major}\n" + \
        f"University: {self.user_university_name}\nAbout: {self.user_about}\n"

    def edit_profile(self) -> None:
        self.user_title = input("Enter title: ")
        self.user_major = input("Enter major: ").title()
        self.user_university_name = input("Enter univeristy name: ").title()
        self.user_about = input("Enter about: ")
        
        # call experiences function

        # call education function

        self.subtitle = self.get_profile_text() # update profile