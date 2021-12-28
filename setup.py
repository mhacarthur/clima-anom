#https://www.tutorialsteacher.com/python/python-package
from setuptools import setup, find_packages
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / 'README.md').read_text(encoding='utf-8')

requires = [
    'numpy==1.16.6',
    'pandas==0.24.2', 
]

setup(
    name='clima_anom',
    version='0.6.8',
    description='Obtain the climatology and anomalies only for monthly data.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/mhacarthur/clima-anom',
    author='Cesar Arturo Sanchez Pena',
    author_email='arturo66cta@gmail.com',
    license='MIT',
    packages=find_packages(where=HERE),
    python_requires='>=3.5, <=3.9.7',
    install_requires=requires,
    keywords=['climatology','anomalies','monthly','correlation','netcdf','closest','MAE','RMSE','BIAS','DiasDoAno','Createnetcdf','remove continent','remove ocean','shapefile remove'],
    zip_safe=False,
)
