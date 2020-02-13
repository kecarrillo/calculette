import unittest
import myString


class TestStringFormat(unittest.TestCase):
    def test_input(self):
        self.assertIsInstance(myString.start, str)

    def test_lenInput(self):  # correction: ajout de len()
        self.assertGreaterEqual(len(myString.start), 50)

    def test_containVoyelle(self):
        list = ["a", "e", "i", "o", "u", "y"]
        self.assertIn(myString.tri, list)


if __name__ == '__main__':
    unittest.main()