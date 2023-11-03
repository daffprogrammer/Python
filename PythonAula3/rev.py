#faça um programa que pede para o usuario inserir o nome de um aluno e nota e adicione ele em uma lista até o usuario escrever no lugar do nome a palavra "fim"
#então mostre na tela o nome do aluno que teve a melhor nota

# alunos = []
# while True:
#     nome = input("digite o nome do aluno: ")
#     if nome == "fim":
#         break
#     nota = float(input("digite uma nota: "))
#     aluno = [nome,nota]
#     alunos.append(aluno)
# maior = 0
# nomemaior = ""
# for aluno in alunos:
#     if aluno [1] > maior:
#         maior = aluno[1]

alunos = []
while True:
    nome = str(input("digite o nome do aluno: "))
    if nome == "fim":
        break
    nota = float(input("digite uma nota: "))
    alunos.append([nome,nota])

maior = 0
maiornome = ""
for aluno in alunos:
   if aluno[1] > maior:
      maior = aluno[1]
      maiornome = aluno[0]
print(f"melhor aluno foi {maiornome} com a nota {maior}")