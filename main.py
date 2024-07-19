import re
import random
import json
import os
import datetime

daily_challenge_data = {
    "date": None,
    "template": None,
    "submissions": {}
}

# Function to save daily challenge data to a file
def save_daily_challenge_data():
    with open("daily_challenge.json", "w") as file:
        json.dump(daily_challenge_data, file, indent=4)

# Function to load daily challenge data from a file
def load_daily_challenge_data():
    global daily_challenge_data
    if os.path.exists("daily_challenge.json"):
        with open("daily_challenge.json", "r") as file:
            daily_challenge_data = json.load(file)

# Load daily challenge data when the script starts
load_daily_challenge_data()

shared_stories_data_file = "shared_stories.json"

# Function to load shared stories data
def load_shared_stories_data():
    if os.path.exists(shared_stories_data_file):
        with open(shared_stories_data_file, "r") as file:
            return json.load(file)
    return {}

# Function to save shared stories data
def save_shared_stories_data(data):
    with open(shared_stories_data_file, "w") as file:
        json.dump(data, file, indent=4)

# Load shared stories data
shared_stories_data = load_shared_stories_data()

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

# Function to save user datadef save_user_data(data):
def save_user_data(data):
    with open(users_data_file, "w") as file:
        json.dump(data, file, indent=4)
    with open(challenges_file, "w") as file:
        json.dump(challenges, file, indent=4)

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
    update_user_badges(username)  # Update badges

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
    check_and_award_badges(username)

# Load challenges
challenges_file = "challenges.json"
def load_challenges():
    if os.path.exists(challenges_file):
        with open(challenges_file, "r") as file:
            return json.load(file)
    return {}

# Load challenges data
challenges = load_challenges()

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
    print("9. View your statistics to see your activity and points earned.")
    print("10. Update your profile information such as username and password.")
    print("11. View your profile details including points and saved items.")
    print("12. Change your profile password.")
    print("13. Delete your profile if you no longer want to play.")
    print("14. View your earned badges and their criteria.")
    print("15. Create a challenge for others to participate in.")  # Updated help text
    print("16. Participate in an existing challenge.")  # Updated help text
    print("17. View submissions for a challenge.")  # Updated help text

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
    print("10. Create Storybook")
    print("11. Add Story to Storybook")
    print("12. View Storybooks")
    print("13. Delete Storybook")
    print("14. Delete Story from Storybook")
    print("15. Share Story")
    print("16. View Shared Stories")
    print("17. Rate Shared Story")
    print("18. Comment on Shared Story")
    print("19. Participate in Daily Challenge")
    print("20. View Daily Challenge Submissions")
    print("21. Vote for a Story")
    print("22. View Top Voted Stories")
    print("23. Exit")

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
    check_and_award_badges(username)

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
            check_and_award_badges(username)
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

challenges = {
    "Epic Adventure": {
        "template": templates["Adventure"],
        "submissions": [],
        "votes": {}
    },
    "Space Odyssey": {
        "template": templates["Sci-Fi"],
        "submissions": [],
        "votes": {}
    }
}

# Function to participate in a challenge
def participate_in_challenge(username):
    display_challenges()
    challenge_name = input("Enter the name of the challenge you want to participate in: ")
    if challenge_name in challenges:
        story_template = challenges[challenge_name]["template"]
        inputs = get_inputs(story_template)
        submission = story_template.format(**inputs)
        challenges[challenge_name]["submissions"].append({"username": username, "story": submission})
        print("\nThank you for participating in the challenge! Your submission has been saved.")
        user_data = users_data[username]
        user_data["challenges_participated"] = user_data.get("challenges_participated", []) + [challenge_name]
        save_user_data(users_data)
    else:
        print("Challenge not found. Please check the challenge name and try again.")

# Function to display available challenges
def display_challenges():
    print("\nAvailable Challenges:")
    for challenge in challenges:
        print(f"- {challenge}: {template_descriptions.get(challenge, 'No description available')}")

