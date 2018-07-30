import numpy as np
from gradiente import gradiente
def hessiano(f,x0):
    N=x0.size
    hessiano=np.zeros((N,N))
    for i in range(N):
        ei=np.zeros(N)
        ei[i]=1
        #print(ei)
#        print(gradiente(f,x0+0.01*ei)),
#        print(gradiente(f,x0-0.01*ei))
        hessiano[:,i]=(np.transpose(gradiente(f,x0+0.001*ei))-np.transpose(gradiente(f,x0-0.001*ei)))/(2*0.001)

    return hessiano

