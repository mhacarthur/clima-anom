
import numpy as np
import matplotlib.colors
from matplotlib import pyplot as plt
import calendar

def redefinir_area(data_in,lat_in,lon_in,lat_min,lat_max,lon_min,lon_max):
    '''
    DESCRIPTION
    Funntion to extract a specific region 

    PARAMETERS
    :param data_in: float
    :param lat_in: float
    :param lon_in: float
    :param lat_min: float
    :param lat_max: float
    :param lon_min: float
    :param lon_max: float

    EXAMPLE
    Read and define hgt, latitude and longitude:
    >>> data_dir = '/home/user/Data/Hgt_1000hPa_Dec49_Feb20.nc'
    >>> data = ca.read_netcdf(data_dir,1)
    >>> hgt = data['hgt'][:,0,:,:]
    >>> lat = data['latitude']
    >>> lon = data['longitude']

    Define limits for region 
    >>> lat_min = -17; lat_max = 17
    >>> lon_min = -50; lon_max = 15

    Extract area
    >>> hgt_cut, lat_cut, lon_cut = redefinir_area(hgt,lat,lon,lat_min,lat_max,lon_min,lon_max)

    '''
    
    y_bounds = np.where((lat_in>=lat_min)&(lat_in<=lat_max))[0]
    lat_tmp = lat_in[y_bounds]
    
    x_bounds = np.where((lon_in>=lon_min)&(lon_in<=lon_max))[0]
    lon_tmp = lon_in[x_bounds]

    data_out = data_in[:,y_bounds[0]:y_bounds[-1]+1,x_bounds[0]:x_bounds[-1]+1]
    
    return data_out, lat_tmp, lon_tmp

def DiasDoAno(ano,mes):
    '''
    DESCRIPTION
    This Function shows start and end day of year.

    PARAMETERS
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

def colorbar_middle_white(cmap,position='middle',n=35,x=0.5):
    """
    DESCRIPTION
    Function to add middle white from another colorbar 

    PARAMETERS
    :param cmap: colormap
    :param position: string or integer
    :param n: integer
    :param x: float

    from a colorbar definas as cmap, n as the number of nivels and the increment, 
    this is a simple function to modify a specific colorbar.

    The parameter position input could be defined as:
    1. Starting with white: position = 'left' or position = -1
    2. midlle with white: position = 'middle' or position = 0
    3. ending with white: position = 'right' or position = 1   

    EXAMPLE
    This example uses a red to blue colorbar 
    >>> cmap = plt.cm.Spectral_r
    Colorbar with white in the left
    >>> cmap_sst = colorbar_middle_white(cmap,-1)
    Colorbar with white in the middle
    >>> cmap_sst = colorbar_middle_white(cmap,0)
    Colorbar with white in the right
    >>> cmap_sst = colorbar_middle_white(cmap,1)
    """

    lower = cmap(np.linspace(0, x, n))
    white = np.ones((80-2*n,4))
    upper = cmap(np.linspace(1-x, 1, n))

    if position == 'left' or position == -1:
        colors = np.vstack((white, lower, upper))
    elif position == 'middle' or position == 0:
        colors = np.vstack((lower, white, upper))
    elif position == 'right' or position == 1:
        colors = np.vstack((lower, upper, white))
    else:
        print(f'ERROR: position {position} is not defined')
        print('Try to: left, middle, right or -1, 0, 1')
        tmap = None
        return tmap

    tmap = matplotlib.colors.LinearSegmentedColormap.from_list('map_white', colors)

    return tmap

