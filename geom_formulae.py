__author__ = 'hagos'
from numpy import *
from numbers import Number
def square_perimeter(side : Number):
    """
    Calculate perimeter of a square from side length.
    :param side:  the side length
    :return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """

    return 4*side

def square_area(side):
    """
    Calculate area of a square from side length.
    :param side: the side length
    :return: the area (units^2 from side)
    >>> square_area(4)
    16
    """

    return side*side

if __name__ == "__main__":
    sampleSide = 4
    print("area:",
          square_area(sampleSide),
          "perimeter:",
          square_perimeter(sampleSide))

def area_circle(radius: Number) -> Number:
    """
    Calculate area of a circle.
    :param radius: the radius of circle
    :return: the area (square units of radius)
    >>>area_circle(7)
    153.93804002589985
    """
    return pi*radius**2

def perimeter_circle(radius: Number) ->Number:
   """
   Calculate perimeter of the circle.
   :param radius: the radius of circle
   :return: the perimeter (same units of radius)
   >>>perimeter_circle(6)
   37.69911184307752

   """
   return 2*pi*radius

def perimeter_rectangle(length: Number, width: Number) -> Number:
    """
    Calculate perimeter of the rectangle.
    :param length: the length of rectangle
    :param width: the width of rectangle
    :return: the perimeter (same units of length and width)
    >>>perimeter_rectangle(8,10)
    36
    """
    return 2*length + 2*width

def area_rectangle(length: Number, width: Number) -> Number:
    """
    Calculate area of the rectangle.
    :param length: the length of rectangle
    :param width: the width of rectangle
    :return: the area (square units of length and width)
    >>>area_rectangle(8,10)
    80
    """
    return length*width

print(area_rectangle(8,10))
def surface_area_cylinder(radius: Number, height: Number) -> Number:
    """
    Calculate surface area of the cylinder.
    :param radius: the radius the cylinder
    :param height: the height of the cylinder
    :return: the surface area (square units of the radius and height)
    >>>

    """
    return 2*pi*radius**2 + 2*pi*radius*height

print(surface_area_cylinder(4,10))

def volum_cylinder(radius: Number, height: Number) -> Number:
    """
    Calculate volume of the cylinder.
    :param radius: the radius the cylinder
    :param height: the height of the cylinder
    :return: the volume (cubic units of the radius and height)
    >>>volum_cylinder(8,10)
    2010.6192982974676

    """
    return pi*radius**2*height

print(volum_cylinder(8,10))

def perimeter_trapezoid(side_1: Number, side_2: Number, base_1: Number, base_2: Number) -> Number:
    """
    Calculate perimeter of the trapezoid.
    :param side_1: the side of trapezoid
    :param side_2_: the  side of trapezoid
    :param base_1: the base of trapezoid
    :param base_2: the base of trapezoid
    :return: the perimeter (same units of sides and bases)
    >>>perimeter_trapezoid(3, 5, 4, 7)
    19
    """
    return side_1 + side_2 + base_1 + base_2

print(perimeter_trapezoid(3, 5, 4, 7))

def area_trapezoid(base_1: Number, base_2: Number, height: Number) -> Number:
    """
    Calculate area of the trapezoid.
    :param base_1: the base of trapezoid
    :param base_2: the base of trapezoid
    :param height: the height of trapezoid
    :return: the area (square units of the base and height)
    >>>
    """
    return 1/2*(base_1 + base_2)*height

print(area_trapezoid(5, 7, 4))

def surface_area_cone(side: Number, radius: Number) -> Number:
    """
    Calculate surface area of the cone.
    :param side: the side of the cone
    :param radius: the radius of the cone
    :return: the surface area (square units of the side and radius)
    >>>surface_area_cone(10,3)
    122.52211349000193
    """
    return pi*radius*side + pi*radius**2

print(surface_area_cone(10, 3))

def volume_cone(r,h: Number) -> Number:
    """
    Calculate volume of the cone.
    :param r: the radius of the cone
    :param h: the height of the cone
    :return: the volume (cubic units of the radius and height)
    >>>volume_cone(3, 8)
    75.39822368615503
    """
    return 1/3*pi*r**2*h

print(volume_cone(3, 8))

def surface_area_rectangular_prism(w,h,l: Number) -> Number:
    """
    Calculate surface area of the rectangular prism.
    :param w: the width of the prism
    :param h: the height of the prism
    :param l: the length of the prism
    :return: the surface area (square units of the width, height and length)
    >>>surface_area_rectangular_prism(2, 4, 8)
    112
    """
    return 2*(w*h + l*w + l*h)

print(surface_area_rectangular_prism(2, 4, 8))

def volume_rectangular_prism(w,h,l: Number) -> Number:
    """
    Calculate volume of the rectangular prism
    :param w: the width of the prism
    :param h: the height of the prism
    :param l: the length of the prism
    :return: the volume (cubic units of the width, height and length)
    >>>volume_rectangular_prism(2, 4, 8)
    64
    """
    return l*w*h

print(volume_rectangular_prism(2, 4, 8))

def surface_area_sphere(r: Number) -> Number:
    """
    Calculate surface area of the sphere.
    :param r: the radius of the sphere
    :return: the surface area (square units of the radius)
    >>>surface_area_sphere(5)
    314.1592653589793
    """
    return 4*pi*r**2

print(surface_area_sphere(5))

def volume_sphere(r: Number) -> Number:
    """
    Calculate volume of the sphere.
    :param r: the radius of the sphere
    :return: the volume (cubic units of the radius)
    >>>volume_sphere(5)
    523.5987755982989
    """
    return 4/3*pi*r**3

print(volume_sphere(5))

def perimeter_regular_polygon(n,s: Number) -> Number:
    """
    Calculate perimeter of the regular polygon.
    :param n: the number of sides of the polygon
    :param s: the side of the polygon
    :return: the perimeter (same unit of the side)
    >>>perimeter_regular_polygon(8, 4)
    32
    """
    return n*s

print(perimeter_regular_polygon(8, 4))

def area_regular_polygon(n,s: Number) -> Number:
    """
    Calculate area of the regular polygon.
    :param n: the number of sides of the polygon
    :param s: the side of the polygon
    :return: the area (square units of the side)
    >>>area_regular_polygon(8, 4)
    77.2548339959
    """
    return 1/4*n*s**2*(cos(pi/n)/sin(pi/n))

print(area_regular_polygon(8, 4))

def lateral_area_regular_pyramid(p,h_1: Number) -> Number:
    """
    Calculate lateral area of the regular pyramid.
    :param p: the perimeter of the pyramid
    :param h_1: the slant height of the pyramid
    :return: the lateral area
    >>>lateral_area_regular_pyramid(15, 6)
    45
    """
    return 1/2*p*h_1

print(lateral_area_regular_pyramid(15, 6))

def surface_area_regular_pyramid(A_b,A_l: Number) -> Number:
    """
    Calculate surface area of the regular pyramid.
    :param A_b: the area of the base of the pyramid
    :param A_l: the lateral area of the pyramid
    :return: the surface area
    >>>surface_area_regular_pyramid(20, 45)
    65
    """
    return A_b + A_l

print(surface_area_regular_pyramid(20, 45))

def volume_regular_pyramid(A_b,h: Number) -> Number:
     """
     Calculate volume of the regular pyramid.
     :param A_b: the area of the base of the pyramid
     :param h: the height of the pyramid
     :return: the volume
     >>>volume_regular_pyramid(20, 8)
     53.33333333333333
     """
     return 1/3*A_b*h

print(volume_regular_pyramid(20, 8))







































