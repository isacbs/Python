import socket

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Configuração do socket servidor UPD
servidor_socket.bind(('localhost', 32396))  # Instanciação do IP e porta do servidor

print("Servidor está apto para receber mensagens.")

while True: # Recebe mensagem do cliente
    data, cliente_address = servidor_socket.recvfrom(1024)
    message = data.decode()  # Decodifica os dados recebidos para string
    print(f"Cliente: {message}")

    if message.strip().upper() == "QUIT": # Verifica se o cliente enviou "QUIT" para encerrar o chat
        print("Cliente encerrou a conexão.")
        break

    resp = input("Servidor: ") # Envia a resposta
    servidor_socket.sendto(resp.encode(), cliente_address)  # Codifica a string

    if resp.strip().upper() == "QUIT": # Encerra se o servidor enviar "QUIT"
        print("Servidor encerrou a conexão.")
        break

servidor_socket.close()  # Encerra o socket do servidor