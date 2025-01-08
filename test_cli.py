import unittest
from unittest.mock import patch
from tracker import Tracker
import cli

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.tracker = Tracker()
        self.tracker.add_habit('Read 10 pages', 'daily')

    @patch('builtins.input', side_effect=['Read 10 pages', 'daily'])
    def test_add_habit(self, mock_input):
        cli.add_habit(self.tracker)
        self.assertIn('Read 10 pages', [habit['name'] for habit in self.tracker.get_habits()])

    @patch('builtins.input', side_effect=['Read 10 pages'])
    def test_check_off_habit(self, mock_input):
        cli.check_off_habit(self.tracker)
        self.assertEqual(len(self.tracker.get_habits()[0]['checkoffs']), 1)

if __name__ == '__main__':
    unittest.main()
