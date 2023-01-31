# https://leetcode.com/problems/permutation-sequence/

# Input: 
n = 3
k = 3
# Output: "213"
# Explicação: n igual a 3, então temos uma lista de 1 a 3.
# 123 e 132 são as duas primeiras combinações possíveis.
# Como k é igual a 3, retornamos a terceira combinação possível.
from itertools import permutations

#Copiar a partir daqui dentro do Class Solution no site em Python3:
def getPermutation(self, n: int, k: int) -> str:
    resultado = ''
    possibilidades = permutations(list(range(1, n+1)))
    for index, permutacao in enumerate(list(possibilidades)):
        if index == (k - 1):
            for numero in permutacao:
                resultado = resultado + str(numero)
            return resultado
#Não copiar no site:
print(getPermutation(..., n, k))
