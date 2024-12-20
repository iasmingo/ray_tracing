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
        Calcula a interseção do raio com o plano.
        origem: Ponto de origem do raio
        direcao: Vetor direção do raio (normalizado)
        Retorna a distância positiva ou None se não houver interseção.
        """
        denominator = self.normal.dot(direction) # o denominador é o seno do angulo do raio com o plano

        if abs(denominator) < 1e-6: # reta paralela ao plano
            return None
        
        # hipotenusa (distancia da interseção) = cateto oposto / seno
        t = (self.point - origin).dot(self.normal) / denominator

        return t if t >= 0 else None # hipotenusa 'negativa' implica que o raio esta se afastando do plano

class Sphere(Intersectable):
    """
    Esfera

    Atributos
        - color (Color): color
        - position (Point3): centro_tela da esfera
        - radius (float): radius da esfera
    """
    def __init__(self, centro_esfera: Point3, radius: float, color: tuple):
        if radius <= 0:
            raise ValueError("O radius deve ser positivo e maior que zero.")
        self.centro_esfera = centro_esfera
        self.radius = radius
        self.color = color

    def intersects(self, origin: Point3, direction: Vector3):
        """
        Calcula a interseção do raio com a esfera.
        origin: Ponto de origem do raio
        direction: Vetor direção do raio (normalizado)
        Retorna a menor distância positiva ou None se não houver interseção.
        """
        distance = self.centro_esfera - origin # vetor distancia da origem pro centro da esfera
        proj_length = distance.dot(direction) # projeção de distance sob o raio
        square_d = distance.dot(distance) - proj_length**2 # distância do ponto mais próximo ao quadrado
        square_radius = self.radius **2 # raio da esfera ao quadrado

        if proj_length < 0: # caso o sentido é oposto, não há interseção
            return None

        if square_d > square_radius: # se a distancia do ponto mais próximo é maior que o raio, não há interseção
            return None
        
        thc = (square_radius - square_d) ** (1/2)
        inter_1 = proj_length - thc
        inter_2 = proj_length + thc

        return inter_1 if inter_1 > 0 else inter_2