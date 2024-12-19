from primitives import *


class Intersectable:
    """
    Classe abstrata para superficies que podem ter interseções com raios da câmera
    """
    def __init__(self):
        raise Exception("Você não pode instanciar essa classe")
    
    def intersects():
        pass

class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r: float = r
        self.g: float = g
        self.b: float = b

Color.BLACK = Color(0, 0, 0)
Color.WHITE = Color(1, 1, 1)
Color.RED = Color(1, 0, 0)
Color.GREEN = Color(0, 1, 0)
Color.BLUE = Color(0, 0, 1)
Color.YELLOW = Color(1, 1, 0)

class Plane(Intersectable):
    """
    Plano tridimensional

    Atributos
        - color (Color): color
        - normal (Point3): vetor normal ao plano
        - position (Point3): point arbitrario que pertence ao plano
    """

    def __init__(self, point: Point3, normal: Vector3, color: tuple):
        if normal.magnitude() == 0:
            raise ValueError("O vetor normal ao plano não pode ser nulo.")
        self.point = point
        self.normal = normal.normalize()
        self.color = color

    def intersects(self, origin, direction):
        """
        Calcula a interseção do radius com o plano.
        origem: Ponto de origem do radius
        direcao: Vetor direção do radius (normalizado)
        Retorna a distância positiva ou None se não houver interseção.
        """
        denominator = self.normal.dot(direction)

        if abs(denominator) < 1e-6:
            return None

        t = (self.point - origin).dot(self.normal) / denominator
        return t if t >= 0 else None

class Sphere(Intersectable):
    """
    Esfera

    Atributos
        - color (Color): color
        - position (Point3): centro_tela da esfera
        - radius (float): radius da esfera
    """
    def __init__(self, centro_tela: Point3, radius: float, color: tuple):
        if radius <= 0:
            raise ValueError("O radius deve ser positivo e maior que zero.")
        self.centro_tela = centro_tela
        self.radius = radius
        self.color = color

    def intersects(self, origin: Point3, direction: Vector3):
        """
        Calcula a interseção do radius com a esfera.
        origin: Ponto de origem do radius
        direction: Vetor direção do radius (normalizado)
        Retorna a menor distância positiva ou None se não houver interseção.
        """
        L = self.centro_tela - origin
        tca = L.dot(direction)
        d2 = L.dot(L) - tca * tca
        r2 = self.radius * self.radius

        if d2 > r2:
            return None
        
        thc = (r2 - d2) ** (1/2)
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0 and t1 < 0:
            return None

        return t0 if t0 > 0 else t1