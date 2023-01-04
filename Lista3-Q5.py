LARGURA = 76                             #largura maxima de 76 caracteres
LINHAS = 60                              #quantidade de linhas por pagina
ARQUIVO = "textoqualquer.txt"            #arquivo original

def verif_pag(file, linha, pagina):      #funcao que escreve no centro do rodape o nome do arquivo e a pagina
    if linha == LINHAS:
        rodape = f"|| {ARQUIVO} - Página: {pagina} ||"
        file.write(rodape.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1
    return linha, pagina

def escreve(file, linha, nlinhas, pagina):  #funcao que escreve as linhas
    file.write(linha + "\n")
    return verif_pag(file, nlinhas + 1, pagina)

file = open(ARQUIVO, encoding="utf-8")
new = open("arq-q5.txt", "w", encoding="utf-8")

linhas = 1
pagina = 1

for linha in file.readlines():          #vai de linha em linha do arquivo original
    palavras = linha.rstrip().split(" ")#faz uma lista de palavras. Separando as palavras a cada espaco usando split()
    linha = ""
    for p in palavras:                  #vai adiconando de palavra em palavra na linha, ate chegar no limite da largura
        p = p.strip()
        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(new, linha, linhas, pagina)   #escrevendo no arquivo novo
            linha = ""                  #zera a linha
        linha += p + " "                #e adiciona a palavra + espaco
    if linha != "":                     #se a linha for diferente da linha vazia
        linhas, pagina = escreve(new, linha, linhas, pagina)#escreve a linha no arquivo novo

#para imprimir o nome do arquivo original e o número da última página
while(linhas != 1):
    linhas, pagina = escreve(new, "", linhas, pagina)

#fechando os arquivos
file.close()
new.close()