import datetime

class Habit:
    def __init__(self, name, periodicity, creation_date=None, checkoffs=None):
        """
        Initialize a new habit.

        :name: The name of the habit.
        :periodicity: The periodicity of the habit (e.g., 'daily', 'weekly').
        :creation_date: The date the habit was created. Defaults to the current date and time.
        :checkoffs: A list of datetime objects representing when the habit was checked off. Defaults to an empty list.
        """
        self.name = name
        self.periodicity = periodicity  
        self.creation_date = creation_date or datetime.datetime.now()
        self.checkoffs = checkoffs or []

    def check_off(self):
        """
        Mark the habit as completed for the current date and time.
        """
        self.checkoffs.append(datetime.datetime.now())

    def get_info(self):
        """
        Get information about the habit.

        :A dictionary containing the habit's name, periodicity, creation date, and checkoff dates.
        """
        return {
            'name': self.name,
            'periodicity': self.periodicity,
            'created_on': self.creation_date.strftime("%Y-%m-%d"),
            'checkoffs': [date.strftime("%Y-%m-%d") for date in self.checkoffs]
        }