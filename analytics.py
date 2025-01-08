from datetime import datetime, timedelta

def longest_streak(habit_name, habits):
    """
    #Calculate the longest streak for a given habit based on checkoffs.
    """
    habit = next((h for h in habits if h["name"] == habit_name), None)
    if not habit or not habit.get("checkoffs"):
        return 0

    dates = sorted(datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in habit["checkoffs"])

    longest = 1
    current_streak = 1

    for i in range(1, len(dates)):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            current_streak += 1
            longest = max(longest, current_streak)
        else:
            current_streak = 1

    return longest

def list_all_habits(habits):
    return [habit["name"] for habit in habits]

def list_habits_by_periodicity(habits, periodicity):
    return [habit["name"] for habit in habits if habit["periodicity"] == periodicity]
