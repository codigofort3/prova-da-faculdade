# Considere a execução estrita desse código e avalie as seguintes afirmações:

# I – No cenário atual do código, ao executar o programa, serão exibidos na tela (saída), os valores “80” e “20”, exatamente nessa ordem.

# II – No cenário atual do código, a variável “desconto” teve o valor “10” atribuído e utilizado como base do cálculo para atualização do valor (cálculo de juros) atribuído para a variável “valorAtualizado”.

# III – No cenário atual do código, ao executar o programa, a linha 16 será executada e exibirá na tela o valor “80”.

# É VERDADEIRO o que se afirma em:


# I, apenas.


#  II, apenas.


#  I e III, apenas.


#  III, apenas.


#  I e II, apenas.

idade = 25
desconto = 0
valor_consumido = 100

if (idade <= 18):
    desconto = 0
    
else:
    if (idade > 18 and idade < 26 ):
        desconto = 10
        
    elif(idade > 25):
        desconto = 20
        
valor_atualizado = valor_consumido - (valor_consumido * desconto / 100)

print(valor_atualizado)
print(desconto)

#Resposta:
# II – No cenário atual do código, a variável “desconto” teve o valor “10” atribuído e utilizado como base do cálculo para atualização do valor (cálculo de juros) atribuído para a variável “valorAtualizado”.
