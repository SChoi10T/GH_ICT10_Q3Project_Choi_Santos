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
    ("Grade7", "Emerald"): ("Blue Bears", "images/bears.jpg"),
    ("Grade7", "Sapphire"): ("Green Hornets", "images/hornets.jpg"),
    ("Grade7", "Ruby"): ("Red Bulldogs", "images/bulldogs.jpg"),
    ("Grade7", "Topaz"): ("Yellow Tigers", "images/tigers.jpg"),

    ("Grade8", "Emerald"): ("Green Hornets", "images/hornets.jpg"),
    ("Grade8", "Sapphire"): ("Blue Bears", "images/bears.jpg"),
    ("Grade8", "Ruby"): ("Red Bulldogs", "images/bulldogs.jpg"),
    ("Grade8", "Topaz"): ("Yellow Tigers", "images/tigers.jpg"),

    ("Grade9", "Emerald"): ("Red Bulldogs", "images/bulldogs.jpg"),
    ("Grade9", "Sapphire"): ("Yellow Tigers", "images/tigers.jpg"),
    ("Grade9", "Ruby"): ("Blue Bears", "images/bears.jpg"),
    ("Grade9", "Topaz"): ("Green Hornets", "images/hornets.jpg"),

    ("Grade10", "Emerald"): ("Yellow Tigers", "images/tigers.jpg"),
    ("Grade10", "Sapphire"): ("Red Bulldogs", "images/bulldogs.jpg"),
    ("Grade10", "Ruby"): ("Green Hornets", "images/hornets.jpg"),
    ("Grade10", "Topaz"): ("Blue Bears", "images/bears.jpg"),
}
    # Find team
    team = teams.get((grade_value, section_value))

    if team:
 display(f"""
        <div class="card text-center mt-3 shadow">
            <div class="card-body">
                <h3 class="card-title">Congratulations!</h3>
                <p class="card-text">
                    You are part of the <strong>{team_name}</strong>!
                </p>
                <img src="{team_image}" class="img-fluid mt-3 rounded" style="max-width:250px;">
            </div>
        </div>
        """, target="output")

    else:
        display("Invalid grade or section selection.", target="output")

