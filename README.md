

clima\_anom - Climatology and Anomalies in Python
=================================================
<img src="https://img.shields.io/badge/Version-0.5.0-green" /> <img src="https://img.shields.io/badge/License-MIT-blue" /> <img src="https://img.shields.io/badge/Followers-3.5M-red" /> <img src="https://img.shields.io/badge/Stars-5-orange" /> 


Overview
--------

Requirements
------------
[numpy](https://numpy.org/)

[netCDF4](https://pypi.org/project/netCDF4/)

[matplotlib](https://pypi.org/project/matplotlib/)

[cartopy](https://pypi.org/project/Cartopy/)

[shapefile](https://pypi.org/project/pyshp/)

Obtain a repository
------------------

Clone 

    $git clone https://github.com/mhacarthur/clima_anom.git

Installation
------------

clima\_anom works on Python 3 on Linux, Windows or OSX.
first clone the package then

    $cd clima_anom

and install

    $pip install .

Requirements
------------

How to install requirements with pip

    $pip install -r requirements.txt
    
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
	
Data use in examples
----
[hgt and uwnd 500 hPa Data](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.pressure.html)


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

Remove a specific mask for uwnd 500 hPa
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/fig/Wind_remove_continent_ocean.png" alt="Wind remove mask" />
</div>

Extract information with a shapefile
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/fig/Extract_shapefile.png" alt="Shapefile" />
</div>

