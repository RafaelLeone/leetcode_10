# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Input: 
haystack = "tristemastriste"
needle = "triste"
# Output: 0
# Explicação: "triste" aparece nos índices 0 e 6.
# A primeira ocorrência é no índice 0, então o retorno é 0.
# Se a agulha não estiver no palheiro, retorna-se -1.

#Copiar a partir daqui dentro do Class Solution no site em Python3:
def strStr(self, haystack: str, needle: str) -> int:
        TAMANHO_AGULHA = len(needle)
        for posicao, caracter in enumerate(haystack):
            contador_de_posicoes_iguais = 0
            try:
                for i in range(posicao, posicao+TAMANHO_AGULHA):
                    if haystack[i] != needle[i-posicao]:
                        continue
                    else:
                        contador_de_posicoes_iguais += 1
                if contador_de_posicoes_iguais == TAMANHO_AGULHA:
                    return posicao
            except:
                break

        return -1
#Não copiar para o site:
print(strStr(..., haystack, needle))
