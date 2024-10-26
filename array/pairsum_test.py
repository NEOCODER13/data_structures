import unittest

from pairsum import pairsum

class TestPairSum(unittest.TestCase):
    
    def test_valid_pair(self):
        N = [1, 2, 3, 4, 5]
        target = 9
        result = pairsum(N, target)
        self.assertEqual(result, [4, 5])  # Expected result

    def test_no_pair(self):
        N = [1, 2, 3, 4, 5]
        target = 10
        result = pairsum(N, target)
        self.assertEqual(result, [])  # No valid pair found

    def test_single_element(self):
        N = [5]
        target = 5
        result = pairsum(N, target)
        self.assertEqual(result, [])  # Not enough elements to form a pair

    def test_empty_list(self):
        N = []
        target = 5
        result = pairsum(N, target)
        self.assertEqual(result, [])  # Empty list should return no pair

    def test_negative_numbers(self):
        N = [-10, -5, 0, 5, 10]
        target = 0
        result = pairsum(N, target)
        self.assertEqual(result, [-10, 10])  # Pair with negative numbers

    def test_duplicate_numbers(self):
        N = [1, 2, 2, 3, 3, 4]
        target = 6
        result = pairsum(N, target)
        self.assertEqual(result, [2, 4])  # Check with duplicates

    def test_large_target(self):
        N = [10, 20, 30, 40, 50]
        target = 90
        result = pairsum(N, target)
        self.assertEqual(result, [40, 50])  # Large target test case
    
    def test_multiple_pairs(self):
        N = [1, 2, 3, 4, 5, 6]
        target = 7
        result = pairsum(N, target)
        self.assertEqual(result, [1, 6])  # Should return the first valid pair
    
if __name__ == '__main__':
    unittest.main()

