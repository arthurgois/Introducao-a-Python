import Matematica as m      #importando o modulo matematica

#definindo as funcoes
def areacirc(r):                        #funcao que retorna a area de um circulo de raio r
    a = m.multiplicacao(m.pi, m.expon(r,2))
    return a

def circunf(r):                         #funcao que retorna a medida de uma circunferencia de raio r
    c = m.multiplicacao(2,m.multiplicacao(m.pi,r))
    return c

def volumereto(a,b,c):                  #funcao que retorna o volume de um prisma reto de lados a, b, c
    v = m.multiplicacao(c,m.multiplicacao(a,b))
    return v

def volumesfera(r):                     #funcao que retorna o volume de uma esfera de raio r
    v = m.multiplicacao(m.divisao(4,3), m.multiplicacao(m.pi, m.expon(r,3)))
    return v

while True:                             #interface
    print("\n---------- Matematica ----------")
    print("Qual operacao deseja realizar?")
    print("1. Area do circulo")
    print("2. Medida da circunferencia")
    print("3. Volume de um prisma reto")
    print("4. Volume de uma esfera")
    print("Caso deseje sair, digite 'sair'.")
    print("--------------------------------")
    
    op = input("Insira o numero correspondente a operacao: ")
    print("--------------------------------")
    
    if op == 'sair':        #quebra o loop, se a pessoa digitar "sair"
        break
    elif int(op) == 1:
        print("\n----------Area do circulo----------")
        r = float(input("Digite o raio: "))
        a = areacirc(r)
        print("area do circulo de raio {:.2f}: {:.2f}".format(r,a))
        print("--------------------------------")
    elif int(op) == 2:
        print("\n------Medida da circunferencia------")
        r = float(input("Digite o raio: "))
        c = circunf(r)
        print("medida da circunferencia de raio {:.2f}: {:.2f}".format(r,c))
        print("--------------------------------")
    elif int(op) == 3:
        print("\n------Volume de um prisma reto------")
        a = float(input("Digite o lado a: "))
        b = float(input("Digite o lado b: "))
        c = float(input("Digite o lado c: "))
        v = volumereto(a,b,c)
        print("volume do prisma de lados {:.2f}, {:.2f}, {:.2f}: {:.2f}".format(a,b,c,v))
        print("--------------------------------")
    elif int(op) == 4:
        print("\n------Volume de uma esfera------")
        r = float(input("Digite o raio: "))
        v = volumesfera(r)
        print("volume de uma esfera de raio {:.2f}: {:.2f}".format(r,v))
        print("--------------------------------")
    #elif...
    else:
        print("\n--------------------------------------------")
        print("Entrada invalida, por favor tente novamente.")
        print("--------------------------------------------")