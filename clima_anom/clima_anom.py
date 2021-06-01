import netCDF4
from netCDF4 import Dataset
import numpy as np
import calendar 
from math import cos, asin, sqrt
import time as time_b
import datetime
from datetime import timedelta
from dateutil.rrule import rrule, YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY
from netCDF4 import date2num
import matplotlib.pyplot as plt
import shapefile
from shapely.geometry import shape, Point

import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom
from shapely.ops import unary_union
from shapely.prepared import prep

def print_bold(msg):
    print("\033[1m"+msg+"\033[0m")

def help_funtion(funtion_name='blank'):

    funtion_name = str(funtion_name)
    
    if funtion_name == 'blank':
        print('')
        print('Todo el codigo usa la notacion Data(time,latitude,longitude)')
        print('')
        print_bold('Funciones Disponibles:')
        print('')
        print('read_netcdf')
        print('clima_anom')
        print('climatology')
        print('anomalies')
        print('season')
        print('correlation')
        print('closest_point')
        print('extract_area')
        print('MAE')
        print('RMSE')
        print('DiasDoAno')
        print('create_netcdf')
        print('remove_continent_ocean')
        print('')
        print('Ejemplo: help_funtion(\'season\')')
        
    elif funtion_name == 'read_netcdf':
        print('')
        print_bold('read_netcdf')
        print('')
        print('clima_anom.read_netcdf(filename_path,show=1)')
        print('')
        print('Cargar un archivo netcdf, ingresando la ubicacion, crea un diccionario de las variables dentro del netcdf.')
        print('show=1 es para mostrar las variables dentro del netcdf')
        print('')
        print('      filename = \'../data/vwn1000_jan50_dec19.nc\'')
        print('')
        print('      data = clima_anom.read_netcdf(filename)')
        print('')
        print('Generando la salida:')
        print('')
        print('      Number of variables:  4')
        print('')
        print('      lat : (73,)')
        print('      lon : (144,)')
        print('      time : (480,)')   
        print('      vwnd : (840, 73, 144)')
        print('')
        print('      Dictionary created')
        print('')
        print('Por ejemplo para obtener los valores de las varibles hgt, time, lat y lon dentro del diccionario data:')
        print('')        
        print('     data[\'lat\']')
        print('     data[\'lon\']')
        print('     data[\'time\']')
        print('     data[\'vwnd\']')
        print('')
        
    elif funtion_name == 'clima_anom':
        print('')
        print_bold('clima_anom')
        print('')
        print('clima_anom.clima_anom(data)')
        print('')
        print('Funcion para obtener la climatologia y anomalia mensual, la variable de entrada debe poseer 3 dimensiones:')
        print('(time,latitude,longitude)')
        print('')
        print('Usando la variable vwnd obtenida de read_netcdf:')
        print('')
        print('Dimension de la variable vwnd:')
        print('')
        print('      np.shape(data[\'vwnd\'])')
        print('      (480, 73, 144)')
        print('')
        print('      vwnd_dic = clima_anom.clima_anom(data[\'vwnd\'])')
        print('')
        print('Generando la salida:')
        print('')
        print('      Keys level 1:  dict_keys([\'jan\', \'feb\', \'mar\', \'apr\', \'may\', \'jun\', \'jul\', \'ago\', \'sep\', \'oct\', \'nov\', \'dec\'])')
        print('      keys level 2:  dict_keys([\'data\', \'clim\', \'anom\'])')
        print('')
        print('      Numbers of years:  70')
        print('      Numbers of months:  840')
        print('')
        print('Por ejemplo para obtener la data, climatologia y anomalia para el mes de enero:')
        print('')  
        print('     vwnd_dic[\'jan\'][\'data\']')
        print('     vwnd_dic[\'jan\'][\'clim\']')
        print('     vwnd_dic[\'jan\'][\'anom\']')
        print('')
        
    elif funtion_name == 'climatology':
        print('')
        print_bold('climatology')
        print('')
        print('clima_anom.climatology(data_dictionary)')
        print('')
        print('Function to obtain a numpy matrix only of the climatology of each month for all period')
        print('')
        print('The input data must be the dictionary of clima_anom')
        print('')
        print('For example:')
        print('     vwnd_clima = clima_anom.climatology(vwnd_dic)')
        print('')
        print('     print(hgt_anom.shape)')
        print('     (12, 73, 144)')
        print('')       
        
    elif funtion_name == 'anomalies':
        print('')
        print_bold('anomalies')
        print('')
        print('clima_anom.anomalies(data_dictionary)')
        print('')
        print('Function to obtain a numpy matrix only of the anomalies of each month for all period')
        print('')
        print('The input data must be the dictionary of clima_anom')
        print('')
        print('For example:')
        print('     vwnd_anom = clima_anom.anomalies(vwnd_dic)')
        print('')
        print('     print(hgt_anom.shape)')
        print('     (480, 73, 144)')
        print('')     
        
    elif funtion_name == 'season':
        print('')
        print_bold('season')
        print('')
        print('clima_anom.season(data_dictionary,season_number)')
        print('')
        print('Funcion para obtener las series estacionales; verano, otono, invierno y primavera.')
        print('')
        print('Se debe usar el diccionario creado con clima_anom.')
        print('')
        print('Donde cada estacion esta definida por numero:')
        print('')
        print('1: Summer')
        print('2: Autumn')
        print('3: winter')
        print('4: Spring')
        print('')
        print('Por ejemplo, usando o diccionario de vwnd:')
        print('')
        print('     summer_clima,summer_anom = clima_anom.season(vwn_dic,season=1)')
        print('')
        print('Generando la salida:')
        print('')
        print('     SUMMER Climatology')
        print('')
        print('     Climatology:  (73, 144)')
        print('     Anomaly:  (69, 73, 144)')
        print('')
        
    elif funtion_name == 'correlation':
        print('')
        print_bold('correlation')
        print('')
        print('clima_anom.correlation(data1,data2)')
        print('')
        print('Con esta funcion a partir de dos matricez de dimensiones iguales se obtiene la correlacion lineal de Person.')
        print('')
        print('Por ejemplo podemos cargar dos matrices con la funcion read_netcdf:')
        print('')
        print('      filename_vwn = \'vwn1000_jan50_dec19.nc\'')
        print('      filename_rhu = \'rhum1000_jan50_dec19.nc\'')
        print('')
        print('      data_vwn = clima_anom.read_netcdf(filename_vwn)')
        print('      data_rhu = clima_anom.read_netcdf(filename_rhu)')
        print('')
        print('      print(np.shape(data_vwn[\'vwnd\']))')
        print('      (840, 73, 144)')
        print('')
        print('      print(np.shape(data_rhu[\'rhum\']))')
        print('      (840, 73, 144)')
        print('')
        print('Ahora podemos obtener la correlacion entre los datos de data_vwn y data_rhu')
        print('')
        print('      corr = clima_anom.correlation(data_vwn[\'vwnd\'],data_rhu[\'rhum\'])')
        print('')
        print('Generando la salida:')
        print('')
        print('      Correlation calculated')
        print('      correlation shape:  (73, 144)')
        print('')

    elif funtion_name == 'closest_point':
        print('')
        print_bold('closest_point')
        print('')
        print('clima_anom.closest_point(data_vwn[\'vwnd\'],data_vwn[\'lat\'],data_vwn[\'lon\'],lat_ref,lon_ref)')
        print('')
        print('Funcion para obtener el punto mas proximo a partir de latitud y longitud dentro de una variable y extraer la serie de tiempo.')
        print('')
        print('      filename_vwn = \'vwn1000_jan50_dec19.nc\'')
        print('')
        print('      data_vwn = clima_anom.read_netcdf(filename_vwn)')
        print('')
        print('      result = clima_anom.closest_point(data_vwn[\'vwnd\'],data_vwn[\'lat\'],data_vwn[\'lon\'],-21.5,201.0)')
        print('')
        print('      Data shape     :  (840, 73, 144)')
        print('      Latitude shape :  (73,)')
        print('      Longitude shape:  (144,)')
        print('')
        print('Generando la salida:')
        print('')
        print('      Id, Latitud mas cercana :  [45] -22.5')
        print('      Id, Longitud mas cercana:  [80] 200.0')

    elif funtion_name == 'extract_area':
        print('')
        print_bold('extract_area')
        print('')
        print('clima_anom.extract_area(data,lat,lon,lat_min,lat_max,lon_min,lon_max)')
        print('')
        print('Ingrensando datos de lat minima y maxima junto con lon minima y maxima puede extraerse los datos del area de interes de una variable.')
        print('')
        print('      filename_vwn = \'vwn1000_jan50_dec19.nc\'')
        print('')
        print('      data_vwn = clima_anom.read_netcdf(filename_vwn)')
        print('')
        print('      data_out,lat_out,lon_out = clima_anom.extract_area(data_vwn[\'vwnd\'],data_vwn[\'lat\'],data_vwn[\'lon\'],-30,0,278,325)')
        print('')
        print('Generando la salida:')
        print('')
        print('      Data shape     :  (840, 73, 144)')
        print('      Latitude shape :  (73,)')
        print('      Longitude shape:  (144,)')
        print('')
        print('      Interest Area dimension:  (840, 13, 20)')

    elif funtion_name == 'MAE':
        print('')
        print_bold('MAE')
        print('Use for obtain the Mean absolute error for two vectors')
        print('Both vectors are the same lenght')
        print('      MAE_1_2 = MAE(data1,data2)')

    elif funtion_name == 'RMSE':
        print('')
        print_bold('RMSE')
        print('Use for obtain the Root-mean-square error for two vectors')
        print('Both vectors are the same lenght')
        print('      RMSE_1_2 = RMSE(data1,data2)')
        
    elif funtion_name == 'DiasDoAno':
        print('')
        print_bold('DiasDoAno')
        print('')
        print('DiasDoAno(ano,mes)')
        print('')
        print('Ingresar el año(int) y el mes(string)')
        print('proporciona los dias de inicio y fin del mes')
        print('')
        print('      day_start,day_end = DiasDoAno(2000,\'Jan\')')
        
    elif funtion_name == 'create_netcdf':
        print('')
        print_bold('create_netcdf')
        print('')
        print('First define o dictionary info, for example:')
        print('')
        print('      info = {\'file\': \'../data/Hgt_500hPa_Anomalies_Jan80_Dec83.nc\',')
        print('              \'title\': \'Geopotential Height\',')
        print('              \'year_start\':1980,\'month_start\':1,\'day_start\':1,\'hour_start\':0,\'minute_start\':0,')
        print('              \'year_end\':1983,\'month_end\':12,\'day_end\':1,\'hour_end\':23,\'minute_end\':59,')
        print('              \'time_frequency\': \'Monthly\',')
        print('              \'time_interval\': 1,')  
        print('              \'var_name\': \'hgt\',')
        print('              \'var_units\': \'hPa\'}')
        print('')
        print('      ca.create_netcdf(info,latitude,longitude,Data)')
        print('')
        print('For \'time_frequency\' we can use: \'Monthly\', \'Weekly\', \'Daily\', \'Hourly\', \'Minutely\'')        
        
    elif funtion_name == 'remove_continent_ocean':
        print('')
        print_bold('remove_continent_ocean')
        print('')
        print('Use data of latitude, longitude and variable for extrat ocean or continent:')
        print('')
        print('      vwn_without_ocean = clima_anom.remove_continent_ocean(vwn,lat,lon,\'ocean\')')
        print('')
        print('For continent, we can use: "Continent", "Continent" or "1"')
        print('For ocean, we can use: "Ocean", "ocean" or "2"')

    elif funtion_name == 'extract_shapefile':
        print('')
        print_bold('extract_shapefile')
        print('')
        print('This funtion extract a variable information using a shapefile, but keeping the same spatial dimensions.')
        print('')
        print('      data_dir = \'../data/Hgt_500hPa_Anomalies_Jan80_Dec83.nc\'')
        print('      data = ca.read_netcdf(data_dir,2)')
        print('      lat = data[\'lat\']')
        print('      lon = data[\'lon\']')
        print('      hgt = data[\'var\']')
        print('')
        print('      hgt_shape = clima_anom.extract_shapefile(\'../shp/continent.shp\',hgt,lat,lon)')
        print('')
        
    else:
        print('')
        print_bold('ERROR')
        print('')
        print('Esa funcion no existe, las funciones son:')
        print('read_netcdf')
        print('clima_anom')
        print('climatology')
        print('anomalies')
        print('season')
        print('correlation')
        print('closest_point')
        print('extract_area')
        print('MAE')
        print('RMSE')
        print('BIAS')
        print('create_netcdf')
        print('remove_continent_ocean')
        print('extract_shapefile')
        print('')

