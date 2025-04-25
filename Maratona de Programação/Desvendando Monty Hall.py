n = int(input())
ganhos = 0

for _ in range(n):
    porta_carro = int(input())
    if porta_carro != 1:  # jogador sempre começa com a 1 e sempre troca
        ganhos += 1

print(ganhos)