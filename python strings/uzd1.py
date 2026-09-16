#https://www.w3schools.com/python/python_strings.asp
#https://www.w3schools.com/python/python_casting.asp
def skaitlis_bin(N):
  rez=bin(N)
  return rez
def skaits(N):
  y = str(N)
  l=len(y)
  return l
N = int(input("Ievadiet veselu skaitli "))
A=skaitlis_bin(N)
print("Skaitļa ", N, "binārais pieraksts ", A)
print("Bināro pierakstu ", A, " simbolu skaits binārajā ierakstā ir ", skaits(A))


#var2
def countBinaryDigits(num):
  binary_num = bin(num)
  print(binary_num, "- binars cipars")
  length = len(binary_num)
  return (length)


number = int(input("Ievadiet skaitli: "))
result = countBinaryDigits(number)
print(number, "Binarā ciparu skaits = ", result)
