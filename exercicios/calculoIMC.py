massa= float(input("Digite seu peso em kg: "))
altura= float(input("Digite sua altura em metros: "))

imc= massa / (altura ** 2)
print ("Seu IMC é: ", imc)
if imc < 17 :
        print("Você está muito abaixo do peso!")
else:
        if imc >= 17 and imc < 18.49:
                print("Você está abaixo do peso!")
        else:
                if imc >= 18.5 and imc < 24.99:
                        print("Você está com o peso normal!")
                
                else:
                        if imc >= 25 and imc < 29.99:
                                print("Você está acima do peso!")
                        
                        else:
                                if imc >= 30 and imc < 34.99:
                                        print("Você está com obesidade grau I!")
                                else:
                                        if imc >= 35 and imc < 39.99:
                                                print("Você está com obesidade grau II!")
                                        else:
                                                print("Você está com obesidade grau III!")
