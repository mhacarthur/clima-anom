
clima\_anom - Climatology and Anomalies in Python
=================================================

Overview
--------

Requirements
------------
[numpy](https://numpy.org/)

[netCDF4](https://pypi.org/project/netCDF4/)

[matplotlib](https://pypi.org/project/matplotlib/)

[cartopy](https://pypi.org/project/Cartopy/)

Obtain a repository
------------------

Clone 

    $git clone https://github.com/mhacarthur/clima_anom.git

Installation
------------

clima\_anom works on Python 3 on Linux, Windows or OSX.
first clone the package then

    $cd clima_anom

and intall

    $pip install .
    
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

Help
----
For obtain a list of funtion into python use:

	import clima_anom as ca
	ca.help_funtion()

For obtain a help for specific funtion:

	ca.help_funtion('read_netcdf')

