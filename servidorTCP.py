import socket

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Configuração do socket servidor TCP
servidor_socket.bind(('localhost', 32396))  # Instanciação do IP e porta do servidor
servidor_socket.listen(1)

print("Servidor esperando a conexão acontecer")

cnx, end = servidor_socket.accept() # cnx é a conexão e addr é o endereço do cliente
print(f"Conectado a {end}") # Aceita a conexão do cliente

arq = cnx.recv(1024).decode()  # Recebe o nome do arquivo que o cliente enviará e converte para string

with open(arq, 'b') as file:  # 'b' indica que o arquivo será escrito em modo binário
    while True:
        data = cnx.recv(1024)
        if not data:
            break
        file.write(data)  # Escreve o bloco de dados no arquivo

print(f"Arquivo {arq} recebido com sucesso.")

cnx.close() # Fecha a conexão e o socket do servidor
servidor_socket.close()