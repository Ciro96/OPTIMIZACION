function [Q,R]=householder(A)
  [m,n]=size(A)
  Q=eye(m)
  
  for k=1:n
    x=A(k:m,k)
    v=sign(x(1,1))*norm(x)*eye(size(x,1),1)+x
    u=v/norm(v)
    A(k:m,k:n)=A(k:m,k:n)-2*u*(u')*A(k:m,k:n)
    Q(:,k:m)=Q(:,k:m)-2*Q(:,k:m)*u*(u')
  endfor
  R=A
endfunction

    
  