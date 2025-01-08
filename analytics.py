from datetime import datetime, timedelta

def longest_streak(habit_name, habits):
    """
    Calculate the longest streak for a given habit based on checkoffs.
    
    :param habit_name: Name of the habit.
    :param habits: List of habit dictionaries.
    :return: Longest streak as an integer.
    """
    # Find the habit
    habit = next((h for h in habits if h["name"] == habit_name), None)
    if not habit or not habit.get("checkoffs"):
        return 0

    # Parse and sort checkoff dates
    dates = sorted(datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in habit["checkoffs"])

    longest = 1
    current_streak = 1

    for i in range(1, len(dates)):
        # Check if the current date is consecutive from the previous one
        if dates[i] - dates[i - 1] == timedelta(days=1):
            current_streak += 1
            longest = max(longest, current_streak)
        else:
            current_streak = 1

    return longest