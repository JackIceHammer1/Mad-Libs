import re
import random
import json
import os

# Define multiple story templates
templates = {
    "Adventure": """
Once upon a time, there was a {noun1} who loved to {verb1}. Every day, they would {verb2} with their {noun2} and enjoy {noun3}. 
One day, a {adjective1} {noun4} appeared and changed everything! The {noun4} was {adjective2} and had the power to {verb3}.
""",
    "Sci-Fi": """
In the distant future, a {adjective1} {noun1} discovered a way to {verb1} through space. Using their {noun2}, they {verb2} to {noun3}. 
Suddenly, they encountered a {noun4} that threatened the mission. The {noun4} was {adjective2} and demanded that they {verb3} immediately.
""",
    "Mystery": """
It was a dark and stormy night when a {noun1} heard a {adjective1} noise. They decided to {verb1} and found a {noun2} lying on the ground. 
Quickly, they {verb2} to {noun3}, only to discover a hidden {noun4}. The {noun4} contained a {adjective2} clue that revealed how to {verb3}.
""",
    "Fantasy": """
In a magical land, a {adjective1} {noun1} found a {noun2} that could {verb1}. With the help of a {adjective2} {noun3}, they embarked on a quest to {verb2} the {noun4}. 
After many adventures, they finally managed to {verb3} and restore peace to the kingdom.
""",
    "Horror": """
On a spooky night, a {adjective1} {noun1} decided to {verb1} in the abandoned {noun2}. As they {verb2}, they heard a {adjective2} sound coming from the {noun3}. 
Terrified, they tried to {verb3}, but the {noun4} blocked their path.
"""
}

template_descriptions = {
    "Adventure": "A story of excitement and daring experiences.",
    "Sci-Fi": "A futuristic tale of exploration and discovery.",
    "Mystery": "A suspenseful narrative full of intrigue and surprises.",
    "Fantasy": "A magical journey full of wonder and quests.",
    "Horror": "A spine-chilling tale of fear and suspense."
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
    update_user_points(username, 10)

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
    share_option = input("\nDo you want to share this story? (yes/no): ").strip().lower()
    if share_option == 'yes':
        share_story(username, story)

# Function to display help
def display_help():
    print("\nMad Libs Game Help:")
    print("1. Choose a story template or let the program select one randomly.")
    print("2. Enter the required words as prompted.")
    print("3. Enjoy your custom Mad Libs story!")
    print("4. Optionally, save your story to view later.")
    print("5. You can create custom templates and save them for later use.")
    print("6. User profiles are created to save stories and favorite templates.")
    print("7. You can share your stories by exporting them to text files.")
    print("8. Earn points for saving stories and creating templates.")
    print("9. View the leaderboard to see the top users.")
    print("10. Edit and update your custom templates.")

# Function to display the main menu
def display_menu():
    print("\nMad Libs Game Menu")
    print("1. Play Mad Libs")
    print("2. View Templates")
    print("3. View Saved Stories")
    print("4. Create Custom Template")
    print("5. Mark Template as Favorite")
    print("6. View Favorite Templates")
    print("7. Delete Saved Story")
    print("8. View Leaderboard")
    print("9. Help")
    print("10. Exit")

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
    update_user_points(username, 20)

# Function to mark a template as favorite
def mark_template_as_favorite(username):
    display_templates()
    favorite_template = input("Enter the name of the template you want to mark as favorite: ")
    if favorite_template in templates:
        user_favorites = users_data.get(username, {}).get("favorites", [])
        if favorite_template not in user_favorites:
            user_favorites.append(favorite_template)
            users_data[username]["favorites"] = user_favorites
            save_user_data(users_data)
            print(f"Template '{favorite_template}' marked as favorite.")
        else:
            print("Template is already marked as favorite.")
    else:
        print("Invalid template choice.")

# Function to view favorite templates
def view_favorite_templates(username):
    user_favorites = users_data.get(username, {}).get("favorites", [])
    if user_favorites:
        print("\nFavorite Templates:\n")
        for template in user_favorites:
            print(f"- {template}: {template_descriptions.get(template, 'No description available')}")
    else:
        print("No favorite templates yet.")

# Function to share a story by exporting it to a text file
def share_story(username, story):
    filename = f"{username}_story_{len(users_data[username]['stories'])}.txt"
    with open(filename, "w") as file:
        file.write(story)
    print(f"Story exported successfully to {filename}")

# Function to update user points
def update_user_points(username, points):
    current_points = users_data.get(username, {}).get("points", 0)
    users_data[username]["points"] = current_points + points
    save_user_data(users_data)
    print(f"You have earned {points} points! Total points: {users_data[username]['points']}")

# Function to view the leaderboard
def view_leaderboard():
    leaderboard = sorted(users_data.items(), key=lambda x: x[1].get("points", 0), reverse=True)
    print("\nLeaderboard:\n")
    for i, (username, data) in enumerate(leaderboard, 1):
        print(f"{i}. {username} - {data.get('points', 0)} points")

# Function to delete a saved story
def delete_saved_story(username):
    user_stories = users_data.get(username, {}).get("stories", [])
    if user_stories:
        print("\nSaved Stories:\n")
        for i, story in enumerate(user_stories, 1):
            print(f"Story {i}:\n{story}\n")
        story_index = int(input("Enter the number of the story you want to delete: ")) - 1
        if 0 <= story_index < len(user_stories):
            del user_stories[story_index]
            users_data[username]["stories"] = user_stories
            save_user_data(users_data)
            print("Story deleted successfully.")
        else:
            print("Invalid story number.")
    else:
        print("No stories saved yet.")

# Function to edit a custom template
def edit_custom_template(username):
    user_templates = users_data.get(username, {}).get("templates", {})
    if user_templates:
        print("\nYour Custom Templates:\n")
        for template in user_templates:
            print(f"- {template}")
        template_name = input("\nEnter the name of the template you want to edit: ")
        if template_name in user_templates:
            new_template_content = input(f"Enter the updated content for '{template_name}' template: ")
            templates[template_name] = new_template_content
            user_templates[template_name] = new_template_content
            users_data[username]["templates"] = user_templates
            save_user_data(users_data)
            print(f"Template '{template_name}' updated successfully.")
        else:
            print("Template not found.")
    else:
        print("No custom templates created yet.")

# Function to get or create a user profile
def get_user_profile():
    username = input("Enter your username: ").strip()
    if username not in users_data:
        users_data[username] = {"stories": [], "templates": {}, "favorites": [], "points": 0}
        save_user_data(users_data)
        print(f"Welcome, {username}! Your profile has been created.")
    else:
        print(f"Welcome back, {username}!")
    return username

# Function to view user statistics
def view_user_statistics(username):
    user_data = users_data.get(username, {})
    total_stories_saved = len(user_data.get("stories", []))
    total_templates_created = len(user_data.get("templates", []))
    total_points = user_data.get("points", 0)
    total_favorites = len(user_data.get("favorites", []))

    print("\nUser Statistics:")
    print(f"Total Stories Saved: {total_stories_saved}")
    print(f"Total Templates Created: {total_templates_created}")
    print(f"Total Favorite Templates: {total_favorites}")
    print(f"Total Points Earned: {total_points}"

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
            mark_template_as_favorite(username)
        elif choice == '6':
            view_favorite_templates(username)
        elif choice == '7':
            delete_saved_story(username)
        elif choice == '8':
            view_leaderboard()
        elif choice == '9':
            display_help()
        elif choice == '10':
            print("Thanks for playing Mad Libs! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

# Run the game
if __name__ == "__main__":
    main()