def read_netcdf(filename,show=1):
    data = Dataset(filename,mode = 'r')
    
    var_total = data.variables
    
    var_list = {}
    nn = 0
    for key, value in var_total.items():
        var_list[nn] = key
        nn = nn + 1
        
    var_len = len(var_list)
    
    for i in range(var_len):
        globals()[var_list[i]] = data.variables[var_list[i]][:]
    
    dict_out = dict()
    
    for i in range(var_len):
        dict_out[var_list[i]] = globals()[var_list[i]]

    if show == 1:
        print('Number of variables: ',var_len)
    if show == 2:
        for i in range(var_len):
            print(var_list[i],':',np.shape(globals()[var_list[i]]))
    if show == 3:
        print(data.variables)
    
    if 'time' in var_total:
        time_0 = data.variables['time'][:]
        time_1 = netCDF4.num2date(time_0[:],data.variables['time'].units)
        dict_out['time'] = time_1
    elif 't' in var_total:
        time_0 = data.variables['t'][:]
        time_1 = netCDF4.num2date(time_0[:],data.variables['t'].units)
        dict_out['t'] = time_1
    
    return dict_out 

def clima_anom(var_in):
    len_in = len(np.shape(var_in))

    if len_in == 3:
        
        time,lat,lon = np.shape(var_in)
    
        lat = int(lat)
        lon = int(lon)
        anos = int(time/12)      
        
        var_name = {"jan": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "feb": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "mar": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "apr": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "may": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "jun": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "jul": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "ago": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "sep": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "oct": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "nov": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},
                    "dec": {'data':np.zeros([anos,lat,lon]),
                            'clim':np.zeros([1,lat,lon]),
                            'anom':np.zeros([anos,lat,lon])},}
        
        print('')
        print('Keys level 1: ',var_name.keys())
        print('keys level 2: ',var_name['jan'].keys())
        print('')
        print('Numbers of years: ',anos)
        print('Numbers of months: ',time)

        for i in range(0,anos):
            for j, key1 in enumerate(var_name.keys()):
                var_name[key1]['data'][i,:,:] = var_in[12*i+j,:,:]

        for i, key1 in enumerate(var_name.keys()):
            var_name[key1]['clim'][0,:,:] = (sum((var_name[key1]['data'][i,:,:]) for i in range(0,anos)))/anos

        for i in range(anos):
            for j, key1 in enumerate(var_name.keys()):
                var_name[key1]['anom'][i, :, :] = var_name[key1]['data'][i, :, :] - var_name[key1]['clim']
                
        return var_name
        
    else:
        print('ERROR: the variable doesn\'t have 3 dimensions, please convert to (time,lat,lon)')
        print('Actual variable Dimension: ',len_in)
        print('')
        var_name = 0
        
        return var_name
    
