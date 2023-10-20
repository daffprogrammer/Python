# Solicitar ao usuário uma frase
frase = input("Digite uma frase: ")

contador_vogais = 0

for letra in frase:
    if letra in "aeiou":
        contador_vogais += 1

print (contador_vogais)

