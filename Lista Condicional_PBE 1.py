'''
print("01 - Esse programa irá mostrar se o número é par ou impar!!")
num = int(input("Insira um número: "))
if num % 2 == 0:
    print("Esse número é par!!")
else:
    print("Esse némro é impar!!")
'''
########################################################################
'''
print("02 - Esse progrmama irá mostrar se o número é maior que 10!!")
num = int(input("Insira um número: "))
if num > 10:
    print("Esse número é maior que 10")
elif num == 10:
    print("Essde número é igual a 10")
else:
    print("Esse número é menor que 10")
'''
########################################################################
'''
print("03 - Esse programa irá verificar se o usuario é maior de idade!!")
idade = int(input("Insira sua idade: "))
if idade >= 18:
    print("Você é maoir de idade!!")
else:
    print("Você é menor de idade!!")
'''
########################################################################
'''
print("04 - Esse programa irá verificar se o voto é obrigatório!!""")
idade = int(input("Informe sua idade: "))
if idade <=15:
    print(f"Não Eleitor. Você ainda não tem idade para votar.")
elif idade <=18:
    print(f"Facultativo (opcional). Você ainda não é obrigado a votar.")
else:
    print(f"Voto Obrigatório.")
'''
########################################################################
'''
print("05 - Esse programa irá verificar se o número é positivo ou negativo!!")
num = int(input("Insira um número: "))
if num > 0:
    print("Esse número é positivo!")
elif num == 0:
    print("Esse número é igual a igual a zaro!")
else:
    print("Esse número é negativo!")
'''
########################################################################
'''
print("06 - Esse programa irá verificar sua nota !!")
nota = float(input("Insira sua nota: "))
if nota >=9.0:
    print("A - Sua nota é Exelente")
elif nota >= 7.0:
    print("B- Sua nota é Boa")
elif nota >= 5.0:
    print("C - Você está na média")
elif nota >= 3.0:
    print("D - Sua nota está ruim. Estudar mais!!")
else:
    print("E - Sua nota está Insuficiente")
'''
########################################################################
'''
print("07 - Esse programa irá verificar SE você tem desconto conforme sua idade!!")
idade = int(input("Insira sua idade: "))
if idade <= 12:
    print("Parabéns!! Você tem direito a um desconto.")
elif idade >=60:
    print("Parabéns!! Você tem direito a um desconto")
else:
    print("Infelizmente você nao tem direito a um desconto")
'''
########################################################################
'''
print("08 - Esse prgrama irá ver se pode ser um triangulo e qual o tipo.")
lado1= float(input("Informa o comprimento do primero lado: "))
lado2 = float(input("Informa o comprimento do segundo lado: "))
lado3 = float(input("Informa o comprimento da terceiro lado: "))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print("Não é triângulo")
elif (lado1 == lado2 ) and (lado1 == lado3):
    print("Esse triângulo é um Equilátero")
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("Esse triângulo é um Isósceles")
else:
    print("Esse triângulo é um Escaleno")
'''
########################################################################
'''
print("09 - Esse programa vai calcular o desconto de acordo com o valor!!")
valor = float(input("Insira o valor: "))
if valor < 100:
    print("Seu desconto é de 5%")

elif valor >= 100 and valor < 500:
    print("Seu desconto é de 10%")
else:
    print("Seu desconto é de 15%")
'''
########################################################################
'''
print("10 - Esse programa irá verificar se o ano é bissexto!!")
ano = int(input("Digita um ano: "))
bissixto = ano
if (ano % 4==0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')
'''
########################################################################
'''
print("11 - Esse programa é uma calculadara de IMC!!")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"Baixo do peso. Seu imc é de: {imc:.2f}")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Normal. Seu imc é de: {imc:.2f}")
elif imc >= 25 and imc <= 29.9:
    print(f"Sobrepeso. Seu imc é de: {imc:.f2}")
elif imc >= 30 and imc <= 34.9:
    print(f"Obesidade. Seu imc é de: {imc:.2f}")
elif imc >= 35 and imc <= 39.9:
    print(f"Obesidade Mórbida. Seu imc é de: {imc:.2f}")
else: print(f"Obesidade. seu imc é de: {imc:.2f}")
'''
########################################################################
'''
print("12 - Esse programa irá mostrar a ordem dos números")
num1 = float(input("Insira um número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

if(num1>num2 and num2>num3):
    print("Ordem decrescente")

elif (num1<num2 and num2<num3):
    print("Ordem crescente")

else:
    print("Números sem ordem")
'''
########################################################################
'''
print("13 - Esse programa irá classificar a temperatura!! ")
temperatura = float(input("Insira a temperatura em Celsius: "))
if temperatura < 10:
    classificacao = "Frio"
elif temperatura >= 10 and temperatura <= 25:
    classificacao = "Aconchegante"
elif temperatura > 25 and temperatura <= 40:
    classificacao = "Quente"
else:
    classificacao = "Muito Quente"
print(f"A temperatura está: {classificacao}")
'''
########################################################################
'''
print("14 - Esse programa irá converter o formato da data!!")
from datetime import datetime
data = input("Digite uma data no formato dd/mm/aaaa: ")
data_mudada = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
print("A data formatada é:", data_mudada)
'''
########################################################################
'''
import re
print("15 - Esse programa verifica se a senha é válida!!")
senha = input("Insira uma senha: ")
erro = ""
if len(senha) < 8:
    erro += "- A senha deve ter pelo menos 8 caracteres.\n"
if not re.search(r"[A-Z]", senha):
    erro += "- A senha deve ter pelo menos uma letra maiúscula.\n"
if not re.search(r"[a-z]", senha):
    erro += "- A senha deve ter pelo menos uma letra minúscula.\n"
if not re.search(r"[0-9]", senha):
    erro += "- A senha deve ter pelo menos um número.\n"
if not re.search(r"[@#$%&]", senha):
    erro += "- A senha deve ter pelo menos um caractere especial (@, #, $, %, &).\n"
if erro == "":
    print("Senha válida!")
else:
    print("Senha inválida! Você tem que corrigir os seguintes erros:\n" + erro)
'''
########################################################################
'''
import math
print("16 - Esse programa calcula a raiz quadrada de um número!!")
num = float(input("Insira um número: "))
if num < 0:
    resultado = "Não é possível calcular a raiz quadrada de um número negativo."
elif num > 100:
    resultado = "Número muito grande, reduza para um valor abaixo de 100."
else:
    raiz = num ** 0.5
    resultado = f"A raiz quadrada de {num} é aproximadamente {raiz:.2f}."
print(resultado)
'''
########################################################################
'''
print("17 - Esse programa irá converter o formato da data!!")
data = input("Insira a data no seguinte formato (dd/mm/aaaa): ")
divisao = data.split("/")
dia = int(divisao[0])
mes = int(divisao[1])
ano = int(divisao[2])
if mes < 1 or mes > 12:
    print("Mês inválido. O mês deve estar entre 1 e 12.")
else:
    if mes == 2:
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            limite = 29
        else:
            limite = 28
    elif mes in [4, 6, 9, 11]:
        limite = 30
    else:
        limite = 31

    if dia < 1 or dia > limite:
        print(f"Dia inválido. O mês {mes} no ano {ano} tem no máximo {limite} dias.")
    else:
        print(f"{ano:04d}-{mes:02d}-{dia:02d}")
'''
########################################################################
'''
print("18 - Esse programa é analisador de expressões matemáticas simples !!")
expressao = input("Insira a expressão matemática: ")
resultado = eval(expressao)
print(f"Resultado: {resultado}")
'''
########################################################################
'''
import re
print("19(Desafio) - Esse programa irá vefificar o  CPF !!")
cpf = input("Insira o seu CPF ex:(XXX.XXX.XXX-XX):\n")
padrao = r"\d{3}\.\d{3}\.\d{3}\-\d{2}"
valido = re.match(padrao, cpf)

if valido:
    penultimo_numero = ((int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)) % 11
    ultimo_numero = ((int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)) % 11

    if penultimo_numero >= 2:
        numero1 = 11 - penultimo_numero
    else:
        numero1 = 0
    if ultimo_numero >= 2:
        numero2 = 11 - ultimo_numero
    else:
        numero2 = 0

    if int(cpf[12]) == numero1 and int(cpf[13]) == numero2:
        print("Esse CPF é válido!")
    else:
        print("Esse CPF é inválido!")
else:
    print("Esse CPF não foi digitado corretamente. Tente novamente!!")
'''
########################################################################