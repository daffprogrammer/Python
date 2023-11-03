#Dado o conjunto Cores com a seguinte estrutura {"Amarelo", "Azul", "Vermelho", "Verde"}
#faça um programa que peça uma cor ao usuário e guarde essa cor em uma lista, o programa
#pedirá cores ao usuário até ele digitar a palavra chave "sair", quando o usuário sair do 
#programa faça ele inserir todas as cores da lista dentro do conjunto e depois mostrar o conjunto na tela

cores = {"Amarelo", "Azul", "Vermelho", "Verde"}
cores2 = []
while True:
    cor = str(input("digite uma nova cor: "))
    if cor == "sair":
        break 
    cores2.append(cor)
cores.update(cores2)
print(cores)