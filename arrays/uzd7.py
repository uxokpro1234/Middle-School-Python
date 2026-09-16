N = 10
A = [0] * N
for i in range(N):
  A[i] = pow(2,N-i-1)

print ( "Masīvs:" )
for i in range(N):
  print("A[", i, "]=", sep="", end="")
  print ( A[i], " ", sep="")  
