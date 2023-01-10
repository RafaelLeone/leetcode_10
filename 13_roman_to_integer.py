# https://leetcode.com/problems/roman-to-integer/

# Símbolo       Valor
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Input: 
string = "III"
# Output: 3
# Explicação: III = 3.

simbolo_x_valor = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
soma = 0

for indice, simbolo in enumerate(string):
    soma += simbolo_x_valor[simbolo]
    if simbolo != 'I' and indice > 0: #caso em que o anterior é menor.
        simbolo_anterior = string[indice-1] #só a partir da segunda posição é possível comparar com o anterior.
        if simbolo_x_valor[simbolo_anterior] < simbolo_x_valor[simbolo]: #na soma romana, se o anterior for menor, preciso subtraí-lo.
            soma -= simbolo_x_valor[simbolo_anterior]*2 #faço duas vezes porque preciso tirar o que acrescentei na linha 21 também.

print(soma)