function [L,U]=lu_sinpivot(A)
  n=size(A,1)
  L=eye(n)
  for k=1:n-1
    L(k+1:n,k)=A(k+1:n,k)/A(k,k)
    for l=k+1:n
      A(l,:)=A(l,:)-L(l,k)*A(k,:)
    end
  end
  U=A
    