precoUni = float(input("Digite o preço unitário do produto: "))

#país de origem e validação do dado
pais = int(input("Determine o país de origem - Digite 1 para BRASIL, 2 para MÉXICO ou 3 para OUTROS: "))
while((pais != 1) and (pais != 2) and (pais != 3)):
    print("Número inválido!")
    pais = int(input("Determine o país de origem - Digite 1 para BRASIL, 2 para MÉXICO ou 3 para OUTROS: "))


#tipo de transporte e validação do dado
transporte = input("Informe o meio de transporte - T para TERRESTRE, F para FLUVIAL ou A para ÁEREO: ")
while(transporte != "T" and transporte != "F" and transporte != "A"):
    print("Transporte inválido")
    transporte = input("Informe o meio de transporte - T para TERRESTRE, F para FLUVIAL ou A para ÁEREO: ")


#carga perigosa e validação do dado
cargaPerigo = input("A carga é perigosa? Digite S para SIM ou N para NÃO: ")
while(cargaPerigo != "S" and cargaPerigo != "N"):
    print("Resposta inválida!")
    cargaPerigo = input("A carga é perigosa? Digite S para SIM ou N para NÃO: ")

#Valor do imposto
if(precoUni <= 100):
    vImposto = precoUni * 0.05

else:
    vImposto = precoUni * 0.2

#Valor do transpote
if(cargaPerigo == "S"):
    if(pais ==  1):
        vTransporte = 21
    elif(pais ==  2):
        vTransporte = 27
    else:
        vTransporte = 50

else:
    if(pais ==  1):
        vTransporte = 21
    elif(pais ==  2):
        vTransporte = 25
    else:
        vTransporte = 40

#Valor do seguro
if((pais == 2) and (transporte == "A")):
    seguro = precoUni / 2
else:
    seguro = 0

#Preço final
precoFinal = precoUni + vImposto + vTransporte + seguro

print("O preço final do produto é R$", round(precoFinal,2))



        