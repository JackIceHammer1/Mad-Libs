# Mad Libs Game - Iteration 5

import re
import random
import json
import os

# Define multiple story templates
templates = {
    "Adventure": """
Once upon a time, there was a {noun1} who loved to {verb1}. Every day, they would {verb2} with their {noun2} and enjoy {noun3}. 
One day, a {adjective1} {noun4} appeared and changed everything!
""",
    "Sci-Fi": """
In the distant future, a {adjective1} {noun1} discovered a way to {verb1} through space. Using their {noun2}, they {verb2} to {noun3}. 
Suddenly, they encountered a {noun4} that threatened the mission.
""",
    "Mystery": """
It was a dark and stormy night when a {noun1} heard a {adjective1} noise. They decided to {verb1} and found a {noun2} lying on the ground. 
Quickly, they {verb2} to {noun3}, only to discover a hidden {noun4}.
"""
}

template_descriptions = {
    "Adventure": "A story of excitement and daring experiences.",
    "Sci-Fi": "A futuristic tale of exploration and discovery.",
    "Mystery": "A suspenseful narrative full of intrigue and surprises."
}

users_data_file = "users_data.json"

# Function to load user data
def load_user_data():
    if os.path.exists(users_data_file):
        with open(users_data_file, "r") as file:
            return json.load(file)
    return {}

# Function to save user data
def save_user_data(data):
    with open(users_data_file, "w") as file:
        json.dump(data, file, indent=4)

# Load user data
users_data = load_user_data()

# Function to validate user input
def validate_input(prompt, word_type):
    while True:
        user_input = input(prompt)
        if word_type == "noun" and re.match(r'^[a-zA-Z]+$', user_input):
            return user_input
        elif word_type == "verb" and re.match(r'^[a-zA-Z]+$', user_input):
            return user_input
        elif word_type == "adjective" and re.match(r'^[a-zA-Z]+$', user_input):
            return user_input
        else:
            print(f"Invalid input. Please enter a {word_type} (only letters allowed).")

# Function to get user inputs for the story
def get_inputs(template):
    placeholders = re.findall(r'{(.*?)}', template)
    inputs = {}
    for placeholder in placeholders:
        word_type = placeholder.rstrip("1234567890")
        inputs[placeholder] = validate_input(f"Enter a {word_type}: ", word_type)
    return inputs

# Function to display available templates
def display_templates():
    print("\nAvailable story templates:")
    for key, description in template_descriptions.items():
        print(f"- {key}: {description}")

# Function to choose a template
def choose_template():
    display_templates()
    chosen_template = input("\nEnter the name of the template you want to use (or press Enter for a random template): ")
    if chosen_template == "":
        chosen_template = random.choice(list(templates.keys()))
        print(f"Randomly selected template: {chosen_template}")
    elif chosen_template not in templates:
        print("Invalid template choice. Using 'Adventure' template by default.")
        chosen_template = "Adventure"
    return templates[chosen_template]

# Function to save the story to a file
def save_story(username, story):
    user_stories = users_data.get(username, {}).get("stories", [])
    user_stories.append(story)
    users_data[username]["stories"] = user_stories
    save_user_data(users_data)
    print("Story saved successfully!")

# Function to view saved stories
def view_saved_stories(username):
    user_stories = users_data.get(username, {}).get("stories", [])
    if user_stories:
        print("\nSaved Stories:\n")
        for i, story in enumerate(user_stories, 1):
            print(f"Story {i}:\n{story}\n")
    else:
        print("No stories saved yet.")

# Function to play a round of Mad Libs
def play_mad_libs(username):
    story_template = choose_template()
    inputs = get_inputs(story_template)
    story = story_template.format(**inputs)
    print("\nHere is your Mad Libs story:")
    print(story)
    save_option = input("\nDo you want to save this story? (yes/no): ").strip().lower()
    if save_option == 'yes':
        save_story(username, story)

# Function to display help
def display_help():
    print("\nMad Libs Game Help:")
    print("1. Choose a story template or let the program select one randomly.")
    print("2. Enter the required words as prompted.")
    print("3. Enjoy your custom Mad Libs story!")
    print("4. Optionally, save your story to view later.")
    print("5. You can create custom templates and save them for later use.")
    print("6. User profiles are created to save stories and favorite templates.")

# Function to display the main menu
def display_menu():
    print("\nMad Libs Game Menu")
    print("1. Play Mad Libs")
    print("2. View Templates")
    print("3. View Saved Stories")
    print("4. Create Custom Template")
    print("5. Help")
    print("6. Exit")

# Function to create a custom template
def create_custom_template(username):
    template_name = input("Enter a name for your custom template: ")
    template_content = input("Enter the content for your custom template (use placeholders like {noun1}, {verb1}): ")
    templates[template_name] = template_content
    template_descriptions[template_name] = "Custom template created by user"
    user_templates = users_data.get(username, {}).get("templates", {})
    user_templates[template_name] = template_content
    users_data[username]["templates"] = user_templates
    save_user_data(users_data)
    print("Custom template created successfully!")

# Function to get or create a user profile
def get_user_profile():
    username = input("Enter your username: ").strip()
    if username not in users_data:
        users_data[username] = {"stories": [], "templates": {}}
        save_user_data(users_data)
        print(f"Welcome, {username}! Your profile has been created.")
    else:
        print(f"Welcome back, {username}!")
    return username

# Main loop to allow multiple rounds
def main():
    username = get_user_profile()
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == '1':
            play_mad_libs(username)
        elif choice == '2':
            display_templates()
        elif choice == '3':
            view_saved_stories(username)
        elif choice == '4':
            create_custom_template(username)
        elif choice == '5':
            display_help()
        elif choice == '6':
            print("Thanks for playing Mad Libs! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

# Run the game
if __name__ == "__main__":
    main()
