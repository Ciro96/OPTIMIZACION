% resuelve y´=y y(0)=1 para aproximar y(1) y compara errores para distintos pasos h
tf=1;
y0=1;
t0=0;
h=0.025:0.01:0.1;
m=size(h)(2);
error=zeros(1,m);
for k=1:m
  t=t0:h(k):tf;
  n=size(t)(2);
  y=zeros(1,n);
  y(1)=y0;
  for i=1:n-1
    y(i+1)=y(i)+h(k)*y(i)+(h(k)**2/2)*y(i);
  end
  error(k)=abs(exp(tf)-y(n));
end
subplot(2,2,1)
plot(h,error)
subplot(2,2,2)
plot(log(h),log(error))
subplot(2,2,3)
plot(t,y)
subplot(2,2,4)
plot(t,exp(t))
