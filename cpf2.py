#Viviane Carvalho da Silva 20261014050024
# Cálculo do 11º número do CPF

cpf = input("Digite os 10 primeiros números do CPF: ")

soma = 0
peso = 11

for numero in cpf:
    soma += int(numero) * peso
    peso -= 1

resto = soma % 11

if resto < 2:
    dv2 = 0
else:
    dv2 = 11 - resto

print("O 11º número do CPF é:", dv2)
