def learn_skills_menu():
    pass


def logout():
    pass


optionsAndActions = [
    ("Job/Internship Search", None),
    ("Find Someone You Know", None),
    ("Learn a New Skill", learn_skills_menu),
    ("Log Out", logout)
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
    selection_text = input("Please make a choice from the menu: ")
    selection = int(selection_text) - 1

    return optionsAndActions[selection][1]


def main_menu():
    while True:
        print("\n")
        print_menu_options()
        print("\n")
        
        try:
            action = get_user_action_selection()
            
            if action is None:
                print("Under Construction")
            else:
                action()
        except:
            print("Invalid selection")