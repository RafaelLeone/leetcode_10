# https://leetcode.com/problems/two-sum/

# Input: 
nums = [2, 7, 9]
target = 9
# Output: [0,1]
# Explicação: Porque nums[0] + nums[1] == 9, retorna-se [0, 1].

from typing import List

#Copiar a partir daqui dentro do Class Soltuion no site:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dicionario_de_numeros = {}
    resultado = []

    for posicao, numero_dado in enumerate(nums):
        if numero_dado not in dicionario_de_numeros.keys():
            dicionario_de_numeros[numero_dado] = [] #porque tem número que vão aparecer/repetir em mais de uma posição.
        dicionario_de_numeros[numero_dado].append(posicao)
        numero_que_precisa = target - numero_dado
        if posicao > 0: #porque não quero que ele some o primeiro duas vezes.
            if numero_que_precisa in dicionario_de_numeros.keys():
                resultado.append(dicionario_de_numeros[numero_que_precisa][0])
                if len(dicionario_de_numeros[numero_que_precisa]) > 1:
                    dicionario_de_numeros[numero_que_precisa].pop(0) #trata casos dos números que aparecem/repetem em mais de uma posição.
                resultado.append(dicionario_de_numeros[numero_dado][0])
                if resultado[0] == resultado[1]:
                    resultado.pop(0)
                    continue
                if len(resultado) > 2:
                    resultado.pop(0)
                break

    return resultado
#Não copiar no site:
print(twoSum(..., nums, target))
