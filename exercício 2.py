
#programa para classificar a idade
idade = int(input("Coloque a idade da pessoa que quer classificar: "))

if  0<= idade <= 12 :
    print ("A pessoa é uma criança")

elif 13<= idade <=17 :
    print ("A pessoa é um adolescente")

elif 18<= idade <=59 :
    print("A pessoa é um adulto")

elif 60<= idade :
    print("A pessoa é um idoso")

#Programa pra calcular o imc
peso = float(input("Coloque aqui o peso da pessoa que quer medir em kg: "))
altura =float(input("Coloque  a altura da pessoa em metros: "))
imc = peso / (altura * altura)
print ("imc é igual a: ", imc)
if imc < 18.5 :
    print ("A pessoa é abaixo do peso")

elif 18.5 <= imc <= 25 :
    print ("A pessoa tem o peso normal")

elif 25 < imc <= 30 :
    print (" A pessoa tem sobrepeso")

else :
    print (" A pessoa é obesa")


#programa conversor de temperatura
tipo = int(input("Escolha a operação que você quer entre 1, que é celsius e fahrenheit, 2 que é fahrenheit e kelvin, e 3 que é kelvin e celsius:\n"))

#conversor de celsius e fahreinheit
if tipo == 1 :
    operac = input("Se quiser transformar celsius em fahrenheit, escolha operac1, e se quiser transformar fahrenheit em celsius, escolha operac2\n")
    if operac == "operac1" :
        tempc = float(input("Coloque a temperatura em celsius que quer transformar para fahrenheit: \n"))
        tempnov = (tempc * 1.8) + 32
        print (f"A temperatura agora em Fahrenheit é :\n{ tempnov:.2f}")

    elif operac == "operac2" :
        tempf = float(input("Coloque a temperatura em fahrenheit que quer transformar para celsius: \n"))
        tempnov = (tempf - 32) * (5/9)
        print (f"A tempoeratura agora em celsius é: \n{tempnov:.2f}")

#conversor de fahrenheit e kelvin
elif tipo == 2:
    operac = input("Se quiser transformar fahrenheit em kelvin, escolha operac1, e se quiser transformar kelvin em fahrenheit, escolha operac2\n")
    if operac == "operac1" :
        tempf = float(input("Coloque a temperatura em fahrenheit que quer transformar para kelvin: \n"))
        tempnov = (tempf + 459.67) * (5/9)
        print(f"A temperatura agora em kelvin é :\n {tempnov:,2f}")

    elif operac == "operac2" :
        tempk = float(input("Coloque a temperatura em kelvin que quer transformar para fahrenheit: \n"))
        tempnov = (tempk * (9/5)) - 459.67
        print(f"A temperatura agora em Fahrenheit é :\n {tempnov:.2f}")

#conversor de kelvin e celsius
elif tipo == 3:
    operac = input( "Se quiser transformar celsius em kelvin, escolha operac1, e se quiser transformar kelvin em celsius, escolha operac2\n")
    if operac == "operac1":
        tempc = float(input("Coloque a temperatura em celsius que quer transformar para kelvin: \n"))
        tempnov = (tempc + 273.15)
        print(f"A temperatura agora em kelvin é :\n {tempnov:.2f}")

    elif operac == "operac2":
        tempk = float(input("Coloque a temperatura em kelvin que quer transformar para celsius: \n"))
        tempnov = (tempk - 273.15)
        print(f"A temperatura agora em celsius é :\n {tempnov:.2f}")

#programa que confere se é ano bissexto

try:
    ano = int(input("Digite um ano para verificar se é bissexto: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

if (ano % 400) == 0:
    print(f"O ano {ano} é BISSEXTO.")

elif (ano % 100) == 0:
    print(f"O ano {ano} NÃO é bissexto.")

elif (ano % 4) == 0:
    print(f"O ano {ano} é BISSEXTO.")

else:
    print(f"O ano {ano} NÃO é bissexto.")

#programa de calculadora
operac = input("escolha  a operação que você quer fazer entre dois números, com as opções de +, -, *, /")

if operac == "+" :
    numero1 = int(input("escolha o primeiro número da operação"))
    numero2 = int(input("escolha o segundo número da operação"))
    soma = numero1 + numero2
    print(f"o resultado da soma dos dois números é{soma}")

elif operac == "-" :
    numero1 = int(input("escolha o primeiro número da operação "))
    numero2 = int(input("escolha o segundo número da operação "))
    subt = numero1 - numero2
    print(f"o resultado da subtração dos dois números é{subt}")

elif operac == "*" :
    numero1 = int(input("escolha o primeiro número da operação "))
    numero2 = int(input("escolha o segundo número da operação "))
    mult = numero1 * numero2
    print(f"o resultado da soma dos dois números é: {mult}")

elif operac == "/":
        numero1 = int(input("escolha o primeiro número da operação"))
        numero2 = int(input("escolha o segundo número da operação"))
        divis =float( numero1 / numero2)
        print(f"o resultado da soma dos dois números é: {divis}")


# cálculo de média dos alunos
notas_alunos = []

try:
    num_alunos = int(input("Quantos alunos a turma tem? "))
    if num_alunos <= 0:
        print("O número de alunos deve ser positivo. Encerrando.")
        exit()
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()


for i in range(num_alunos):
    while True:
        try:
            nota = float(input(f"Digite a nota do Aluno {i + 1}: "))
            if 0 <= nota <= 10:
                notas_alunos.append(nota)
                break
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número para a nota.")


soma_notas = sum(notas_alunos)
media_turma = soma_notas / num_alunos

print(f"Número total de alunos: {num_alunos}")
print(f"Notas registradas: {notas_alunos}")
print(f"Média da Turma: {media_turma:.2f}")


# Criação de senha
senha = input("Digite sua senha: ")

tamanho_ok = len(senha) >= 8
tem_numero = False
for caractere in senha:
    # O .isdigit() retorna True se o caractere for um dígito (0-9)
    if caractere.isdigit():
        tem_numero = True
        break
print("\n--- Resultado da Verificação ---")

if tamanho_ok and tem_numero:
    print("Senha OK! Atende a todos os requisitos básicos de segurança.")

else:
    print("Senha não atende aos requisitos de segurança. Por favor, tente novamente.")

    if not tamanho_ok:
        print("  - FALHA: A senha deve ter pelo menos 8 caracteres.")

    if not tem_numero:
        print("  - FALHA: A senha deve conter pelo menos um número.")


#programa pra conferir se é par ou ímpar
contador_par = 0
contador_impar = 0
total_numeros = 0

print("--- Classificador de Pares e Ímpares ---")
print("Digite um número por vez. Digite 'FIM' ou qualquer texto para encerrar e ver o resultado.\n")

while True:
    entrada = input(f"Digite o {total_numeros + 1}º número: ")

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"  -> {numero} é PAR.")
            contador_par += 1
        else:
            print(f"  -> {numero} é ÍMPAR.")
            contador_impar += 1

        total_numeros += 1

    except ValueError:
        # Verifica se o usuário realmente digitou 'fim' (para ser mais amigável), senão qualquer texto serve
        if entrada.lower() == 'fim' and total_numeros == 0:
            print("\nNenhum número foi inserido.")
            break
        elif total_numeros > 0:
            print("\nEntrada não numérica detectada. Encerrando contagem...")
            break
        else:
            print("\nEntrada não numérica detectada. Encerrando.")
            break


print("\n--- Resultados Finais ---")
print(f"Total de números inseridos: {total_numeros}")
print(f"Total de números PARES: {contador_par}")
print(f"Total de números ÍMPARES: {contador_impar}")
