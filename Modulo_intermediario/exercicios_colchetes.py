# Dada uma string s contendo apenas os caracteres '(', ')', '{', '}', '[' e ']', determine se a string de entrada é válida.

# Uma string de entrada é válida se:

# Os colchetes abertos devem ser fechados pelo mesmo tipo de colchetes.
# Os colchetes abertos devem ser fechados na ordem correta.
# Cada colchete fechado possui um colchete aberto correspondente do mesmo tipo.

def isValid(s):
    # Dicionário para mapear colchetes de fechamento aos de abertura
    mapa_colchetes = {')': '(', '}': '{', ']': '['}
    # Pilha para armazenar colchetes de abertura
    pilha = []
    
    # Itera sobre cada caractere na string
    for char in s:
        # Se for um colchete de fechamento
        if char in mapa_colchetes:
            # Verifica se o topo da pilha corresponde ao colchete de abertura esperado
            topo_pilha = pilha.pop() if pilha else '#'  # Se pilha estiver vazia, define um valor qualquer para causar erro
            if mapa_colchetes[char] != topo_pilha:
                return False
        else:
            # Se for um colchete de abertura, adiciona à pilha
            pilha.append(char)
    
    # No final, se a pilha estiver vazia, a string é válida
    return not pilha

print (isValid('[]'))