# Function to vote on challenge submissions
def vote_on_challenge(username):
    display_challenges()
    challenge_name = input("Enter the name of the challenge you want to vote on: ")
    if challenge_name in challenges:
        submissions = challenges[challenge_name]["submissions"]
        if not submissions:
            print("No submissions for this challenge yet.")
            return
        print("\nSubmissions:")
        for i, submission in enumerate(submissions, 1):
            print(f"{i}. {submission['story']} (by {submission['username']})")
        vote_index = int(input("Enter the number of the submission you want to vote for: ")) - 1
        if 0 <= vote_index < len(submissions):
            voted_username = submissions[vote_index]["username"]
            if voted_username not in challenges[challenge_name]["votes"]:
                challenges[challenge_name]["votes"][voted_username] = 0
            challenges[challenge_name]["votes"][voted_username] += 1
            print("Vote recorded successfully.")
        else:
            print("Invalid submission number.")
    else:
        print("Challenge not found. Please check the challenge name and try again.")

# Function to display challenge results
def display_challenge_results():
    display_challenges()
    challenge_name = input("Enter the name of the challenge you want to see results for: ")
    if challenge_name in challenges:
        votes = challenges[challenge_name]["votes"]
        if not votes:
            print("No votes for this challenge yet.")
            return
        sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
        print("\nChallenge Results:")
        for i, (username, vote_count) in enumerate(sorted_votes, 1):
            print(f"{i}. {username}: {vote_count} votes")
    else:
        print("Challenge not found. Please check the challenge name and try again.")

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

# Function to update user profile information
def update_user_profile(username):
    print("\nUpdate Profile Information:")
    new_username = input("Enter new username (press Enter to keep current): ").strip()
    if new_username:
        users_data[new_username] = users_data.pop(username)
        username = new_username
    new_password = input("Enter new password (press Enter to keep current): ").strip()
    if new_password:
        users_data[username]["password"] = new_password
    print("Profile updated successfully!")

# Function to view user profile details
def view_user_profile(username):
    print(f"\nUser Profile Details for '{username}':")
    print(f"Username: {username}")
    print(f"Points: {users_data[username].get('points', 0)}")
    print(f"Number of Stories Saved: {len(users_data[username].get('stories', []))}")
    print(f"Number of Custom Templates Created: {len(users_data[username].get('templates', []))}")
    print(f"Number of Favorite Templates: {len(users_data[username].get('favorites', []))}")

# Function to change user password
def change_password(username):
    new_password = input("Enter new password: ").strip()
    users_data[username]["password"] = new_password
    print("Password changed successfully!")

# Function to delete user profile
def delete_user_profile(username):
    confirm = input("Are you sure you want to delete your profile? This action cannot be undone. (yes/no): ").strip().lower()
    if confirm == "yes":
        del users_data[username]
        save_user_data(users_data)
        print("Profile deleted successfully. Goodbye!")
        exit()
    else:
        print("Profile deletion cancelled.")

# Function to update user badges
def update_user_badges(username):
    user_data = users_data[username]
    badges = user_data.get("badges", [])
    
    # Check conditions for earning badges
    if len(user_data.get("stories", [])) >= 5 and "Story Saver" not in badges:
        badges.append("Story Saver")
        print("Congratulations! You've earned the 'Story Saver' badge for saving 5 stories.")
    
    if len(user_data.get("templates", [])) >= 3 and "Template Creator" not in badges:
        badges.append("Template Creator")
        print("Congratulations! You've earned the 'Template Creator' badge for creating 3 custom templates.")
    
    if len(user_data.get("favorites", [])) >= 3 and "Favorite Collector" not in badges:
        badges.append("Favorite Collector")
        print("Congratulations! You've earned the 'Favorite Collector' badge for marking 3 templates as favorite.")
    
    user_data["badges"] = badges
    save_user_data(users_data)

# Function to view user badges
def view_user_badges(username):
    badges = users_data.get(username, {}).get("badges", [])
    if badges:
        print("\nYour Badges:")
        for badge in badges:
            print(f"- {badge}")
    else:
        print("No badges earned yet.")

# Function to create a challenge
def create_challenge(username):
    story_template = choose_template()
    challenge_name = input("Enter a name for your challenge: ")
    inputs = get_inputs(story_template)
    challenge_story = story_template.format(**inputs)
    challenges[challenge_name] = {"template": story_template, "creator": username, "submissions": []}
    print("\nYour challenge has been created! Share the challenge name with others so they can participate.")
    save_user_data(users_data)

