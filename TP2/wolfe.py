
from math import inf

def wolfe(g,a=1,delta1=0.001,delta2=0.001):
    b1=0
    b2=inf # b2=infinito
    
    derivada=(g(0.001)-g(0))/0.001
    while (True):
        if (g(a)>g(0)+delta1*a*derivada):
            b2=a
            a=(1/2)*(b1+b2)
            #print(a)
        elif (((g(a+0.001)-g(a))/0.001)<delta2*derivada):
            b1=a
            if (b2 is inf):
                a=2*b1
            else:
                a=(1/2)*(b1+b2)
            #print(a)
        else:
            return a
