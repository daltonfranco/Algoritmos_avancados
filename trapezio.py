base_menor = int(input("Base menor do trapezio: "))
base_maior = int(input("Base maior do trapezio: "))
altura = int(input("Altura do trapezio: "))

def area(base_menor, base_maior, altura):
    area_trap = ((base_maior*base_menor)*altura)/2
    print(f"A area do trapezio é: {area_trap}")

area(base_menor, base_maior, altura)