def climatology(var_in):
    num_anos,len_lat,len_lon = np.shape(var_in['jan']['data'])
    var_out = np.zeros([12,len_lat,len_lon])
    
    var_out[0,:,:] = var_in['jan']['clim']
    var_out[1,:,:] = var_in['feb']['clim']
    var_out[2,:,:] = var_in['mar']['clim']
    var_out[3,:,:] = var_in['apr']['clim']
    var_out[4,:,:] = var_in['may']['clim']
    var_out[5,:,:] = var_in['jun']['clim']
    var_out[6,:,:] = var_in['jul']['clim']
    var_out[7,:,:] = var_in['ago']['clim']
    var_out[8,:,:] = var_in['sep']['clim']
    var_out[9,:,:] = var_in['oct']['clim']
    var_out[10,:,:] = var_in['nov']['clim']
    var_out[11,:,:] = var_in['dec']['clim']
        
    return var_out

def anomalies(var_in):
    num_anos,len_lat,len_lon = np.shape(var_in['jan']['data'])
    var_out = np.zeros([12*num_anos,len_lat,len_lon])
    
    for i in range(num_anos):
        var_out[12*i,:,:] = var_in['jan']['anom'][i,:,:]
        var_out[12*i+1,:,:] = var_in['feb']['anom'][i,:,:]
        var_out[12*i+2,:,:] = var_in['mar']['anom'][i,:,:]
        var_out[12*i+3,:,:] = var_in['apr']['anom'][i,:,:]
        var_out[12*i+4,:,:] = var_in['may']['anom'][i,:,:]
        var_out[12*i+5,:,:] = var_in['jun']['anom'][i,:,:]
        var_out[12*i+6,:,:] = var_in['jul']['anom'][i,:,:]
        var_out[12*i+7,:,:] = var_in['ago']['anom'][i,:,:]
        var_out[12*i+8,:,:] = var_in['sep']['anom'][i,:,:]
        var_out[12*i+9,:,:] = var_in['oct']['anom'][i,:,:]
        var_out[12*i+10,:,:] = var_in['nov']['anom'][i,:,:]
        var_out[12*i+11,:,:] = var_in['dec']['anom'][i,:,:]
        
    return var_out

