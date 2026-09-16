print ( "Ievadiet virkni, kas satur 0,1, burtus: " )
A=str(input())
sNew = ""
for i in range(len(A)):
  if A[i]=="1":
     sNew +="0"
  elif A[i]=="0":
     sNew += "1"
  else:
    sNew += A[i]
print ( "Virkne līdz apstrādes: ",A )
print ( "Binārais kods, virkne pēc apstrādes: ",sNew )
