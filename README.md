
# Geometric Calculator CLI

## Description
This is a command-line-based Geometric Calculator that allows users to define 2D shapes and query their measurements.

## Features
- Define shapes: Point, Line, Circle, Rectangle.
- Perform geometric operations:
  - Calculate distance between points.
  - Compute area, perimeter, and circumference.
  - Find the length of a line.

## Commands
- Define shapes:
  - `p1 = Point(x, y)`
  - `l1 = Line(p1, p2)`
  - `c1 = Circle(p1, radius)`
  - `r1 = Rectangle(p1, p2)`
- Query shapes:
  - `p1.distance(p2)`
  - `c1.area()`
  - `c1.circumference()`
  - `r1.area()`
  - `r1.perimeter()`
  - `l1.length()`
- Exit: `exit` or `quit`

## How to Run
1. Install Python 3.x.
2. Save the `geometric_calculator.py` script in a directory.
3. Run the script using:
   ```bash
   python geometric_calculator.py
   ```

## Assumptions and Known Issues
- Assumes user input follows the specified syntax.
- Currently does not support persistent storage of shapes.

## License
This project is for educational purposes.
