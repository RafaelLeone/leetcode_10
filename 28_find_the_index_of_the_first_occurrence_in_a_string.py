# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Input: 
palheiro = "tristemastriste"
agulha = "triste"
# Output: 0
# Explicação: "triste" aparece nos índices 0 e 6.
# A primeira ocorrência é no índice 0, então o retorno é 0.
# Se a agulha não estiver no palheiro, retorna-se -1.

TAMANHO_AGULHA = len(agulha)
teve_resultado = False

for posicao, caracter in enumerate(palheiro):
    contador_de_posicoes_iguais = 0
    try:
        for i in range(posicao, posicao+TAMANHO_AGULHA):
            if palheiro[i] != agulha[i-posicao]:
                continue
            else:
                contador_de_posicoes_iguais += 1
        if contador_de_posicoes_iguais == TAMANHO_AGULHA:
            print(posicao)
            teve_resultado = True
            exit()
    except:
        break

if not teve_resultado:
    print(-1)