# Function to participate in a challenge
def participate_in_challenge(username):
    challenge_name = input("Enter the name of the challenge you want to participate in: ")
    if challenge_name in challenges:
        story_template = challenges[challenge_name]["template"]
        inputs = get_inputs(story_template)
        submission = story_template.format(**inputs)
        challenges[challenge_name]["submissions"].append({"username": username, "story": submission})
        print("\nThank you for participating in the challenge! Your submission has been saved.")
        user_data = users_data[username]
        user_data["challenges_participated"] = user_data.get("challenges_participated", []) + [challenge_name]
        save_user_data(users_data)
        check_and_award_badges(username)
    else:
        print("Challenge not found. Please check the challenge name and try again.")

# Function to view challenge submissions
def view_challenge_submissions():
    challenge_name = input("Enter the name of the challenge you want to view: ")
    if challenge_name in challenges:
        submissions = challenges[challenge_name]["submissions"]
        if submissions:
            print(f"\nSubmissions for challenge '{challenge_name}':")
            for submission in submissions:
                print(f"\nBy {submission['username']}:\n{submission['story']}\n")
        else:
            print("No submissions for this challenge yet.")
    else:
        print("Challenge not found. Please check the challenge name and try again.")

# Define badges and their criteria
badges = {
    "Story Creator": {
        "description": "Create 5 stories.",
        "criteria": lambda data: len(data.get("stories", [])) >= 5
    },
    "Challenge Participant": {
        "description": "Participate in 3 challenges.",
        "criteria": lambda data: len(data.get("challenges_participated", [])) >= 3
    },
    "Template Creator": {
        "description": "Create 3 custom templates.",
        "criteria": lambda data: len(data.get("templates", {})) >= 3
    },
    "Favorite Collector": {
        "description": "Mark 5 templates as favorite.",
        "criteria": lambda data: len(data.get("favorites", [])) >= 5
    },
    "Story Saver": {
        "description": "Save 10 stories.",
        "criteria": lambda data: len(data.get("stories", [])) >= 10
    }
}

# Function to check and award badges
def check_and_award_badges(username):
    user_data = users_data[username]
    awarded_badges = user_data.get("badges", [])
    for badge, info in badges.items():
        if badge not in awarded_badges and info["criteria"](user_data):
            awarded_badges.append(badge)
            print(f"Congratulations {username}! You have earned the '{badge}' badge: {info['description']}")
    user_data["badges"] = awarded_badges
    save_user_data(users_data)

# Function to view earned badges
def view_user_badges(username):
    user_badges = users_data.get(username, {}).get("badges", [])
    if user_badges:
        print("\nYour Earned Badges:\n")
        for badge in user_badges:
            print(f"- {badge}: {badges[badge]['description']}")
    else:
        print("No badges earned yet. Start playing and creating to earn badges!")

storybooks = {}

# Function to create a new storybook
def create_storybook(username):
    storybook_name = input("Enter a name for your storybook: ").strip()
    if username not in storybooks:
        storybooks[username] = {}
    if storybook_name in storybooks[username]:
        print("You already have a storybook with this name.")
    else:
        storybooks[username][storybook_name] = []
        print(f"Storybook '{storybook_name}' created successfully.")

# Function to add a story to a storybook
def add_story_to_storybook(username):
    if username not in storybooks or not storybooks[username]:
        print("You don't have any storybooks yet. Create one first.")
        return
    storybook_name = input("Enter the name of the storybook you want to add a story to: ").strip()
    if storybook_name not in storybooks[username]:
        print("Storybook not found. Please check the name and try again.")
        return
    view_saved_stories(username)
    story_index = int(input("Enter the number of the story you want to add to the storybook: ")) - 1
    user_stories = users_data.get(username, {}).get("stories", [])
    if 0 <= story_index < len(user_stories):
        storybooks[username][storybook_name].append(user_stories[story_index])
        print(f"Story added to storybook '{storybook_name}' successfully.")
    else:
        print("Invalid story number.")

