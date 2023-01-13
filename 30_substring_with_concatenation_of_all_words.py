# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# Input: 
palheiro = "barfoofoobarthefoobarman"
palavras = ["bar","foo","the"]
# Output: [0,9]
# Explicação: words.length == 2 e words[i].length == 3, a substring concatenada deve ser de tamanho 6.
# A substring que começa em 0 é "barfoo". É a concatenação de ["bar","foo"] que é uma permutação de palavras.
# A substring que começa em 9 é "foobar". É a concatenação de ["foo","bar"] que é uma permutação de palavras.
# A ordem do output não importa. Retornar [9,0] está bom também.

from itertools import permutations


permutacoes = permutations(palavras)
agulhas = []
posicoes = []

for permutacao in permutacoes:
    substring = ''
    for elemento in permutacao:
        substring += elemento
    agulhas.append(substring)

for agulha in agulhas:
    TAMANHO_AGULHA = len(agulha)

    for posicao, caracter in enumerate(palheiro):
        contador_de_posicoes_iguais = 0
        try:
            for i in range(posicao, posicao+TAMANHO_AGULHA):
                if palheiro[i] != agulha[i-posicao]:
                    continue
                else:
                    contador_de_posicoes_iguais += 1
            if contador_de_posicoes_iguais == TAMANHO_AGULHA:
                if posicao not in posicoes:
                    posicoes.append(posicao)
        except:
            break

posicoes.sort()
print(posicoes)
