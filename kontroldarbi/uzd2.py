N = 10
A = [0] * N

def mas( N ):
  
  print ( "Ievadiet M:" )
  M = int ( input( ) )
  for i in range( N ):
    
    A[i] = M
    M=M+5

def printmas( N ):
  
  print ( "Masīvs:" )
  for i in range(N):
    
    print( "A[", i, "]=", sep="", end="" )
    print ( A[i], " ", sep="" )

mas( N )
printmas( N )

