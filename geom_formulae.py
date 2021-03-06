__author__ = 'hagos'
from numpy import *
from numbers import Number


def area_circle(radius: Number) -> Number:
    """
    Calculate area of a circle.
    @param radius: the radius of circle
    @return: the area (square units of radius)
    >>>area_circle(3)
    28.274333882308138
    """
    return pi*radius**2


def perimeter_circle(radius: Number) ->Number:
    """
   Calculate perimeter of the circle.
   @param radius: the radius of circle
   @return: the perimeter (same units of radius)
   >>>perimeter_circle(3)
   18.84955592153876
   """
    return 2*pi*radius


def perimeter_rectangle(length: Number, width: Number) -> Number:
    """
    Calculate perimeter of the rectangle.
    @param length: the length of rectangle
    @param width: the width of rectangle
    @return: the perimeter (same units of length and width)
    >>>perimeter_rectangle(8,10)
    36
    """
    return (2*length) + (2*width)


def area_rectangle(length, width) -> Number:
    """
    Calculate area of the rectangle.
    @param length: the length of rectangle
    @param width: the width of rectangle
    @return: the area (square units of length and width)
    >>>area_rectangle(8,10)
    80
    """
    return length*width


def surface_area_cylinder(radius: Number, height: Number) -> Number:
    """
    Calculate surface area of the cylinder.
    @param radius: the radius the cylinder
    @param height: the height of the cylinder
    @return: the surface area (square units of the radius and height)
    >>>surface_area_cylinder(3, 4)
    131.94689145077132
    """
    return 2*pi*radius**2 + 2*pi*radius*height


def volume_cylinder(radius: Number, height: Number) -> Number:
    """
    Calculate volume of the cylinder.
    @param radius: the radius the cylinder
    @param height: the height of the cylinder
    @return: the volume (cubic units of the radius and height)
    >>>volume_cylinder(3,4)
    113.09733552923255
    """
    return pi*radius**2*height


def perimeter_trapezoid(side_1, side_2, base_1, base_2) -> Number:
    """
    Calculate perimeter of the trapezoid.
    @param side_1: the side of trapezoid
    @param side_2: the  side of trapezoid
    @param base_1: the base of trapezoid
    @param base_2: the base of trapezoid
    @return: the perimeter (same units of sides and bases)
    >>>perimeter_trapezoid(3, 5, 4, 7)
    19
    """
    return side_1 + side_2 + base_1 + base_2


def area_trapezoid(base_1, base_2, height) -> Number:
    """
    Calculate area of the trapezoid.
    @param base_1: the base of trapezoid
    @param base_2: the base of trapezoid
    @param height: the height of trapezoid
    @return: the area (square units of the base and height)
    >>>area_trapezoid(4, 7, 6)
    33.0
    """
    return 1/2*(base_1 + base_2)*height


def surface_area_cone(side: Number, radius: Number) -> Number:
    """
    Calculate surface area of the cone.
    @param side: the side of the cone
    @param radius: the radius of the cone
    @return: the surface area (square units of the side and radius)
    >>>surface_area_cone(5,3)
    75.39822368615503
    """
    return pi*radius*side + pi*radius**2


def volume_cone(r, h: Number) -> Number:
    """
    Calculate volume of the cone.
    @param r: the radius of the cone
    @param h: the height of the cone
    @return: the volume (cubic units of the radius and height)
    >>>volume_cone(3, 4)
    37.69911184307752
    """
    return 1/3*pi*r**2*h


def surface_area_rectangular_prism(w, h, l) -> Number:
    """
    Calculate surface area of the rectangular prism.
    @param w: the width of the prism
    @param h: the height of the prism
    @param l: the length of the prism
    @return: the surface area (square units of the width, height and length)
    >>>surface_area_rectangular_prism(2, 4, 8)
    112
    """
    return 2*(w*h + l*w + l*h)


def volume_rectangular_prism(w, h, l) -> Number:
    """
    Calculate volume of the rectangular prism
    @param w: the width of the prism
    @param h: the height of the prism
    @param l: the length of the prism
    @return: the volume (cubic units of the width, height and length)
    >>>volume_rectangular_prism(2, 4, 8)
    64
    """
    return l*w*h


