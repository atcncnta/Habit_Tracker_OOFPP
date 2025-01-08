# Overview

This Habit Tracker Application is designed to help users develop and maintain positive habits through a consistent and efficient system. This document outlines the technical foundation of the application, including the architecture, data management, user interaction flow, and key components. 

# Features

1.Add a Habit: Create new habits with daily or weekly periodicity.
2.Predefined Habits: Select predefined habits (if implemented).
3.List Habits: View all the habits currently being tracked.
4.Mark Habits as Completed: Check off habits as completed for the day/week.
5.Analyze Habits: Analyze habit completion patterns (requires analytics module).
6.Exit: Exits the app

You can also do below: 

Add Custom Habits: Create new habits with daily or weekly periodicity.
Choose Predefined Habits: Select from habits like:
- Read 10 pages
- Do 10 minutes yoga
- Take the dog out for a walk
- Do grocery shopping
- Call parents

Track Progress: Mark habits as completed, and track streaks.

Analyze Habits: Analyze your habits to:
- View all tracked habits.
- Filter habits by periodicity.
- Check the longest streak across all habits.
- Check the longest streak for a specific habit.

Persistence: Save and load habit data using JSON files.
Test Fixtures: Includes sample tracking data for predefined habits spanning 4 weeks.

# Installation

1. Clone the Repository
git clone <repository_url>

2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install Dependencies
Install the required Python packages using: pip install -r requirements.txt

# Usage

Run the application using: python cli.py
Menu Options:

1. Add a Habit: Create a new habit by entering its name and periodicity.
2. Choose a Predefined Habit: Select from the predefined habits to track.
3. List Habits: View all habits you are tracking.
4. Check Off a Habit: Mark a habit as completed for today.
5. Analyze Habits: Gain insights into your habits:
- List all habits.
- Filter habits by periodicity.
- View the longest streak for all habits or a specific habit.
6. Exit: Quit the application.

# Code Structure

- habit.py: Defines the Habit class with attributes like name, periodicity, creation date, and check-offs.
- tracker.py: Manages habit storage, predefined habits, and data persistence using JSON.
- cli.py: Command-line interface for managing habits and analytics.
- analytics.py: Functional programming-based analytics for habits.


Predefined habits include 4 weeks of example tracking data for validation and analytics.
