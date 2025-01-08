import json
import datetime

"""
This file contains the Tracker class, which is the main part of the app for managing habits.
It handles creating, checking off, listing, and saving habits so the user can track their progress.
"""

class Tracker:
    """
    The Tracker class manages all habit-related tasks, such as adding, deleting, and saving habits.
    """
    def __init__(self, file_path='habits.json'):
        """
        The __init__ method is the constructor. It runs when you create a Tracker object.
        It sets up the habits list and loads existing habits from the file (if available).
        """
        self.file_path = file_path
        self.habits = self.load_habits()

    def load_habits(self):
        """
        The load_habits method reads habits from the JSON file and returns them.
        If the file doesn't exist yet, it returns an empty list.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_habits(self):
        """
        The save_habits method writes the current habits list to the JSON file.
        This ensures the user's data is saved for future use.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.habits, file)

    def add_habit(self, name, periodicity):
        """
        The add_habit method creates a new habit with the given name and periodicity (daily or weekly).
        It adds the habit to the list and saves it to the file.
        """
        habit = {
            'name': name,
            'periodicity': periodicity,
            'created_at': datetime.datetime.now().isoformat(),
            'checkoffs': []
        }
        self.habits.append(habit)
        self.save_habits()

    def delete_habit(self, name):
        """
        The delete_habit method removes a habit with the given name from the list.
        It saves the updated list to the file.
        """
        self.habits = [habit for habit in self.habits if habit['name'] != name]
        self.save_habits()

    def get_habits(self):
        """
        The get_habits method returns the list of current habits.
        """
        return self.habits

    def check_off_habit(self, name):
        """
        Mark a habit as completed by adding the current date and time to its checkoffs.
        If the habit doesn't exist, the function returns False.

        :param name: The name of the habit to check off.
        :return: True if the habit was found and checked off, False otherwise.
        """
        for habit in self.habits:
            if habit['name'] == name:
                # Avoid duplicate checkoffs for the same date
                today = datetime.datetime.now().strftime("%Y-%m-%d")
                if today in [checkoff[:10] for checkoff in habit['checkoffs']]:
                    return False
                habit['checkoffs'].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.save_habits()
                return True
        return False