import re
import random

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
def get_inputs():
    inputs = {
        "noun1": validate_input("Enter a noun: ", "noun"),
        "verb1": validate_input("Enter a verb: ", "verb"),
        "verb2": validate_input("Enter another verb: ", "verb"),
        "noun2": validate_input("Enter another noun: ", "noun"),
        "noun3": validate_input("Enter another noun: ", "noun"),
        "adjective1": validate_input("Enter an adjective: ", "adjective"),
        "noun4": validate_input("Enter another noun: ", "noun")
    }
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
def save_story(story):
    with open("saved_stories.txt", "a") as file:
        file.write(story + "\n\n")
    print("Story saved successfully!")

# Function to view saved stories
def view_saved_stories():
    try:
        with open("saved_stories.txt", "r") as file:
            stories = file.read()
            if stories:
                print("\nSaved Stories:\n")
                print(stories)
            else:
                print("No stories saved yet.")
    except FileNotFoundError:
        print("No stories saved yet.")

# Function to play a round of Mad Libs
def play_mad_libs():
    story_template = choose_template()
    inputs = get_inputs()
    story = story_template.format(**inputs)
    print("\nHere is your Mad Libs story:")
    print(story)
    save_option = input("\nDo you want to save this story? (yes/no): ").strip().lower()
    if save_option == 'yes':
        save_story(story)

# Function to display help
def display_help():
    print("\nMad Libs Game Help:")
    print("1. Choose a story template or let the program select one randomly.")
    print("2. Enter the required words as prompted.")
    print("3. Enjoy your custom Mad Libs story!")
    print("4. Optionally, save your story to view later.")

# Function to display the main menu
def display_menu():
    print("\nMad Libs Game Menu")
    print("1. Play Mad Libs")
    print("2. View Templates")
    print("3. View Saved Stories")
    print("4. Help")
    print("5. Exit")

# Main loop to allow multiple rounds
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == '1':
            play_mad_libs()
        elif choice == '2':
            display_templates()
        elif choice == '3':
            view_saved_stories()
        elif choice == '4':
            display_help()
        elif choice == '5':
            print("Thanks for playing Mad Libs! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

# Run the game
if __name__ == "__main__":
    main()
