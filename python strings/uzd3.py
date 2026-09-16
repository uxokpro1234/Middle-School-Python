#https://www.w3schools.com/python/python_strings.asp
#https://www.w3schools.com/python/python_casting.asp
def skaitlis_bin(N):
  rez=bin(N)
  return rez
def skaits(N):
  y = str(N)
  l=len(y)
  v=0
  for i in range(l):
    if y[i]=="1":
      v=v+1 
  return v
N = int(input("Ievadiet veselu skaitli "))
A=skaitlis_bin(N)
print("Skaitļa ", N, "binārais pieraksts ", A)
print("Bināro pierakstu ", A, " 1 vienību skaits ir ", skaits(A))

#var2

def countBinaryOnes(num):
  binary_num = bin(num)
  print(binary_num, "- binars skaitlis")
  length = len(binary_num)
  ones = 0
  for i in range(length):
    if binary_num[i] == "1":
      ones += 1
  return(ones)

number = int(input("Ievadiet skaitli: "))
result = countBinaryOnes(number)
print(number, "Binarā vienu skaits = ", result)