def season(var_in,season=1):
    
    anos,len_lat,len_lon = np.shape(var_in['jan']['data'])
    
    if season == 1:

        print('SUMMER Climatology')

        clima = 0
        clima = (var_in['dec']['clim'][0,:,:] + var_in['jan']['clim'][0,:,:] + var_in['feb']['clim'][0,:,:])/3
        
        anom = np.zeros([(anos)-1,len_lat,len_lon])
        for i in range(anos-1):
            anom[i,:,:]=(var_in['dec']['anom'][i,:,:]+var_in['jan']['anom'][i+1,:,:]+var_in['feb']['anom'][i+1,:,:])/3
         
        print('')
        print('Climatology: ',np.shape(clima))
        print('Anomaly: ',np.shape(anom))
        print('')

        return clima,anom

    elif season == 2:

        print('AUTUMN climatology')

        clima = 0
        clima = (var_in['mar']['clim'][0,:,:] + var_in['apr']['clim'][0,:,:] + var_in['may']['clim'][0,:,:])/3
        
        anom = np.zeros([(anos)-1,len_lat,len_lon])
        for i in range(anos-1):
            anom[i,:,:]=(var_in['mar']['anom'][i,:,:]+var_in['apr']['anom'][i+1,:,:]+var_in['may']['anom'][i+1,:,:])/3
         
        print('')
        print('Climatology: ',np.shape(clima))
        print('Anomaly: ',np.shape(anom))

        return clima,anom

    elif season == 3:

        print('WINTER Climatology')

        clima = 0
        clima = (var_in['jun']['clim'][0,:,:] + var_in['jul']['clim'][0,:,:] + var_in['ago']['clim'][0,:,:])/3
        
        anom = np.zeros([(anos)-1,len_lat,len_lon])
        for i in range(anos-1):
            anom[i,:,:]=(var_in['jun']['anom'][i,:,:]+var_in['jul']['anom'][i+1,:,:]+var_in['ago']['anom'][i+1,:,:])/3
         
        print('')
        print('Climatology: ',np.shape(clima))
        print('Anomaly: ',np.shape(anom))

        return clima,anom

    elif season == 4:

        print('SPRING Climatology')

        clima = 0
        clima = (var_in['sep']['clim'][0,:,:] + var_in['oct']['clim'][0,:,:] + var_in['nov']['clim'][0,:,:])/3
        
        anom = np.zeros([(anos)-1,len_lat,len_lon])
        for i in range(anos-1):
            anom[i,:,:]=(var_in['sep']['anom'][i,:,:]+var_in['oct']['anom'][i+1,:,:]+var_in['nov']['anom'][i+1,:,:])/3
         
        print('')
        print('Climatology: ',np.shape(clima))
        print('Anomaly: ',np.shape(anom))

        return clima,anom

    else:
        print('')
        print('ERROR: Season doesn\'t exist, choose one:')
        print('1: Summer')
        print('2: Autumn')
        print('3: winter')
        print('4: Spring')
        anom = 0
        clima = 0  

        return anom,clima

