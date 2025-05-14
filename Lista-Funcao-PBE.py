'''
def promocao_relampago(preco):
    dobro = preco * 2
    return dobro


print("01 - Esse programa vai calcular a promoção de uma loja!! ")
preco = float(input("Insira o preço do produto: "))
promocao_relampago(preco)
print(f"O preço para a promoção relâmpago é de: R${promocao_relampago(preco)}")
'''
################################################################################
'''
def boas_vindas(nome):
    print(f"Boa-Vinda!! Estamos felizes por ter você no nosso curso {nome}.")


print("02 - Esse programa vai dar as boa-vinda!! ")
nome = input("Digite seu nome: ")
boas_vindas(nome)
'''
################################################################################
'''
import random
def dado(num):
    if num % 2 == 0:
        print(f"Parabéns!! Você avança no jogo ")
    else:
        print(f"Infelizmente você vai tar que recuar")

print("04 - Esse programa é um jogo, vc vai jogar o dado e ver o número que retirou!!")
num = random.randint(1, 10)
print(f"O número que você tirou foi: {num}")
dado(num)
'''
################################################################################
'''
def tabuada(num):
    for count in range(10):
        print("%d x %d = %d" % (num, count + 1, num * (count + 1)))


print("05 - Esse programa vai mostrar a tabuada do número desejado!!")
num = int(input("Insira o número da tabuada que deseja saber: "))
tabuada(num)
'''
################################################################################
'''
def cinema(idade):
    if idade < 18:
        return print(f"Sua idade não está adquada para assistir esse filme")
    else:
        return print(f"Sua idade está adquada para assistir esse filme")


print("06 - Esse programa vai verificar a idade para ver se pode entrar ou não no cinema!!")
idade = int(input("Insira sua idade: "))
cinema(idade)
'''
################################################################################
'''
def desconto (preco_original):
    valor_desconto=float(preco_original*0.10)
    valor_final=preco_original-valor_desconto
    return print(f"O desconto foi de: R${valor_desconto}\nO preço final é de: R${valor_final}")


print("07 - Esse programa vai calcular um desconto de 10%!!")
preco_original=float(input("Digite o valor do produto: "))
desconto(preco_original)
'''
################################################################################
'''
def contagem_letras(palavra):
    numero_de_letras = len(palavra)
    return print(f"Esse palavra tem {numero_de_letras} letras.")


print("08 - Esse programa vai contar quantas letras tem uma palavra!!")
palavra = input("Insira uma palavra: ")
contagem_letras(palavra)
'''
################################################################################
'''
def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    return print(f"Temperatura em Celsius: {celsius}\nTemperatura em Fahrenheit: {fahrenheit}")


print("09 - Esse programa converte uma temperatura de Celsius para Fahrenheit!") 
celsius = float(input("Informe a temperatura em Celsius: ")) 
converter_temperatura(celsius)
'''
################################################################################
'''
def classificador_rpg(num):
    if num < 5:
        return print(f"Classificação: Pequeno")
    elif num > 5 and num < 9:
        return print(f"Classificação: Médio")
    else:
        return print(f"Classificação: Grande")


print("10 - Esse programa é um jogo de RPG classifica números como Pequeno, Médio ou Grande!!")
num = int(input("Insira um número: "))
classificador_rpg(num)
'''
################################################################################
'''
def palindromo(frase):
    frase_minuscula = frase.lower()
    if frase_minuscula == frase_minuscula[::-1]:
        print(f"A frase '{frase}' é um PALÍNDROMO!")

    else:
        print(f"A frase '{frase}' NÃO é um palíndromo!")


print("11 - Esse programa vai mostrar se a frase é um Palíndromo ou não!!")
palindromo("Ana Ana")
palindromo("1DSTB-SENAI")
palindromo("Subi no Onibus")
'''
################################################################################

def fatoral_numero(num):
    if num < 0:
        print("O número tem que ser positivo!")
    else:
        resultado = 1
        count = 1
        while count <= num:
            resultado *= count
            count += 1
        print(f"O fatorial de {num} é: {resultado}")

print("12 - Esse programa vai mostrar o fatorial do número escolhido!!")
num = int(input("Insira um número: "))
fatoral_numero(num)