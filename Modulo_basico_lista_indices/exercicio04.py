nome = input ('Qual seu nome: ')
idade = input ('Qual a sua idade: ') 
contar_letras = len(nome.replace(" ", ""))

#
if nome and idade:
    print (f'Seu nome é {nome}')
    print (f'Seu nome ao contrário é {nome[::-1]}')
    
    if " " in nome:
         print ('O seu nome contém espaços!')  
    else:
        print ('O seu nome não contém espaços!')
    
    print (f'Seu nome tem {contar_letras} letras!')
    print (f'A primeira letra do seu nome é {nome [0]}')
    print (f'A última letra do seu nome é {nome [-1]}')

    
else:
    print('Desculpe, você deixou campos vazios.')