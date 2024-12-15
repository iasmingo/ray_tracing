from obj_reader import ObjReader
from cython_classes.primitives import *

# Divirtam-se :)

def main():
    obj = ObjReader('../inputs/icosahedron.obj')
    obj.print_faces()
    a = Point3(2, 1, 0)
    b = Point3(-1, 0, 1)
    v = a.to(b)
    u = a.to(v)
    dist = a.dist(b)

if __name__ == "__main__":
    main()
