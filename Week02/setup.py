#setup.py

#Run as
#    python setup.py build 编译
#    python setup.py install 安装
from setuptolls import setup
from Cython.Build import cythonize
from distutils.core import setup, Extension
import numpy


setup(
    name='target_encoding',
    ext_module=cythonize('target_encoding'),
    