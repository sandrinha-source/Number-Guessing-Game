num = int(input("Digite um número de 0 a 100: "))

while num < 0 or num > 100:
    print("Número inválido! Digite um número de 0 a 100")
    num = int(input("Digite um número de 0 a 100: "))

palpite = int(input("Tente adivinhar o número que o outro usuário digitou: "))

while palpite < 0 or palpite > 100:
    print("Número inválido! Digite um número de 0 a 100: ")
    palpite = int(input("Tente adivinhar o número que o outro usuário digitou: "))

while palpite != num:
    if palpite > num:
        print("Errou, o número é menor.")
        palpite = int(input("Tente adivinhar o número que o outro usuário digitou: "))
    else:
        print("Errou, o número é maior.")
        palpite = int(input("Tente adivinhar o número que o outro usuário digitou: "))

print("Parabéns, você acertou!")