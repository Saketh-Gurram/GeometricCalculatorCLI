import unittest
from geometric_calculator import Point, Line, Circle, Rectangle, ShapeOperations


class TestGeometricCalculator(unittest.TestCase):
    def test_point_distance(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertAlmostEqual(p1.distance(p2), 5.0)
        self.assertAlmostEqual(p1.distance(p1), 0.0)

    def test_line_length(self):
        l = Line(Point(0, 0), Point(3, 4))
        self.assertAlmostEqual(l.length(), 5.0)
        l_zero = Line(Point(0, 0), Point(0, 0))
        self.assertAlmostEqual(l_zero.length(), 0.0)

    def test_circle_area_circumference(self):
        c = Circle(Point(0, 0), 5)
        self.assertAlmostEqual(c.area(), 78.53981633974483)
        self.assertAlmostEqual(c.circumference(), 31.41592653589793)
        c_zero = Circle(Point(0, 0), 0)
        self.assertAlmostEqual(c_zero.area(), 0.0)
        self.assertAlmostEqual(c_zero.circumference(), 0.0)

    def test_rectangle_area_perimeter(self):
        r = Rectangle(Point(0, 0), Point(4, 6))
        self.assertEqual(r.area(), 24.0)
        self.assertEqual(r.perimeter(), 20.0)
        with self.assertRaises(ValueError):
            Rectangle(Point(0, 0), Point(0, 6))  # Invalid rectangle

    def test_distance_circles(self):
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(10, 0), 3)
        self.assertAlmostEqual(ShapeOperations.distance_circles(c1, c2), 2.0)
        c3 = Circle(Point(0, 0), 3)
        self.assertAlmostEqual(ShapeOperations.distance_circles(c1, c3), 2.0)

    def test_union_circles(self):
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(10, 0), 3)
        union = ShapeOperations.union_circles(c1, c2)
        self.assertAlmostEqual(union.radius, 8.75)
        self.assertAlmostEqual(union.center.x, 6.25)
        self.assertAlmostEqual(union.center.y, 0.0)

    def test_intersection_circles(self):
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(6, 0), 5)
        self.assertAlmostEqual(ShapeOperations.intersection_circles(c1, c2), 45.544927054359336)

    def test_union_rectangle(self):
        r1 = Rectangle(Point(0, 0), Point(4, 4))
        r2 = Rectangle(Point(2, 2), Point(6, 6))
        union = ShapeOperations.union(r1, r2)
        self.assertEqual(union.bottom_left.x, 0)
        self.assertEqual(union.bottom_left.y, 0)
        self.assertEqual(union.top_right.x, 6)
        self.assertEqual(union.top_right.y, 6)

    def test_intersection_rectangle(self):
        r1 = Rectangle(Point(0, 0), Point(4, 4))
        r2 = Rectangle(Point(2, 2), Point(6, 6))
        intersection = ShapeOperations.intersection(r1, r2)
        self.assertEqual(intersection.bottom_left.x, 2)
        self.assertEqual(intersection.bottom_left.y, 2)
        self.assertEqual(intersection.top_right.x, 4)
        self.assertEqual(intersection.top_right.y, 4)
        r3 = Rectangle(Point(5, 5), Point(8, 8))
        self.assertIsNone(ShapeOperations.intersection(r1, r3))


if __name__ == "__main__":
    unittest.main()
