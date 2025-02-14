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

def battle(tanques):
    while len(tanques) > 1:
        sniper = random.choice(tanques)  #escolhe um tanque aleatório para atirar
        target = [t for t in tanques if t != sniper]
        if not target:
            break
        target = random.choice(target)  #escolhe um alvo aleatório
        sniper.fire_at(target)  #tanque atira no alvo

        tanques = [t for t in tanques if t.alive] #remove tanques destruídos

        print("\nBattle Status:") #mostra status após cada rodada
        for t in tanques:
            print(t)

    print("\nThe Winner is", tanques[0].name)

meusTanques = [Tank("Tiger I"), Tank("M1 Abrams"), Tank("Comet Cruiser"), Tank("StuG III"), Tank("Marder II")] #crie 5 objetos e armazene-os objetos em um array

battle(meusTanques)