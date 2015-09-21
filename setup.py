from setuptools import setup
from setuptools import Extension

setup(
    name = 'cHaversine',
    packages = ['cHaversine'],
    version = '0.2.3',
    description = 'Fast haversine calculation',
    author = 'Eric Jiang',
    author_email = 'eric@doublemap.com',
    url = 'https://github.com/doublemap/cHaversine',
    keywords = ['math', 'geo', 'cython'],
    classifiers = ['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'],
    ext_modules = [Extension("cHaversine", ["cHaversine/cHaversine.c"])]
)
