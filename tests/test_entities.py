import unittest

from nlp.entities import extract_application


class TestEntities(unittest.TestCase):

    def test_extract_application(self):

        app = extract_application("Please open Chrome")

        self.assertEqual(app, "Google Chrome")


if __name__ == "__main__":
    unittest.main()