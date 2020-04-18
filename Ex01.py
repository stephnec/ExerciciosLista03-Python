salBruto = float(input("Digite o valor do salário bruto: "))
valPrestacao = float(input("Digite o valor da prestação: "))

while(valPrestacao * 100 / salBruto) > (salBruto * 0.3):
    print("O valor da prestação não deve ultrapassar 30% do valor do salário!!!")
    valPrestacao = float(input("Digite o valor da prestação: "))

print("O empréstimo pode ser concedido!")