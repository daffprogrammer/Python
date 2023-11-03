# Dado O Dicionário pessoa com a seguinte estrutura: {"Nome": "Abel", "Idade": 28, "Altura": 1.79, "Habilitacao": True},
# faça um programa que imprima na tela quantas chaves existem nesse dicionário, e quais os nomes de cada uma delas

pessoa_dicionario = {"Nome": "Abel", "Idade": 28, "Altura": 1.79, "Habilitacao": True}
print(f"O dicionário possui {len(pessoa_dicionario)} chaves")

lista_chaves = list(pessoa_dicionario)

for chave in lista_chaves:
    print(chave)
