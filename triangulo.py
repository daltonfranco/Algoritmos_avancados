base = int(input("Qual o tamanho da base do triangulo: "))

altura = int(input("Qual é o tamanho da altura do triangulo: "))

def area(base, altura):
    area_tri = (base*altura)/2
    print(f"A area do triangulo é: {area_tri}")

area(base, altura)
