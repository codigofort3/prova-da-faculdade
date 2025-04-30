# Considere a execução estrita desse código e leve em consideração que o usuário do programa irá digitar números decimais positivos ou inteiros positivos. Nesse cenário, avalie as seguintes afirmações:

# I – Não será exibido nenhum resultado, pois há algum erro de sintaxe( significa que o código foi escrito de uma forma que não segue as regras da linguagem.) ou falta de alguma instrução em uma ou mais linhas do código.

# II – Ao finalizar as repetições, será exibido o valor contido na variável “média”.

# III – Na linha 8, a sequência de instruções está corretamente calculando a média de notas.

# É VERDADEIRO o que se afirma em:


#  III, apenas.


#  I, apenas.


#  I e III, apenas.


#  II, apenas.


#  II e III, apenas.

# contador = 0
# notas = 0

while contador < 6:
    notas = float(input("Digite a nota do aluno: "))
    
media = notas / contador
print(f"A média de notas é : ,{media}")

#Resposta:
#  I, apenas.
#O problema está na linha que calcula a média:
# media = notas / contador
# O valor da variável contador nunca é incrementado dentro do while, então ele permanece 0. Como qualquer divisão por zero resulta em erro, a execução do programa falhará nesse ponto.



# Abaixo o código executado de maneira correta




# contador = 0
# soma_notas = 0  # Variável para armazenar a soma das notas

# while contador < 6:
#     nota = float(input("Digite a nota do aluno: "))
#     soma_notas += nota  # Somando as notas
#     contador += 1  # Incrementando contador

# media = soma_notas / contador  # Calculando a média corretamente
# print(f"A média de notas é: {media:.2f}")