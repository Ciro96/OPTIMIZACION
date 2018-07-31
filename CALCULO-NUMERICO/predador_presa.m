f=@(t,x)[2*x(1)-x(1)*x(2);-3*x(2)+2*x(1)*x(2)]
%  grafico del sistema predador-presa
x0=[3/2,2]
[t,y]=EulerVectorial(f,0,10,0.025,x0)
plot(y(:,1),y(:,2))  
