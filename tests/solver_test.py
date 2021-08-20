from solver import funcs
import unittest


class TestSolver(unittest.TestCase):
    def test_fibb_at_position(self):
        test_cases = [
            0, 1, 1, 2, 3, 5, 8, 13,
        ]
        for pos, result in enumerate(test_cases):
            self.assertEqual(funcs.fibbonaci(pos), result)

    def test_fibb_at_position_recursive(self):
        test_cases = [
            0, 1, 1, 2, 3, 5, 8, 13,
            21, 34, 55, 89, 144, 233,
            377, 610, 987, 1597, 2584,
            4181, 6765, 10946, 17711, 28657,
            46368, 75025, 121393, 196418, 317811
        ]
        for pos, result in enumerate(test_cases):
            self.assertEqual(funcs.fibbonaci_recursive(pos), result)

    def test_factorial_of_number(self):
        test_cases = {
            10: 3628800,
            9: 362880,
            8: 40320,
            1: 1
        }
        for input_value, solution in test_cases.items():
            self.assertEqual(solution, funcs.factorial(input_value))

    def test_recursive_factorial(self):
        test_cases = {
            10: 3628800,
            4: 24,
            5: 120,
            1: 1
        }
        for input_value, solution in test_cases.items():
            self.assertEqual(solution, funcs.factorial_recursive(input_value))

    def _test_recursive_ackermann(self):
        test_set = [
            ((0, 0), 1),
            ((0, 1), 2),
            ((0, 2), 3),
            ((0, 3), 4),
            ((0, 4), 5),
            ((0, 5), 6),
            ((0, 6), 7),
            ((0, 7), 8),
            ((0, 8), 9),
            ((1, 0), 2),
            ((1, 1), 3),
            ((1, 2), 4),
            ((1, 3), 5),
            ((1, 4), 6),
            ((1, 5), 7),
            ((1, 6), 8),
            ((1, 7), 9),
            ((1, 8), 10),
            ((2, 0), 3),
            ((2, 1), 5),
            ((2, 2), 7),
            ((2, 3), 9),
            ((2, 4), 11),
            ((2, 5), 13),
            ((2, 6), 15),
            ((2, 7), 17),
            ((2, 8), 19),
            ((3, 0), 5),
            ((3, 1), 13),
            ((3, 2), 29),
            ((3, 3), 61),
            ((3, 4), 125),
            ((3, 5), 253),
            ((3, 6), 509),
            ((3, 7), 1021),
            ((3, 8), 2045)
        ]
        for input_values in test_set:
            (n, m) = input_values[0]
            result = input_values[1]
            # NOTE: not goona work for all cases
            self.assertEqual(funcs.ackermann_recursive(n, m), result)
