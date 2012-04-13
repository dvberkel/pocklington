import unittest

from pocklington.criteria import PrimalityTester

class testCriteria(unittest.TestCase):
    def setUp(self):
        self.tester = PrimalityTester();

    def testPositiveGermainPrime(self):
        self.assertTrue(self.tester.isGermainPrime(2))
        self.assertTrue(self.tester.isGermainPrime(3))
        self.assertTrue(self.tester.isGermainPrime(5))
        self.assertTrue(self.tester.isGermainPrime(11))

    def testNegativeGermainPrime(self):
        self.assertFalse(self.tester.isGermainPrime(7))
        self.assertFalse(self.tester.isGermainPrime(13))
        self.assertFalse(self.tester.isGermainPrime(17))
        self.assertFalse(self.tester.isGermainPrime(19))

if __name__ == '__main__':
    unittest.main()
