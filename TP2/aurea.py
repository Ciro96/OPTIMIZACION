from math import sqrt
def aurea(g,b=2,N=200,tol=0.005):
    a=0
    GR=(-1+sqrt(5))/2
    x1=GR*(b-a)
    x2=b-GR*(b-a)
    g1=g(x1)
    g2=g(x2)
    i=0
    while  b-a>tol and i<N:
        if g1<g2:
            a=x2
            x2=x1
            x1=a+GR*(b-a)
            g2=g1
            g1=g(x1)
        else:
            b=x1
            x1=x2
            x2=b-GR*(b-a)
            g1=g2
            g2=g(x2)
        i=i+1
    #print("aurea",i,(a+b)/2)
    return (a+b)/2		
