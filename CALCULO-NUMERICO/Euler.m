function y=Euler(f,t0,tf,h,y0)
  t=t0:h:tf;
  n=size(t)(2);
  y=zeros(1,n);
  y(1)=y0;
  for i=1:n-1
    y(i+1)=y(i)+h*f(t(i),y(i));
  end
end