N = 5
A = [ 0 ] * N

def a ( N ) :
  
  print ( "Ievadiet masīva elementus:" )
  for i in range ( N ) :
    
    print( "A[" , i , "]=" , sep = "" , end = "" )
    A [ i ] = int ( input ( ) )
    
def ez ( N ) :
  
  print ( "Skaitli 3. pakapē :" )
  for i in range ( N ) :
    
    print ( "A[", i , "]=", sep = "" , end = "" )
    print ( pow ( A [ i ] , 3 ) , " " , sep=  "" )

a ( N )
ez ( N )
