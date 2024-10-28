import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Configuração do socket UDP do cliente
servidor_address = ('localhost', 32396)  # IP e porta do servidor

while True:
    message = input("Cliente: ") # Envia mensagem para o servidor
    cliente_socket.sendto(message.encode(), servidor_address)  # Codifica e envia a mensagem como bytes

    if message.strip().upper() == "QUIT": # Verifica se o cliente enviou "QUIT" para encerrar o chat
        print("Cliente encerrou a conexão do socket.")
        break

    data, _ = cliente_socket.recvfrom(1024)  #  Recebe resposta do servidor
    resp = data.decode()  # Decodifica os dados recebidos para string
    print(f"Servidor: {resp}")

    if resp.strip().upper() == "QUIT": # Encerra se o servidor enviar "QUIT"
        print("Servidor encerrou a conexão do socket.")
        break

cliente_socket.close()  # Fecha o socket do cliente