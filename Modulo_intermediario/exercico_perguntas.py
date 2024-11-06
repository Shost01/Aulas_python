def pergunta():
    perguntas = [
        {
            'Pergunta': ' Quantos é 2 + 2 ?',
            'Opções': ['1', '3', '4', '5'],
            'Resposta': '4',
        },
        {
            'Pergunta': ' Quantos é 5 * 5 ?',
            'Opções': ['25', '55', '10', '51'],
            'Resposta': '25',           
        },
        {
            'Pergunta': ' Quantos é 10 / 2 ?',
            'Opções': ['4', '5', '2', '1'],
            'Resposta': '5',
        },      
    ]

    qtd_acertos = 0
    for perg in perguntas:
        print (perg['Pergunta'])
        print()   
        
        opcoes = perg['Opções']
        for i,opcao in enumerate(opcoes):
            print (f'{i})',opcao)
            print()
            
        escolha = input ('escolha uma opção: ')
        
        escolha_int = None
        acertou = False
        qtd_opcoes = len(opcoes)
        
        if escolha.isdigit():
            escolha_int = int(escolha)

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == perg['Resposta']:
                    acertou = True

        print()
        if acertou:
            qtd_acertos += 1
            print ('Acertou!')
        else:
            print ('Errou!')
        print()  
            
    print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')   
            
pergunta()
      

