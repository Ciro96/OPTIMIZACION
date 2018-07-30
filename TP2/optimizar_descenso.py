from funcionalT import braq
import numpy as np
import matplotlib.pyplot as plt

from descenso_braq import descenso

def optimizar_braq(x0,cant,busque=None):

	#Parámetros:--------------------------------------------------------
	#	x0=punto inicial,cant=cantidad de iteraciones,
	#	busque="armijo","wolfe" o "aurea"
	#
	#Resultado:
	#	(x minimo,braq(x))
	#-------------------------------------------------------------------		

    if busque==None:
        x_min,braq_min=descenso(braq,x0,cant)
    else:
        x_min,braq_min=descenso(braq,x0,cant,busqueda=busque)
    return x_min,braq_min
   
def grafico_iteracion(N,punto_inicial,busqueda=None):
	
	#Parámetros:--------------------------------------------------------
	#	N=cantidad de puntos,punto_inicial es 1 si empiezo con x0 equiespaciado
	#busqueda="armijo","wolfe" o "aurea"
	#
	#Resultado:
	#	gráfico de (iteraciones,valor de la braquistocrona en el minimo)
	#-------------------------------------------------------------------
	
    iteraciones=np.linspace(0,2000,11)
    x=np.linspace(0,1,N+2)
    if punto_inicial==1:
        braquistocrona=[braq(x[1:N+1])]
        x_0=x[1:N+1]
    else:
        braquistocrona=[braq(x[1:N+1][::-1])]
        x_0=x[1:N+1][::-1]
    for i in range(10):

        x_min,braq_min=optimizar_braq(x_0,200,busqueda)
        braquistocrona.append(braq_min)
        x_0=x_min
    fig=plt.figure()    
    ax = fig.gca()
    ax.set_xticks(np.arange(0,2200, 200))
    if punto_inicial==1:
        ax.set_yticks(np.arange(0.58, 0.64, 0.005))
    else:
        ax.set_yticks(np.arange(0.58, 3.17, 0.1))
    plt.plot(iteraciones,braquistocrona,'.r-')
    plt.grid()
    plt.title(busqueda)
    plt.xlim([0,2000])
    if punto_inicial==1:
        plt.ylim([0.58,0.64])
    else:
        plt.ylim([0.58,3.17])
    
    plt.xlabel("k")
    plt.ylabel(r"$T(X_k)$")
    print(iteraciones,braquistocrona)
    #plt.show() muestra el grafico
    if punto_inicial==1:
        plt.savefig('{}{}'.format('grafico',busqueda))#guarda el grafico
    else:
        plt.savefig('{}{}'.format('grafico2',busqueda))

  

def curva_braq(cant_p,cant_iter,punto_inicial,busqueda=None):
	
	#Parámetros:--------------------------------------------------------
	#	cant_p=cantidad de puntos,cant_iter=cantidad de iteraciones
	#	punto_inicial es 1 si empiezo con x0 equiespaciado, busqueda="armijo","wolfe" o "aurea"
	#
	#Resultado:
	#	grafico de la curva braquistocrona
	#-------------------------------------------------------------------
	
    x=np.linspace(0,1,cant_p +2)
    if punto_inicial==1:
        x_min,braq_min=optimizar_braq(x[1:cant_p +1],cant_iter,busqueda)
    else:
        x_min,braq_min=optimizar_braq(x[1:cant_p +1][::-1],cant_iter,busqueda)
    f=np.linspace(0,1,cant_p +2)[::-1]
    x[1:cant_p+1]=x_min
    fig=plt.figure()    
    ax = fig.gca()
    ax.set_xticks(np.arange(0, 1.1, 0.1))
    ax.set_yticks(np.arange(0, 1.1, 0.1))
    plt.plot(x,f,'.r-')
    plt.grid()
    plt.title("BRAQUISTOCRONA: " + busqueda)
    plt.xlim([0,1])
    plt.ylim([0,1])
    if punto_inicial==1:
        plt.savefig('{}{}{}'.format('curva_',cant_iter,busqueda))
    else:
        plt.savefig('{}{}{}'.format('curva2_',cant_iter,busqueda)) #guarda el grafico
	#plt.show() esta linea muestra el gráficos

    

#creo y guardo todos los gráficos con x0=linspace(0,1,N+2)[1:N+1]
curva_braq(5,200,1,"aurea")
curva_braq(30,2000,1,"aurea")
curva_braq(5,200,1,"wolfe")
curva_braq(30,2000,1,"wolfe")
curva_braq(5,200,1,"armijo")
curva_braq(30,2000,1,"armijo")
grafico_iteracion(30,1,"aurea")
grafico_iteracion(30,1,"armijo")
grafico_iteracion(30,1,"wolfe")
#creo y guardo todos los gráficos con x0=linspace(0,1,N+2)[1:N+1][::-1]
curva_braq(5,200,2,"aurea")
curva_braq(30,2000,2,"aurea")
curva_braq(5,200,2,"wolfe")
curva_braq(30,2000,2,"wolfe")
curva_braq(5,200,2,"armijo")
curva_braq(30,2000,2,"armijo")
grafico_iteracion(30,2,"aurea")
grafico_iteracion(30,2,"armijo")
grafico_iteracion(30,2,"wolfe")

