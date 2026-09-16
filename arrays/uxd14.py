from random import randint
N = 10     # masīva lielums
A = [0]*N  # piešķirt atmiņu
def mas(N):
 for i in range(N):
   A[i] = randint(10,60)
def printmas(N):  
  print ( "Masīvs:" )
  for i in range(N):
    print("A[", i, "]=", sep="", end="")
    print ( A[i], " ", sep="") 
def reizinajums(N):
  pr=1
  for i in range(N):
     pr=pr*A[i]
  print ("Masīva elementu vērtību reizinājums= ",pr,sep="") 

mas(N)
printmas(N)
