def verifica(x):
    nome = x
    if nome in lista:
        return "Possui - ", nome
    else:
        return "Não possui, veja: ", lista

lista = []

for i in range (5):
    nome = input("Digite um nome: ")
    lista.append(nome)
    
print(verifica(input("Qual nome deseja verificar: ")))