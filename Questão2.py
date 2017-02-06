# Importação do módulo random, precisamos fazer isso para podermos utilizar as funçôes do modelo em questão
import random
# A função seed serve para inicializar o gerador de números aleatórios.
random.seed()
# Sortear um número de 1 à 10
sorteio = random.randint(1,10)
# Uma váriável para mostrar ao computador por onde começar a execução do programa
contador = 0
# O laço de repetição while irá repetir um bloco de instrução enquanto a condição definida em seu cabeçalho seja verdadeira; no caso dessa irá repetir 3 vezes consecutivas
while (contador < 3): #poderia utilizar o for
# Pedir ao usuário que informe um número de 1 a 10
 num = input ("Informe um Número de 1 a 10: ")
# Condição definida pelo while
 contador = contador + 1
# Usando o if para verificar se o número´informado pelo usuário é igual ao sorteio
 if (num == sorteio):
   print("O Numero Sorteado foi: ",sorteio)
   print("Parabéns você Acertou!")
# A instrução break finalizará a iteração e continuará a execução normalmente
   break
# A instrução else é uma instrução dependente, isto é, uma instrução que não pode ser utilizada sozinha; e se as condições acima não forem verdadeiras, o programna executará o que está dentro de 'else'
 else:
   print("Que Pena, o Número Sorteado Foi: ", sorteio)
   print("Tente Novamente")
   
'''
Portanto, este programa tem como finalidade pedir ao usuário que insira/informe um número de 1 á 10, como em um jogo de adivinhação por exemplo, e mostrar ao usuário se ele conseguiu adivinhar o número aleatório que foi sorteado pelo computador. Sendo assim, podemos observar um erro no programa, pois ele pede para o usuário informar 3(três) vezes o número, sendo que o sorteado é o mesmo.
'''
