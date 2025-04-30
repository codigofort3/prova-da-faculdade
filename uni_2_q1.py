# Considere a execução estrita desse código e avalie as seguintes afirmações:
# I – Ao executar o programa, serão exibidos na tela (saída), os valores “2” e “o valor de div é maior ou igual a x”, exatamente nessa ordem.
# II – No cenário atual do código, ao executar o programa, a linha 8 será executada e exibirá na tela o valor “2,5”.
# III – No cenário atual do código, ao executar o programa, a linha 6 será executada e exibirá na tela o valor “o valor de div é maior ou igual a x”.
# É VERDADEIRO o que se afirma em:


#  I e III, apenas.
#  III, apenas.
#  I, apenas.
#  II, apenas.
#  I e II, apenas.

x = 5
div = x // 2

if (div >= (x - 3)):
    print(div)
    print("O valor de div é maior ou igual x ")

else:
    print("div")
    print("O valor de civ é menor que x")
