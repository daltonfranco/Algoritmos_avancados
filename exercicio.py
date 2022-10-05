from rich import print

total = 0

n_colunas_inteira = 20
n_linhas_inteira = 20

n_colunas_user = int(input("Quantidade de colunas no teatro: "))
n_linhas_user = int(input("Quantidade de linhas no teatro: "))

preco_cadeira = 100

matriz_teatro = []

for x in range(n_colunas_user):
    matriz_fileira = [] 
    for calica in range(n_linhas_user):
        matriz_fileira.append("L")
    matriz_teatro.append(matriz_fileira)

print(matriz_teatro)

while True:

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

    sair = input("Quer sair -- sim / nao :  ")

    if sair == "sim":
        break
       



print(matriz_teatro)
print(total) 