# Function to view storybooks
def view_storybooks(username):
    if username not in storybooks or not storybooks[username]:
        print("You don't have any storybooks yet.")
    else:
        for storybook_name, stories in storybooks[username].items():
            print(f"\nStorybook: {storybook_name}")
            for i, story in enumerate(stories, 1):
                print(f"\nStory {i}:\n{story}\n")

# Function to delete a storybook
def delete_storybook(username):
    if username not in storybooks or not storybooks[username]:
        print("You don't have any storybooks yet.")
        return
    storybook_name = input("Enter the name of the storybook you want to delete: ").strip()
    if storybook_name in storybooks[username]:
        del storybooks[username][storybook_name]
        print(f"Storybook '{storybook_name}' deleted successfully.")
    else:
        print("Storybook not found. Please check the name and try again.")

# Function to delete a story from a storybook
def delete_story_from_storybook(username):
    if username not in storybooks or not storybooks[username]:
        print("You don't have any storybooks yet.")
        return
    storybook_name = input("Enter the name of the storybook you want to remove a story from: ").strip()
    if storybook_name not in storybooks[username]:
        print("Storybook not found. Please check the name and try again.")
        return
    stories = storybooks[username][storybook_name]
    for i, story in enumerate(stories, 1):
        print(f"\nStory {i}:\n{story}\n")
    story_index = int(input("Enter the number of the story you want to remove: ")) - 1
    if 0 <= story_index < len(stories):
        del stories[story_index]
        print(f"Story removed from storybook '{storybook_name}' successfully.")
    else:
        print("Invalid story number.")

# Function to save storybooks to a file
def save_storybooks():
    with open("storybooks.json", "w") as file:
        json.dump(storybooks, file, indent=4)

# Function to load storybooks from a file
def load_storybooks():
    global storybooks
    if os.path.exists("storybooks.json"):
        with open("storybooks.json", "r") as file:
            storybooks = json.load(file)

# Load storybooks when the script starts
load_storybooks()

shared_stories = {}

# Function to share a story
def share_story_with_feedback(username):
    view_saved_stories(username)
    story_index = int(input("Enter the number of the story you want to share: ")) - 1
    user_stories = users_data.get(username, {}).get("stories", [])
    if 0 <= story_index < len(user_stories):
        story = user_stories[story_index]
        shared_story_id = len(shared_stories) + 1
        shared_stories[shared_story_id] = {
            "username": username,
            "story": story,
            "ratings": [],
            "comments": []
        }
        print(f"Story shared successfully with ID: {shared_story_id}")
    else:
        print("Invalid story number.")

# Function to view shared stories
def view_shared_stories():
    if not shared_stories:
        print("No stories have been shared yet.")
        return
    for story_id, story_data in shared_stories.items():
        print(f"\nStory ID: {story_id}")
        print(f"Shared by: {story_data['username']}")
        print(f"Story:\n{story_data['story']}")
        if story_data['ratings']:
            average_rating = sum(story_data['ratings']) / len(story_data['ratings'])
            print(f"Average Rating: {average_rating:.2f}")
        else:
            print("No ratings yet.")
        if story_data['comments']:
            print("Comments:")
            for comment in story_data['comments']:
                print(f"- {comment}")
        else:
            print("No comments yet.")

# Function to rate a shared story
def rate_shared_story():
    view_shared_stories()
    story_id = int(input("Enter the ID of the story you want to rate: "))
    if story_id in shared_stories:
        rating = int(input("Enter your rating (1-5): "))
        if 1 <= rating <= 5:
            shared_stories[story_id]['ratings'].append(rating)
            print("Rating submitted successfully.")
        else:
            print("Invalid rating. Please enter a number between 1 and 5.")
    else:
        print("Invalid story ID.")

# Function to comment on a shared story
def comment_on_shared_story():
    view_shared_stories()
    story_id = int(input("Enter the ID of the story you want to comment on: "))
    if story_id in shared_stories:
        comment = input("Enter your comment: ").strip()
        shared_stories[story_id]['comments'].append(comment)
        print("Comment submitted successfully.")
    else:
        print("Invalid story ID.")

# Function to save shared stories to a file
def save_shared_stories():
    with open("shared_stories.json", "w") as file:
        json.dump(shared_stories, file, indent=4)

