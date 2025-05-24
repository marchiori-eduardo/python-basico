R: float
D: float
C: int
Q = int(input("Quantas conversões você deseja fazer? "))

C = 1
while (C <= Q):
    R = input("Qual o valor em R$? ")
    D = float(R) / 5.67
    print("O valor em Dólares é: {:.2f}".format(D))
    C = C + 1