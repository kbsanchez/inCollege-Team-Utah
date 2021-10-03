def get_user_selection():
    selection_text = input("Please make a choice from the menu: ")
    return int(selection_text)


def learn_skills_menu():
    while True:
        print(
            """1 - Networking
2 - Time Management
3 - Public Speaking
4 - Agile and Scrum
5 - Leadership

6 - Go Back"""
        )

        selection = None

        try:
            selection = get_user_selection()
        except:
            print("Invalid selection")
            continue

        if selection == 6:
            return
        if selection not in list(range(7)):
            print("Invalid selection")
        else:
            print("Under Construction")




optionsAndActions = [
    ("Job/Internship Search", None),
    ("Find Someone You Know", None),
    ("Learn a New Skill", learn_skills_menu),
    ("Log Out", "Thank you for using InCollege!")
]


def print_menu_options():
    options = [
        f"{i + 1} - {x[0]}"
        for i, x
        in enumerate(optionsAndActions)
    ]

    options_text = "\n".join(options)

    print(options_text)


def get_user_action_selection():
    selection = get_user_selection() - 1

    action = optionsAndActions[selection][1]

    if action is None:
        print("Under Construction")

    if selection == 2:
        action()

    if selection not in list(range(4)):
        print("Invalid selection")

    if selection==3:
        print(action)
        return -1

    return 1


def main_menu():
    while True:
        print("\n")
        print_menu_options()
        print("\n")

        action = get_user_action_selection()

        if action==-1:
            break

