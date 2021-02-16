""" The primary goal of this file is to demonstrate a simple python program to classify triangles

    author: Fatih Izgi
    date: 16-Feb-2021
    python: v3.9.1
"""


def classifyTriangle(a, b, c):
    """ This function returns a string with the type of triangle from three integer values
        corresponding to the lengths of the three sides of the Triangle.
    """

    # verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a < 0 or a > 200 or c < 0 or b > 200 or c < 0 or c > 200:
        return 'InvalidInput'

    # the sum of any two sides must be strictly less than the third side
    if (a <= abs(b - c)) or abs(b <= (a - c)) or abs(c <= (a - b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle 
    if a == b and a == c and b == c:
        return 'Equilateral'
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    elif (a != b) and (a != c) and (b != c):
        return 'Scalene'
    else:
        return 'Isosceles'
