import unittest

import functions

class TestFunctions(unittest.TestCase):
    def test_implied_volatility(self):
        S = 1074.310893
        K = 1022.5
        T = 0.065753
        r = 0.015593
        C = 55.85
        row = {'forward_price': S, 'strike_price': K, 'time_to_maturity': T, 'risk_free_rate': r, 'option_price': C}

        call_price = functions.implied_volatility(row)
        self.assertEqual(call_price, 0.17355964711160923) # what the test ?

if __name__ == '__main__':
    unittest.main()