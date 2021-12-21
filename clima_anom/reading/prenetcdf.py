import numpy as np
import netCDF4
from netCDF4 import Dataset
from netCDF4 import date2num

import calendar
import datetime
from datetime import timedelta
from dateutil.rrule import rrule, YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY

def read_netcdf(filename,show=1):
    """
    DESCRIPTION
    Function to read netcdf files. 

    ca.read_netcdf(namefile,id)
    
    The function needs two inputs. Namefile is the name of the netcdf file and 
    id is the descriptor number to show the different levels of details of the 
    variables inside the netcdf.

    :param namefile: string 
    :param id: integer

    ID LEVELS
    * ca.read_netcdf(data_dir,3)
    Shows all the information contained about the variables

    * ca.read_netcdf(data_dir,2)
    Shows name of variables and its shapes

    * ca.read_netcdf(data_dir,1)
    Shows only the number of variables

    * ca.read_netcdf(data_dir,0)
    Shows nothing
    
    EXAMPLE
    >>> namefile = '/home/user/Data/Hgt_1000hPa_Dec49_Feb20.nc'
    >>> data = ca.read_netcdf(data_dir,1)
    """

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

    if show == 0:
        pass

    elif show == 1:
        print('Number of variables: ',var_len)

    elif show == 2:
        for i in range(var_len):
            print(var_list[i],':',np.shape(globals()[var_list[i]]))

    elif show == 3:
        print(data.variables)

    else:
        print(f'Error: Id value {show} doesn\'t exits')
        print('Try with Id: 0, 1, 2 or 3')
        return None
    
    if 'time' in var_total:
        time_0 = data.variables['time'][:]
        time_1 = netCDF4.num2date(time_0[:],data.variables['time'].units)
        dict_out['time'] = time_1
    elif 't' in var_total:
        time_0 = data.variables['t'][:]
        time_1 = netCDF4.num2date(time_0[:],data.variables['t'].units)
        dict_out['t'] = time_1
    
    return dict_out

def create_netcdf(info,latitude,longitude,data):
    """
    DESCRIPTION
    Funtion for export data array to netcdf format

    ca.create_netcdf(info,latitude,longitude,var_input)

    This funtion uses four inputs, one dictionary called info and three variables,
    which are:

    :param latitude: float 
    :param longitude: float
    :param var_input: float

    And the info:

    info = {'file': filename_out, # filename for netcdf file
            'title': description, # netcdf title or little descriptionn
            'year_start':y_s,'month_start':m_s,'day_start':d_s,
            'hour_start':h_s,'minute_start':m_s, # time start 
            'year_end':y_e,'month_end':m_e,'day_end':d_e,
            'hour_end':h_e,'minute_end':m_e, # time end
            'time_frequency': frequency, # Monthly, Daily, Hourly, Minutely
            'time_interval':time_int, # time interval
            'var_name': var_name, # variable short name
            'var_units': var_units} # variable units

    EXAMPLE
    >>> namefile = '/home/user/Data/Hgt_1000hPa_Dec49_Feb20.nc'
    >>> data = ca.read_netcdf(data_dir,1)

    >>> latitude = data['lat']
    >>> longitude = data['lon']
    >>> hgt = data['hgt'][:,0,:,:]

    >>> info = {
        'file': '/home/user/Data/Hgt_1000hPa_Dec49_Feb20_new.nc',
        'title': 'Geopotential Height 1000 hPa', 
        'year_start':1949, 'month_start':12, 'day_start':1, 
        'hour_start':0, 'minute_start':0, 
        'year_end':2020, 'month_end':2, 'day_end':1, 
        'hour_end':23, 'minute_end':59, 
        'time_frequency': 'Monthly', 
        'time_interval':1,
        'var_name': 'hgt',
        'var_units': 'hPa'} 

    >>> ca.create_netcdf(info,latitude,longitude,hgt)
    """
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