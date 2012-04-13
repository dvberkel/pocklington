class PrimalityTester:
    def isGermainPrime(self, q):
        """Determines if q is a Sophie Germain prime"""
        p = 2 * q + 1           # p satisfies q | p-1
        a = self.candidateTo(p) # s satisfies a**(p-1) % p == 1 mod p        
        
        return self.gcd(a**((p-1)/q) - 1, p) == 1

    def candidateTo(self, p):
        """Return an a such that a**(p-1) % p == 1"""
        a = 2
        while (self.powmod(a, p-1, p) != 1):
            a += 1
        return a

    def powmod(self, a, exponent, modulus):
        """Return a**exponent % modulus"""
        return a**exponent % modulus
    
    def gcd(self, a, b):
        while (b != 0):
            a, b = b, a % b
        return a
