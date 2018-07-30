
def armijo(g,M=1,delta=10**(-5),beta=7/8):#recive una funcion g(a)=f(x+a.d)
	#los parametros delta y beta los eleji arbitrariamente, minimizo bien con esos
    a=M
    derivada=(g(0.001)-g(0))/0.001
    g0=g(0)
    if (g0-g(a))>=-delta*a*derivada:
        return a
    else:
        i=0
        while (g0-g(beta*a))<-delta*beta*a*derivada:
            beta=beta**2
            #print(i,beta*a)
            i=i+1
        return beta*a
			

	
