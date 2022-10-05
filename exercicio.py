from rich import print
import math

total = 0

n_colunas_user = int(input("Quantidade de colunas no teatro: "))
n_linhas_user = int(input("Quantidade de linhas no teatro: "))

preco_cadeira = 100

matriz_teatro = []

for x in range(n_colunas_user):
    matriz_fileira = [] 
    for adenor in range(n_linhas_user):
        matriz_fileira.append("L")
    matriz_teatro.append(matriz_fileira)

print(matriz_teatro)

print()


while True:

    print("O preço de cada cadeira é 100 reais")

    print()

    print("Qual acento deseja: ")

    fileira = int(input("fileira: ")) - 1
    coluna = int(input("coluna: ")) - 1

    erro = fileira > n_linhas_user or coluna > n_colunas_user 
    if erro:
        input("ERRO")

    else:
        if matriz_teatro[fileira][coluna] == "L":

            cond = input("Esta cadeira está LIBERADA, deseja ALUGAR ou COMPRAR: ")
            if cond == "comprar":
                total += preco_cadeira
                matriz_teatro[fileira][coluna] = "V"
            elif cond == "alugar":
                total += preco_cadeira * 0.3
                matriz_teatro[fileira][coluna] = "A"
        
        elif matriz_teatro[fileira][coluna] == "V":
            print("Esta cadeira está comprada, não é possivel alugar e nem comprar")
        
        elif matriz_teatro[fileira][coluna] == "A":
            print("Esta cadeira está alugada!")
            print("Neste caso, voce pagará 70% do valor total da cadeira.")

            cond_2 = input("Deseja comprala? sim/nao:  ")

            if cond_2 == "sim":
                total += preco_cadeira * 0.7
                matriz_teatro[fileira][coluna] = "V"
            



            




    print(f"Sua carteira é igual a: {total}")

    print()

    sair = input("Quer sair -- sim / nao :  ")

    if sair == "sim":
        cont = 0
        for x in range(n_linhas_user):
            for y in range(n_colunas_user):
                if(matriz_teatro[x][y] != "L"):
                    cont += 1

        qtd_minima = math.floor((n_colunas_user * n_linhas_user) / 2) + 1
        if cont >= qtd_minima:    
            break
       
        input("Não é possível fechar o teatro agora. Você não atingiu 50% + 1 de cadeiras vendidas/alugadas")

print(matriz_teatro)
print(total) 


