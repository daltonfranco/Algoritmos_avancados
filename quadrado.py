lado = int(input("Qual é o lado do quadrado: "))

def perimetro(lado):
    perimetro = lado*4
    print(f"O perimetro do quadrado é igual a: {perimetro}")

def area(lado):
    area = lado*lado
    print(f"A Área do quadrado é igual a: {area} ")

print()
area(lado)
print()
perimetro(lado)


