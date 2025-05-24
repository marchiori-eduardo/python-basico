Cont = int


V= int(input("Digite um valor: "))
if (V % 2 == 1):
    V = V - 1
for Cont in range (V, 0, -2):
    print(Cont)