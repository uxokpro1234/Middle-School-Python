N = int(input("Ievadiet N "))     # lielums
def output(N):
  k=1
  L=""
  while k<N:
    for i in range(k):
      L=L+"o"
      print (L)
    k=k+1
output(N)
print()
