from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["cython_classes/primitives.py", "cython_classes/camera.py"], annotate = True)
)