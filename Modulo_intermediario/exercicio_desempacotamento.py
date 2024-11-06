def exibir_informacoes (*args, **kwargs):
    for chave, valor in kwargs.items():
        print (F'{chave}: {valor}')
        
    if 'Idade' in kwargs:          
        print(f'A pessoa tem {kwargs["Idade"]} anos.')


informacoes = {
    'Nome': 'Nathan',
    'Idade': '22',
    'Profissão': 'Programador',
}

exibir_informacoes(1, 2, 3, **informacoes)
