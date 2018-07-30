import numpy as np
import matplotlib.pyplot as plt
from gradiente import gradiente
from hessiano import hessiano
from funcionalT import braq
   
def newton(a_inicial,f,cant):
    a=a_inicial
    grad=gradiente(f,a)
    hess=hessiano(f,a)
    i=0
    tolerancia=1
    while i<cant:
         print(i,braq(a))
         a=a-np.linalg.solve(hess,grad)
         grad=gradiente(f,a)
         hess=hessiano(f,a)
         #print(hessiano(f,a))
         tolerancia=np.linalg.norm(grad)
         i=i+1
    return a

def graf_braq(N):
    x=np.linspace(0,1,N+2) # para empezar con el otro punto comentar esta linea 
    #y descomentar la que sigue 
    #x=np.linspace(0,1,N+2)[::-1]
    x_min=newton(x[1:N+1],braq,11)
    f=np.linspace(0,1,N+2)[::-1]
    x[1:N+1]=x_min
    fig=plt.figure()    
    ax = fig.gca()
    ax.set_xticks(np.arange(0, 1.1, 0.1))
    ax.set_yticks(np.arange(0, 1.1, 0.1))
    plt.plot(x,f,'.r-')
    plt.grid()
    plt.title("BRAQUISTOCRONA: newton")
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.savefig('curva_newton.png')#comentar esto si no queres guardar el grafico
    plt.show()
graf_braq(30)



