def palindromo (nome):
    nome_str = str(nome).lower()
    nome_reverso = nome_str[::-1]
    if nome_str == nome_str[::-1]:
        return f'{nome_str} é lido como {nome_reverso} ao contrário. É um palíndromo!'
    return f'{nome_str} se lê {nome_reverso} ao contrário, portanto, não é um palíndromo.'

print (palindromo('Natan'))
print (palindromo('Sabrina'))