def correlation(data_1,data_2):
    
    anos,len_lat,len_lon = np.shape(data_1)
    
    corr = np.zeros([len_lat,len_lon])

    for i in range(len_lat):
        for j in range(len_lon):
            pearson = np.corrcoef(data_1[:,i,j],data_2[:,i,j])
            corr[i,j] = pearson[0,1]
   
    return corr

def closest_point(data,lat,lon,lat_ref,lon_ref):
    
    #print('Data shape     : ',np.shape(data))
    #print('Latitude shape : ',np.shape(lat))
    #print('Longitude shape: ',np.shape(lon))
    #print('')
    
    t,m,n = np.shape(data)
    
    def distance(lat1, lon1, lat2, lon2):
        p = 0.017453292519943295
        a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
        return 12742 * asin(sqrt(a))
    
    a = np.zeros([m*n,3])

    count = 0
    for i in range(m):
        for j in range(n):
            a[count,0] = distance(lat[i],lon[j],lat_ref,lon_ref)
            a[count,1] = lat[i]
            a[count,2] = lon[j]
            count = count + 1
            
	    #result = np.where(a == min(a[:,0]))
	    #index_lat = np.where(lat == a[result[0],1])
	    #index_lon = np.where(lon == a[result[0],2])
	    #print('Id, Latitud mas cercana : ',index_lat[0],lat[index_lat[0]])
	    #print('Id, Longitud mas cercana: ',index_lon[0],lon[index_lon[0]])
	    #salida = data[:,index_lat[0],index_lon[0]]

    result = a[a[:,0].argsort()]
    
    distance = result[0,0]
    lat_out = result[0,1]
    lon_ou = result[0,2]

    index_lat = np.where(lat == result[0,1])
    index_lon = np.where(lon == result[0,2])

    #print('Id, Latitud mas cercana : ',index_lat[0],result[0,1])
    #print('Id, Longitud mas cercana: ',index_lon[0],result[0,2])
    #print('')
        
    salida = data[:,index_lat[0],index_lon[0]]
            
    return salida

def extract_area(data,lat,lon,lat_min,lat_max,lon_min,lon_max):
    
    #https://stackoverflow.com/questions/29135885/netcdf4-extract-for-subset-of-lat-lon
    
    print('Data shape     : ',np.shape(data))
    print('Latitude shape : ',np.shape(lat))
    print('Longitude shape: ',np.shape(lon))
    print('')
    
    latbounds = [lat_min,lat_max]
    lonbounds = [lon_min,lon_max]
    
    #latli = np.argmin( np.abs( lat - latbounds[0] ) )
    #latui = np.argmin( np.abs( lat - latbounds[1] ) ) 
    latli = np.argmin( np.abs( lat - latbounds[1] ) ) 
    latui = np.argmin( np.abs( lat - latbounds[0] ) )
    
    lonli = np.argmin( np.abs( lon - lonbounds[0] ) )
    lonui = np.argmin( np.abs( lon - lonbounds[1] ) )  
    
    lat_out = lat[latli:latui+1]
    lon_out = lon[lonli:lonui+1]
    
    data_out = data[ : , latli:latui+1 , lonli:lonui+1 ] 
    
    print('Interest Area dimension: ',np.shape(data_out))
    print('')
    
    return data_out,lat_out,lon_out

