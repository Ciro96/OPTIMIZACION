import numpy as np
def grad_braq(x):
    N=x.size
    g=10
    f=np.linspace(0,1,N+2)[::-1]
    grad=np.zeros(N)
    for i in range(1,N-1):
        grad[i]=np.sqrt(2/g)*(1/2)*(np.sqrt(1+((x[i+1]-x[i])/(f[i+2]-f[i+1]))**2)**(-1))*(np.sqrt(1-f[i+2])-np.sqrt(1-f[i+1]))*(-2*(x[i+1]-x[i])/((f[i+2]-f[i+1])**2))
        grad[i]=grad[i]+np.sqrt(2/g)*(1/2)*(np.sqrt(1+((x[i]-x[i-1])/(f[i+1]-f[i]))**2)**(-1))*(np.sqrt(1-f[i+1])-np.sqrt(1-f[i]))*(2*(x[i]-x[i-1])/((f[i+1]-f[i])**2))
    grad[0]=np.sqrt(2/g)*(1/2)*(np.sqrt(1+((x[0])/(f[1]-f[0]))**2)**(-1))*(np.sqrt(1-f[1])-np.sqrt(1-f[0]))*(2*(x[0])/((f[1]-f[0])**2))
    grad[0]=grad[0]+ np.sqrt(2/g)*(1/2)*(np.sqrt(1+((x[1]-x[0])/(f[2]-f[1]))**2)**(-1))*(np.sqrt(1-f[2])-np.sqrt(1-f[1]))*(-2*(x[1]-x[0])/((f[2]-f[1])**2))   
    grad[N-1]=np.sqrt(2/g)*(1/2)*(np.sqrt(1+((1-x[N-1])/(f[N+1]-f[N]))**2)**(-1))*(np.sqrt(1-f[N+1])-np.sqrt(1-f[N]))*(-2*(1-x[N-1])/((f[N+1]-f[N])**2))
    grad[N-1]=grad[N-1]+np.sqrt(2/g)*(1/2)*(np.sqrt(1+((x[N-1]-x[N-2])/(f[N]-f[N-1]))**2)**(-1))*(np.sqrt(1-f[N])-np.sqrt(1-f[N-1]))*(2*(x[N-1]-x[N-2])/((f[N]-f[N-1])**2))
    return grad
    
