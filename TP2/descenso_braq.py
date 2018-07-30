import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
from armijo import armijo #mi line search
from wolfe import wolfe
from gradiente import gradiente
from aurea import aurea
from funcionalT import braq
    

def descenso(f,x0,cant,grad=None,busqueda=None):
    x=x0
    i=0
    if grad==None: # elijo gradiente numerico o analitico
        d=gradiente(f,x)
    else:
        d=grad(x)
    while i<cant:
        #print(i,braq(x))
        g=lambda a:f(x-a*d)
        if busqueda==None: # elijo el tipo de busqueda lineal
            t=scipy.optimize.fmin(func=g,x0=0)
        elif busqueda=="armijo":
            t=armijo(g)
        elif busqueda=="wolfe":
            t=wolfe(g)
        elif busqueda=="aurea":
            t=aurea(g)
        x=x-t*d
        if grad==None:
            d=gradiente(f,x)
        else:
            d=grad(x)
        i=i+1
    #print(i,braq(x))
    return x,braq(x)

