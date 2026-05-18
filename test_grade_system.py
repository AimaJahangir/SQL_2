import unittest

from grade_system import calculate_grade


class TestGradeSystem(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(calculate_grade(95), "A")

    def test_grade_B(self):
        self.assertEqual(calculate_grade(85), "B")

    def test_grade_C(self):
        self.assertEqual(calculate_grade(75), "C")

    def test_grade_D(self):
        self.assertEqual(calculate_grade(65), "D")

    def test_grade_F(self):
        self.assertEqual(calculate_grade(40), "F")


if __name__ == "__main__":
    unittest.main()