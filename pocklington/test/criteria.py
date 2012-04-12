import unittest

from pocklington.criteria import PrimalityTester

class testCriteria(unittest.TestCase):
    def testGermainPrime(self):
        tester = PrimalityTester()
        self.assertTrue(tester.isGermainPrime(5))

if __name__ == '__main__':
    unittest.main()