def MAE(data1,data2):
    
    if data1.ndim != 3:
        print('')
        print('ERROR: data1 does not have 3 dimentions')
        print(np.shape(data1))
        MAE = 0
        return MAE
        
    if data2.ndim != 3:
        print('')
        print('ERROR: data2 does not have 3 dimentions')
        print(np.shape(data2))
        MAE = 0
        return MAE
    
    t1,n1,m1 = np.shape(data1)
    t2,n2,m2 = np.shape(data2)
    
    if n1 != n2:
        print('')
        print('ERROR: Matrices do not have the same latitude dimension')
        MAE = 0
        return MAE
    elif m1 != m2:
        print('')
        print('ERROR: Matrices do not have the same longitude dimension')
        MAE = 0
        return MAE
    elif t1 != t2:
        print('')
        print('ERROR: Matrices do not have the same time dimension')
        MAE = 0
        return MAE
    
    DIFF = abs(data1 - data2)
    
    MAE = np.zeros([n1,m1])
    
    for i in range(n1):
        for j in range(m1):
            MAE[i,j] = np.sum(DIFF[:,i,j])/t1
        
    return MAE

def RMSE(data1,data2):
    
    if data1.ndim != 3:
        print('')
        print('ERROR: Data1 does not have 3 dimensions')
        RMSE = 0
        return RMSE
        
    if data2.ndim != 3:
        print('')
        print('ERROR: Data2 does not have 3 dimensions')
        RMSE = 0
        return RMSE
    
    t1,n1,m1 = np.shape(data1)
    t2,n2,m2 = np.shape(data2)
    
    if n1 != n2:
        print('')
        print('ERROR: Matrices do not have the same latitude dimension')
        RMSE = 0
        return RMSE
    elif m1 != m2:
        print('')
        print('ERROR: Matrices do not have the same longitude dimension')
        RMSE = 0
        return RMSE
    elif t1 != t2:
        print('')
        print('ERROR: Matrices do not have the same time dimension')
        RMSE = 0
        return RMSE
    
    DIFF = (data1 - data2)
    
    RMSE = np.zeros([n1,m1])
    
    for i in range(n1):
        for j in range(m1):
            RMSE[i,j] = np.sqrt(np.sum(DIFF[:,i,j]*DIFF[:,i,j])/t1)
        
    return RMSE 

def BIAS(data1,data2):
    
    if data1.ndim != 3:
        print('')
        print('ERROR: Data1 does not have 3 dimensions')
        BIAS = 0
        return BIAS
        
    if data2.ndim != 3:
        print('')
        print('ERROR: Data2 does not have 3 dimensions')
        BIAS = 0
        return BIAS
    
    t1,n1,m1 = np.shape(data1)
    t2,n2,m2 = np.shape(data2)
    
    if n1 != n2:
        print('')
        print('ERROR: Matrices do not have the same latitude dimension')
        BIAS = 0
        return BIAS

    elif m1 != m2:
        print('')
        print('ERROR: Matrices do not have the same longitude dimension')
        BIAS = 0
        return BIAS

    elif t1 != t2:
        print('')
        print('ERROR: Matrices do not have the same time dimension')
        BIAS = 0
        return BIAS
    
    BIAS = np.zeros([n1,m1])
    
    for i in range(n1):
        for j in range(m1):
            BIAS[i,j] = np.sum(data1[:,i,j] - data2[:,i,j])/t2
        
    return BIAS

def RBIAS(data1,data2):
    
    if data1.ndim != 3:
        print('')
        print('ERROR: Data1 does not have 3 dimensions')
        RBIAS = 0
        return RBIAS
        
    if data2.ndim != 3:
        print('')
        print('ERROR: Data2 does not have 3 dimensions')
        RBIAS = 0
        return RBIAS
    
    t1,n1,m1 = np.shape(data1)
    t2,n2,m2 = np.shape(data2)
    
    if n1 != n2:
        print('')
        print('ERROR: Matrices do not have the same latitude dimension')
        RBIAS = 0
        return RBIAS

    elif m1 != m2:
        print('')
        print('ERROR: Matrices do not have the same longitude dimension')
        RBIAS = 0
        return RBIAS

    elif t1 != t2:
        print('')
        print('ERROR: Matrices do not have the same time dimension')
        RBIAS = 0
        return RBIAS
    
    RBIAS = np.zeros([n1,m1])
    
    for i in range(n1):
        for j in range(m1):
            RBIAS[i,j] = ((np.sum(data1[:,i,j]-data2[:,i,j]))/(np.sum(data2[:,i,j])))*100
        
    return RBIAS

def DiasDoAno(ano,mes):
    
