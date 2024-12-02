import unittest
from solutions.day1 import calculate_sums, calculate_similarity_score

class TestFunctions(unittest.TestCase):
   
    def test_calculate_sums(self):
        data = [1, 2, 3, 4, 5, 6]
        result = calculate_sums(data)

        expected = 3
        self.assertEqual(result, expected)

    def test_calculate_similarity_score(self):
        data = [1, 2, 3, 4, 5, 1]
        result = calculate_similarity_score(data)

        expected = 1
        self.assertEqual(result, expected)

    def test_calculate_sums_empty_input(self):
        data = []
        result = calculate_sums(data)

        expected = 0
        self.assertEqual(result, expected)

    def test_calculate_similarity_score_empty_input(self):
        data = []
        result = calculate_similarity_score(data)
        
        expected = 0
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
