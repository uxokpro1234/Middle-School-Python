from random import randint
N = 10     # masīva lielums
A = [0]*N  # piešķirt atmiņu
def mas(N):
 for i in range(N):
   A[i] = randint(50,500)
def printmas(N):  
  print ( "Masīvs:" )
  for i in range(N):
    print("A[", i, "]=", sep="", end="")
    print ( A[i], " ", sep="") 
def avg(N):
  sum=0
  for i in range(N):
   sum=sum+A[i]
  print ("Masīva elementu summa= ",sum,sep="")
  avg=sum/N
  print ("Masīva elementu vidējo aritmētisko vērtība= ",avg, sep="") 
mas(N)
printmas(N)
avg(N)
