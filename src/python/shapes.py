from primitives import *


class Intersectable:
    """
    Classe abstrata para superfícies que podem ter interseções com raios da câmera.
    """
    def __init__(self):
        raise Exception("Esta classe não é instanciável")
    
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

    Atributos:
        - point (Point3): ponto arbitrário pertencente ao plano
        - normal (Vector3): vetor normal ao plano
        - color (Color): cor do plano
    """
    def __init__(self, point: Point3, normal: Vector3, color: tuple):
        if normal.magnitude() == 0:
            raise ValueError("O vetor normal ao plano não pode ser nulo.")
        self.point = point
        self.normal = normal.normalize()
        self.color = color

    def intersects(self, origin, direction):
        """
        Calcula a interseção do raio com o plano.
        origin (Point3): ponto de origem do raio
        direction (Vector3): vetor direção do raio (normalizado)
        Retorna a distância positiva ou None se não houver interseção.
        """
        # Seno do ângulo do raio com o plano
        denominator = self.normal.dot(direction)

        # Reta paralela ao plano
        if abs(denominator) < 1e-6:
            return None
        
        # Hipotenusa (distância da interseção) = cateto oposto / seno
        t = (self.point - origin).dot(self.normal) / denominator

        # Hipotenusa "negativa": raio está se afastando do plano
        return t if t >= 0 else None

class Sphere(Intersectable):
    """
    Esfera

    Atributos:
        - center (Point3): centro da esfera
        - radius (float): raio da esfera
        - color (Color): cor
    """
    def __init__(self, center: Point3, radius: float, color: tuple):
        if radius <= 0:
            raise ValueError("O radius deve ser positivo e maior que zero.")
        self.center = center
        self.radius = radius
        self.color = color

    def intersects(self, origin: Point3, direction: Vector3):
        """
        Calcula a interseção do raio com a esfera.
        origin (Point3): ponto de origem do raio
        direction (Vector3): vetor direção do raio (normalizado)
        Retorna a menor distância positiva ou None se não houver interseção.
        """
        # Vetor distância da origem para o centro da esfera
        distance = self.center - origin

        # Projeção de distance sobre o raio
        proj_length = distance.dot(direction)

        # Distância do ponto mais próximo ao quadrado
        square_d = distance.dot(distance) - proj_length**2

        # Raio da esfera ao quadrado
        square_radius = self.radius**2 

        # Caso o sentido seja oposto, não há interseção
        if proj_length < 0:
            return None

        # Caso a distância do ponto mais próximo seja maior que o raio, não há interseção
        if square_d > square_radius:
            return None
        
        thc = (square_radius - square_d) ** (1/2)
        inter_1 = proj_length - thc
        inter_2 = proj_length + thc

        return inter_1 if inter_1 > 0 else inter_2