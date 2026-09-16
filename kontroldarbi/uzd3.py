from random import randint
N = 10     # masīva lielums
A = [0]*N  # piešķirt atmiņu

def mas(N):
  
 for i in range(N):
   
   A[i] = randint(100,200)
   
def printmas(N):  
  
  print ( "Masīvs:" )
  for i in range ( N ) :
    
    print ( "A[", i, "]=", sep="", end="" )
    print ( A[i], " ", sep="" ) 
    
def printsum ( N ) :
  
  sum = 0
  for i in range ( N ) :
    
   sum = sum + A [ i ] 
  print ( "Masīva elementu summa= ",sum,sep="" )  
  
mas ( N )
printmas ( N ) 
printsum ( N )
