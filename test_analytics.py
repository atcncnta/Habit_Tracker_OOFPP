import unittest
from analytics import longest_streak

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.habits = [
            {
                "name": "Read 10 pages",
                "periodicity": "daily",
                "checkoffs": [
                    "2025-01-01 00:00:00",
                    "2025-01-02 00:00:00",
                    "2025-01-03 00:00:00",
                    "2025-01-05 00:00:00"  # Break in streak
                ]
            }
        ]

    def test_longest_streak_for_habit(self):
        streak = longest_streak("Read 10 pages", self.habits)
        self.assertEqual(streak, 3)  # Expect streak of 3 days

if __name__ == "__main__":
    unittest.main()
