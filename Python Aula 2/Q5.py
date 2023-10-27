# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO CADASTRAR 5 ALUNOS
# COM NOME E NOTA, E NO FINAL MOSTRA O NOME E NOTA DO ALUNO QUE TIROU A MAIOR NOTA


alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    alunos.append((nome, nota))

maior = 0
nome_maior = ""
for i in alunos:
    if i[1] > maior:
        maior = i[1]
        nome_maior = i[0]
print (f"a maior nota foi {maior} do aluno {nome_maior}")

