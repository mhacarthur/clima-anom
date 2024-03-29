

<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" /> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mhacarthur/clima_anom?style=for-the-badge"> <img alt="PyPI" src="https://img.shields.io/pypi/v/clima-anom?color=red&label=clima-anom&style=for-the-badge"> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mhacarthur/clima_anom?style=for-the-badge"> <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/mhacarthur/clima_anom?style=for-the-badge">

Climatology and Anomalies in Python
=================================================

Overview
---
This code provides experimental and simples tools for differents operations on climate data, mainly obtaining climatologies and anomalies values, in addition to others operations such as data extraction from continent, ocean or a shapefile.

Pip install
---
```bash
pip install clima_anom
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
- cartopy >= 0.18.0
- netcdf4 >= 1.5.7
- pyshp >= 2.1.3
- OS: Linux

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

### Read  data
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

### Colorbar with middle white
```python
import clima_anom as ca
import matplotlib.pyplot as plt

cmap = plt.cm.Spectral_r
cmap_midle_white = ca.colorbar_middle_white(cmap,'middle')
```
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Colorbar_1.png" alt="colorbar1" />
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Colorbar_2.png" alt="colorbar2" />
</div>

### Remove ocean or continent
```python
import numpy as np
import clima_anom as ca

data_dir = '..'+os.sep+'data'+os.sep+'3B42_199901_201212_climatology.nc'
data = ca.read_netcdf(data_dir,2)
lat = data['lat']
lon = data['lon']
pre = data['pre']

pre_continent = ca.remove_continent_ocean(pre,lat,lon,'continent')
pre_ocen = ca.remove_continent_ocean(pre,lat,lon,'ocean')
```
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Wind_remove_continent_ocean.png" alt="Wind remove mask" />
</div>

### Extract data using shapefile
```python
import clima_anom as ca
import cartopy.io.shapereader as shpreader

file_shape = '..'+os.sep+'shapefile'+os.sep+''+os.sep+'Amazonas.shp'
amazonas = list(shpreader.Reader(file_shape).geometries())

data_dir = '..'+os.sep+'data'+os.sep+'3B42_199901_201212_climatology.nc'
data = ca.read_netcdf(data_dir,2)
lat = data['lat']
lon = data['lon']
pre = data['pre']

pre_amazonas = ca.extract_shapefile('..'+os.sep+'shapefile'+os.sep+'Amazonas.shp',pre,lat,lon,0)

```
<div align="center">
  <img src="https://raw.githubusercontent.com/mhacarthur/clima_anom/master/figures/Extract_shapefile.png" alt="Shapefile" />
</div>
