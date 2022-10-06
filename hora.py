seg = int(input("Informe os segundos: "))

minutos = 0
horas = 0

if seg//60 == 0:
    minutos += 1 

if minutos//60 == 0:
    horas += 1

print(f"são {horas} horas {minutos} minutos")