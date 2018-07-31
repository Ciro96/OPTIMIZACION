function [A]=luFact(A)
n=size(A,1)
  for k=1:n-1
    A(k+1:n,k)=A(k+1:n,k)/A(k,k) #calculo L por filas
    for i=k+1:n
        A(i,k+1:n)=A(i,k+1:n)-A(i,k)*A(k,k+1:n) #calculo U por columnas
    endfor
  endfor

      
#A=[4,-2,1;20,-7,12;-8,13,17]
#luFact(A)
      
    