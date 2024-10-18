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


print (inteiro_romano('IMLIXXX'))