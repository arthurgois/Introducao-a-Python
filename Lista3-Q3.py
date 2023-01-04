#JOGO DA FORCA
import time
import getpass      #modulo para receber senhas, que no caso, usei para receber a palavra secreta sem exibir na tela

def cronometro(end, start):              #criei uma funcao que serve como cronometro e imprime na tela o tempo em hr, min e seg.
    tempo = end - start
    tempoH = (tempo/60)/24
    horas = int(tempoH)

    tempoM = (tempoH - horas)*24
    minutos = int(tempoM)

    tempoS = (tempoM - minutos)*60
    segundos = int(tempoS)

    print(horas, "h, ", minutos, "min, ", segundos, "seg.\n")

print("\n----------JOGO DA FORCA----------")
print("Voce tem 10 tentativas (erradas) para desvendar a a palavra secreta!\n")
p = list(map(str, getpass.getpass("Entre com a palavra secreta: ").strip()))        #usando a funcao getpass para receber a palavra em sigilo
start = time.time()         #registrando na variavel start o tempo em que a partida comeca
c = p.copy()                #fazendo uma copia da palavra para manipula-la

w = []                  
for i in range (0, len(p)): #criando os tracinhos para representar a palavra
    w.append('_')
cont = 0                    #zerando o contador. Nele, ficarão registrados os erros.
while cont < 10:            #o 10 é o numero de tentativas erradas que a pessoa tem
    print("\nAdvinhe:   ",*w)
    letra = input("\nEntre com a letra: ")  #recebe o palpite
    if letra in c:          #se a letra estiver na palavra
        while c.count(letra)>0:     #o loop encontra o indice da letra em todas as suas ocorrencias e as coloca no lugar do "_" na lista w
            idx = c.index(letra)
            w[idx] = letra
            c[idx] = 0
    else:                   #caso contrario, o contador aumenta 1
        cont += 1
        print("Errou, voce ainda tem {:d} tentativas".format(10-cont))
    if w == p:              #se w (lista dos palpites) for igua
        print("\n       ",*w)
        print("\n       Você ganhou!!")
        end = time.time()
        print("\nA partida teve duração de: ", end='')
        cronometro(end,start)       
        cont = 11           #acaba a partida

if cont == 10:              #se errar 10 vezes
    print("\n       Você perdeu!!")
    print("A palavra era: ", *p)    #mostra a palavra
    end = time.time()
    print("\nPartida teve duração de: ", end='')
    cronometro(end,start)   #função cronometro que printa o tempo da partida