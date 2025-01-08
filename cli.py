from tracker import Tracker
import analytics

def show_menu():
    """
    Display the main menu and prompt the user to choose an option.
    """
    print("\nWhat do you want to do?")
    print("1. Add a Habit")
    print("2. Choose a Predefined Habit")
    print("3. List Habits")
    print("4. Check Off a Habit")
    print("5. Analyze Habits")
    print("6. Exit")
    return input("Choose an option (1-6): ")

def add_habit(tracker):
    """
    Prompt the user to add a new habit.
    """
    name = input("Enter the habit name: ")
    periodicity = input("Enter the periodicity ('daily' or 'weekly'): ").lower()
    if periodicity not in ['daily', 'weekly']:
        print("Invalid periodicity. Please choose 'daily' or 'weekly'.")
        return
    tracker.add_habit(name, periodicity)
    print(f"Habit '{name}' added with {periodicity} periodicity!")

def choose_predefined_habit(tracker):
    """
    Allow the user to choose a predefined habit from a list.
    """
    predefined_habits = [
        {'name': 'Read 10 pages', 'periodicity': 'daily'},
        {'name': 'Do 10 minutes yoga', 'periodicity': 'daily'},
        {'name': 'Take the dog out for a walk', 'periodicity': 'daily'},
        {'name': 'Do grocery shopping', 'periodicity': 'weekly'},
        {'name': 'Call parents', 'periodicity': 'weekly'},
    ]
    print("\nChoose a predefined habit:")
    for i, habit in enumerate(predefined_habits, 1):
        print(f"{i}. {habit['name']} ({habit['periodicity']})")
    choice = int(input("Enter the number of your choice: "))
    if 1 <= choice <= len(predefined_habits):
        selected_habit = predefined_habits[choice - 1]
        tracker.add_habit(selected_habit['name'], selected_habit['periodicity'])
        print(f"Predefined habit '{selected_habit['name']}' added!")
    else:
        print("Invalid choice. Please try again.")

def list_habits(tracker):
    print("\nYour Habits:")
    habits = tracker.get_habits()
    if not habits:
        print("No habits yet. Add one!")
    else:
        for habit in habits:
            print(f"- {habit['name']} ({habit['periodicity']})")

def check_off_habit(tracker):
    name = input("Enter the name of the habit you completed: ")
    if tracker.check_off_habit(name):
        print(f"Great job! You checked off '{name}'!")
    else:
        print(f"Habit '{name}' not found.")

def analyze_habits(tracker):
    print("\nAnalyze Your Habits:")
    print("1. List all habits")
    print("2. List habits by periodicity")
    print("3. Longest streak of all habits")
    print("4. Longest streak for a specific habit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        all_habits = analytics.list_all_habits(tracker.get_habits())
        print("All Habits:")
        for habit in all_habits:
            print(f"- {habit}")
    elif choice == "2":
        periodicity = input("Enter periodicity ('daily' or 'weekly'): ").lower()
        filtered_habits = analytics.list_habits_by_periodicity(tracker.get_habits(), periodicity)
        print(f"Habits with {periodicity} periodicity:")
        for habit in filtered_habits:
            print(f"- {habit}")
    elif choice == "3":
        longest = analytics.longest_streak("all", tracker.get_habits())
        print(f"Longest streak across all habits: {longest}")
    elif choice == "4":
        habit_name = input("Enter the name of the habit: ")
        streak = analytics.longest_streak(habit_name, tracker.get_habits())
        print(f"Longest streak for '{habit_name}': {streak}")
    else:
        print("Invalid option.")

def main():
    tracker = Tracker()
    print("Predefined habits loaded! You can add, choose, check off, or analyze habits.")
    while True:
        choice = show_menu()
        if choice == "1":
            add_habit(tracker)
        elif choice == "2":
            choose_predefined_habit(tracker)
        elif choice == "3":
            list_habits(tracker)
        elif choice == "4":
            check_off_habit(tracker)
        elif choice == "5":
            analyze_habits(tracker)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
