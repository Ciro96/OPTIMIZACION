import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from funcionesTP import gnewton,cuadMin

def grad_cuadNorma_r(X,Y):#gradiente de (1/2)*|r|^2
    def grad(a,r):
        return np.dot(np.transpose(jacobiano_1(X,Y)(a)),np.transpose(r(a)))
    return grad

def cuad_Norma_r(a,r):#cuadrado de la norma de r_1 
    return np.dot(r(a),r(a))

def r_1(X,Y):
    def r(a):
        return a[0]*np.exp(-a[1]*X)-Y
    return r
    
def jacobiano_1(X,Y):#jacobiano de r_1
    def jacobiano(a):
        N=X.size
        A=np.zeros((N,2))
        A[:,0]=np.exp(-a[1]*X)
        A[:,1]=-X*a[0]*np.exp(-a[1]*X)
        return A
    return jacobiano 

#-----------------------------------------------------------------------
#tomo logaritmo y obtengo a con cuadrados minimos
#uso a=[e^a0,a1] para inicializar Gauss-Newton con el modelo no-lineal 
#------------------------------------------------------------------------
def modelo_1(X,Y):    
    a=cuadMin(X,np.log(Y))

    a[0]=np.exp(a[0])
    print("error con a de cuadrados minimos",cuad_Norma_r(a,r_1(X,Y)))
    print("parametros obtenidos por cuadrados minimos",a)
    X1=np.r_[200:4000]
    Y_cuadMin=a[0]*np.exp(-a[1]*X1) # valores obtenidos con cuadrados minimos
    a=gnewton(a,jacobiano_1(X,Y),grad_cuadNorma_r(X,Y),r_1(X,Y),(10**(-10)))
    print("error con a de gauss-newton",cuad_Norma_r(a,r_1(X,Y)))
    print("parametros obtenidos por gauss-newton",a)
    print("norma del gradiente de 1/2*|r|^2 ",np.linalg.norm(grad_cuadNorma_r(X,Y)(a,r_1(X,Y))))
    Y_gnewton=a[0]*np.exp(-a[1]*X1)#valores obtenidos con gauss_newton
    return X1,Y_cuadMin,Y_gnewton

X_A=np.array([200,400,800,1200,1600,2000,3000,4000])
Y_A=np.array([0.65,0.46,0.34,0.26,0.17,0.15,0.06,0.04])
X_B=np.array([200,400,800,1200,1600,2000,3000,4000])
Y_B=np.array([0.63,0.5,0.3,0.24,0.19,0.12,0.08,0.05])


print("-----------------ciudad A------------------\n")
X,Y_B_cuadMin,Y_B_gnewton=modelo_1(X_B,Y_B)
print("-----------------ciudad B------------------\n")
X,Y_A_cuadMin,Y_A_gnewton=modelo_1(X_A,Y_A)

#armo los gráficos de las curvas con cuadrados minimos y gauss-newton
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(X_A,Y_A,"o",color="green")
ax[0].plot(X,Y_A_cuadMin,"blue")
ax[0].plot(X,Y_A_gnewton,"red")
ax[0].set_title("ciudad A")
blue_patch= mpatches.Patch(color='blue', label='cuadrados minimos')
red_patch = mpatches.Patch(color='red', label='Gauss-Newton')
ax[0].legend(handles=[blue_patch,red_patch])
ax[1].plot(X_B,Y_B,"o",color="green")
ax[1].plot(X,Y_B_cuadMin,"blue")
ax[1].plot(X,Y_B_gnewton,"red")
ax[1].set_title("ciudad B")
blue_patch= mpatches.Patch(color='blue', label='cuadrados minimos')
red_patch = mpatches.Patch(color='red', label='Gauss-Newton')
ax[1].legend(handles=[blue_patch,red_patch])

plt.suptitle(r'$\alpha_0 e^{-\alpha_1 X_i}$')
plt.show()


