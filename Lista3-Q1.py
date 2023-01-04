from email.message import EmailMessage
import random
import smtplib
import time

#funcao que envia o email
def sendmail(temp, date):
    sender = "insira o e-mail aqui"          #endereço de email do remetente
    password = "insira a senha"                  #senha do email do remetente
    receiver = "destinatario@email.com"    #endereço de email do destinatario

    message = EmailMessage()
    message['Subject'] = "ALERTA DE TEMPERATURA: Sua máquina superou os 40°C!"      #assunto do email
    message['From'] = sender        #remetente
    message['To'] = receiver        #destinatario
    m = ("Sua máquina atingiu a temperatura de {:.1f}°C em {:s}.".format(temp,date))    #corpo do email
    message.set_content(m)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:       #talvez seja necessário abrir as configurações do e-mail para liberar o uso por outros aplicativos
        smtp.login(sender, password)    #logando no email
        smtp.send_message(message)      #enviando a mensagem

#aqui eu simulo um sensor usando um loop
print("-----Monitoramento de temperatura-----")
aux = True                  #flag
while aux == True:          #enquanto aux for verdade, o loop fica rodando.
    ltemp = list(range(20,61))              #criando uma lista com as temperaturas, como se fosse o range de temperaturas do sensor.
    tempsens = float(random.choice(ltemp))  #variavel que recebe uma temperatura aleatória da lista de temperaturas. Se tivesse um sensor, o sinal dele entraria aqui.
    print("A temperatura da sua maquina é:", tempsens, "em", time.asctime())
    if tempsens > 40:                       #condicao para quando a temperatura superar os 40 graus
        date = str(time.asctime())          #date recebendo os dados de data e hora
        sendmail(tempsens, date)            #chamando a funcao que envia o email alertando a temperatura(tempsens) no momento que ela foi atingida(date)
        print("Email enviado!")             #printando o envio de um email
        aux = False                         #flag = False, quebrando o loop. Caso quisesse fazer monitoramento infinito, basta eliminar essa linha
    time.sleep(5)                     
    
