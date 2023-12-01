import unittest
import pandas as pd
from slack_data_loader import SlackDataLoader

class TestSlackDataLoader(unittest.TestCase):

    def setUp(self):
        # Initialize SlackDataLoader instance
        self.data_loader = SlackDataLoader()

    def test_load_messages(self):
        # Load messages DataFrame
        messages_df = self.data_loader.load_messages()

        # Define expected columns
        expected_columns = ['message_id', 'channel', 'sender_name', 'msg_content', 'timestamp']

        # Check if DataFrame has the expected columns
        self.assertCountEqual(messages_df.columns, expected_columns)

    def test_load_reactions(self):
        # Load reactions DataFrame
        reactions_df = self.data_loader.load_reactions()

        # Define expected columns
        expected_columns = ['message_id', 'channel', 'reaction', 'user']

        # Check if DataFrame has the expected columns
        self.assertCountEqual(reactions_df.columns, expected_columns)

if __name__ == '__main__':
    unittest.main()