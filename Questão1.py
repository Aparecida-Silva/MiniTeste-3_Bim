# Importação do módulo random, precisamos fazer isso para podermos utilizar as funçôes do modelo em questão
import random
# A função seed para inicializar o gerador de números aleatórios.
random.seed()
# Sortear um número de 1 à 10
sorteio = random.randint(1, 10)
# Pedir para o usuário informar um número
numero = int(input("Informe o número: "))
# Condição só será executada se o número informado pelo usuário for igual até o determinado número que está dentro do sorteio, no caso 1 até o número 10
if (sorteio == numero):
 print("Parabéns")
# Senão, o programa finalizará e mostrará que errou o número do sorteio
else:
 print("Você errou. Execute o programa novamente")
print("fim")

'''
Portanto, este programa tem como o objetivo de sortear um número de 1 à 10, pedir ao usuário que insira um número, e por fim, mostrar ao usuário se ele acertou o determinado número sorteado pelo computador.
'''
