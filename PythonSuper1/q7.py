
numero = int(input("Digite um número inteiro positivo: "))

if numero < 1:
    print("Por favor, digite um número inteiro positivo.")
else:
    print(f"Contagem regressiva a partir de {numero}:")

while numero >0:
    print(numero)
    numero = numero - 1
