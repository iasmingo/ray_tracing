from primitives import *

class Intersectable:
    """
    Classe abstrata para superficies que podem ter interseções com raios da câmera
    """
    def __init__(self):
        raise Exception("Você não pode instanciar essa classe")

class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r: float = r
        self.g: float = g
        self.b: float = b

Color.WHITE = Color(1, 1, 1)
Color.RED = Color(1, 0, 0)
Color.GREEN = Color(0, 1, 0)
Color.BLUE = Color(0, 0, 1)
Color.YELLOW = Color(1, 1, 0)

class Plane(Intersectable):
    def __init__(self, position: Point3, normal: Vector3, color: Color = Color.WHITE):
        self.color = color
        self.position = position
        self.normal = normal

class Sphere(Intersectable):
    def __init__(self, position: Point3, radius: float, color: Color = Color.WHITE):
        self.color: Color = color
        self.position: Point3 = position
        self.radius: float = radius

a = Sphere(Point3(0, 0, 0), 2)
print(a)
