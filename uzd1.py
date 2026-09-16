Fin = open ( "input.txt" )
A = []
while True:
  s = Fin.readline()
  if not s: break
  A.append ( int(s) )
print('Masīvs:',A)
A.sort()
print("Masīvs sortēts:",A)
