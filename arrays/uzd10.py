N=5
A = [0]*N
def find (a):
  n = a[0]
  for i in range(N):
    if a[i] > n:
      n = a[i]
    return a

result = find([2,5,1,8,4])
print(result)
