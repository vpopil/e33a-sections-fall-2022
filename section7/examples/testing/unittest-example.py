import unittest

from pow import pow

class Tests(unittest.TestCase):

    def setUpClass():
        print('SETTING UP CLASS')
        #pass

    def setUp(self):
        print('Setting up the test')

    def test_1(self):
        """Check that 2^5."""
        self.assertEqual(pow(2, 5), 32)

    def test_2(self):
        """Check that 2^10."""
        self.assertEqual(pow(2, 10), 1024)

    def test_3(self):
        """Check that 2^100."""
        self.assertEqual(pow(2, 100), 1267650600228229401496703205376)

    def test_4(self):
        """Check that 2^1."""
        self.assertEqual(pow(2, 1), 2)

    def test_5(self):
        """Check that 2^0."""
        self.assertEqual(pow(2, 0), 1)

    def test_6(self):
        """Check that 2^-1."""
        self.assertEqual(pow(2, -1), 0.5)

    def test_7(self):
        """Check that 2^-1."""
        self.assertEqual(pow(2, 0), 1)

    def tearDown(self):
        print('Tearing down the test')
        #pass

if __name__ == "__main__":
    unittest.main()
