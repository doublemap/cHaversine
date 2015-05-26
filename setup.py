from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'cHaversine',
    packages = ['cHaversine'],
    version = '0.0.1',
    description = 'Fast haversine calculation',
    author = 'Eric Jiang',
    author_email = 'eric@doublemap.com',
    url = 'https://github.com/doublemap/cHaversine',
    keywords = ['math', 'geo', 'cython'],
    ext_modules = cythonize("cHaversine.pyx")
)
