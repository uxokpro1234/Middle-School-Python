from random import randint
N = 10     # masīva lielums
A = [0]*N  # piešķirt atmiņu
def mas(N):
 for i in range(N):
   A[i] = randint(10,90)
def uzmin(N):
  B = int(input("Uzminējāt ciparu no masīva diapazonā [10,90] ")) 
  K=0
  for i in range(N):
    if A[i]==B:
      print ("Masīvā ir tāds cipars ",B,sep="") 
      K=1
  if K==0:
     print ("Masīvā nav tādu ciparu ",B,sep="") 
def printmas(N):  
  for i in range(N):
     print("A[", i, "]=", sep="", end="")
     print (A[i]) 
mas(N)
uzmin(N)
printmas(N)
