
import numpy as np

import matplotlib.pyplot as plt
import shapefile
from shapely.geometry import shape, Point

import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom
from shapely.ops import unary_union
from shapely.prepared import prep

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
    
    if len_in == 2:
        
        if remove == 'continent' or remove == 'Continent' or remove == '1':
            for i in longitude:
                for j in latitude:
                    if land.contains(sgeom.Point(i,j)) == True:
                        a, = np.where(latitude == j)
                        b, = np.where(longitude == i)
                        var_out[a,b] = np.nan
            return var_out
        
        if remove == 'ocean' or remove == 'Ocean' or remove == '2':
            for i in longitude:
                for j in latitude:
                    if land.contains(sgeom.Point(i,j)) == False:
                        a, = np.where(latitude == j)
                        b, = np.where(longitude == i)
                        var_out[a,b] = np.nan
            return var_out
        
        else:
            print('')
            print('ERROR: Option',remove,'doesn\'t exist, choose one:')
            print('1: continent')
            print('2: ocean')
            var_out = 0
            return var_out
        
    elif len_in == 3:
        
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
        print('ERROR: the variable doesn\'t have 2 or 3 dimensions, please convert to (lat,lon) or (time,lat,lon)')
        print('Actual variable Dimension: ',len_in)
        print('')
        var_out = 0
        
        return var_out

def extract_shapefile(shapefile_dir,data_in,lat_in,lon_in,shp_id=0):
    
    r = shapefile.Reader(shapefile_dir)

    shapes = r.shapes()
    print('Shapes ID len: ',len(shapes))
    polygon = shape(shapes[shp_id]) 
    
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