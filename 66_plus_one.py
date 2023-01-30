# https://leetcode.com/problems/plus-one/

# Input: 
digits = [1,2,3]
# Output: [1,2,4]
# Explicação: A lista representa o inteiro 123.
# Somando 1 temos: 123 + 1 = 124.
# Então, o output deve ser: [1,2,4].
from typing import List

#Copiar a partir daqui dentro do Class Solution no site em Python3:
def plusOne(self, digits: List[int]) -> List[int]:
    resultado = []
    numero = str(digits).strip('[]')
    numero = numero.replace(',', '')
    numero = numero.replace(' ', '')
    numero = int(numero)+1
    numero = str(numero)
    for algarismo in numero:
        resultado.append(int(algarismo))

    return resultado
#Não copiar para o site:
print(plusOne(..., digits))
