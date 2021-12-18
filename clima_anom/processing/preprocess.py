
import numpy as np

def data_dictionary(var_in):

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