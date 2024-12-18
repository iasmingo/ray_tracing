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
        - color (Color): cor
        - normal (Point3): vetor normal ao plano
        - position (Point3): ponto arbitrario que pertence ao plano
    """

    def __init__(self, position: Point3, normal: Vector3, color: Color = Color.WHITE):
        self.color = color
        self.position = position
        self.normal = normal

    def intersects(self, origin, direction):
        """
        Calcula a interseção do raio com o plano.
        origem: Ponto de origem do raio
        direcao: Vetor direção do raio (normalizado)
        Retorna a distância positiva ou None se não houver interseção.
        """
        denominator = self.normal * direction

        if abs(denominator) < 1e-6:
            return None

        t = (origin.to(self.position) * self.normal) / denominator
        return t if t >= 0 else None

class Sphere(Intersectable):
    """
    Esfera

    Atributos
        - color (Color): cor
        - position (Point3): centro da esfera
        - radius (float): raio da esfera
    """
    def __init__(self, position: Point3, radius: float, color: Color = Color.WHITE):
        self.color: Color = color
        self.position: Point3 = position
        self.radius: float = radius

    def intersects(self, origin: Point3, direction: Vector3):
        """
        Calcula a interseção do raio com a esfera.
        origin: Ponto de origem do raio
        direction: Vetor direção do raio (normalizado)
        Retorna a menor distância positiva ou None se não houver interseção.
        """
        L = origin.to(self.position)
        tca = L * direction
        d2 = (L * L) - tca * tca
        r2 = self.radius * self.radius

        if d2 > r2:
            return None
        
        thc = (r2 - d2) ** (1/2)
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0 and t1 < 0:
            return None

        return t0 if t0 > 0 else t1