def surface_area_sphere(r: Number) -> Number:
    """
    Calculate surface area of the sphere.
    @param r: the radius of the sphere
    @return: the surface area (square units of the radius)
    >>>surface_area_sphere(3)
    113.09733552923255
    """
    return 4*pi*r**2


def volume_sphere(r: Number) -> Number:
    """
    Calculate volume of the sphere.
    @param r: the radius of the sphere
    @return: the volume (cubic units of the radius)
    >>>volume_sphere(3)
    113.09733552923254
    """
    return 4/3*pi*r**3


def perimeter_regular_polygon(n, s: Number) -> Number:
    """
    Calculate perimeter of the regular polygon.
    @param n: the number of sides of the polygon
    @param s: the side of the polygon
    @return: the perimeter (same unit of the side)
    >>>perimeter_regular_polygon(8, 4)
    32
    """
    return n*s


def area_regular_polygon(n, s: Number) -> Number:
    """
    Calculate area of the regular polygon.
    @param n: the number of sides of the polygon
    @param s: the side of the polygon
    @return: the area (square units of the side)
    >>>area_regular_polygon(8, 4)
    77.2548339959
    """
    return 1/4*n*s**2*(cos(pi/n)/sin(pi/n))


def lateral_area_regular_pyramid(p, h_1: Number) -> Number:
    """
    Calculate lateral area of the regular pyramid.
    @param p: the perimeter of the pyramid
    @param h_1: the slant height of the pyramid
    @return: the lateral area
    >>>lateral_area_regular_pyramid(15, 6)
    45
    """
    return 1/2*p*h_1


def surface_area_regular_pyramid(a_b, a_l: Number) -> Number:
    """
    Calculate surface area of the regular pyramid.
    @param a_b: the area of the base of the pyramid
    @param a_l: the lateral area of the pyramid
    @return: the surface area
    >>>surface_area_regular_pyramid(20, 45)
    65
    """
    return a_b + a_l


def volume_regular_pyramid(a_b, h: Number) -> Number:
    """
     Calculate volume of the regular pyramid.
     @param a_b: the area of the base of the pyramid
     @param h: the height of the pyramid
     @return: the volume
     >>>volume_regular_pyramid(20, 8)
     53.33333333333333
     """
    return 1/3*a_b*h


def surface_area_cube(s: Number) -> Number:
    """
    Calculate surface area of the cube.
    @param s: the side of the cube
    @return: the surface area
    >>>surface_area_cube(6)
    216
    """
    return 6*s**2


def volume_cube(s: Number) -> Number:
    """
    Calculate volume of the cube.
    @param s: the side of the cube
    @return: the volume
    >>>volume_cube(6)
    216
    """
    return s**3


def perimeter_triangle(a, b, c: Number) -> Number:
    """
    Calculate perimeter of the triangle.
    @param a: the side of the triangle
    @param b: the side of the triangle
    @param c: the side of the triangle
    @return: the perimeter
    >>>perimeter_triangle(3, 5, 6)
    14
    """
    return a + b + c


def area_triangle(b, h: Number) -> Number:
    """
    Calculate area of the triangle.
    @param b: the base of the triangle
    @param h: the height of the triangle
    @return: the area
    >>>area_triangle(5, 6)
    15
    """
    return 1/2*b*h


def area_triangle(x=None, y=None, z=None, h=None, theta=None) ->Number:
    """
    Calculate area of a triangle given adequate arguments.
    @param x: the dimension of the first side of the triangle
    @param y: the dimension of the second side of the triangle
    @param z: the dimension of the third side of the triangle
    @param h: the height of the triangle
    @param theta: the angle given in the triangle (in radian)
    @return: the area of the triangle
    >>>area_triangle(x=4, y=3, z=5)
    6
    >>>area_triangle(x=4, y=3, theta=pi/2)
    6
    >>>area_triangle(x=4, h=3)
    6
    """
    if (x is not None) & (y is not None) & (z is not None):
        s = (x + y + z)/2
        area = (s*(s - x)*(s - y)*(s - z))**(1/2)
        return area
    elif (x is not None) & (y is not None) & (theta is not None):
        area = 1/2*x*y*sin(theta)
        return area
    elif (x is not None) & (h is not None):
        area = x*h/2
        return area
    else:
        return "the argument given are inadequate to compute area"

print(area_triangle(x=10))
print(area_triangle(y=15))
print(area_triangle(z=20))
