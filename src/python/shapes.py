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
        - point: ponto arbitrário pertencente ao plano
        - normal: vetor normal ao plano
        - color: cor do plano
    """
    def __init__(self, point: Point3, normal: Vector3, color: tuple):
        if normal.magnitude() == 0:
            raise ValueError("O vetor normal ao plano não pode ser nulo.")
        self.point = point
        self.normal = normal.normalize()
        self.color = color

    def intersects(self, origin: Point3, direction: Vector3):
        """
        Calcula a interseção do raio com o plano.
        origin: ponto de origem do raio
        direction: vetor direção do raio (normalizado)
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
        - center: centro da esfera
        - radius: raio da esfera
        - color: cor
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
        origin: ponto de origem do raio
        direction: vetor direção do raio (normalizado)
        Retorna a menor distância positiva ou None se não houver interseção.
        """
        # Vetor distância da origem para o centro da esfera
        distance = self.center - origin

        # Projeção da distância sobre o raio
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

class TriangleMesh(Intersectable):
    """
    Malha triangular

    Atributos:
    - n_t: número de triângulos
    - n_v: número de vértices
    - v_list: lista com todos os vértices
    - t_list: lista com todos os triângulos
    - normals_t_list: lista com todas as normais de todos os triângulos
    - normals_v_list: lista com todas as normais de todos os vértices
    - color: cor
    """
    def __init__(self, n_t: int, n_v: int, v_list, t_list, normals_t_list, normals_v_list, color: tuple):
        self.n_t = n_t
        self.n_v = n_v
        self.v_list = v_list
        self.t_list = t_list
        self.t_list_planes = []
        for i in range(0, len(t_list)):
            plane = Plane(v_list[t_list[i][0]], normals_t_list[i], color)
            self.t_list_planes.append(plane)
        self.normals_t_list = normals_t_list
        self.normals_v_list = normals_v_list
        self.color = color

    def intersects(self, origin: Point3, direction: Vector3):
        found = False
        mindist = float('inf')

        # Verifica se o raio intercepta o plano de cada triângulo da malha
        for i in range(0, len(self.t_list_planes)):
            dist = self.t_list_planes[i].intersects(origin, direction)
            if(dist == None):
                continue
            else:
                ## Checa se o ponto de impacto está dentro do triângulo

                # Encontra o ponto de impacto usando a equação paramétrica da reta
                x = (direction.x * dist) + origin.x
                y = (direction.y * dist) + origin.y
                z = (direction.z * dist) + origin.z
                p = Point3(x, y, z)

                # Vetores das arestas do triângulo
                ba = self.v_list[self.t_list[i][1]] - self.v_list[self.t_list[i][0]]
                ca = self.v_list[self.t_list[i][2]] - self.v_list[self.t_list[i][0]] 
                bc = self.v_list[self.t_list[i][2]] - self.v_list[self.t_list[i][1]]

                # Semiperímetro e área do triângulo
                s = (ba.magnitude() + ca.magnitude() + bc.magnitude())/2
                area_t = (s * (s - ba.magnitude()) * (s - ca.magnitude()) * (s - bc.magnitude())) ** 0.5
                
                # Vetores do ponto de interseção para os vértices do triângulo 
                bp = self.v_list[self.t_list[i][1]] - p
                cp = self.v_list[self.t_list[i][2]] - p
                ap = self.v_list[self.t_list[i][0]] - p

                # Semiperímetros dos triângulos menores formados por p e o vértice do triângulo original
                s1 = (bp.magnitude() + cp.magnitude() + bc.magnitude())/2
                s2 = (bp.magnitude() + ap.magnitude() + ba.magnitude())/2
                s3 = (ap.magnitude() + cp.magnitude() + ca.magnitude())/2
                
                # Áreas dos triângulos menores formados
                area1 = (s1 * (s1 - bp.magnitude()) * (s1 - cp.magnitude()) * (s1 - bc.magnitude())) ** 0.5
                area2 = (s2 * (s2 - bp.magnitude()) * (s2 - ap.magnitude()) * (s2 - ba.magnitude())) ** 0.5
                area3 = (s3 * (s3 - ap.magnitude()) * (s3 - cp.magnitude()) * (s3 - ca.magnitude())) ** 0.5

                if(abs((area1 + area2 + area3) - area_t) < 0.000001):
                    mindist = min(dist, mindist)
                    found = True
        
        if(found):
            return mindist
        else:
            return None