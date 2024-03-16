import socket

while (True):
    host = input ("Digite o host a ser escaneado: ")
    port = int(input("Informe a porta a ser escaneada: "))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    conn = client.connect_ex((host, port))

#Define se a porta está aberta ou fechada de acordo com o valor retornado da conexão
    if conn != 0:
        conexao = "Fechada"
    else:
        conexao = "Aberta"

#Exibe a porta e se a mesma está aberta ou fechada
    print ("Porta \tConexão\n", port, "\t",conexao)
    cntrl = int(input("Digite 0 para encerrar ou 1 para continuar: "))
    if cntrl == 0:
        client.close()
        break
    elif cntrl == 1:
        print("Continuando...\n")
    else:
        print("Opção não encontrada, encerrando programa...\n")
        client.close()
        break