def simplificar_caminho (caminho):
    partes = caminho.split('/') # ivide o caminho em /
    pilha = [] # cria uma pilha vazia
    
    for parte in partes: # neste laço itero sobre a pilha 
        if parte == '' or parte == '.':
            continue #ignor a linha se conter algun destes caracteres
        elif parte == '..':
            if pilha: # verificando se a pilha está vazia
                pilha.pop() # removendo a ultima parte da pilha
        else:
            pilha.append(parte)# Adicionando a pilga
        
    caminho_final = '/' + '/'.join(pilha) # juntando as partes na pilha
        
    return caminho_final
            