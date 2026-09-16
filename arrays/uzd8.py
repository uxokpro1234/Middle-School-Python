#A = input("")
A=input("uzvards, vards: ")
x = A.find(" ")
s = A[x+1]+ ". " + A[0 : x]
print(s)
