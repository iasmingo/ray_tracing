import cython

@cython.cclass
class Point3:
    """
    Representa um ponto em um espaço tridimensional.

    Atributos:
        x (cython.double): Coordenada X do ponto.
        y (cython.double): Coordenada Y do ponto.
        z (cython.double): Coordenada Z do ponto.
    """
    x = cython.declare(cython.double, visibility='public')
    y = cython.declare(cython.double, visibility='public')
    z = cython.declare(cython.double, visibility='public')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dist(p1, p2: Point3):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        dz = p1.z - p2.z
        return (dx**2 + dy**2 + dz**2) ** (1/2)

    def __str__(p):
        return f"({p.x}, {p.y}, {p.z})"

    def to(self, p: Vector3) -> Vector3:
        """
        Retorna o vetor até o ponto p.

        Argumentos:
            - p (Point3) : ponto de destino
        """
        
        return Vector3(p.x - self.x, p.y - self.y, p.z - self.z)
    
    # @cython.locals(p = Point3, v = Vector3) # type: ignore
    def translate(p, v) -> Point3:
        return Point3(p.x + v.x, p.y + v.y, p.z + v.z)
    
@cython.cclass
class Vector3():
    """
    Representa um vetor em um espaço tridimensional.

    Atributos:
        x (cython.double): Componente do vetor na direção X.
        y (cython.double): Componente do vetor na direção Y.
        z (cython.double): Componente do vetor na direção Z.
    """
    x = cython.declare(cython.double, visibility='public')
    y = cython.declare(cython.double, visibility='public')
    z = cython.declare(cython.double, visibility='public')
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z     

    def __str__(p):
        return f"({p.x}, {p.y}, {p.z})"
        
    def __add__(p1, p2: Vector3) -> Vector3:
        return Vector3(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)

    def __sub__(p1, p2: Vector3) -> Vector3:
        return Vector3(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)

    def __mul__(p1, p2: Vector3) -> Vector3:
        return (p1.x * p2.x) + (p1.y * p2.y) + (p1.z * p2.z)
    
    # @cython.locals(k = cython.double)
    def scale(v, k: cython.double) -> Vector3:
        """
        Retorna o produto do vetor pelo escalar k.

        Argumentos:
            - k (float) escalar
        """
        return Vector3(k*v.x, k*v.y, k*v.z)