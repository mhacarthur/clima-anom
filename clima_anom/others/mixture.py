
import numpy as np
import matplotlib.colors
from matplotlib import pyplot as plt
import calendar

def extract_area(data,lat,lon,lat_min,lat_max,lon_min,lon_max):
    '''
    DESCRIPTION
    Extract info for a specific region using latitude and longitude limits.

    :param data: float
    :param lat: float
    :param lon: float

    EXAMPLE
    data_out, lat_out, lon_out = extract_area(data,lat,lon,-10.5,10.5,-60.5,50.5)
    '''
    
    print('Data shape     : ',np.shape(data))
    print('Latitude shape : ',np.shape(lat))
    print('Longitude shape: ',np.shape(lon))
    print('')
    
    latbounds = [lat_min,lat_max]
    lonbounds = [lon_min,lon_max]
    
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

def DiasDoAno(ano,mes):
    '''
    DESCRIPTION
    This Funtion shows start and end day of year.

    :param ano: integer
    :param mes: string

    EXAMPLE
    >>> DiasDoAno(2015,feb)
    >>> DiasDoAno(2015,Feb)
    >>> DiasDoAno(2015,February)
    '''
    
    if calendar.isleap(ano) == True:

        if mes == 'jan' or mes == 'Jan' or mes == 'January': 
            day_start=1;day_end=31
        elif mes == 'feb' or mes == 'Feb' or mes == 'February':
            day_start=32;day_end=60
        elif mes == 'mar' or mes == 'Mar' or mes == 'March':
            day_start=61;day_end=91
        elif mes == 'apr' or mes == 'Apr' or mes == 'April':
            day_start=92;day_end=121
        elif mes == 'may' or mes == 'May' or mes == 'May':
            day_start=122;day_end=152
        elif mes == 'jun' or mes == 'Jun' or mes == 'June':
            day_start=153;day_end=182
        elif mes == 'jul' or mes == 'Jul' or mes == 'July':
            day_start=183;day_end=213
        elif mes == 'ago' or mes == 'Ago' or mes == 'August':
            day_start=214;day_end=244
        elif mes == 'sep' or mes == 'Sep' or mes == 'September':
            day_start=245;day_end=274
        elif mes == 'oct' or mes == 'Oct' or mes == 'October':
            day_start=275;day_end=305
        elif mes == 'nov' or mes == 'Nov' or mes == 'November':
            day_start=306;day_end=335
        elif mes == 'dec' or mes == 'Dec' or mes == 'December':
            day_start=336;day_end=366
        else:
            print('ERROR: Month name')
            day_start=0;day_end=0
            return day_start,day_end

    else:

        if mes == 'jan' or mes == 'Jan' or mes == 'January':
            day_start=1;day_end=31
        elif mes == 'feb' or mes == 'Feb' or mes == 'February':
            day_start=32;day_end=59
        elif mes == 'mar' or mes == 'Mar' or mes == 'March':
            day_start=60;day_end=90
        elif mes == 'apr' or mes == 'Apr' or mes == 'April':
            day_start=91;day_end=120
        elif mes == 'may' or mes == 'May' or mes == 'May':
            day_start=121;day_end=151
        elif mes == 'jun' or mes == 'Jun' or mes == 'June':
            day_start=152;day_end=181
        elif mes == 'jul' or mes == 'Jul' or mes == 'July':
            day_start=182;day_end=212
        elif mes == 'ago' or mes == 'Ago' or mes == 'August':
            day_start=213;day_end=243
        elif mes == 'sep' or mes == 'Sep' or mes == 'September':
            day_start=244;day_end=273
        elif mes == 'oct' or mes == 'Oct' or mes == 'October':
            day_start=274;day_end=304
        elif mes == 'nov' or mes == 'Nov' or mes == 'November':
            day_start=305;day_end=334
        elif mes == 'dec' or mes == 'Dec' or mes == 'December':
            day_start=335;day_end=365
        else:
            print('ERROR: Month name')
            day_start=0;day_end=0
            return day_start,day_end
                
    return day_start,day_end



def colorbar_white_middle(cmap,n=35,x=0.5):
    """
    
    """

    n = 35
    x = 0.5

    lower = cmap(np.linspace(0, x, n))
    white = np.ones((80-2*n,4))
    upper = cmap(np.linspace(1-x, 1, n))

    colors = np.vstack((lower, white, upper))

    tmap = matplotlib.colors.LinearSegmentedColormap.from_list('map_white', colors)

    return tmap