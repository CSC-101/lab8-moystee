import group
import unittest

class TestCases(unittest.TestCase):
    # Part 1
    def test_groups_of_3_1(self):
        input = [2, 1, 9, 0, 4, 5, 1, 9, 0, 3]
        expected = [[2,1,9],[0,4,5],[1,9,0],[3]]
        actual = group.groups_of_3(input)
        self.assertEqual(expected, actual)
    def test_groups_of_3_2(self):
        input = [2, 1, 9, 0, 4]
        expected = [[2,1,9],[0,4]]
        actual = group.groups_of_3(input)
        self.assertEqual(expected, actual)