#     ano = int(ano)
    
    if calendar.isleap(ano) == True:

        if mes == 'jan' or mes == 'Jan': 
            day_start=1;day_end=31
        elif mes == 'feb' or mes == 'Feb':
            day_start=32;day_end=60
        elif mes == 'mar' or mes == 'Mar':
            day_start=61;day_end=91
        elif mes == 'apr' or mes == 'Apr':
            day_start=92;day_end=121
        elif mes == 'may' or mes == 'May':
            day_start=122;day_end=152
        elif mes == 'jun' or mes == 'Jun':
            day_start=153;day_end=182
        elif mes == 'jul' or mes == 'Jul':
            day_start=183;day_end=213
        elif mes == 'ago' or mes == 'Ago':
            day_start=214;day_end=244
        elif mes == 'sep' or mes == 'Sep':
            day_start=245;day_end=274
        elif mes == 'oct' or mes == 'Oct':
            day_start=275;day_end=305
        elif mes == 'nov' or mes == 'Nov':
            day_start=306;day_end=335
        elif mes == 'dec' or mes == 'Dec':
            day_start=336;day_end=366
        else:
            print('ERROR: Month name')
            day_start=0;day_end=0
            return day_start,day_end

    else:

        if mes == 'jan' or mes == 'Jan':
            day_start=1;day_end=31
        elif mes == 'feb' or mes == 'Feb':
            day_start=32;day_end=59
        elif mes == 'mar' or mes == 'Mar':
            day_start=60;day_end=90
        elif mes == 'apr' or mes == 'Apr':
            day_start=91;day_end=120
        elif mes == 'may' or mes == 'May':
            day_start=121;day_end=151
        elif mes == 'jun' or mes == 'Jun':
            day_start=152;day_end=181
        elif mes == 'jul' or mes == 'Jul':
            day_start=182;day_end=212
        elif mes == 'ago' or mes == 'Ago':
            day_start=213;day_end=243
        elif mes == 'sep' or mes == 'Sep':
            day_start=244;day_end=273
        elif mes == 'oct' or mes == 'Oct':
            day_start=274;day_end=304
        elif mes == 'nov' or mes == 'Nov':
            day_start=305;day_end=334
        elif mes == 'dec' or mes == 'Dec':
            day_start=335;day_end=365
        else:
            print('ERROR: Month name')
            day_start=0;day_end=0
            return day_start,day_end
                
    return day_start,day_end
    
def create_netcdf(info,latitude,longitude,data):
    
    if info['year_start'] > info['year_end']:
        print('ERROR: Year Start cannot be greater than Year End')
        dates = 0
        return dates

    str_dt = datetime.datetime(info['year_start'],info['month_start'],info['day_start'],info['hour_start'],info['minute_start'])
    end_dt = datetime.datetime(info['year_end'],info['month_end'],info['day_end'],info['hour_end'],info['minute_end'])
    
    if info['time_frequency'] == 'Monthly' or info['time_frequency'] == 'monthly':
        dates = [dt for dt in rrule(MONTHLY, interval=info['time_interval'], dtstart=str_dt, until=end_dt)]
        print('Time Start:',dates[0])
        print('Time End:',dates[-1])
        print('Time Frequency:',info['time_frequency'])
        print('Time Lenght:',len(dates))
    
    elif info['time_frequency'] == 'Weekly' or info['time_frequency'] == 'weekly':
        dates = [dt for dt in rrule(WEEKLY, interval=info['time_interval'], dtstart=str_dt, until=end_dt)]
        print('Time Start:',dates[0])
        print('Time End:',dates[-1])
        print('Time Frequency:',info['time_frequency'])
        print('Time Lenght:',len(dates))

    elif info['time_frequency'] == 'Daily' or info['time_frequency'] == 'daily':
        dates = [dt for dt in rrule(DAILY, interval=info['time_interval'], dtstart=str_dt, until=end_dt)]
        print('Time Start:',dates[0])
        print('Time End:',dates[-1])
        print('Time Frequency:',info['time_frequency'])
        print('Time Lenght:',len(dates))
           
    elif info['time_frequency'] == 'Hourly' or info['time_frequency'] == 'hourly':
        dates = [dt for dt in rrule(HOURLY, interval=info['time_interval'], dtstart=str_dt, until=end_dt)]
        print('Time Start:',dates[0])
        print('Time End:',dates[-1])
        print('Time Frequency:',info['time_frequency'])
        print('Time Lenght:',len(dates))
    
    elif info['time_frequency'] == 'Minutely' or info['time_frequency'] == 'minutely':
        dates = [dt for dt in rrule(MINUTELY, interval=info['time_interval'], dtstart=str_dt, until=end_dt)]
        print('Time Start:',dates[0])
        print('Time End:',dates[-1])
        print('Time Frequency:',info['time_frequency'])
        print('Time Lenght:',len(dates))
        
    else:
        print('ERROR: time_frequency \"' + info['time_frequency'] +'\" not defined')
        dates = 'time_frequency should be: Monthly, Weekly, Daily, Hourly or Minutely'
        return dates
    
    tiempo = np.zeros([len(dates)])
    
