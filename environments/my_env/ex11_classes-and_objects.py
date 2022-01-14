import random

class Enemy:
    atkl = 70
    atkh = 80
    
    def getAtk(self):
        print(self.atkl)
  
enemy1 = Enemy()
enemy1.getAtk()     

enemy2 = Enemy()
enemy2.getAtk()  

      
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