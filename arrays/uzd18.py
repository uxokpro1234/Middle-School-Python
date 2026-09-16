N = int(input("Ievadiet N "))     # lielums
def output(N):
  for i in range(N):
    print ("@", end="")
def output1(N):
  L="@"
  for i in range(N-2):
    L=L+" "
  L=L+"@"
  print (L)
  print()
  print (L)

output(N)
print()
print()
output1(N)
print()
output(N)
print()
