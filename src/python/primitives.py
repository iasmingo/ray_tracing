from __future__ import annotations
import math


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

    @staticmethod
    def dist(p1, p2):
        assert isinstance(p1, Point3)
        assert isinstance(p2, Point3)
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        dz = p1.z - p2.z
        return (dx**2 + dy**2 + dz**2)**(1/2)

    def __str__(p):
        return f"({p.x}, {p.y}, {p.z})"

    def to(self, p: Vector3) -> Vector3:
        """
        Retorna o vetor até o ponto p.

        Argumentos:
            - p (Point3) : ponto de destino
        """
        assert isinstance(p, Point3)
        return Vector3(p.x - self.x, p.y - self.y, p.z - self.z)

    def translate(p, v: Vector3) -> Point3:
        """
        Retorna o ponto mais o vetor v

        Argumentos:
            - v (Vector3) Vetor de translação
        """
        assert isinstance(v, Vector3)
        return Point3(p.x + v.x, p.y + v.y, p.z + v.z)
    
class Vector3():
    """
    Representa um vetor em um espaço tridimensional.

    Atributos:
        x (float): Componente do vetor na direção X.
        y (float): Componente do vetor na direção Y.
        z (float): Componente do vetor na direção Z.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z     

    def __str__(p):
        return f"({p.x}, {p.y}, {p.z})"
    
    def __add__(p1, p2):
        return Vector3(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)

    def __sub__(p1, p2):
        return Vector3(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)
    
    def __mul__(p1, p2):
        return (p1.x * p2.x) + (p1.y * p2.y) + (p1.z * p2.z)
    
    def scale(v, k: float) -> Vector3:
        """
        Retorna o produto do vetor pelo escalar k.

        Argumentos:
            - k (float) escalar
        """
        return Vector3(k*v.x, k*v.y, k*v.z)
    
    def prod_vetorial(v1, v2):
        return Vector3(
            (v1.y * v2.z) - (v1.z * v2.y),
            (v1.z * v2.x) - (v1.x * v2.z),
            (v1.x * v2.y) - (v1.y * v2.x)
        )
    
    def norma(v):
        return math.sqrt((v.x * v.x) + (v.y * v.y) + (v.z * v.z))