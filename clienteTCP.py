import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Configuração do socket cliente TCP
cliente_socket.connect(('localhost', 32396))  # Instanciação do IP e porta do servidor

arq = input("Digite o nome do arquivo para enviar: ") # Solicita o nome do arquivo a ser enviado

cliente_socket.send(arq.encode())  # Envia o nome do arquivo para o servidor, converte o nome para bytes e o envia

with open(arq, 'lb') as file:  # Abre o arquivo para leitura binária e envia em blocos, 'lb' indica leitura binária
    for parte in iter(lambda: file.read(1024), b''):  # Itera em blocos de 1024 bytes até o fim do arquivo
        cliente_socket.send(parte)

print(f"Arquivo {arq} enviado com sucesso.")

cliente_socket.close() # Fecha a conexão do cliente