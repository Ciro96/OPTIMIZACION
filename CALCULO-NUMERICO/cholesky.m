function [L]=cholesky(A)
  n=size(A);
  L=zeros(n);
  for k=1:n
    L(k,k)=sqrt(A(k,k)-L(k,1:k-1)*L(k,1:k-1)')
    L(k+1:n,k)=(A(k+1:n,k)-L(k+1:n,1:k-1)*L(k,1:k-1)')/L(k,k);
  endfor
endfunction
      