from __future__ import annotations
# import cython
from cython import (
    cclass,
    cfunc,
    double,
    declare
)

@cclass
class Point3:
    """
    Representa um ponto em um espaço tridimensional.

    Atributos:
        x (cython.double): Coordenada X do ponto.
        y (cython.double): Coordenada Y do ponto.
        z (cython.double): Coordenada Z do ponto.
    """
    x: double
    y: double
    z: double

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @cfunc
    def dist(self, p: Point3) -> double:
        """
        Retorna a distancia até o ponto p

        Argumentos:
            - p (Point3) : ponto de destino

        Valor de Retono: (double) A distancia entre os pontos
        """
        dx = self.x - p.x
        dy = self.y - p.y
        dz = self.z - p.z
        return (dx**2 + dy**2 + dz**2) ** (1/2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    @cfunc
    def to(self, p: Point3) -> Vector3:
        """
        Retorna o vetor até o ponto p.

        Argumentos:
            - p (Point3) : ponto de destino
        """
        
        return Vector3(p.x - self.x, p.y - self.y, p.z - self.z)
    
    @cfunc
    def translate(self, v: Vector3) -> Point3:
        """
        Retorna o ponto mais o vetor v

        Argumentos:
            - v (Vector3) Vetor de translação
        """
        assert isinstance(v, Vector3), "v precisa ser Vector3, mas é "+type(v)
        return Point3(self.x + v.x, self.y + v.y, self.z + v.z)
    
@cclass
class Vector3():
    """
    Representa um vetor em um espaço tridimensional.

    Atributos:
        x (cython.double): Componente do vetor na direção X.
        y (cython.double): Componente do vetor na direção Y.
        z (cython.double): Componente do vetor na direção Z.
    """
    x = declare(double, visibility="readonly")
    y = declare(double, visibility="readonly")
    z = declare(double, visibility="readonly")
    i = declare(object, visibility="readonly")
    j = declare(object, visibility="readonly")
    k = declare(object, visibility="readonly")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other) -> double:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    def __div__(self, k: double) -> Vector3:
        return Vector3(self.x/k, self.y/k, self.z/k)
    
    @cfunc
    def scale(self, k: double) -> double:
        """
        Retorna o produto do vetor pelo escalar k.

        Argumentos:
            - k (cython.double) escalar
        """
        return Vector3(k*self.x, k*self.y, k*self.z)

    @cfunc
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

    @cfunc
    def norm(self) -> double:
        """
        Retorna a norma do vetor
        """
        return (self * self)**(1/2)
    
    @cfunc
    def normalized(self) -> double:
        """
        Retorna o vetor normalizado
        """
        return self.scale(1/self.norm())

Vector3.i = Vector3(1, 0, 0)
Vector3.j = Vector3(0, 1, 0)
Vector3.k = Vector3(0, 0, 1)

# UP: cython.const[Vector3] = Vector3(0, 1, 0)
# FW: cython.const[Vector3] = Vector3(0, 0, 1)
# RG: cython.const[Vector3] = Vector3(-1, 0, 0)
# DW: cython.const[Vector3] = Vector3(0, -1, 0)
# BK: cython.const[Vector3] = Vector3(0, 0, -1)
