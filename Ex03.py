numConta = int(input("Digite o número da conta: "))

while(numConta > 999):
    print("O número da conta deve ter 3 dígitos")
    numConta = int(input("Digite o número da conta: "))

print("O número da conta digitado é: ", numConta)

n1 = int(numConta / 10)
i1 = int(numConta % 10)

n2 = int(n1 / 10)
i2 = int(n1 % 10)

i3 = int(n2 % 10)

numContaInverso = (i1 * 100) + (i2 * 10) + i3

print("O número inverso é: ", numContaInverso)

somaCoIn = numConta + numContaInverso

print("A soma do número da conta com seu inverso é: ", somaCoIn)

r1 = int(somaCoIn / 10)
posi3 = int(somaCoIn % 10)

r2 = int(r1 / 10)
posi2 = int(r1 % 10)

posi1 = int(r2 % 10)

multiplicacao = posi1 + posi2 * 2 + posi3 *3 

print("O dígito verificador é: ", multiplicacao)
