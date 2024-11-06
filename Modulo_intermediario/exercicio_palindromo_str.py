# def palindromo (nome):
#     nome_str = str(nome).lower()
#     nome_reverso = nome_str[::-1]
#     if nome_str == nome_str[::-1]:
#         return f'{nome_str} é lido como {nome_reverso} ao contrário. É um palíndromo!'
#     return f'{nome_str} se lê {nome_reverso} ao contrário, portanto, não é um palíndromo.'

# print (palindromo('Natan'))
# print (palindromo('Sabrina'))

def isPalindrome(x: int) -> bool:
    x_str = str(x)
    x_reverse = x_str[::-1]
    if x_str == x_reverse:
        print(f'{x} é lido como {x_reverse} da esquerda para a direita e da direita para a esquerda.')
        return True
    return False

print (isPalindrome(121))
        
        