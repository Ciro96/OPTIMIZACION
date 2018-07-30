import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from funcionesTP import gnewton,cuadMin
   
def grad_cuadNorma_r(X,Y):#gradiente de (1/2)*norma cuadrado de r 
    def grad(a,r):
        return np.dot(np.transpose(jacobiano_2(X,Y)(a)),np.transpose(r(a)))
    return grad

def cuad_Norma_r(a,r):#cuadrado de la norma de r_2
    return np.dot(r(a),r(a))

def r_2(X,Y):
    def r(a): 
        return a[0]*np.exp(-a[1]*X) + a[2]-Y
    return r
    
def jacobiano_2(X,Y):# jacobiano de r_2
    def jacobiano(a):
        N=X.size
        A=np.ones((N,3))
        A[:,0]=np.exp(-a[1]*X)
        A[:,1]=-X*a[0]*np.exp(-a[1]*X)
        return A
    return jacobiano
    
def modelo_2(X,Y):    
    a=gnewton(np.array([0.723,0.00088,0]),jacobiano_2(X,Y),grad_cuadNorma_r(X,Y),r_2(X,Y),0.0001)
    print("error con a de gauss-newton",cuad_Norma_r(a,r_2(X,Y)))
    print("parametros con gauss-newton",a)
    print("norma del gradiente de 1/2*|r|^2 ",np.linalg.norm(grad_cuadNorma_r(X,Y)(a,r_2(X,Y))))
    X=np.r_[200:4000]
    Y_gnewton=a[0]*np.exp(-a[1]*X)+a[2] 
    return X,Y_gnewton

X_A=np.array([200,400,800,1200,1600,2000,3000,4000])
Y_A=np.array([0.65,0.46,0.34,0.26,0.17,0.15,0.06,0.04])
X_B=np.array([200,400,800,1200,1600,2000,3000,4000])
Y_B=np.array([0.63,0.5,0.3,0.24,0.19,0.12,0.08,0.05])

print("-----------------ciudad A------------------\n")
X,Y_A_gnewton=modelo_2(X_A,Y_A)
print("-----------------ciudad B------------------\n")
X,Y_B_gnewton=modelo_2(X_B,Y_B)

#armo los gráficos de las curvas con gauss-newton
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(X_A,Y_A,"o")
ax[0].plot(X,Y_A_gnewton,color="orange")
ax[0].set_title("ciudad A")
orange= mpatches.Patch(color='orange', label='Gauss-Newton')
ax[0].legend(handles=[orange])
ax[1].plot(X_B,Y_B,"o")
ax[1].plot(X,Y_B_gnewton,color="orange")
ax[1].set_title("ciudad B")
orange= mpatches.Patch(color='orange', label='Gauss-Newton')
ax[1].legend(handles=[orange])



plt.suptitle(r'$\alpha_0 e^{-\alpha_1 X_i}+\alpha_2$')
plt.show()

