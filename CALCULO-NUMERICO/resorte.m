function y=resorte(m,k,h,tf,yf)
#resuelve m(y'')=-k*y
  t=0:h:tf;
  N=size(t)(2)
  a=m*ones(1,N-3);
  b=k*h**2-2*m*ones(1,N-2);
  M1=diag(a,-1);
  M2=diag(a,1);
  M3=diag(b,0);
  A=M1+M2+M3;
  y=zeros(N,1);
  y(N,1)=yf;
  B=zeros(N-2,1);
  B(N-2,1)=-m*yf;
  y(2:N-1,1)=A\B;
  plot(t,y)
end
