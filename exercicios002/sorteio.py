n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
import random
alunos = [n1, n2, n3, n4]
lista = random.shuffle (alunos)
print(f"A ordem da apresentação será: {alunos[0]}, {alunos[1]}, {alunos[2]}, {alunos[3]}.")

