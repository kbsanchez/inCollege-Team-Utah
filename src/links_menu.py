from .menu import Menu
from typing import Optional
from .db_session import db
from colorama import Fore, Style


class LinksMenu(Menu):
    """inCollege links menu class"""
    def __init__(self) -> None:
        super().__init__()
        self.title = "InCollege Important Links"
        self.options["About"] = AboutMenu().run
        self.options["Copyright Notice"] = CopyrightNoticeMenu().run
        self.options["Accessibility"] = AccessibilityMenu().run
        self.options["User Agreement"] = UserAgreementMenu().run
        self.options["Privacy Policy"] = PrivacyPolicyMenu().run
        self.options["Cookie Policy"] = CookiePolicyMenu().run
        self.options["Copyright Policy"] = CopyrightPolicyMenu().run
        self.options["Brand Policy"] = BrandPolicyMenu().run
        self.options["Languages"] = LanguagesMenu().run


class CopyrightNoticeMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Copyright Notice"
        self.subtitle = "This is a copyright notice"


class AboutMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "About"
        self.subtitle = "This is the about section"


class AccessibilityMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Accessibility"
        self.subtitle = "This is the accessibility menu"


class UserAgreementMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "User Agreement"
        self.subtitle = "This is the user agreement menu"


class PrivacyPolicyMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Privacy Policy"
        self.subtitle = "This is the privacy policy"
        self.options["Guest Controls"] = GuestControlsMenu().run


class CookiePolicyMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Cookie Policy"
        self.subtitle = "This is our cookie policy"


class CopyrightPolicyMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Copyright Policy"
        self.subtitle = "This is our copyright policy"


class BrandPolicyMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Brand Policy"
        self.subtitle = "This is our brand policy"


class GuestControlsMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Guest Controls"

        # database variables
        self.username: str = str()
        self.has_email: Optional[bool] = True
        self.has_sms: Optional[bool] = True
        self.has_marketing: Optional[bool] = True
        self.logedin: Optional[bool] = False

        # menu options
        self.options["Toggle InCollege Email"] = self._toggle_email
        self.options["Toggle SMS"] = self._toggle_sms
        self.options["Toggle Targeted Marketing Features"] = self._toggle_marketing

    def read_db(self) -> None:
        """read values from database"""
        cursor = db.cursor()
        query: str = "SELECT username, email, sms, marketing FROM Username WHERE logedin=1;"
        cursor.execute(query)
        result = cursor.fetchone()
        if result is not None:
            self.username, self.has_email, self.has_sms, self.has_marketing = result
            self.logedin = True
        else:
            # user is not signed in
            self.logedin = False

    def write_db(self):
        """write values to database"""
        cursor = db.cursor()
        query: str = "UPDATE Username SET email=?, sms=?, marketing=? WHERE username=?;"
        cursor.execute(query, (self.has_email, self.has_sms, self.has_marketing, self.username))
        db.commit()

    def _toggle_email(self) -> False:
        self.has_email ^= 1
        status = "on" if self.has_email else "off"
        print(f"{Fore.GREEN}Email switched {status} {Style.RESET_ALL}\n")

    def _toggle_sms(self):
        self.has_sms ^= 1
        status = "on" if self.has_sms else "off"
        print(f"{Fore.GREEN}SMS switched {status} {Style.RESET_ALL}\n")

    def _toggle_marketing(self):
        self.has_marketing ^= 1
        status = "on" if self.has_marketing else "off"
        print(f"{Fore.GREEN}Targeted marketing switched {status} {Style.RESET_ALL}\n")        

    def run(self) -> None:
        self.read_db()
        super(GuestControlsMenu, self).run()
        self.write_db()


class LanguagesMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Languages"

        # database variables
        self.username: str = str()
        self.language: str = str()
        self.logedin: Optional[bool] = None

        # menu options
        self.options["English"] = self._set_lang_english  # TODO Joseph 9/29: abstract
        self.options["Spanish"] = self._set_lang_spanish

    def read_db(self) -> None:
        """read values from database"""
        cursor = db.cursor()
        query: str = "SELECT Username, language FROM Username WHERE logedin=1;"
        cursor.execute(query)
        result = cursor.fetchone()
        if result is not None:
            self.username, self.language = result
            self.logedin = True
        else:
            self.logedin = False

    def write_db(self):
        """write values to database"""
        cursor = db.cursor()
        query: str = "UPDATE Username SET language=? WHERE username=?;"
        cursor.execute(query, (self.language, self.username))
        db.commit()

    def _set_lang_english(self):
        print(f"{Fore.GREEN}Language changed to English{Style.RESET_ALL}\n")
        self.language = 'english'

    def _set_lang_spanish(self):
        print(f"{Fore.GREEN}Language changed to Spanish{Style.RESET_ALL}\n")
        self.language = 'spanish'

    def run(self) -> None:
        self.read_db()
        super(LanguagesMenu, self).run()
        self.write_db()
