function [t,y]=EulerVectorial(f,t0,tf,h,y0)
%  modificaion de euler para que acepte ecuaciones vectoriales
  t=t0:h:tf;
  n=size(t)(2);
  y=zeros(n,size(y0)(2));
  y(1,:)=y0;
  for i=1:n-1
    y(i+1,:)=y(i,:)+h*(f(t(i),y(i,:))');
  end
end
