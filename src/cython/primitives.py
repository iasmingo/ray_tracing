import math
import cython

@cython.cclass
class Point3:
    """
    Representa um ponto em um espaço tridimensional.

    Atributos:
        x (float): Coordenada X do ponto.
        y (float): Coordenada Y do ponto.
        z (float): Coordenada Z do ponto.
    """
    x = cython.declare(cython.double, visibility='public')
    y = cython.declare(cython.double, visibility='public')
    z = cython.declare(cython.double, visibility='public')

    @cython.locals(x=cython.double, y=cython.double, z=cython.double)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @cython.locals(p2 = Point3) # type: ignore
    @cython.returns(cython.double)
    def dist(p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        dz = p1.z - p2.z
        return (dx**2 + dy**2 + dz**2) ** (1/2)

    def __str__(p):
        return f"({p.x}, {p.y}, {p.z})"

    @cython.locals(p = Point3) #type: ignore
    @cython.returns(Vector3) #type: ignore
    def to(self, p): 
        return Vector3(p.x - self.x, p.y - self.y, p.z - self.z)
    
    @cython.locals(p = Point3, v = Vector3) # type: ignore
    def translate(p, v) -> Point3: #type: ignore
        return Point3(p.x + v.x, p.y + v.y, p.z + v.z)
    
@cython.cclass
class Vector3():
    """
    Representa um vetor em um espaço tridimensional.

    Atributos:
        x (float): Componente do vetor na direção X.
        y (float): Componente do vetor na direção Y.
        z (float): Componente do vetor na direção Z.
    """
    x = cython.declare(cython.double, visibility='public')
    y = cython.declare(cython.double, visibility='public')
    z = cython.declare(cython.double, visibility='public')
    
    @cython.locals(x=cython.double, y=cython.double, z=cython.double)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z     

    def __str__(p):
        return f"({p.x}, {p.y}, {p.z})"
        
    @cython.locals(p2 = Vector3) # type: ignore
    def __add__(p1, p2):
        return Vector3(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)

    @cython.locals(p2 = Vector3) # type: ignore
    def __sub__(p1, p2):
        return Vector3(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)

    @cython.locals(p2 = Vector3) # type: ignore
    def __mul__(p1, p2):
        return (p1.x * p2.x) + (p1.y * p2.y) + (p1.z * p2.z)