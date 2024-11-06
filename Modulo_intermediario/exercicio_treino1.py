def inteiro_romano (s: str) -> int:
    algarismos = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    valor_esperado = 0
    total = 0
    for algarismo in reversed(s):
        valor = algarismos[algarismo]
        if valor < valor_esperado:
            total -= valor
        else:
            total += valor
            valor_esperado = valor
    return total

####### FORMA NÃO SIMPLIFICADA ###########
# print (inteiro_romano('IMLIXXX'))        algarismos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         total = 0
        
#         for i in range(len(s) - 1):
#             valor_atual = algarismos[s[i]]
#             valor_proximo = algarismos[s[i + 1]]
            
#             if valor_atual < valor_proximo:
#                 total -= valor_atual
#             else:
#                 total += valor_atual

#         # Somamos o último caractere, que não foi incluído no loop
#         total += algarismos[s[-1]]
        
#         return total

