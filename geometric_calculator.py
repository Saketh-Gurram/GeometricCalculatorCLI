import math


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance(self, other):
        if isinstance(other, Point):
            return math.hypot(self.x - other.x, self.y - other.y)
        raise ValueError("Distance can only be calculated between two Points.")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, start, end):
        if isinstance(start, Point) and isinstance(end, Point):
            self.start = start
            self.end = end
        else:
            raise ValueError("Start and End must be Points.")

    def length(self):
        return self.start.distance(self.end)

    def __repr__(self):
        return f"Line({self.start}, {self.end})"


class Circle:
    def __init__(self, center, radius):
        if isinstance(center, Point) and isinstance(radius, (int, float)):
            self.center = center
            self.radius = float(radius)
        else:
            raise ValueError("Center must be a Point and radius must be a number.")

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"


class Rectangle:
    def __init__(self, bottom_left, top_right):
        if isinstance(bottom_left, Point) and isinstance(top_right, Point):
            # Validate that the points form a valid rectangle
            if bottom_left.x == top_right.x or bottom_left.y == top_right.y:
                raise ValueError("The points provided are colinear or identical and cannot form a valid rectangle.")
            self.bottom_left = bottom_left
            self.top_right = top_right
        else:
            raise ValueError("Bottom left and top right must be Points.")

    def area(self):
        width = abs(self.top_right.x - self.bottom_left.x)
        height = abs(self.top_right.y - self.bottom_left.y)
        return width * height

    def perimeter(self):
        width = abs(self.top_right.x - self.bottom_left.x)
        height = abs(self.top_right.y - self.bottom_left.y)
        return 2 * (width + height)

    def __repr__(self):
        return f"Rectangle({self.bottom_left}, {self.top_right})"


class ShapeOperations:
    @staticmethod
    def distance(shape1, shape2):
        if isinstance(shape1, Point) and isinstance(shape2, Point):
            return shape1.distance(shape2)
        elif isinstance(shape1, Circle) and isinstance(shape2, Circle):
            return max(0, shape1.center.distance(shape2.center) - (shape1.radius + shape2.radius))
        elif isinstance(shape1, Rectangle) and isinstance(shape2, Rectangle):
            return ShapeOperations._rectangle_to_rectangle_distance(shape1, shape2)
        elif isinstance(shape1, Circle) and isinstance(shape2, Rectangle):
            return ShapeOperations._circle_to_rectangle_distance(shape1, shape2)
        elif isinstance(shape1, Rectangle) and isinstance(shape2, Circle):
            return ShapeOperations._circle_to_rectangle_distance(shape2, shape1)
        else:
            raise ValueError("Distance calculation is not supported for these shapes.")

    @staticmethod
    def _rectangle_to_rectangle_distance(rect1, rect2):
        horizontal_gap = max(0,
                             rect1.bottom_left.x - rect2.top_right.x,
                             rect2.bottom_left.x - rect1.top_right.x)
        vertical_gap = max(0,
                           rect1.bottom_left.y - rect2.top_right.y,
                           rect2.bottom_left.y - rect1.top_right.y)
        if horizontal_gap == 0 and vertical_gap == 0:
            return 0
        return math.hypot(horizontal_gap, vertical_gap)

    @staticmethod
    def _circle_to_rectangle_distance(circle, rectangle):
        closest_x = max(rectangle.bottom_left.x, min(circle.center.x, rectangle.top_right.x))
        closest_y = max(rectangle.bottom_left.y, min(circle.center.y, rectangle.top_right.y))
        center_to_closest_distance = math.hypot(circle.center.x - closest_x, circle.center.y - closest_y)
        return max(0, center_to_closest_distance - circle.radius)

    @staticmethod
    def union(rect1, rect2):
        if isinstance(rect1, Rectangle) and isinstance(rect2, Rectangle):
            bottom_left = Point(min(rect1.bottom_left.x, rect2.bottom_left.x),
                                min(rect1.bottom_left.y, rect2.bottom_left.y))
            top_right = Point(max(rect1.top_right.x, rect2.top_right.x),
                              max(rect1.top_right.y, rect2.top_right.y))
            return Rectangle(bottom_left, top_right)
        raise NotImplementedError("Union is only implemented for Rectangles.")

    @staticmethod
    def intersection(rect1, rect2):
        if isinstance(rect1, Rectangle) and isinstance(rect2, Rectangle):
            bottom_left = Point(max(rect1.bottom_left.x, rect2.bottom_left.x),
                                max(rect1.bottom_left.y, rect2.bottom_left.y))
            top_right = Point(min(rect1.top_right.x, rect2.top_right.x),
                              min(rect1.top_right.y, rect2.top_right.y))
            if bottom_left.x < top_right.x and bottom_left.y < top_right.y:
                return Rectangle(bottom_left, top_right)
            return None  # No intersection
        raise NotImplementedError("Intersection is only implemented for Rectangles.")


class GeometricCalculatorCLI:
    def __init__(self):
        self.shapes = {}

    def start(self):
        print("Welcome to the Geometric Calculator!")
        print("Type 'help' for a list of commands.")
        while True:
            try:
                command = input(">>> ").strip()
                if command.lower() in ("exit", "quit"):
                    break
                elif command.lower() == "help":
                    self.print_help()
                else:
                    self.process_command(command)
            except Exception as e:
                print(f"Error: {e}")

    def print_help(self):
        print("""
Commands:
- Define shapes:
  > p1 = Point(x, y)
  > l1 = Line(p1, p2)
  > c1 = Circle(p1, radius)
  > r1 = Rectangle(p1, p2)

- Query shapes:
  > p1.distance(p2)
  > c1.area()
  > c1.circumference()
  > r1.area()
  > r1.perimeter()
  > ShapeOperations.distance(shape1, shape2)
  > ShapeOperations.union(rect1, rect2)
  > ShapeOperations.intersection(rect1, rect2)

- Exit:
  > exit / quit
""")

    def process_command(self, command):
        context = {
            "Point": Point,
            "Line": Line,
            "Circle": Circle,
            "Rectangle": Rectangle,
            "ShapeOperations": ShapeOperations,
            **self.shapes
        }
        if "=" in command:
            name, expr = command.split("=", 1)
            name = name.strip()
            shape = eval(expr.strip(), context)
            self.shapes[name] = shape
            print(f"{name} = {shape}")
        else:
            result = eval(command.strip(), context)
            print(result)


if __name__ == "__main__":
    GeometricCalculatorCLI().start()
