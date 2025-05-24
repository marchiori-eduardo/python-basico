A = float(input())
B = float(input())

def media (A, B):
    return(A + B) /2
    
S = float(media(A, B))

if S >= 7.0:
    print('Aprovado')
elif S >=4.0 <= 7.0:
    print('Recuperacao')
elif S <4.0:
    print('Reprovado')
    
print(f'Media: {S}')