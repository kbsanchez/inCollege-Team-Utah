from .menu import Menu
from .db_session import db
from .exp_n_edu import exp_n_edu_menu
from typing import Optional, Tuple
from columnar import columnar


class ProfileMenu(Menu):
    def __init__(self) -> None:
        super().__init__()

        # database variables
        self.firstname = str()
        self.lastname = str()
        self.username = str()
        self.user_title = str()
        self.user_major = str()
        self.user_university_name = str()
        self.user_about = str()
        self.user_expeirences = list()
        self.user_education = list()
        self.has_profile = False

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

            self.username, self.firstname, self.lastname = result
            query = """
            SELECT * FROM Profile
            WHERE username = ?
            """
            cursor.execute(query, (self.username, ))
            result: Optional[Tuple] = cursor.fetchone()

        if result is None:
            return

        self.has_profile = True
                self.username, self.user_title, self.user_major, \
                self.user_university_name, self.user_about = result
            self.read_education_db()
            self.read_experience_db()

        # title should be the user's name
        self.title = f"{self.firstname} {self.lastname}"
        self.subtitle = self.get_profile_text()

    def read_experience_db(self) -> None:
        """get user experience info from database"""
        cursor = db.cursor()
        query = """SELECT title, employer, startDate, endDate, 
        location, description FROM Experience WHERE username=?"""
        cursor.execute(query, (self.username,))
        self.user_expeirences = cursor.fetchall()

    def read_education_db(self) -> None:
        """get user education info from database"""
        cursor = db.cursor()
        query = """SELECT schoolName, degree, yearsAttended 
        FROM Education WHERE username=?"""
        cursor.execute(query, (self.username,))
        self.user_education = cursor.fetchall()        

    def write_db(self) -> None:
        """write values to database"""
        cursor = db.cursor()
        query: str = """INSERT OR REPLACE INTO 
        Profile(username, title, major, universityName, about) 
            VALUES(?, ?, ?, ?, ?)
            """
        cursor.execute(query, (self.username, self.user_title, self.user_major,
        self.user_university_name, self.user_about))
        db.commit()

    def get_profile_text(self) -> str:
        """string form of user's profile data"""
        if not self.has_profile:
            return "No profile set up!"

        # align text
        return f"{'Title:':<15}{self.user_title}\n" + \
        f"{'Major:':<15}{self.user_major}\n" + \
        f"{'University:':<15}{self.user_university_name}\n" + \
        f"{'About:':<15}{self.user_about}\n" + \
            f"{'Experiences:':<15}\n{self.get_experience_text()}\n" + \
        f"{'Education:':<15}\n{self.get_education_text()}\n"

    def get_experience_text(self) -> str:
        """return well formatted string of user's experience data"""
        if len(self.user_expeirences) == 0:
            return "None"

        headers = ['Title', 'Employer', 'Start date',
                   'End date', 'Location', 'description']
        return columnar([list(experience) for experience in self.user_expeirences], headers, no_borders=True)
    
    def get_education_text(self) -> str:
        """return well formatted string of user's education data"""
        if len(self.user_education) == 0:
            return "None"

        headers = ['School name', 'Degree', 'Years attended']
        return columnar([list(education) for education in self.user_education], headers, no_borders=True)

    def edit_profile(self) -> None:
        """Allow user to make changes to their profile"""
        self.user_title = input("Enter title: ")
        self.user_major = input("Enter major: ").title()
        self.user_university_name = input("Enter univeristy name: ").title()
        self.user_about = input("Enter about: ")
        exp_n_edu_menu()  # get experiences and education
        self.read_experience_db()  # update experiences info
        self.read_education_db()  # update education info
        self.subtitle = self.get_profile_text()  # update profile

    def run(self) -> None:
        self.read_db()
        super(ProfileMenu, self).run()
        self.write_db()        
