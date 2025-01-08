import sqlite3
import json
from habit import Habit
import datetime

class DBHandler:
    def __init__(self, db_file='data/habits.db'):
        """ Connect to the SQLite database file. If the file does not exist, it will be created."""
        self.conn = sqlite3.connect(db_file)
        """" Create the table for storing habits if it does not already exist."""
        self.create_table()

    def create_table(self):
        """ SQL query to create a table named 'habits' with columns for name, periodicity, created_at, and completed_dates."""
        query = """
        CREATE TABLE IF NOT EXISTS habits (
            name TEXT PRIMARY KEY,
            periodicity INTEGER,
            created_at TEXT,
            completed_dates TEXT
        );
        """
        """ Execute the SQL query to create the table."""
        self.conn.execute(query)
        """Commit the changes to the database."""
        self.conn.commit()

    def save_habit(self, habit):
        """ SQL query to insert a new habit into the 'habits' table."""
        query = """
        INSERT INTO habits (name, periodicity, created_at, completed_dates)
        VALUES (?, ?, ?, ?);
        """
        """ Execute the SQL query with the habit's details."""
        self.conn.execute(query, (habit.name, habit.periodicity, habit.creation_date.isoformat(), json.dumps(habit.checkoffs)))
        """" Commit the changes to the database."""
        self.conn.commit()

    def get_all_habits(self):
        """ SQL query to select all habits from the 'habits' table."""
        query = "SELECT name, periodicity, created_at, completed_dates FROM habits;"
        """ Execute the SQL query and fetch all the results."""
        rows = self.conn.execute(query).fetchall()
        """ Initialize an empty list to store the habits."""
        habits = []
        """" Loop through each row in the results."""
        for row in rows:
            """ Create a new Habit object with the name and periodicity from the row."""
            habit = Habit(row[0], row[1])
            """ Set the creation_date of the habit from the row."""
            habit.creation_date = datetime.datetime.fromisoformat(row[2])
            """ Set the checkoffs of the habit by converting the JSON string back to a list of datetime objects."""
            habit.checkoffs = [datetime.datetime.fromisoformat(date) for date in json.loads(row[3])]
            """ Add the habit to the list of habits."""
            habits.append(habit)
        """ Return the list of habits."""
        return habits

    def get_habit(self, name):
        query = "SELECT name, periodicity, created_at, completed_dates FROM habits WHERE name = ?;"
        row = self.conn.execute(query, (name,)).fetchone()
        if row:
            habit = Habit(row[0], row[1])
            habit.creation_date = datetime.datetime.fromisoformat(row[2])
            habit.checkoffs = [datetime.datetime.fromisoformat(date) for date in json.loads(row[3])]
            return habit

    def delete_habit(self, name):
        query = "DELETE FROM habits WHERE name = ?;"
        self.conn.execute(query, (name,))
        self.conn.commit()

    def update_habit(self, habit):
        query = """
        UPDATE habits
        SET completed_dates = ?
        WHERE name = ?;
        """
        self.conn.execute(query, (json.dumps(habit.checkoffs), habit.name))
        self.conn.commit()
