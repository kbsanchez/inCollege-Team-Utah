from .context import links_menu


def test_toggle_email_on():
    menu = links_menu.GuestControlsMenu()
    menu.has_email = False
    menu._toggle_email()

    assert menu.has_email == True


def test_toggle_email_off():
    menu = links_menu.GuestControlsMenu()
    menu.has_email = True
    menu._toggle_email()

    assert menu.has_email == False


def test_toggle_sms_on():
    menu = links_menu.GuestControlsMenu()
    menu.has_sms = True
    menu._toggle_sms()

    assert menu.has_sms == False


def test_toggle_sms_off():
    menu = links_menu.GuestControlsMenu()
    menu.has_sms = False
    menu._toggle_sms()

    assert menu.has_sms == True


def test_toggle_ads_on():
    menu = links_menu.GuestControlsMenu()
    menu.has_marketing = True
    menu._toggle_marketing()

    assert menu.has_marketing == False


def test_toggle_ads_off():
    menu = links_menu.GuestControlsMenu()
    menu.has_marketing = False
    menu._toggle_marketing()

    assert menu.has_marketing == True


def test_set_language_english():
    menu = links_menu.LanguagesMenu()
    menu.language = "other language"
    menu._set_lang_english()

    assert menu.language == "english"


def test_set_language_spanish():
    menu = links_menu.LanguagesMenu()
    menu.language = "other language"
    menu._set_lang_spanish()

    assert menu.language == "spanish"
