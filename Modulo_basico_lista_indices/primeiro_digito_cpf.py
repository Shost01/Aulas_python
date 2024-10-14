import re
import sys
entrada =input('Digite o seu CPF: ')
cpf_usuário = re.sub(r'[^0-9]', '', entrada)

entrada_em_sequencia = entrada == entrada[0] * len(entrada)

if entrada_em_sequencia:
    print ('Voce enviou dados inválidos.')
    sys.exit()

cpf_numeros = [int(digito) for digito in cpf_usuário if digito.isdigit()]

# Primeiro Digito
nove_digitos = cpf_numeros[:9]

multiplicadores_01 = list(range(10, 1, -1))

soma_1 = 0
for i in range(9):soma_1 += nove_digitos[i] * multiplicadores_01[i]

primeiro_digito = (soma_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Segundo Digito
dez_digitos = nove_digitos + [primeiro_digito]
multiplicadores_02 = list(range(11, 1, -1))

soma_2 = 0
for i in range(10):soma_2 += dez_digitos[i] * multiplicadores_02[i]
segundo_digito = (soma_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_calculo = f"{''.join(map(str, nove_digitos[:3]))}{''.join(map(str, nove_digitos[3:6]))}{''.join(map(str, nove_digitos[6:]))}{primeiro_digito}{segundo_digito}"

if cpf_usuário == cpf_calculo:
    print (f'{cpf_usuário} é válido')
else:
    print ('CPF inválido')