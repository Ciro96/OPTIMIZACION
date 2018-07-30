import numpy as np
def braq(x):
    N=x.size
    g=9.81
    f=np.linspace(0,1,N+2)[::-1]
    braq=np.sqrt(2/g)*np.sqrt(1+((x[0])/(f[1]-f[0]))**2)*(np.sqrt(1-f[1])-np.sqrt(1-f[0])) #es un quilombo de indices,escribir un comentario
    for i in range(0,N-1):
        braq=braq + np.sqrt(2/g)*np.sqrt(1+((x[i+1]-x[i])/(f[i+2]-f[i+1]))**2)*(np.sqrt(1-f[i+2])-np.sqrt(1-f[i+1]))
    braq=braq+np.sqrt(2/g)*np.sqrt(1+((1-x[N-1])/(f[N+1]-f[N]))**2)*(np.sqrt(1-f[N+1])-np.sqrt(1-f[N]))
    return braq


        

