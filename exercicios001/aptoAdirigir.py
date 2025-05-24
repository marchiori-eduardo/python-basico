ano_atual = input("Digite em que ano estamos: ")
ano_nasc = input("Digite o seu ano de nascimento: ")


idade = int(ano_atual) - int(ano_nasc)
if idade < 18 or idade >= 70:
    print("Você não pode dirigir.")
elif idade >= 18 and idade < 70:
    print("Você pode dirigir.")
    