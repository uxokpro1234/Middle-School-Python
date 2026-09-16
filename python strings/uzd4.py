#1var
def zeroOrone(a):
  if  (a%10) == 0 or (a%10) == 1: return "jā"
  else:return "nē"
variable = int(input("Input variable "))
rez = zeroOrone(variable)
print("Rezultāts:",rez)


#2var
def atbilde(N):
  N = N % 10
  atb="nē"
  if N == 0 or N == 1:
    atb="jā"
  return atb
N = int(input("Ievadiet veselu skaitli "))
print("skaitļa  ", N, "decimālais ieraksts beidzas ar skaitli 0 vai 1? ", atbilde(N))
