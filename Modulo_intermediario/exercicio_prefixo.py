# from typing import List
def longestCommonPrefix(strs):
    if not strs:
        return 'A lista está vazia'
    prefixo = strs[0]
    
    for string in strs[1:]:
        while string[:len(prefixo)] != prefixo:
            prefixo = prefixo[:-1]
            if not prefixo:
                return 'não há um prefixo comum'
    return prefixo
    
print(longestCommonPrefix(['moeda', 'moer', 'moema']))
print(longestCommonPrefix(['fonte', 'fome', 'folha']))