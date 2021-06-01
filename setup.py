#https://www.tutorialsteacher.com/python/python-package
from setuptools import setup
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / 'README.md').read_text(encoding='utf-8')

setup(
name='clima-anom',
version='0.5.3',
description='Obtain the climatology and anomalies only for monthly data.',
long_description=LONG_DESCRIPTION,
long_description_content_type='text/markdown',
url='https://github.com/mhacarthur/clima_anom',
author='Cesar Arturo Sanchez Pena',
author_email='arturo66cta@gmail.com',
license='MIT',
packages=['clima_anom'],
keywords=['climatology','anomalies','monthly','correlation','netcdf','closest','MAE','RMSE','BIAS','DiasDoAno','Createnetcdf','remove continent','remove ocean','shapefile remove'],
zip_safe=False)
