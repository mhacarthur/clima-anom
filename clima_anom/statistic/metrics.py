
import numpy as np

def correlation(data_1,data_2):
    
    anos,len_lat,len_lon = np.shape(data_1)
    
    corr = np.zeros([len_lat,len_lon])
    
    for i in range(len_lat):
        for j in range(len_lon):
            
            nan_bnd = (np.argwhere(~np.isnan(data_1[:,i,j])))[:,0]
            pearson = np.corrcoef(data_1[:,i,j][nan_bnd],data_2[:,i,j][nan_bnd])
            corr_temp = pearson[0,1]
            corr[i,j] = corr_temp
            
    return corr

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

