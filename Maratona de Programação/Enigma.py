mensagem = input()
crib = input()
tamanho = len(crib)
possibilidades = 0

for i in range(len(mensagem) - tamanho + 1):
    trecho = mensagem[i:i + tamanho]
    if all(trecho[j] != crib[j] for j in range(tamanho)):
        possibilidades += 1

print(possibilidades)