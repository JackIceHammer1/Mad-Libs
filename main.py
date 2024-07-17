# Mad Libs Game - Iteration 2

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

# Prompt the user to choose a template
print("Choose a story template:")
for key in templates:
    print(f"- {key}")

chosen_template = input("Enter the name of the template you want to use: ")

# Ensure the chosen template exists
if chosen_template not in templates:
    print("Invalid template choice. Using 'Adventure' template by default.")
    chosen_template = "Adventure"

# Get the selected template
story_template = templates[chosen_template]

# Prompt the user for inputs based on the chosen template
inputs = {
    "noun1": input("Enter a noun: "),
    "verb1": input("Enter a verb: "),
    "verb2": input("Enter another verb: "),
    "noun2": input("Enter another noun: "),
    "noun3": input("Enter another noun: "),
    "adjective1": input("Enter an adjective: "),
    "noun4": input("Enter another noun: ")
}

# Fill in the story template with user inputs
story = story_template.format(**inputs)

# Display the story
print("\nHere is your Mad Libs story:")
print(story)
