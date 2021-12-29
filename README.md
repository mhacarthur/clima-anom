

<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" /> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mhacarthur/clima_anom?style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/clima-anom?color=red&label=clima-anom&style=for-the-badge"> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/mhacarthur/clima_anom?style=for-the-badge">

Climatology and Anomalies in Python
=================================================

Overview
--------
This code provides experimental and simples tools for differents operations on climate data, mainly obtaining climatologies and anomalies values, in addition to others operations such as data extraction from continent, ocean or a shapefile.

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

Data
----
The data use for examples is in directory data. For complete data see:

[TRMM 3B42-v7 daily](https://disc.gsfc.nasa.gov/datasets/TRMM_3B42_Daily_7/summary)


Figures
----
Montlhy climatology for rainfall
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Monthly_Climatology.png" alt="Monthly_Climatology" />
</div>

Sesonal climatology for rainfall
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Monthly_Seasonal.png" alt="Seasonal Climatology" />
</div>

Remove a specific ocean or continent for rainfall
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Wind_remove_continent_ocean.png" alt="Wind remove mask" />
</div>

Extract information with a shapefile
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Extract_shapefile.png" alt="Shapefile" />
</div>
