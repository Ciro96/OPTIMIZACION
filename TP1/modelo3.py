import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from funcionesTP import gnewton


def r_3(a):
    X=np.array([200,400,800,1200,1600,2000,3000,4000])
    Y_1=np.array([0.65,0.46,0.34,0.26,0.17,0.15,0.06,0.04])
    Y_2=np.array([0.63,0.5,0.3,0.24,0.19,0.12,0.08,0.05])
    N=X.size
    res=np.zeros(2*N)
    res[0:N]=a[2]+a[3]+a[0]*np.exp(-a[1]*X)-Y_1
    res[N:2*N]=a[2]+a[0]*np.exp(-a[1]*X)-Y_2
    return res

def cuad_Norma_r(a,r):#cuadrado de la norma de r_2
    return np.dot(r(a),r(a))

def cuad_Norma_r_A(a,r,X_size): #cuadrado de la norma de r_2[0,X.size]
	return np.dot(r(a)[0:X_size],r(a)[0:X_size])
def cuad_Norma_r_B(a,r,X_size):#cuadrado de la norma de r_2[X.size,2*X.size]
	return np.dot(r(a)[X_size:2*X_size],r(a)[X_size:2*X_size])
    
def jacobiano_3(a):# jacobiano de r_3
    X=np.array([200,400,800,1200,1600,2000,3000,4000])
    Y_1=np.array([0.65,0.46,0.34,0.26,0.17,0.15,0.06,0.04])
    Y_2=np.array([0.63,0.5,0.3,0.24,0.19,0.12,0.08,0.05])
    N=X.size
    A=np.ones((2*N,4))
    A[0:N,0]=np.exp(-a[1]*X)
    A[N:2*N,0]=np.exp(-a[1]*X)
    A[0:N,1]=-X*a[0]*np.exp(-a[1]*X)
    A[N:2*N,1]=-X*a[0]*np.exp(-a[1]*X)
    A[N:2*N,3]=np.zeros(N)
    
    return A

def grad_cuadNorma_r(a,r):#gradiente de (1/2)*norma cuadrado de r 
    return np.dot(np.transpose(jacobiano_3(a)),np.transpose(r(a)))


    
X=np.array([200,400,800,1200,1600,2000,3000,4000])
Y_A=np.array([0.65,0.46,0.34,0.26,0.17,0.15,0.06,0.04])
Y_B=np.array([0.63,0.5,0.3,0.24,0.19,0.12,0.08,0.05])

a=gnewton(np.array([0.723,0.00088,0,0]),jacobiano_3,grad_cuadNorma_r,r_3,0.0001)
print("parametros con gauss-newton ",a)
print("error con a de gn",cuad_Norma_r(a,r_3))
print("error en ciudad A",cuad_Norma_r_A(a,r_3,X.size))
print("error en ciudad B",cuad_Norma_r_B(a,r_3,X.size))
print("norma del gradiente de 1/2*|r|^2",np.linalg.norm(grad_cuadNorma_r(a,r_3)))

#armo los gráficos de las curvas con gauss-newton
X1=np.r_[200:4000]
Y_A_gnewton=a[0]*np.exp(-a[1]*X1)+a[2]+a[3]
Y_B_gnewton=a[0]*np.exp(-a[1]*X1)+a[2]
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(X,Y_A,"o")
ax[0].plot(X1,Y_A_gnewton,color="orange")
ax[0].set_title("ciudad A")
orange= mpatches.Patch(color='orange', label='Gauss-Newton')
ax[0].legend(handles=[orange])
ax[1].plot(X,Y_B,"o")
ax[1].plot(X1,Y_B_gnewton,color="orange")
ax[1].set_title("ciudad B")
orange= mpatches.Patch(color='orange', label='Gauss-Newton')
ax[1].legend(handles=[orange])

plt.suptitle(r'$\alpha_0 e^{-\alpha_1 X_i}+\alpha_2 + \alpha_3 Z_i$')
plt.show()

