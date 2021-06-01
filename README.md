

clima-anom - Climatology and Anomalies in Python
=================================================

<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" /> <img alt="PyPI" src="https://img.shields.io/pypi/v/numpy?color=green&label=numpy&style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/netCDF4?color=green&label=netCDF4&style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/matplotlib?color=green&label=matplotlib&style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/cartopy?color=green&label=cartopy&style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/pyshp?color=green&label=pyshp&style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/clima-anom?color=red&label=clima-anom&style=for-the-badge">

Overview
--------
This code provides tools for the aid of different operations on monthly climate data, mainly obtaining climatologie and anomalies information, in addition to other operations such as data extraction from a shapefile.

Requirements
------------

How to install requirements with pip

    $pip install -r requirements.txt
    
[numpy](https://numpy.org/)

[netCDF4](https://pypi.org/project/netCDF4/)

[matplotlib](https://pypi.org/project/matplotlib/)

[cartopy](https://pypi.org/project/Cartopy/)

[pyshp](https://pypi.org/project/pyshp/)

Manual installation
------------
clima\_anom works on Python 3 for Linux, Windows or OSX.

    $git clone https://github.com/mhacarthur/clima_anom.git

first clone the package then inside

    $cd clima_anom

and install

    $pip install .

Pip install
------------
    $pip install clima-anom

Install a specific version, for example 0.5.2

    $pip install clima-anom==0.5.2

Content
-------
List of funtions

	read_netcdf
	clima_anom
	season
	correlation
	closest_point
	extract_area
	MAE
	RMSE
	DiasDoAno
	create_netcdf
	remove_continent_ocean
	extract_shapefile

Help
----
For obtain a list of funtions:

	import clima_anom as ca
	ca.help_funtion()

Help for specific funtion:

	ca.help_funtion('read_netcdf')
	
Data
----
The data use for examples correspond to NCEP/NCAR Reanalysis 1

[Reanalysis Data](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.pressure.html)


Figures
----
Montlhy climatology for hgt 500 hPa
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/fig/Monthly_Climatology.png" alt="Monthly_Climatology" />
</div>

Sesonal climatology for hgt 500 hPa
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/fig/Monthly_Seasonal.png" alt="Seasonal Climatology" />
</div>

Remove a specific ocean or continent for uwnd 500 hPa
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/fig/Wind_remove_continent_ocean.png" alt="Wind remove mask" />
</div>

Extract information with a shapefile
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/fig/Extract_shapefile.png" alt="Shapefile" />
</div>


