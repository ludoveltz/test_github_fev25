import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        """Initialize circle with either radius or diameter"""
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified")

    @property
    def diameter(self):
        """Get circle's diameter"""
        return self.radius * 2

    @property
    def area(self):
        """Calculate circle's area"""
        return math.pi * self.radius ** 2

    def __str__(self):
        """String representation of the circle"""
        return f"Circle with radius: {self.radius:.2f}"

    def __repr__(self):
        """Formal string representation"""
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """Add two circles together"""
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        """Compare if this circle is greater than other"""
        return self.radius > other.radius

    def __eq__(self, other):
        """Compare if circles are equal"""
        return self.radius == other.radius

    def __lt__(self, other):
        """Compare if this circle is less than other (for sorting)"""
        return self.radius < other.radius

# Optional: Drawing circles with Turtle
try:
    import turtle

    def draw_circles(circles):
        """Draw sorted circles using Turtle"""
        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed(0)  # Fastest speed
        
        # Start from the smallest circle
        for circle in sorted(circles):
            t.circle(circle.radius * 10)  # Multiply by 10 for better visibility
            t.up()
            t.right(90)
            t.forward(10)
            t.left(90)
            t.down()
        
        screen.exitonclick()

except ImportError:
    print("Turtle module not available")

# Test the implementation
def test_circles():
    # Create circles
    c1 = Circle(radius=3)
    c2 = Circle(diameter=8)
    c3 = Circle(radius=5)

    # Test string representation
    print(f"Circle 1: {c1}")
    print(f"Circle 2: {c2}")

    # Test area calculation
    print(f"\nArea of circle 1: {c1.area:.2f}")

    # Test addition
    c4 = c1 + c2
    print(f"\nNew circle after addition: {c4}")

    # Test comparisons
    print(f"\nIs circle 1 bigger than circle 2? {c1 > c2}")
    print(f"Are circle 1 and circle 2 equal? {c1 == c2}")

    # Test sorting
    circles = [c1, c2, c3]
    sorted_circles = sorted(circles)
    print("\nSorted circles:")
    for circle in sorted_circles:
        print(circle)

    # Optional: Draw circles
    try:
        draw_circles(circles)
    except NameError:
        pass

if __name__ == "__main__":
    test_circles()