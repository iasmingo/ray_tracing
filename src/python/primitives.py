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

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Permitido somar apenas Point3 a Vector3")

    def __sub__(self, other):
        if isinstance(other, Point3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Permitido subtrair apenas Point3 de Point3 ou Vector3 de Point3")

    def dist(self, other):
        if isinstance(other, Point3):
            dx = self.x - other.x
            dy = self.y - other.y
            dz = self.z - other.z
            return (dx**2 + dy**2 + dz**2)**(1/2)
        else:
            raise TypeError("Argumento deve ser outro Point3")

    def to(self, other):
        if isinstance(other, Point3):
            return Vector3(p.x - self.x, p.y - self.y, p.z - self.z)
        else:
            raise TypeError("Argumento deve ser outro Point3")
    
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

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vector3(self.x * escalar, self.y * escalar, self.z * escalar)
        raise TypeError("Multiplicação apenas com um escalar")

    def __truediv__(self, escalar):
        if isinstance(escalar, (int, float)) and escalar != 0:
            return Vector3(self.x / escalar, self.y / escalar, self.z / escalar)
        raise ValueError("Divisão apenas por um escalar não nulo")
    
    def dot(self, other):
        if isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError("Produto escalar requer outro Vector3")
    
    def cross(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        raise TypeError("Produto vetorial requer outro Vector3")
    
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)**(1/2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Não é possível normalizar um vetor nulo")
        return self / mag