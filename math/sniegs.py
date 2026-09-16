sniega_cena = float(input("Ievadiet sniega cenu "))
sniega_uz_kg=float(input("Ievadiet cik daudz sniega vajag uz kg "))
saldejumu_svars=float(input("Ievadiet cik daudz saldejumu kg "))
if (sniega_cena >0 and sniega_uz_kg >0 and saldejumu_svars >0):
   izmaksa_kg = sniega_cena * sniega_uz_kg
   maksa= izmaksa_kg * saldejumu_svars
   print(f"Uz {saldejumu_svars} kg saldejuma izmaksas būs {maksa} EUR ")
  
else:
   print("Kļūda datos")
