import json

bus1 = {
  "Abrenes iela": "10:00",
  "Vecmilgravis": "11:00"
}

bus2 = {
  "Daugavpils": "10:30",
  "Plavnieki": "11:30"
}

inputt = input("Enter bus stop (Abrenes iela, Daugavpils, Vecmilgravis, or Plavnieki): ")
if inputt in bus1:
  print("Bus 1 arrives at", bus1[inputt])
  
if inputt in bus2:
  print("Bus 2 arrives at", bus2[inputt])

