import unittest

import functions

class TestFunctions(unittest.TestCase):
    def test_black_scholes_call(self):
        S = 100
        K = 105
        T = -.5
        r = -0.2
        vol = 0.2
        call_price = functions.black_scholes_call(S, K, T, r, vol)
        self.assertEqual(call_price, 0.0)

if __name__ == '__main__':
    unittest.main()