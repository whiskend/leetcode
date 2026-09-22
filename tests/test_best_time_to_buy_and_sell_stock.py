import unittest

from python.easy.best_time_to_buy_and_sell_stock import Solution


class BestTimeToBuyAndSellStockTests(unittest.TestCase):
    def test_returns_best_profit(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_returns_zero_when_prices_only_fall(self):
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)

    def test_handles_two_prices(self):
        self.assertEqual(Solution().maxProfit([2, 4]), 2)
