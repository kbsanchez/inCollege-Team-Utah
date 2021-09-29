from menu import Menu

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
        self.subtitle = "These are our guest controls"
        self.options["Toggle InCollege Email"] = self._do_nothing
        self.options["Toggle SMS"] = self._do_nothing
        self.options["Toggle Targeted Marketing Features"] = self._do_nothing


class LanguagesMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = "Languages"
        self.subtitle = "These are our guest controls"
        self.options["English"] = self._do_nothing
        self.options["Spanish"] = self._do_nothing


if __name__ == '__main__':
    LinksMenu().run()