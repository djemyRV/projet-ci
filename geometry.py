"""
@file geometry.py
@brief This module provides basic geometric calculations.
"""def rectangle_area(length, width):
    """
    Calculates the area of a rectangle.    @param length Length of the rectangle
    @param width Width of the rectangle
    @return The area of the rectangle
    """
    return length * widthdef rectangle_perimeter(length, width):
    """
    Calculates the perimeter of a rectangle.    @param length Length of the rectangle
    @param width Width of the rectangle
    @return The perimeter of the rectangle
    """
    return 2 * (length + width)def circle_area(radius):
    """
    Calculates the area of a circle.    @param radius Radius of the circle
    @return The area of the circle
    """
    from math import pi
    return pi * (radius ** 2)def circle_circumference(radius):
    """
    Calculates the circumference of a circle.    @param radius Radius of the circle
    @return The circumference of the circle
    """
    from math import pi
    return 2 * pi * radius
