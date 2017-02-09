'''
 Construa uma função que receba uma String como parâmetro e devolva outra String
com os caráteres embaralhados. Por exemplo, se função receber a palavra Python, pode
retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
Verifique a utilização das funções sample e/ou shuffle da biblioteca random.
'''
palavra = str(input("Digite uma palavra para embaralhar: "))

import random
def embaralhar(palavra):
    embaralha = random.sample(palavra, len(palavra))
    string = "".join(embaralha)
    print(string)

print("")
print("Palavra embaralhada: ")
embaralhar(palavra)
