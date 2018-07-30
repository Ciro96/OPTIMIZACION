import numpy as np
#x0 es numpy array
#en matlab es gradient(F)
def gradiente(f,x0):
    N=x0.size
    gradiente=np.zeros(N)
    for i in range(N):
        ei=np.zeros(N)
        ei[i]=1
        gradiente[i]=(f(x0+0.0001*ei)-f(x0))/0.0001
        #como elijo h
	#hacer algo que elija solo el h
    return gradiente



