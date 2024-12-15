from cython import (
    cclass,
    cfunc,
    double
)
from primitives import *

@cclass
class Intersectable:
    """
    Classe abstrata para superficies que podem ter interseções com raios da câmera
    """
    def __init__(self):
        raise Exception("Você não pode instanciar essa classe")

@cclass
class Color:
    def __init__(self, r: double, g: double, b: double):
        self.r: double = r
        self.g: double = g
        self.b: double = b

Color.WHITE =   Color(1, 1, 1)
Color.RED =     Color(1, 0, 0)
Color.GREEN =   Color(0, 1, 0)
Color.BLUE =    Color(0, 0, 1)
Color.YELLOW =  Color(1, 1, 0)

@cclass
class Plane (Intersectable):
    color: Color
    position: Point3
    normal: Vector3

    def __init__(self, position: Point3, normal: Vector3, color: Color = Color.WHITE):
        self.color = color
        self.position = position
        self.normal = normal

@cclass
class Sphere (Intersectable):
    color: Color
    position: Point3
    radius: double

    def __init__(self, position: Point3, radius: double, color: Color = Color.WHITE):
        self.color: Color = color
        self.position: Point3 = position
        self.radius: double = radius

a = Sphere(Point3(0, 0, 0), 2)
print(a)