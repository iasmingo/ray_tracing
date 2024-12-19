from primitives import *
from shapes import Color, Intersectable

class Camera:
    def __init__(self, 
                 posicao: Point3, 
                 mira: Point3, 
                 vetor_up: Vector3, 
                 distancia_tela: float, 
                 altura_resolucao: int, 
                 largura_resolucao: int):
        if vetor_up.magnitude() == 0:
            raise ValueError("O vetor para cima (vetor_up) não pode ser nulo.")

        self.posicao = posicao
        self.mira = mira
        self.vetor_up = vetor_up.normalize()
        self.distancia_tela = distancia_tela
        self.altura_resolucao = altura_resolucao
        self.largura_resolucao = largura_resolucao

        # Vetores ortonormais
        self.w = (self.posicao - self.mira).normalize()
        self.u = self.vetor_up.cross(self.w).normalize()
        self.v = self.w.cross(self.u).normalize()

        # Dimensões dos pixels
        self.tamanho_pixel_h = 1 / largura_resolucao
        self.tamanho_pixel_v = 1 / altura_resolucao

    def __str__(self):
        return (
            "Camera:\n"
            f"  Position: {self.position}\n"
            f"  Target: {self.target}"
        )

    def translate(self, v: Vector3) -> None:
        """
        Executa uma tranformação de translação sobre a camera
        """
        self.position = self.position.translate(v)
        self.target = self.target.translate(v)

    def calculate_point_screen(self, i, j):
        """
        Calcula a posição do centro do pixel (i, j) na tela.
        i: linha do pixel (0 é o pixel mais alto)
        j: coluna do pixel (0 é o pixel mais à esquerda)
        Retorna um ponto 3D na tela no espaço do mundo.
        """
        if not (0 <= i < self.altura_resolucao and 0 <= j < self.largura_resolucao):
            raise ValueError("Índices do pixel fora do intervalo da resolução da tela.")

        # Centro da tela no espaço do mundo
        centro_tela = self.posicao - self.w * self.distancia_tela

        # Vetor para o pixel na direção horizontal e vertical
        delta_h = self.u * (j - (self.largura_resolucao - 1) / 2) * self.tamanho_pixel_h
        delta_v = self.v * ((self.altura_resolucao - 1) / 2 - i) * self.tamanho_pixel_v

        return centro_tela + delta_h + delta_v


    def draw(self, objects):
        width = self.largura_resolucao
        height = self.altura_resolucao

        image = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                pixel_pos = self.calculate_point_screen(i, j)
                direction = (pixel_pos - self.posicao).normalize()

                pixel_color: Color = Color.BLACK
                min_dist = float('inf')

                for obj in objects:
                    distance = obj.intersects(self.posicao, direction)

                    if distance is not None and distance < min_dist:
                        min_dist = distance
                        pixel_color = obj.color

                image[i][j] = (pixel_color.r, pixel_color.g, pixel_color.b)

        return image