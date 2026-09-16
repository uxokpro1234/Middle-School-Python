def count(x):
  result = 0
  
  while x != 0:
    result += 1
    x = x // 10  
  return result

number = int(input("Ievadiet skaitli "))
l = count(number)
print(number, "Ciparu skaits:", l )
