from pyscript import display, document # pyright: ignore[reportMissingImports]

# Account Creation
def account_creation(e):
    document.getElementById("output").innerHTML = "" # Clear Output

    # Get values from the inputs
    username = document.getElementById("input1").value
    password = document.getElementById("input2").value
    username_length = len(username)
    password_length = len(password)

    # Username and Password Restrictions
    if username_length < 7 and password_length < 10: # Checks if the information isn't valid/long enough
        display(f'Username must be at least 7 characters and password must be at least 10 characters.', target='output')
    elif username_length < 7: # Checks if the username length requirement is too short
        display(f'Your username is too short. Try again.', target='output')
    elif password_length < 10: # Checks if the password length requirement is too short
        display(f'Your password is too short. Try again.', target='output')
    elif password.isalpha(): # Checks if the required numbers aren't sufficient
        display(f'Password must contain at least one number. Try again.', target='output')
    elif password.isdigit(): # Checks if the required letters aren't sufficient
        display(f'Password must contain at least one letter. Try again.', target='output')
    else: # If all conditions are satisfied
        display(f'Welcome, {username}! You may now log in using your credentials.', target='output')

# Intramurals Team Checker
def team_checker(e):
    document.getElementById("output").innerHTML = "" # Clear Output

    # Get values from the dropdown inputs
    registration = document.getElementById("RegistrationDropdown").value
    clearance = document.getElementById("ClearanceDropdown").value
    grade_value = document.getElementById("GradeDropdown").value
    section_value = document.getElementById("SectionDropdown").value

    # Incomplete Form
    if not registration or not clearance or not grade_value or not section_value:
        display("Please fill out this form properly.", target="output")
        return

    # Uneligible, if the student is not registered or has no medical clearance
    if registration != "Yes" or clearance != "Yes":
        display("You aren't eligible, fill out the online registration or secure your medical certificate.", target="output")
        return

    # Team assignments: Uses Dictionary
    teams = {
        # Grade 7
        ("Grade7", "Emerald"): "Blue Bears",
        ("Grade7", "Sapphire"): "Green Hornets",
        ("Grade7", "Ruby"): "Red Bulldogs",
        ("Grade7", "Topaz"): "Yellow Tigers",

        # Grade 8
        ("Grade8", "Emerald"): "Green Hornets",
        ("Grade8", "Sapphire"): "Blue Bears",
        ("Grade8", "Ruby"): "Red Bulldogs",
        ("Grade8", "Topaz"): "Yellow Tigers",

        # Grade 9
        ("Grade9", "Emerald"): "Red Bulldogs",
        ("Grade9", "Sapphire"): "Yellow Tigers",
        ("Grade9", "Ruby"): "Blue Bears",
        ("Grade9", "Topaz"): "Green Hornets",

        # Grade 10
        ("Grade10", "Emerald"): "Yellow Tigers",
        ("Grade10", "Sapphire"): "Red Bulldogs",
        ("Grade10", "Ruby"): "Green Hornets",
        ("Grade10", "Topaz"): "Blue Bears",
    }

    # Find team
    team = teams.get((grade_value, section_value))

    if team:
        display(f"Congratulations! You are part of the {team}!", target="output")
    else:
        display("Invalid grade or section selection.", target="output")