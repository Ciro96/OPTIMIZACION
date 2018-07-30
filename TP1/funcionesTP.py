import numpy as np
import matplotlib.pyplot as plt

def gnewton(a0,jacobiano,gradNormar,r,tol):
    a=a0
    jac=jacobiano(a)
    error=r(a)
    T=1
    i=0
    while(T>tol and i<2000):
        Norma_error=np.dot(r(a),r(a))
        #print(i,"error",Norma_error)
        A=np.dot(np.transpose(jac),jac)
        b=np.dot(np.transpose(jac),np.transpose(np.dot(jac,a)-error))
        a=np.transpose(np.linalg.solve(A,b))
        jac=jacobiano(a)
        error=r(a)
        T=np.linalg.norm(gradNormar(a,r))
        i=i+1
        
    #print(T)
    #print("cantidad de iteraciones",i)
    
    return a
    
def cuadMin(X,Y):
    #resuelve cuadrados minimos con modelo a0 +a1*X
    #devuelve np.array([a0,a1])
    N=X.size
    A=np.ones((N,2))
    A[:,1]=np.array(-X)
    b=np.dot(np.transpose(A),Y)
    M=np.dot(np.transpose(A),A)
    return np.linalg.solve(M,b)



	
	
