from descenso_braq import descenso
from grad_funcionalT import grad_braq
from funcionalT import braq
import numpy as np
import matplotlib.pyplot as plt
from gradiente import gradiente
#comparo el gradiente analitico con el numerico
for i in range(100):
	x=10*np.random.random_sample((4,))
	res=grad_braq(x)
	res2=gradiente(braq,x)
	print(res,res2,"\n")

	
