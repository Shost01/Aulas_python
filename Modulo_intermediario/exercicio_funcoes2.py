def parImpar (numero):
   par = numero % 2 == 0
   if par:
       return f'{numero} é par'
   
   return f'{numero} é impar'
     
print (parImpar(4946578))
print (parImpar(548))
print (parImpar(86))
print (parImpar(2645))
