'''
print("01 - Esse programa irá mostra o nome João!")
nome = "João"
print(nome)
'''
###############################################################
'''
print("02 - Esse programa irá fazer as 4 operações principis entre 2 números!")
a = 5
b = 10
soma = a + b
subtracao = a - b
multiplicacao = a * b
disisao = a / b
print(f"Resultados das operações:\nSoma:{soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {disisao}")
'''
###############################################################
'''
print("03 - Esse progrma irá calcular o desconto!")
preco = 50
desconto = 10
resultado = preco - desconto
print(f"O preço final é de: {resultado}")
'''
###############################################################
'''
print("04 - Esse programa irá calcular o resultado dsessa expressão : 10 + 5 * 2")
resultado = 10 + 5 * 2
print(f"O resultado da expressão é de: {resultado}")
'''
###############################################################
'''
print("05 - Esse programa irá converter string para int")
num1 = "150"
int_num1 = int(num1)
total = int_num1 * 2
print(total)
'''
###############################################################
'''
print("07 - Esse programa irá somar dois números")
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
soma = num1 + num2
print(f"O resultado da soma é de: {soma}")
'''
###############################################################
'''
print("08 - Esse programa irá dividir dois números")
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
divisao = num1 / num2
print(f"O resultado da divisão é de: {divisao}")
'''
###############################################################
'''
print("09 - Esse programa irá verificar qual número é maior")
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
maior = num1 > num2
print(f"O número {num1} é maior que o número {num2}? {maior}")
'''
###############################################################
'''
print("10 - Esse programa irá verificar quantos dias o usuario já viveu")
idade = int(input("Digite sua idade: "))
tempo = idade * 365
print(f"Seu tempo de vida é de aproximadamente de: {tempo} dias")
'''
###############################################################
'''
print("11 - Esse programa irá calcular uma exponenciação")
base = int(input("Digite um número (base) inteiro: "))
expoente = int(input("Digite outro número (expoente) inteiro: "))
total = base ** expoente
print(f"O resultado da exponenciação é de: {total}")
'''
###############################################################
'''
print("12 - Esse programa irá converter um valor para string")
preco = float(input("Digita um preço: "))
string_preco = str(preco)
print(f"O preço é R${string_preco}")
'''
###############################################################
'''
print("13 - Esse programa irá calcular a área de um circulo")
raio = float(input("Digite o raio do circulo: "))
area = 3.1415 * (raio ** 2)
print(f"A área do circulo é aproximadamente de: {area:.2f}")
'''
###############################################################
'''
print("14 - Esse programa irá trocar os valores das variaveis")
a = int(input("Digita um número:"))
b = int(input("Digita outro número:"))
print(f"Os valores são: {a} e {b}")
a, b = b, a
print(f"Agora os valores são: {a} e {b}")
'''
###############################################################
'''
print("15 - Esse progrma irá realizar a média ponderada")
nota1 = float(input("Informe a primeira nota: "))
peso1 = 2

nota2 = float(input("Informe a segunda nota: "))
peso2 = 3

nota3 = float(input("Informe a terceira nota:"))
peso3 = 5

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
print(f"A média é: {media}")
'''
###############################################################
'''
print("16 - Esse programa irá calcular a distância entre dois pontos!!")
x1 = float(input("Informe um número para x1: "))
y1 = float(input("Informe um número para y1: "))
x2 = float(input("Informe um número para x2: "))
y2 = float(input("Informe um número para y2: "))
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)
print(f"A distancia desses pontos é de: {distancia:.2f}")
'''
###############################################################