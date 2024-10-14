import random

for _ in range(10):
    # Primeiro Digito
    nove_digitos = '' 

    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    multiplicadores_01 = list(range(10, 1, -1))

    soma_1 = 0
    for i in range(9):soma_1 += int(nove_digitos[i]) * multiplicadores_01[i]

    primeiro_digito = (soma_1 * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

    # Segundo Digito
    dez_digitos = nove_digitos + str(primeiro_digito)
    multiplicadores_02 = list(range(11, 1, -1))

    soma_2 = 0
    for i in range(10):soma_2 += int(dez_digitos[i]) * multiplicadores_02[i]
    segundo_digito = (soma_2 * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    cpf_calculo = f'{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}-{primeiro_digito}{segundo_digito}'

    print (cpf_calculo)