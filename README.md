

clima-anom - Climatology and Anomalies in Python
=================================================

<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" /> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mhacarthur/clima_anom?style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/clima-anom?color=red&label=clima-anom&style=for-the-badge"> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/mhacarthur/clima_anom?style=for-the-badge">

Overview
--------
This code provides tools for the aid of different operations on monthly climate data, mainly obtaining climatologie and anomalies information, in addition to other operations such as data extraction from a shapefile.

Requirements
------------

How to install requirements with pip

    $pip install -r requirements.txt

Pip install
------------
    $pip install clima-anom

Manual installation
------------
clima\_anom works on Python 3 for Linux, Windows or OSX.

    $git clone https://github.com/mhacarthur/clima_anom.git

first clone the package then inside

    $cd clima_anom

and install

    $pip install .
    
Content
-------
List of funtions

	help_funtion
	read_netcdf
	clima_anom
	climatology
	anomalies
	season
	correlation
	closest_point
	MAE
	RMSE
	BIAS
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



