from primitives import *

class Camera:
    """
    ### Camera
    Câmera móvel
    
    #### Atributos:
        - position (Point3): posição da câmera
        - target (Point3): posição da tela
        - u (Vector3): Vetor que aponta para cima da câmera
        - v (Vector3): Vetor que aponta para a frente da câmera
        - w (Vector3): Vetor que aponta para a direita da câmera
        - d (cython.double): distacia de position para target
        - height (cython.int): altura da tela em pixels
        - width (cython.int): largura da tela em pixels
    """
    def __init__(self, height: int, width: int, position: Point3, target: Point3 = None):
        self.position = position
        if target is None:
            self.target = position.translate(Vector3(0, 0, 10))
        else:
            self.target = target

        self.v: Vector3 = position.to(self.target)
        self.d: float = self.v.norm()
        self.v = self.v.normalized()
        self.w = -(self.v).cross(Vector3.j)
        self.u = self.v.cross(self.w)
        self.height = height
        self.width = width

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
