import unittest

from nlp.parser import parse
from nlp.intents import Intent


class TestParser(unittest.TestCase):

    def test_greeting(self):
        result = parse("Hello")

        self.assertEqual(result.intent, Intent.GREETING)

    def test_open_application(self):
        result = parse("Open Chrome")

        self.assertEqual(result.intent, Intent.OPEN_APPLICATION)
        self.assertEqual(result.entities["type"], "application")

    def test_google_search(self):
        result = parse("Search for Python")

        self.assertEqual(result.intent, Intent.SEARCH_GOOGLE)

    def test_time(self):
        result = parse("What time is it?")

        self.assertEqual(result.intent, Intent.ASK_TIME)


if __name__ == "__main__":
    unittest.main()