nomes = ("Anna", "Fernanda", "Maria")
nomes.append('Lucas')
print(nomes)




# Considere a execução estrita desse código e avalie as seguintes afirmações:

# I – Não será exibido nenhum resultado, pois há algum erro de sintaxe em uma ou mais linhas do código e o programa não irá executar.

# II – Na linha 2, a sintaxe para adicionar um elemento está correta.

# III – Ao finalizar da execução do programa, serão exibidos na tela os seguintes valores: “Anna”, “Fernanda”, “Maria” e “Lucas”.

# É VERDADEIRO o que se afirma em:


#  I, apenas.
#  II, apenas.
#  II e III, apenas.
#  III, apenas.
#  I e III, apenas.

# Resposta:
# I – Não será exibido nenhum resultado, pois há algum erro de sintaxe em uma ou mais linhas do código e o programa não irá executar.

#Explicação do erro:
# A variável nomes foi definida como uma tupla em Python, pois está entre parênteses ().
# - Tuplas são imutáveis, ou seja, seus elementos não podem ser alterados ou adicionados após a criação.
# - O método .append() é usado para listas (list), mas não existe para tuplas, o que causará um erro:

# AttributeError: 'tuple' object has no attribute 'append'


