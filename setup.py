from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'cHaversine',
    packages = ['cHaversine'],
    version = '0.1.0',
    description = 'Fast haversine calculation',
    author = 'Eric Jiang',
    author_email = 'eric@doublemap.com',
    url = 'https://github.com/doublemap/cHaversine',
    keywords = ['math', 'geo', 'cython'],
    classifiers = ['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'],
    ext_modules = cythonize("cHaversine.pyx")
)
