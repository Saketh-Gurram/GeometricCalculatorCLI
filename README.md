# Geometric Calculator

## **Overview**
The Geometric Calculator is a command-line application that allows users to define, query, and perform operations on 2D geometric shapes. It supports dynamic interactions through a Python-like REPL (Read-Eval-Print Loop) interface.

---

## **Features**
### Supported Shapes
- **Point**: Represented by `(x, y)` coordinates.
- **Line**: Defined by two points.
- **Circle**: Defined by a center point and radius.
- **Rectangle**: Defined by two points (bottom-left and top-right).

### Queries
1. **Area**:
   - Available for circles and rectangles.
2. **Perimeter / Circumference / Length**:
   - Perimeter for rectangles.
   - Circumference for circles.
   - Length for lines.
3. **Distance Between Shapes**:
   - Point-to-Point.
   - Circle-to-Circle.
   - Rectangle-to-Rectangle.
4. **Union**:
   - Compute the smallest shape enclosing two shapes.
   - Supported for circles and rectangles.
5. **Intersection**:
   - Compute overlapping areas or regions.
   - Supported for circles and rectangles.
6. **Numeric Calculations**:
   - Combine numeric and geometric operations dynamically.
     Example:
     ```plaintext
     >>> p1.distance(p2) + p3.distance(p1)
     ```

---

## **Setup Instructions**
1. **Requirements**:
   - Python 3.7 or higher.
   - No additional libraries required (uses built-in Python modules).

2. **Installation**:
   - Clone or download the project files.
   - Ensure the following files are present:
     - `geometric_calculator.py`: The main application code.
     - `test_geometric_calculator.py`: Automated test suite.

3. **Running the Application**:
   - Navigate to the project directory and run:
     ```bash
     python geometric_calculator.py
     ```

4. **Running the Tests**:
   - Execute the test suite to verify functionality:
     ```bash
     python -m unittest test_geometric_calculator.py
     ```

---

## **Usage**
### Commands
1. **Define Shapes**:
   ```plaintext
   >>> p1 = Point(x, y)
   >>> l1 = Line(p1, p2)
   >>> c1 = Circle(p1, radius)
   >>> r1 = Rectangle(p1, p2)
