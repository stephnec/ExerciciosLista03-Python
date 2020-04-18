regiao = input("Informe para qual região deseja viajar: ")
while(regiao == "sudeste" or regiao == "sul"):
    print("A empresa não trabalha nos trechos sul e sudeste")
    regiao = input("Informe para qual região deseja viajar: ")

tipoIdaVolta = int(input("Digite 1 para passagem só de Ida ou digite 2 para passagem de Ida e Volta: "))

qntPassagem = int(input("Digite o número de passagens: "))

if(regiao == "norte"):
    if(tipoIdaVolta == 1):
        preco = qntPassagem * 280
    else:
        preco = qntPassagem * 400

elif(regiao == "nordeste"):
    if(tipoIdaVolta == 1):
        preco = qntPassagem * 380
    else:
        preco = qntPassagem * 628

elif(regiao == "centro-oeste"):
    if(tipoIdaVolta == 1):
        preco = qntPassagem * 620
    else:
        preco = qntPassagem * 1100


print("O valor da passagem será de ", preco, " reais")