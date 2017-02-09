# Criando listas com as seguintes váriaveis
qtPrest = []
listaVc = []
# Auxiliador com várivel ct para iniciar uma contagem a partir do número 0
ct = 0
#Função "VP", incluindo dois parâmetros dentro dele
def funcVP(VP, NumDias):
# Cálculos para saber o número de dias em atraso; prestações...
  Vpm = VP * 1.03
  valorC = round(Vpm *((1 + 0.001) ** NumDias), 2)
# O método append () anexa um passado objeto a ser acrescentado na lista existente, nesse caso acrescentará o "valorC" a "listaVc"
  listaVc.append(valorC)
  print('Valor corrigido:', valorC)
  global ct
  ct += 1
  qtPrest.append(ct)
# Função menu criada para que o usuário escolha um item e com base na escolha o programa execute um dado bloco de código, porem o programa é quem define as opções do menu, quantos itens vão ter, qual nome dos itens, etc.. 
def menu():
  # Condição de repetição caso for verdadeira
  while True:
    VP = float(input('Digite o valor da prestação: (0 para sair) '))
    # Se o Valor do Pagamento (VP) for igual 0, então será utilizado a instrução break
    if VP == 0:
      # A instrução break finalizará a iteração e continuará a execução normalmente
      break
    NumDias = int(input('Quantos dias que está em atraso: ')
    funcVP(VP, NumDias)
# Agora vamos imprimir e fazer ainda mais digitação de variáveis
print('Quantidade de prestações pagas: ', ct)
print('Valor total de prestações pagas no dia: R$', round(sum(listaVc)), 2)

def main():
 # Início da aplicação
 menu()
if __name__ == "__main__":
 main()
 
'''
 Finalidade do Programa:
 Este programa tem como finalidade utilizar a função valorPagamento (funcVP) para determinar
 o valor a ser pago por uma prestação de uma conta. O programa solicita ao usuário o valor
 da prestação e o número de dias em atraso e passa estes valores para a função valorPagamento,
 que calcula o valor a ser pago e devolve este valor ao programa que a chamou. O programa
 então exibi o valor a ser pago na tela. Após a execução o programa volta a pedir outro valor
 de prestação e assim continua até que seja informado um valor igual a zero para a prestação.
 Neste momento o programa é encerrado, exibindo o relatório do dia, que contem a quantidade e 
 o valor total de prestações pagas no dia.
'''
 
print("")
 
'''
 Importância do método main:
 Em Python, na minha opinião, não é tão preciso definir a função/método main. Mas funciona da
 seguinte forma: quando um módulo é executado (seja por importação, por exemplo), a variável
 interna __name__ é inicializada com o nome do módulo. Se ele foi importado, __name__ é o nome
 do módulo; se ele foi invocado, __name__ possui a string "__main__" como valor. Logo, queremos
 executar o código apenas se __name__ é igual a "__main__". Ou seja, "main" é a função
 principal do programa. Quando o programa for executado ele irá, na verdade, chamar a função
 main.
'''
 
