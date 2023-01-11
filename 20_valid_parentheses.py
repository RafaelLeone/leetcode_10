# https://leetcode.com/problems/valid-parentheses/

# Input: 
string = "({([])}()[]{})"
# Output: True

output = False
dicionario_parenteses = {'abre': ['(', '{', '['], 'fecha': [')', '}', ']']}
dicionario_correspondencia = {'(': ')', '{': '}', '[': ']'}
parenteses_a_fechar = {}
parenteses_fechando = {}
contador_de_abertura = 0
contador_de_fechamento = 0
dicionario_de_fechados = {'()': [], '{}': [], '[]': []}

# Se for ímpar não vai fechar:
if len(string)%2 != 0:
    print(output)
    exit()

for posicao, caractere in enumerate(string):
    # Se começar com fechado não vai fechar:
    if posicao == 0 and caractere in dicionario_parenteses['fecha']:
        print(output)
        exit()
    elif caractere in dicionario_parenteses['abre']:
        if caractere not in parenteses_a_fechar:
            parenteses_a_fechar[caractere] = []
        parenteses_a_fechar[caractere].append(posicao)
        contador_de_abertura += 1
    elif caractere in dicionario_parenteses['fecha']:
        if caractere not in parenteses_fechando:
            parenteses_fechando[caractere] = []
        parenteses_fechando[caractere].append(posicao)

# Se não for abrir e fechar o mesmo tanto não vai fechar:
if len(parenteses_a_fechar) != len(parenteses_fechando):
    print(output)
    exit()

for chave in dicionario_correspondencia.keys():
    if chave in parenteses_a_fechar.keys() and dicionario_correspondencia[chave] in parenteses_fechando.keys() and len(parenteses_a_fechar[chave]) == len(parenteses_fechando[dicionario_correspondencia[chave]]):
        contador_de_fechamento += len(parenteses_a_fechar[chave])

if contador_de_abertura == contador_de_fechamento:
    try:
        dicionario_de_fechados['()'].append(*parenteses_a_fechar['('])
        dicionario_de_fechados['()'].append(*parenteses_fechando[')'])
    except:
        pass
    try:
        dicionario_de_fechados['{}'].append(*parenteses_a_fechar['{'])
        dicionario_de_fechados['{}'].append(*parenteses_fechando['}'])
    except:
        pass
    try:
        dicionario_de_fechados['[]'].append(*parenteses_a_fechar['['])
        dicionario_de_fechados['[]'].append(*parenteses_fechando[']'])
    except:
        pass
else:
    print(output)
    exit()

for lista in dicionario_de_fechados.values():
    while len(lista) > 0:
        if (lista[-1] - lista[0] -1)%2 != 0:
            print(output)
            exit()
        else:
            lista.pop(0)
            lista.pop(-1)

    # if ...:
    #     output = True
    # else:
    #     print(output)
    #     exit()

# print(str(parenteses_a_fechar) + '\n' + str(parenteses_fechando))
output = True
print(output)
