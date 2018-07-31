function u=calor(hx,ht,a,g,tf)
% resuelve la ecuacion del calor u_t=a*u_xx, condicion inicial g y bordes 0
%  grafica una pelicula con la evolucion de la solucion
  t=0:ht:tf;
  x=0:hx:1;
  r=a*ht/(hx**2);
  N=size(x)(2);
  M=size(t)(2);
  a1=r*ones(N-3,1);
  a2=1-2*r*ones(N-2,1);
  A1=diag(a1,-1);
  A2=diag(a2,0);
  A3=diag(a1,1);
  A=A1+A2+A3;
  u=zeros(N,M);
  u(:,1)=g(x);
  u(1,:)=0;
  u(N,:)=0;
  plt=plot(x,u(:,1));
  xlim([0,1]);
  ylim([0,1]);
  drawnow
  for j=2:M
    u(2:N-1,j)=A*u(2:N-1,j-1);
    plot(x,u(:,j));
    xlim([0,1]);
    ylim([0,1]);
    drawnow
  endfor
end
  
