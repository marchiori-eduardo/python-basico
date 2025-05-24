cont = int(0)
num = int(input("Digite um número para ver a tabuada dele: "))

while(cont <= 10):
    print(cont,f"* {num} =",cont*num)
    cont = cont + 1
else:
    print (f"Tabuada do {num} calculada com sucesso!")