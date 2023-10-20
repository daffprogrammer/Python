#Faça um Programa que verifique se a letra digitada pelo usuário é vogal ou consoante.

letra = input("Digite uma letra: ").lower()

if letra in 'aeiou':
        print("É uma vogal.")
elif letra in "bcdfghjklmmpqrstvwxyz":
        print("É uma consoante.")
else:
        print("letra invalida")


# letra = str(input("Digite uma letra: ")).lower()

# if letra in "aeiou":
#     print(f"{letra} é uma vogal")
# elif letra in "bcdfghjklmnpqrstvxywz":
#     print(f"{letra} é uma consoante")
# else:
#     print("Meu fi, digite uma LEEEEEETRA, conhece o alfabeto tu? ")