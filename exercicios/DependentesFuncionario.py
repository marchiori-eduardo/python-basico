nome = input("Qual o nome do funcionário: ")
sal = float(input("Qual o salário do funcionário: "))
dep = int(input("Quantos dependentes o funcionário tem: "))

match dep:
    case 0:
        nsal = int(sal + (sal*5/100))
    case 1, 2, 3:
        nsal = int(sal + (sal*10/100))
    case 4, 5, 6:
        nsal = int(sal + (sal*15/100))
    case _:
        nsal = int(sal + (sal*20/100))

print(f'O novo salário de {nome} é {nsal}')
# O código calcula o novo salário de um funcionário com base no número de dependentes que ele tem.