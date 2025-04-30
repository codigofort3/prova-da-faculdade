# Considere a execução estrita desse código e de que o usuário do programa, irá digitar os seguintes números: 5, 8 e 9, nessa exata ordem. Nesse cenário, avalie as seguintes afirmações:

# I – O número de repetições executadas pelo for será 3.

# II – Na linha 3, a sequência de códigos acarretará um erro.

# III – Ao finalizar as repetições, será exibido na tela o resultado “22”.

# É VERDADEIRO o que se afirma em:


#  I e III, apenas.


#  II e III, apenas.


#  I, apenas.


#  II, apenas.


#  III, apenas.

valor = 0
for i in range(3):
    valor = float(input("Digite um valor: "))
    
print(valor)
