Fin = open ( "input.txt" )
P = 1
while True:
  s = Fin.readline()
  if not s: break
  P *= int(s)
Fin.close()
print("reizinajums:",P)
