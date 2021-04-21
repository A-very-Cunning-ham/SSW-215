import random
import math
import unittest

class TestRandom(unittest.TestCase):
    def test_12sided(self):
        rands = []

        a = 1
        b = 12

        for _ in range(10000):
            rands.append(random.randint(a, b))

        n = (b-a) + 1

        expected_mean = (a + b) / 2
        expected_var = (n**2 - 1) / 12

        sample_mean = sum(rands) / len(rands)

        sample_std = 0
        for i in range(0, len(rands)):
            sample_std += ((rands[i] - sample_mean) ** 2)

        sample_std = (sample_std / (len(rands) - 1)) ** (1/2)
        sample_var = sample_std ** 2


        self.assertAlmostEqual(expected_mean, sample_mean, places=1)
        self.assertAlmostEqual(expected_var, sample_var, places=0)

if __name__ == "__main__":
    unittest.main()

