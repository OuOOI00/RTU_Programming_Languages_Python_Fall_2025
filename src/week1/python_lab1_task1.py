"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""


import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    return (math.pi*pow(radius,2))
    # TODO: implement formula using math.pi
    pass

if __name__ == "__main__":
    print("Give us radius - ")
    us_answ = int(input())
    print(circle_area(us_answ))
    # TODO: ask for user input, call circle_area(), and print formatted result
    pass