# ===================================================
#    GENERA ERRORES     
#    for i in range(12):  #No se porque 12
#    for i in range(len(dates)):
#        dtt = dates[i].timetuple() 
#        stamp = time_b.mktime(dtt)
#        tiempo[i] = int(stamp)

    tiempo = date2num(dates, units='days since '+str(info['year_start'])+'-'+str(info['month_start'])+'-'+str(info['day_start']))

    info_a = { 'comment': info['time_frequency']+' '+info['title']+' from '+str(info['year_start'])+'-'+str(info['month_start'])+'-'+str(info['day_start'])+' to december '+str(info['year_end'])+'-'+str(info['month_end'])+'-'+str(info['day_end']),
           'time_units': 'days since '+str(info['year_start'])+'-'+str(info['month_start'])+'-'+str(info['day_start'])} # don't edit
    
    nc_title = info['title']
    nc_comment = info_a['comment']

    nc_time_units = info_a['time_units']

    nc_var_name = info['var_name']
    nc_var_units = info['var_units']
    
    ncfile = netCDF4.Dataset(info['file'],mode='w',format='NETCDF4_CLASSIC')
    
    ncfile.title = nc_title
    ncfile.anything = nc_comment
    
    lat_dim = len(latitude)
    lon_dim = len(longitude)
    time_dim = len(tiempo)
    
    lat_dim = ncfile.createDimension('lat',lat_dim)
    lon_dim = ncfile.createDimension('lon',lon_dim)
    time_dim = ncfile.createDimension('time',None)
    
    lat = ncfile.createVariable('lat',np.float32,('lat',))
    lat.units = 'degrees_north'
    lat.long_name = 'latitude'

    lon = ncfile.createVariable('lon',np.float32,('lon',))
    lon.units = 'degrees_east'
    lon.long_name = 'longitude'

    time = ncfile.createVariable('time',np.float64,('time',))
    time.units = nc_time_units
    time.long_name = 'time'
    
    var = ncfile.createVariable(info['var_name'],np.float64,('time','lat','lon'))
    var.units = nc_var_units
    var.standard_name = nc_var_name
    
    lat[:] = latitude
    lon[:] = longitude
    
    var[:,:,:] = data
    
    time[:] = tiempo
    
    print()
    print('File created in: ',info['file'])
    print('File title: ',info['title'])
    print('var title: ',info['var_name'])
    print('var units: ',info['var_units'])
    
    ncfile.close()

def remove_continent_ocean(var_in,latitude,longitude,remove='continent'):
    
    land_shp_fname = shpreader.natural_earth(resolution='50m',category='physical', name='land')

    land_geom = unary_union(list(shpreader.Reader(land_shp_fname).geometries()))
    land = prep(land_geom)
    
    def is_land(x, y):
        return land.contains(sgeom.Point(x, y))

    len_in = len(np.shape(var_in))
    
    lat_mi = min(latitude)
    lat_ma = max(latitude)
    lon_mi = min(longitude)
    lon_ma = max(longitude)
    
    len_latitude = len(np.shape(latitude))
    if len_latitude != 1:
        print('ERROR: latitude doesn\'t have 1 dimension')
        print('Actual latitude Dimension: ',len_latitude)
        print('')
        var_out = 0
        return var_out
    
    len_longitude = len(np.shape(longitude))
    if len_longitude != 1:
        print('ERROR: longitude doesn\'t have 1 dimension')
        print('Actual longitude Dimension: ',len_longitude)
        print('')
        var_out = 0
        return var_out
    
    var_out = np.copy(var_in)
    
    if len_in == 3:
        
        if remove == 'continent' or remove == 'Continent' or remove == '1':
            for i in longitude:
                for j in latitude:
                    if land.contains(sgeom.Point(i,j)) == True:
                        a, = np.where(latitude == j)
                        b, = np.where(longitude == i)
                        var_out[:,a,b] = np.nan
            return var_out
        
        if remove == 'ocean' or remove == 'Ocean' or remove == '2':
            for i in longitude:
                for j in latitude:
                    if land.contains(sgeom.Point(i,j)) == False:
                        a, = np.where(latitude == j)
                        b, = np.where(longitude == i)
                        var_out[:,a,b] = np.nan
            return var_out
    
        else:
            print('')
            print('ERROR: Option',remove,'doesn\'t exist, choose one:')
            print('1: continent')
            print('2: ocean')
            var_out = 0
            return var_out
                    
    else:
        print('ERROR: the variable doesn\'t have 3 dimensions, please convert to (time,lat,lon)')
        print('Actual variable Dimension: ',len_in)
        print('')
        var_out = 0
        
        return var_out

def extract_shapefile(shapefile_dir,data_in,lat_in,lon_in):
    
    r = shapefile.Reader(shapefile_dir)

    shapes = r.shapes()
    polygon = shape(shapes[0]) 
    
    data_out = np.copy(data_in)
    
    if len(data_in.shape) == 1:
        for i in range(len(lat_in)):
            a = Point(lon_in[i],lat_in[i])

            if polygon.contains(a) == False:
                data_out[i] = np.nan
            
        return data_out
    
    if len(data_in.shape) == 2 or len(data_in.shape) == 3:
        for j in lat_in:
            for i in lon_in:
                a = Point(i,j)
                if polygon.contains(a) == False:
                    temp1, = np.where(lon_in == i)
                    temp2, = np.where(lat_in == j)

                    if len(data_in.shape) == 2:
                        data_out[temp2,temp1] = np.nan
                    elif len(data_in.shape) == 3:
                        data_out[:,temp2,temp1] = np.nan

        return data_out
