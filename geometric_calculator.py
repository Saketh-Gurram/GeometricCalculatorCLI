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
    def distance_circles(circle1, circle2):
        if isinstance(circle1, Circle) and isinstance(circle2, Circle):
            center_distance = circle1.center.distance(circle2.center)
            if center_distance == 0:  # Concentric circles
                return abs(circle1.radius - circle2.radius)
            return max(0, center_distance - (circle1.radius + circle2.radius))
        raise ValueError("Distance is only implemented for Circles.")

    @staticmethod
    def union_circles(circle1, circle2):
        if isinstance(circle1, Circle) and isinstance(circle2, Circle):
            center_distance = circle1.center.distance(circle2.center)
            if center_distance == 0:  # Concentric circles
                return circle1 if circle1.radius > circle2.radius else circle2
            if center_distance + min(circle1.radius, circle2.radius) <= max(circle1.radius, circle2.radius):
                return circle1 if circle1.radius > circle2.radius else circle2

            new_radius = (center_distance + circle1.radius + circle2.radius) / 2
            dx = (circle2.center.x - circle1.center.x) / center_distance
            dy = (circle2.center.y - circle1.center.y) / center_distance
            new_center_x = circle1.center.x + dx * (new_radius - circle1.radius)
            new_center_y = circle1.center.y + dy * (new_radius - circle1.radius)

            new_center = Point(new_center_x, new_center_y)
            return Circle(new_center, new_radius)
        raise ValueError("Union is only implemented for Circles.")

    @staticmethod
    def intersection_circles(circle1, circle2):
        if isinstance(circle1, Circle) and isinstance(circle2, Circle):
            center_distance = circle1.center.distance(circle2.center)
            if center_distance == 0:  # Concentric circles
                smaller_circle = circle1 if circle1.radius < circle2.radius else circle2
                return math.pi * smaller_circle.radius ** 2
            if center_distance >= circle1.radius + circle2.radius:  # No overlap
                return 0

            # Partial overlap
            r1, r2, d = circle1.radius, circle2.radius, center_distance
            term1 = r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
            term2 = r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
            term3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
            return term1 + term2 - term3
        raise ValueError("Intersection is only implemented for Circles.")


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
  > ShapeOperations.distance_circles(c1, c2)
  > ShapeOperations.union_circles(c1, c2)
  > ShapeOperations.intersection_circles(c1, c2)

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
