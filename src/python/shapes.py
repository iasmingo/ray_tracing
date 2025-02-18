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
    
class TriangleMesh(Intersectable):
    def __init__(self, n_triang, n_vert, lista_vert, lista_triang, lista_normais, normais_vert, cor):
        self.n_triang = n_triang
        self.n_vert = n_vert
        self.lista_vert = lista_vert
        self.triangs = lista_triang
        self.lista_triang = []
        for i in range(0, len(lista_triang)):
            plano = Plane(lista_vert[lista_triang[i][0]], lista_normais[i], cor)
            self.lista_triang.append(plano)
        self.lista_normais = lista_normais
        self.normais_vert = normais_vert
        self.color = cor

    def intersects(self, origin: Point3, direction: Vector3):
        found = False
        mindist = float('inf')
        for i in range(0, len(self.lista_triang)):
            dist = self.lista_triang[i].intersects(origin, direction)
            if(dist == None):
                continue
            else:
                # checar se está dentro do plano
                # precisa primeiro achar o ponto
                # pra isso usa a origem e a direção para fazer
                # uma equação paramétrica da reta
                # e colocar t como a distância do ponto origin
                x = (direction.x * dist) + origin.x
                y = (direction.y * dist) + origin.y
                z = (direction.z * dist) + origin.z
                p = Point3(x, y, z)
                # https://www.youtube.com/watch?v=3MJ-k15te_k
                ba = self.lista_vert[self.triangs[i][1]] - self.lista_vert[self.triangs[i][0]]
                ca = self.lista_vert[self.triangs[i][2]] - self.lista_vert[self.triangs[i][0]] 
                bc = self.lista_vert[self.triangs[i][2]] - self.lista_vert[self.triangs[i][1]]
                s = (ba.magnitude() + ca.magnitude() + bc.magnitude())/2
                areatotal = (s * (s - ba.magnitude()) * (s - ca.magnitude()) * (s - bc.magnitude())) ** 0.5
                # https://mundoeducacao.uol.com.br/matematica/formula-heron.htm
                bp = self.lista_vert[self.triangs[i][1]] - p
                cp = self.lista_vert[self.triangs[i][2]] - p
                ap = self.lista_vert[self.triangs[i][0]] - p


                s1 = (bp.magnitude() + cp.magnitude() + bc.magnitude())/2
                area1 = (s1 * (s1 - bp.magnitude()) * (s1 - cp.magnitude()) * (s1 - bc.magnitude())) ** 0.5
                
                s2 = (bp.magnitude() + ap.magnitude() + ba.magnitude())/2
                area2 = (s2 * (s2 - bp.magnitude()) * (s2 - ap.magnitude()) * (s2 - ba.magnitude())) ** 0.5
                
                s3 = (ap.magnitude() + cp.magnitude() + ca.magnitude())/2
                area3 = (s3 * (s3 - ap.magnitude()) * (s3 - cp.magnitude()) * (s3 - ca.magnitude())) ** 0.5

                if(abs((area1 + area2 + area3) - areatotal) < 0.000001):
                    mindist = min(dist, mindist)
                    found = True
        
        if(found):
            return mindist
        else:
            return None
