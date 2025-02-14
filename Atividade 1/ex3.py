import random

class Tank(object):
    def __init__(self, name):
        self.name = name    #nome do tanque
        self.alive = True   #para saber se o tanque está vivo ou não
        self.ammo = 5       #para armazenar a munição do tanque
        self.armor = 60     #para armazenar a armadura do tanque

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <= 0:
            self.explode()

    def fire_at(self, enemy):
        if self.ammo >=1: #verifica a qtde de balas
            self.ammo -=1 #subtrai uma bala ref a um tiro
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

def create_tanques():
    num_tanques = 0
    while num_tanques < 2 or num_tanques > 10:
        try:
            num_tanques = int(input("How many tanks do you want? (2-10): "))
        except ValueError:
            print("Please write a number between 2 and 10.") #mensagem de erro

    tanques = {}  #dicionário para armazenar os tanques criados

    for i in range(num_tanques):
        name = input(f"Register the tank name {chr(97 + i)}: ") #solicita o nome do tanque, sendo o nome gerado com letras
        tanques[chr(97 + i)] = Tank(name) #adiciona o tanque ao dicionário de tanques

    return tanques

def loop(tanques):
    while len([t for t in tanques.values() if t.alive]) > 1:
        snipers = [key for key, tanque in tanques.items() if tanque.alive]
        sniper = random.choice(snipers) #escolhe aleatoriamente um jogador para ser o atirador
        print(f"\n{tanques[sniper].name} is the sniper!")

        rivals = [key for key in snipers if key != sniper] #cria uma lista de oponentes com os oponentes do atirador
        if not rivals:
            break

        print("Rivals:")
        for r in rivals:
            print(f"{r}: {tanques[r]}")

        target = ""  #solicita ao jogador para escolher um oponente para atirar
        while target not in rivals:
            target = input(f"Choose one rival to shoot ({', '.join(rivals)}): ")

        tanques[sniper].fire_at(tanques[target])

        tanques = {k: v for k, v in tanques.items() if v.alive} #atualiza o dicionário de tanques para remover os destruídos

        print("\Battle Status:") #exibe o status atual da batalha
        for t in tanques.values():
            print(t)

    winner = [t for t in tanques.values() if t.alive][0]
    print(f"\nThe winner is {winner.name}!") #após o loop, exibe o tanque sobrevivente

tanques = create_tanques()
loop(tanques)