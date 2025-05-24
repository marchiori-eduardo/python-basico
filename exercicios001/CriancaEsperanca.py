print ('---------------------')
print ('  Crianca Esperanca  ')
print ('---------------------')
print ('Muito Obrigado por ajudar!')
print ('[1] para doar R$10,00')
print ('[2] para doar R$25,00')
print ('[3] para doar R$50,00')
print ('[4] para doar outros valores')
print ('[5] para cancelar')

match input('Escolha uma opção: '):
    case '1':
        valor = 10,00
    case '2':
        valor = 25,00
    case '3':
        valor = 50,00
    case '4':
        valor = input('Digite o valor que deseja doar: ')
    case '5':
        print ('Você cancelou a doação')
        valor = 0
    case _:
        print ('Opção inválida, tente novamente')
        valor = 0

print ('---------------------')
print (f'Sua doação foi de R${valor}')
print ('Agradecemos sua doação!')
print ('---------------------')