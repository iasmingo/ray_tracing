from __future__ import annotations


class Point3:
    """
    Ponto tridimensional

    Atributos:
        x (float): coordenada X do ponto
        y (float): coordenada Y do ponto
        z (float): coordenada Z do ponto
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
        raise TypeError("Adição requer um Vector3")

    def __sub__(self, other):
        if isinstance(other, Point3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Subtração requer um Point3 ou Vector3")

    def dist(self, other):
        if isinstance(other, Point3):
            dx = self.x - other.x
            dy = self.y - other.y
            dz = self.z - other.z
            return (dx**2 + dy**2 + dz**2)**(1/2)
        else:
            raise TypeError("Cálculo da distância requer um Point3")
    
class Vector3:
    """
    Vetor tridimensional

    Atributos:
        - x (float): componente X do vetor
        - y (float): componente Y do vetor
        - z (float): componente Z do vetor
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z     

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z) 
        elif isinstance(other, Point3):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Adição requer um Point3 ou Vector3")

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Point3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Subtração requer um Point3 ou Vector3")

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vector3(self.x * escalar, self.y * escalar, self.z * escalar)
        raise TypeError("Multiplicação requer um escalar")

    def __truediv__(self, escalar):
        if isinstance(escalar, (int, float)) and escalar != 0:
            return Vector3(self.x / escalar, self.y / escalar, self.z / escalar)
        raise ValueError("Divisão requer um escalar não nulo")
    
    def dot(self, other):
        if isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError("Produto escalar requer um Vector3")
    
    def cross(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        raise TypeError("Produto vetorial requer um Vector3")
    
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)**(1/2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Não é possível normalizar um vetor nulo")
        return self / mag