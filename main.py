import re

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

# Function to choose a template
def choose_template():
    print("Choose a story template:")
    for key in templates:
        print(f"- {key}")
    chosen_template = input("Enter the name of the template you want to use: ")
    if chosen_template not in templates:
        print("Invalid template choice. Using 'Adventure' template by default.")
        chosen_template = "Adventure"
    return templates[chosen_template]

# Function to play a round of Mad Libs
def play_mad_libs():
    story_template = choose_template()
    inputs = get_inputs()
    story = story_template.format(**inputs)
    print("\nHere is your Mad Libs story:")
    print(story)

# Main loop to allow multiple rounds
def main():
    while True:
        play_mad_libs()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing Mad Libs! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    main()