# Function to load shared stories from a file
def load_shared_stories():
    global shared_stories
    if os.path.exists("shared_stories.json"):
        with open("shared_stories.json", "r") as file:
            shared_stories = json.load(file)

# Load shared stories when the script starts
load_shared_stories()

# Function to set up a new daily challenge
def setup_daily_challenge():
    current_date = str(datetime.date.today())
    if daily_challenge_data["date"] != current_date:
        daily_challenge_data["date"] = current_date
        daily_challenge_data["template"] = random.choice(list(templates.keys()))
        daily_challenge_data["submissions"] = {}
        save_daily_challenge_data()
        print(f"New Daily Challenge set up for {current_date} with template: {daily_challenge_data['template']}")
    else:
        print(f"Daily Challenge for {current_date} is already set up with template: {daily_challenge_data['template']}")

# Function to participate in the daily challenge
def participate_in_daily_challenge(username):
    setup_daily_challenge()
    template_name = daily_challenge_data["template"]
    story_template = templates[template_name]
    inputs = get_inputs(story_template)
    story = story_template.format(**inputs)
    print("\nHere is your Daily Challenge story:")
    print(story)
    daily_challenge_data["submissions"][username] = story
    save_daily_challenge_data()
    print("Story submitted for the Daily Challenge.")

# Function to view daily challenge submissions
def view_daily_challenge_submissions():
    setup_daily_challenge()
    if not daily_challenge_data["submissions"]:
        print("No submissions for today's challenge yet.")
        return
    print("\nDaily Challenge Submissions:\n")
    for username, story in daily_challenge_data["submissions"].items():
        print(f"{username}'s submission:\n{story}\n")

# Function to share a story
def share_story(username, story):
    story_id = len(shared_stories_data) + 1
    shared_stories_data[story_id] = {
        "username": username,
        "story": story,
        "votes": 0
    }
    save_shared_stories_data(shared_stories_data)
    print("Story shared successfully!")

# Function to view shared stories
def view_shared_stories():
    if not shared_stories_data:
        print("No shared stories yet.")
        return
    print("\nShared Stories:\n")
    for story_id, data in shared_stories_data.items():
        print(f"Story ID: {story_id}")
        print(f"Username: {data['username']}")
        print(f"Story:\n{data['story']}")
        print(f"Votes: {data['votes']}\n")

# Function to vote for a story
def vote_for_story():
    view_shared_stories()
    story_id = int(input("Enter the Story ID of the story you want to vote for: "))
    if story_id in shared_stories_data:
        shared_stories_data[story_id]["votes"] += 1
        save_shared_stories_data(shared_stories_data)
        print("Vote cast successfully!")
    else:
        print("Invalid Story ID.")

# Function to view top-voted stories
def view_top_voted_stories():
    if not shared_stories_data:
        print("No shared stories yet.")
        return
    sorted_stories = sorted(shared_stories_data.items(), key=lambda x: x[1]["votes"], reverse=True)
    print("\nTop Voted Stories:\n")
    for story_id, data in sorted_stories:
        print(f"Story ID: {story_id}")
        print(f"Username: {data['username']}")
        print(f"Story:\n{data['story']}")
        print(f"Votes: {data['votes']}\n")
        if len(sorted_stories) == 5:
            break  # Display top 5 stories

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
            create_storybook(username)
        elif choice == '11':
            add_story_to_storybook(username)
        elif choice == '12':
            view_storybooks(username)
        elif choice == '13':
            delete_storybook(username)
        elif choice == '14':
            delete_story_from_storybook(username)
        elif choice == '15':
            share_story(username)
        elif choice == '16':
            view_shared_stories()
        elif choice == '17':
            rate_shared_story()
        elif choice == '18':
            comment_on_shared_story()
        elif choice == '19':
            participate_in_daily_challenge(username)
        elif choice == '20':
            view_daily_challenge_submissions()
        elif choice == '21':
            vote_for_story()
        elif choice == '22':
            view_top_voted_stories()
        elif choice == '23':
            print("Thanks for playing Mad Libs! Goodbye!")
            save_storybooks()
            save_shared_stories()
            save_daily_challenge_data()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 23.")

# Run the game
if __name__ == "__main__":
    main()
