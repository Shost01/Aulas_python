import os

lista = []

while True:
    print ('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system ('clear')
        valor = input ('Valor: ')
        lista.append (valor)
        
    elif opcao == 'a':
        indice_str = input ('Escolha o indice para apagar: ')
        try:
            indice = int (indice_str)
            del lista[indice]
        except ValueError:
            print ('Por favor digite um numero inteiro')
        except IndexError:
            print ('Indice não existente')
        except Exception:
            print ('Erro desconhecido')
            
    elif opcao == 'l': 
        os.system ('clear')
        
        if len(lista) == 0:
            print ('Nada para listar')
        
        for indice, nome in enumerate(lista):
                print(indice, nome)