aa = ["Gulbis", "Zoss", "Rubenis", "Pīle","BalodiS", "Gārgale"]
B = input("Uzminēt putnu no  masīva ") 
N=len(aa)
def a(N):
  K=0
  for i in range(N):
    if aa[i]==B:
      print ("Masīvā ir tāds putnis ",B,sep="") 
      K=1
  if K==0:
     print ("Masīvā nav tādu putnu ",B,sep="")
    
def b(N):
  for i in range(N):
    print("A[", i, "]=", sep="", end="")
    print(aa[i]) 

a(N)
b(N)
