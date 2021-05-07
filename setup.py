#https://www.tutorialsteacher.com/python/python-package
from setuptools import setup
setup(
name='clima-anom',
version='0.5.1',
description='Obtain the climatology and anomalies only for monthly data.',
url='https://github.com/mhacarthur/clima_anom',
author='Cesar Arturo Sanchez Pena',
author_email='arturo66cta@gmail.com',
license='MIT',
packages=['clima_anom'],
keywords=['climatology','anomalies','monthly','correlation','netcdf','closest','MAE','RMSE','BIAS','DiasDoAno','Createnetcdf','remove continent','remove ocean','shapefile remove'],
zip_safe=False)
