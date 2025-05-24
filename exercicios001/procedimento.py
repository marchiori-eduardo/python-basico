def Topo ():
    print('\n' * 50)
    print ('----------------------')
    print ('Detector de Pesado')
    print (f"Maior peso até agora: {Mai} Kg")
    print ('----------------------')





Mai = 0
Topo()
for I in range (1, 5):
    N = input('Digite o nome:')
    P = float(input(f'Digite o peso de {N} :'))
    if P > Mai:
        Mai = float(P)
        Pesado = N
        
    
    Topo()



Topo()

print (f"A pessoa mais pesada foi {Pesado}, com {Mai} Kg")