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
    read netcdf funtion
    
    for read netcdf file

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