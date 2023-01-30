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
string = "MCMXCIV"
# Output: 1994
# Explicação: M = 1000, CM = 900, XC = 90 and IV = 4.

#Copiar a partir daqui dentro do Class Solution no site em Python3:
def romanToInt(self, s: str) -> int:

        simbolo_x_valor = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
        soma = 0

        for indice, simbolo in enumerate(s):
            soma += simbolo_x_valor[simbolo]
            if simbolo != 'I' and indice > 0: #caso em que o anterior é menor.
                simbolo_anterior = s[indice-1] #só a partir da segunda posição é possível comparar com o anterior.
                if simbolo_x_valor[simbolo_anterior] < simbolo_x_valor[simbolo]: #na soma romana, se o anterior for menor, preciso subtraí-lo.
                    soma -= simbolo_x_valor[simbolo_anterior]*2 #faço duas vezes porque preciso tirar o que acrescentei na linha 21 também.

        return soma
#Não copiar para o site:
print(romanToInt(..., string))
