class PrimalityTester:
    def isGermainPrime(self, q):
        """Determines if q is a Sophie Germain prime"""
        p = 2 * q + 1           # p satisfies q | p-1
        a = self.candidateTo(p) # s satisfies a**(p-1) % p == 1 mod p        
        
        return self.gcd(self.pow(a,(p-1)/q) - 1, p) == 1

    def candidateTo(self, p):
        """Return an a such that a**(p-1) % p == 1"""
        a = 2
        while (self.powmod(a, p-1, p) != 1):
            a += 1
        return a

    def powmod(self, a, exponent, modulus):
        """Return a**exponent % modulus"""
        result, power = 1, a
        while (exponent > 0):
            if (exponent % 2 != 0):
                result = (result * power) % modulus
            exponent, power = exponent / 2, power**2 % modulus
        return result

    def pow(self, a, exponent):
        """Return a**exponent"""
        result, power = 1, a
        while (exponent > 0):
            if (exponent % 2 != 0):
                result = (result * power)
            exponent, power = exponent / 2, power**2
        return result
    
    def gcd(self, a, b):
        while (b != 0):
            a, b = b, a % b
        return a
