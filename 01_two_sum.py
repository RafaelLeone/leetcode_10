# https://leetcode.com/problems/two-sum/

# Input: 
numeros_dados = [2,7,11,15]
soma_esperada = 9
# Output: [0,1]
# Explicação: Porque numeros[0] + numeros[1] == 9, retorna-se [0, 1].

dicionario_de_numeros = {}
resultado = []

for posicao, numero_dado in enumerate(numeros_dados):
    if numero_dado not in dicionario_de_numeros.keys():
        dicionario_de_numeros[numero_dado] = [] #porque tem número que vão aparecer/repetir em mais de uma posição.
    dicionario_de_numeros[numero_dado].append(posicao)
    numero_que_precisa = soma_esperada - numero_dado
    if posicao > 0: #porque não quero que ele some o primeiro duas vezes.
        if numero_que_precisa in dicionario_de_numeros.keys():
            resultado.append(dicionario_de_numeros[numero_que_precisa][0])
            if len(dicionario_de_numeros[numero_que_precisa]) > 1:
                dicionario_de_numeros[numero_que_precisa].pop(0) #trata casos dos números que aparecem/repetem em mais de uma posição.
            resultado.append(dicionario_de_numeros[numero_dado][0])
            break

print(resultado)
