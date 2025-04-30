valor = 0
for i is range(0,3):
    valor += float(input("Digite um valor: "))
    
    
media = valor/3
print(media)









# Considere a execução estrita desse código e de que o usuário do programa, irá digitar os seguintes números: 2, 3 e 4 , nessa exata ordem. Nesse cenário, avalie as seguintes afirmações:

# I – A instrução contida da linha 2 está incorreta.

# II – Não será exibido nenhum resultado, pois há algum erro de sintaxe em uma ou mais linhas do código e o programa não irá executar.

# III – Ao finalizar as repetições, será exibido na tela o resultado “3”.

# É VERDADEIRO o que se afirma em:


#  III, apenas.


#  I e II, apenas.


#  II, apenas.


#  II e III, apenas.


#  I, apenas.


#Resposta:
#  I e II, apenas.


#Abaixo o código corrigido

valor = 0
for i in range(0,3):  # Corrigindo "is" para "in"
    valor += float(input("Digite um valor: "))  
    
media = valor / 3
print(media)