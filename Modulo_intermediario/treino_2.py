def reverse_string(strs):
    pilha = []
    string_reversa = ''
    
    for char in strs:
        pilha.append(char)

    while pilha:
        topo_pilha = pilha.pop()
        string_reversa += topo_pilha
       
    return string_reversa

print (reverse_string('kwrs'))