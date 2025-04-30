nomes = ("Anna", "Maria", "Fernanda")
nomes.pop()
print(nomes)




# Considere a execução estrita desse código e avalie as seguintes afirmações:

# I – Na linha 2, a sintaxe para excluir um elemento está correta.

# II – Não será exibido nenhum resultado, pois há algum erro de sintaxe em uma ou mais linhas do código e o programa não irá executar.

# III – Ao finalizar da execução do programa, serão exibidos na tela os seguintes valores: “Anna”, “Fernanda” e “Maria”.

# É VERDADEIRO o que se afirma em:


#  I e III, apenas.


#  II, apenas.


#  III, apenas.


# I, apenas.


#  II e III, apenas.

#Respostas:
# II – Não será exibido nenhum resultado, pois há algum erro de sintaxe em uma ou mais linhas do código e o programa não irá executar.


# Explicação do erro:
# A variável nomes foi definida como uma tupla em Python, pois está entre parênteses ().
# - Tuplas são imutáveis, ou seja, seus elementos não podem ser alterados, removidos ou adicionados após a criação.
# - O método .pop() é usado para listas (list), mas não existe para tuplas, o que causará um erro:

# AttributeError: 'tuple' object has no attribute 'pop'


