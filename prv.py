def main (n):
    resultado = []  
    
    for i in range (1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            resultado.append ('DesenvolvimentoSoftware')
        elif i % 3 == 0:
            resultado.append ('Desenvolvimento')
        elif i % 5 == 0:
            resultado.append ('Software')
        else:
            resultado.append (str(i))  

    
    return ', '.join (resultado)


