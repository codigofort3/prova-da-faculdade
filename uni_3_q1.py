# Considere a execução estrita desse código e leve em consideração que o usuário do programa irá digitar dados de entrada de forma esperada, ou seja, para sexo o usuário irá digitar somente os caracteres M ou H (maiúsculo ou minúsculo) e para idade, irá digitar números inteiros positivos. Nesse cenário, avalie as seguintes afirmações:

# I – Na linha 6, a instrução da função “range” está incorreta.

# II – Não será exibido nenhum resultado, pois há algum erro de sintaxe em uma ou mais linhas do código e o programa não irá executar.

# III – Ao finalizar as repetições, serão exibidos os valores contidos nas variáveis “qtdMulheres” e “qtdHomens”.

# É VERDADEIRO o que se afirma em:


#  I, apenas.


#  II e III, apenas.


#  I e II, apenas.


#  II, apenas.


#  III, apenas.

sexo = " "
idade = 0
qtdMulheres = 0
qtdHomens = 0

for i in range(0,5):
    sexo = input("Digite o sexo:  (H ou M) :")
    idade = int(input("Digite a idade:  "))
    
    if(sexo == "M" or sexo == "m"):
        qtdMulheres += 1
        
    elif(sexo == "H" or sexo == "h"):
        qtdHomens += 1
        
print("A quantidade de mulheres é", qtdMulheres)
print("A quantidade de homens é" , qtdHomens)
    
#Resposta:
# III – Ao finalizar as repetições, serão exibidos os valores contidos nas variáveis “qtdMulheres” e “qtdHomens”.
# É VERDADEIRO o que se afirma em: