import unittest
from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumferenceclass TestGeometry(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(5, 5), 25)
        self.assertEqual(rectangle_area(0, 4), 0)    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(5, 5), 20)
        self.assertEqual(rectangle_perimeter(0, 4), 8)    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), 3.14159, places=5)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.5), 19.63495, places=5)    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(1), 6.28318, places=5)
        self.assertAlmostEqual(circle_circumference(0), 0)
        self.assertAlmostEqual(circle_circumference(2.5), 15.70796, places=5)if __name__ == '__main__':
    unittest.main()
