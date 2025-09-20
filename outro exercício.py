#teste
# Programa de dizer olá mundo!

print(f"Olá, mundo!")

#Programa de somaem
numero1 = 12
numero2 = 14
soma = numero1 + numero2

print ("A soma dos dois números,12 e 14, é: ", soma)

#Calculadora de volume com tamanhos pré - definidos
compr = 12
alt = 20
larg = 14
volume = compr * alt * larg

print ("Volume da forma geométrica sugerida é: ", volume,"cm\u00b3")

preco_unitario = 12.40
quant = 3
preco_total = preco_unitario * quant
print (f"O preço unitário da cadeira infantil é :R$ {preco_unitario:.2f}, sendo a quantidade comprada {quant}, dando um total de R$ {preco_total:.2f} ")
#calculadora
preco_unitario = 12.40
quant = 3
preco_total = preco_unitario * quant

print (f"O preço unitário da cadeira infantil é :R$ {preco_unitario:.2f}, sendo a quantidade comprada {quant}, dando um total de R$ {preco_total:.2f} ")

#Conversor de moeda com números pré -definidos
quant_reais = 100
tax_dol = 5.20
tax_eur = 6.15

print (f"R$ {quant_reais:.2f} são {quant_reais/tax_dol:.2f} em dólares e {quant_reais/tax_eur:.2f} em euros")

#calculadora de desconto com números pré -definidos
preco = 50
porc_desc = 20
preco_desc =  preco * (porc_desc/100)

print (f"Uma camiseta tem preço inicial de R$ {preco:.2f}, com o desconto de {porc_desc}%, o valor chega em R$ {preco - preco_desc:.2f} ")

#calculo de média escolar com números pré -definidos
n1 = 7.5
n2 = 8.0
n3 = 6.5
media = (7.5 + 8 + 6.5) / 3
media_a = round(media, 2)

print (f" Com as notas {n1}, {n2}, {n3}, a média do aluno/a deve ser {media_a}")

#Calculo de consumo médio de combustível com números pré - definidos
dist_p = 300
combust_g = 25
consumo = dist_p / combust_g
consumo_arrendado = round (consumo,2)

print (f" Em uma distância de {dist_p} km, um veículo gasta {combust_g} litros, dando um consumo médio de {consumo_arrendado} km/l")



