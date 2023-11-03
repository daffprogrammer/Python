#Dado o Dicionário Animal com a seguinte estrutura: {"Especie": "Cachorro", "Raça": "Pinscher", "Idade": 1, "Adestrado": "Sim"},
#faça um programa que cheque se o cachorro tem mais de 2 anos de idade, se tiver, crie uma nova chave chamada "Vacinado" e atribua o valor de
#verdadeiro, caso contrário, mude o valor da chave "Adestrado" para "Não"

cachorro_dicionario = {"Especie": "Cachorro", "Raça": "Pinscher", "Idade": int(input("digite a idade ")), "Adestrado": "Sim"}

if cachorro_dicionario["Idade"] > 2:
    cachorro_dicionario["Vacinado"] = True
else:
    cachorro_dicionario["Adestrado"] = False

print(cachorro_dicionario)