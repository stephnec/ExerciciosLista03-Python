print("ESTACIONAMENTO SEMPRE BEM-VINDO")
veiculo = int(input("Digite 1 para MOTO e 2 para CARRO: "))
tempo = int(input("Digite o tempo (em minutos) de permanencia do veículo: " ))

if((veiculo == "1" or veiculo == "2") and tempo <= 15):
    print("O valor do estacionamento é grátis!!")

elif((veiculo == "1" or veiculo == "2") and tempo <= 180):
    if(veiculo == "1"):
        print("O valor do estacionamento da moto é de R$17,00")
    else:
        print("O valor do estacionamento do carro é de R$20,00")

elif((veiculo == "1" or veiculo == "2") and tempo > 180):
    if(veiculo == "1"):
        adicional = tempo - 180
        adicional *= 0.1
    
        preco = 17 + adicional
        print("O valor do estacionamento da moto é de R$", preco)
    else:
        adicional = tempo - 180
        adicional *= 0.15
    
        preco = 20 + adicional
        print("O valor do estacionamento do carro é de R$", preco)