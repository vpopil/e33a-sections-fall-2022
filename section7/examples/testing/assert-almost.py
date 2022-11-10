import unittest

class Tests(unittest.TestCase):

    def test1(self):
        self.assertAlmostEqual(2.00061, 2.0006, places=5)  # try 4

if __name__ == "__main__":
    unittest.main()
