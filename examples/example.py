
import clima_anom as ca
import numpy as np

data_dir = '/mnt/Data/Datos/IMERG/IMERG_2000_12_2021_02_05x05_monthly.nc'
data = ca.read_netcdf(data_dir,2)

lat = data['lat'].data
lon = data['lon'].data
pre = data['prec'].data

data_dic = ca.data_dictionary(pre)

clima = ca.climatology(data_dic)

anom = ca.anomalies(data_dic)
print(f'Anom shape: {anom.shape}')

pre_summer = ca.season(data_dic,season=1)

pre_clima = np.array(clima)

print(pre_clima.shape)

print()

tt = np.random.randint(0, 100, size=(30, 10, 2))
print(tt.shape)

test = ca.correlation(tt,tt)
test = ca.RBIAS(tt,tt)

test = ca.remove_continent_ocean(pre_clima,lat,lon,'ocean')