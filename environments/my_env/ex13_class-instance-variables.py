import random

class Enemy:
    hp = 200
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
         
    
    def getAtk(self):
        print("atk is", self.atkl)
    
    def getHp(self):
        print("Hp is", self.hp)
        
        
enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp() 

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()

enemy3 = Enemy(90, 120)
enemy3.getAtk()
enemy3.getHp() 

      
'''       
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg
    
    if playerhp <= 30:
        playerhp = 30
        
    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)
    
    if playerhp > 30:
        continue
    
'''