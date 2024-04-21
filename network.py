import socket
commonPorts = [20, 21, 22, 23, 80, 110, 443]
services = ["FTP   ", "FTP   ", "SSH   ", "Telnet", "HTTP   ", "POP3   ", "HTTPS   "]
#Espaço nas siglas dos protocolos, pois o telnet ultrapassa o espaço de uma tabulação,
#logo, para printar se a porta estava aberta ou não, acaba contando duas tabulação
#então, todos tendo um tamanho maior de caracteres traz esse "bug" para todas as siglas.

while (True):
    cntrl0 = int(input("Escolha um das opções abaixo:\n1\tEscolher uma porta individual a ser escaneada\n2\tEscanear portas comuns\n"))
    
    host = input("Informe o host a ser escaneado: ")

    if cntrl0 == 1:
        port = int(input("Informe a porta a ser escaneada: "))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        conn = client.connect_ex((host, port))
        if conn != 0:
            conexao = "Fechada"
        else:
            conexao = "Aberta"
        #Exibe a porta e se a mesma está aberta ou fechada
        print ("Porta \tConexão\n", port, "\t",conexao)

    if cntrl0 == 2:
        print("\nPorta\tServiço\t\tConexão")
        for i in range(7):
        #Range de 7, pois são 7 portas a serem escaneadas, para o próximo update: deixar de acordo com o tamanho do array de portas
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.1)
            conn = client.connect_ex((host, commonPorts[i]))
            if conn != 0:
                conexao = "Fechada"
            else:
                conexao = "Aberta"
            #Exibe a porta e se a mesma está aberta ou fechada
            print (commonPorts[i], "\t", services[i], "\t", conexao)

#Define se a porta está aberta ou fechada de acordo com o valor retornado da conexão
    
    cntrl1 = int(input("\nDigite 0 para encerrar ou 1 para continuar: "))
    if cntrl1 == 0:
        client.close()
        break
    elif cntrl1 == 1:
        print("Continuando...\n")
    else:
        print("Opção não encontrada, encerrando programa...\n")
        client.close()
        break