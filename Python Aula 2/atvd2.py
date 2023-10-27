# nome1 = input("digite um nome")
# nome2 = input("digite um nome")
# nome3 = input("digite um nome")
# nome4 = input("digite um nome")
# nome5 = input("digite um nome")

# nomes = [nome1, nome2, nome3, nome4, nome5]
# print (nomes)

# lista = []
# for i in range(5):
#     nome = input("digite um nome")
#     lista.append(nome)
# print(lista)

contador = 0
lista=[]
while contador <5:
    nome = str(input("digite um nome"))
    contador = contador + 1
    lista.append(nome)


posicao = int(input("digite uma posicao para adicionar"))
novonome = str(input("digite novo nome"))
lista.insert(posicao, novonome)
print (lista)