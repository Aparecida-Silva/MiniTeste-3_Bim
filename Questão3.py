'''
Implemente um jogo que realize o sorteio de um número de 1 até 50 para que o
jogador tente adivinhar o número escolhido em três tentativas. Além disso, o jogo 
deverá fornecer dicas se o número sugerido pelo usuário é maior ou menor que o
número sorteado.
'''

import random
random.seed()
sorteio = random.randint(0, 50)
contador = 3
print("Tente adivinhar o número do sorteio de 1 a 50!")
print("Você tem 3 tentativas!")
print("")
while (contador > 0):
    contador -= 1
    Num = int(input("Informe um número para o sorteio: "))
    if (Num > sorteio):
        print("DICA: O número sorteado é menor!")
        print("      Você tem", contador, "tentativas")
        print("")
    elif (Num < sorteio):
        print("DICA: O número sorteado é maior!")
        print("      Você tem", contador, "tentativas")
        print("")
    else:
        print("Parabéns! Você acertou! O número sorteado é: ", Num)
        contador = -1
if (contador == 0):
    print("")
    print("Que pena! Você perdeu! Não desista, continue tentando!")
    print("O número sorteado era: ", sorteio)
    input("")
elif (contador == -1):
    input()
