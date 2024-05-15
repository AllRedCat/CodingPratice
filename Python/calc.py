def sum(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c

print("calculadora em python")

contin = "s"
while contin == "s":
    select = int(input("Qual operação você quer fazer \n1: Soma\n2: Subtracao\n3: Multiplicacao\n"))
    a = int(input("Primeiro Valor: "))
    b = int(input("Segundo Valor: "))

    if (select == 1):
        result = sum(a, b)
        print(result)
    elif (select == 2):
        result = sub(a, b)
        print(result)
    elif (select == 3):
        result = mul(a, b)
        print(result)
    else:
        print("Operacao inesistente!")

    contin = input("Quer fazer outra operacao? (s/n): ")
