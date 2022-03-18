

<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" /> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mhacarthur/clima_anom?style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/clima-anom?color=red&label=clima-anom&style=for-the-badge"> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/mhacarthur/clima_anom?style=for-the-badge">

Climatology and Anomalies in Python
=================================================

Overview
---
This code provides experimental and simples tools for differents operations on climate data, mainly obtaining climatologies and anomalies values, in addition to others operations such as data extraction from continent, ocean or a shapefile.

Pip install
---
```bash
pip install clima-anom
```

Manual installation
---
clone clima\_anom and install in exists or new conda env. 

1. Clone repo and install

  ```bash
  git clone https://github.com/mhacarthur/clima_anom.git
  cd clima_anom
  pip install .
  ```

Dependencies
----
- Python >= 3.5 
- cartopy == 0.18.0
- netcdf4 == 1.5.7
- pyshp == 2.1.3
- Option: Linux

1. How to install dependencies

  ```bash
  # cartopy
  conda install -c conda-forge cartopy
  # netcdf4
  conda install netcdf4
  # pyshp
  pip install pyshp
  ```

Data
----
The data use for examples is in directory data. For complete data see:

[TRMM Precipitation L3 daily 0.25x0.25 V7](https://disc.gsfc.nasa.gov/datasets/TRMM_3B42_Daily_7/summary)

Example
---
```python
import os
import clima_anom as ca

data_dir = '..'+os.sep+'data'+os.sep+'3B42_199901_201212.nc'
data = ca.read_netcdf(data_dir,2)

lat = data['lat']
lon = data['lon']
pre = data['prec']

pre_dictionary = ca.data_dictionary(pre)
```

Figures
----
Montlhy climatology for rainfall
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Monthly_Climatology.png" alt="Monthly_Climatology" />
</div>

Colorbar example
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Colorbar_1.png" alt="colorbar1" />
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Colorbar_2.png" alt="colorbar2" />
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
