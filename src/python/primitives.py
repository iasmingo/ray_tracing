from __future__ import annotations

class Point3:
    """
    Representa um ponto em um espaço tridimensional.

    Atributos:
        x (float): Coordenada X do ponto.
        y (float): Coordenada Y do ponto.
        z (float): Coordenada Z do ponto.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dist(self, other) -> float:
        """
        Retorna a distância para outro ponto.

        Argumentos:
            - other (Point3) : outro ponto
        """
        assert isinstance(other, Point3), "other precisa ser Point3"
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return (dx**2 + dy**2 + dz**2)**(1/2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def to(self, p: Point3) -> Vector3:
        """
        Retorna o vetor até o ponto p.

        Argumentos:
            - p (Point3) : ponto de destino
        """
        assert isinstance(p, Point3), "p precisa ser Point3, mas é "+type(p)
        return Vector3(p.x - self.x, p.y - self.y, p.z - self.z)

    def translate(self, v: Vector3) -> Point3:
        """
        Retorna o ponto mais o vetor v

        Argumentos:
            - v (Vector3) Vetor de translação
        """
        assert isinstance(v, Vector3), "v precisa ser Vector3, mas é "+type(v)
        return Point3(self.x + v.x, self.y + v.y, self.z + v.z)
    
class Vector3:
    """
    Representa um vetor em um espaço tridimensional.

    Atributos:
        - x (float): Componente do vetor na direção X.
        - y (float): Componente do vetor na direção Y.
        - z (float): Componente do vetor na direção Z.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z     

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other) -> float:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    def scale(self, k: float) -> Vector3:
        """
        Retorna o produto do vetor pelo escalar k.

        Argumentos:
            - k (float) escalar
        """
        return Vector3(k*self.x, k*self.y, k*self.z)
    
    def cross(self, other: Vector3) -> Vector3:
        """
        Retorna o produto velorial deste vetor por outro

        Argumentos:
            - other (Vector3): outro vetor
        """
        return Vector3(
            (self.y * other.z) - (self.z * other.y),
            (self.z * other.x) - (self.x * other.z),
            (self.x * other.y) - (self.y * other.x)
        )
    
    def norm(self) -> float:
        """
        Retorna a norma do vetor
        """
        return (self * self)**(1/2)