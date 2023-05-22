import re

primeiro_verificador = 0
segundo_verificador = 0

def validar_cpf():
    primeira_soma = 0
    segunda_soma = 0
    
    primeira_div = 0

    n1 = cpf[0]
    n2 = cpf[1]
    n3 = cpf[2]
    n4 = cpf[4]
    n5 = cpf[5]
    n6 = cpf[6]
    n7 = cpf[8]
    n8 = cpf[9]
    n9 = cpf[10]
    n10 = cpf[12]
    n11 = cpf[13]

    nums_cpf = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

    primeira_multi = []
    segunda_multi = []

    indice = 10

    for i in nums_cpf:
        primeira_multi.append(int(i)*indice)
        indice = indice - 1
    
    for i in primeira_multi:
        primeira_soma += i

    primeira_div = primeira_soma%11

    if primeira_div < 2:
        primeiro_verificador = 0
    else:
        primeiro_verificador = 11 - primeira_div

    indice = 11
    nums_cpf.append(n10)

    for i in nums_cpf:
        segunda_multi.append(int(i)*indice)
        indice = indice - 1

    for i in segunda_multi:
        segunda_soma += i

    segunda_div = segunda_soma%11

    if segunda_div < 2:
        segundo_verificador = 0
    else:
        segundo_verificador = 11 - segunda_div

    if int(n10) == int(primeiro_verificador) and int(n11) == int(segundo_verificador):
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")

def validar_formato():
    if not re.search("\d{3}.\d{3}.\d{3}-\d{2}", cpf):
        print("Seu CPF está escrito da maneira errada. O formato desejado é este: 000.000.000-00.")
    else:
        validar_cpf()

cpf = input("Digite o seu CPF: ")
validar_formato()