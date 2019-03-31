import tkinter as tk
import random

global Damage
global AttackerAC
global EnemyRoll

class mobBattle:
    def __init__(self,enemies,hd,numberofHd,hdModification,ac,attackDice,attackDiceNo,attackModifier,toHit):
        self.enemies = enemies
        self.hd = hd
        self.numberofHd = numberofHd
        self.hdModification = hdModification
        self.enemyHealth = []
        self.enemiesLeft = len(self.enemyHealth)
        self.ac = ac
        self.attackDice = attackDice
        self.attackDiceNo = attackDiceNo
        self.attackModifier = attackModifier
        self.toHit = toHit
        self.makeEnemyList()

    def makeEnemyList(self):
        enemyHealth = []
        for i in range(0, self.enemies):
            health = (random.randint(1,self.hd) * self.numberofHd) + self.hdModification
            enemyHealth.append(health)
        # enemyHealth.sort()
        self.enemyHealth = enemyHealth
        self.enemiesLeft = len(self.enemyHealth)
        return enemyHealth
    
    def add(self,list):
        total = 0
        for i in list:
            total += i
        return total

    def mobAttacks(self,roll,AC):
        listOfValues = []
        hits = 0
        for x in range(self.enemiesLeft):
            if roll-x+self.toHit > 0 and roll+x+self.toHit <= 20+self.toHit:
                listOfValues.append(random.randint((roll-x+self.toHit),(roll+x+self.toHit+1)))
            elif roll-x+self.toHit < 0 and roll+x+self.toHit <= 20+self.toHit:
                listOfValues.append(random.randint(1,(roll+x+self.toHit+1)))
            elif roll-x+self.toHit < 0 and roll+x+self.toHit >= 20+self.toHit:
                listOfValues.append(random.randint(1,(20+self.toHit+1)))
            elif roll-x+self.toHit > 0 and roll+x+self.toHit >= 20+self.toHit:
                listOfValues.append(random.randint((roll-x+self.toHit),(20+self.toHit+1)))      
        valueOfList = self.add(listOfValues)
        meanOfList = round(valueOfList/self.enemiesLeft,None)
        iterations = 0
        while meanOfList != roll+self.toHit:
            listOfValues = []
            for x in range(self.enemiesLeft):
                if roll-x+self.toHit > 0 and roll+x+self.toHit <= 20+self.toHit:
                    listOfValues.append(random.randint((roll-x+self.toHit),(roll+x+self.toHit+1)))
                # elif roll-x+self.toHit < 0 and roll+x+self.toHit <= 20+self.toHit:
                #     listOfValues.append(random.randint(1,(roll+x+self.toHit+1)))
                # elif roll-x+self.toHit < 0 and roll+x+self.toHit >= 20+self.toHit:
                #     listOfValues.append(random.randint(1,(20+self.toHit+1)))
                elif roll-x+self.toHit > 0 and roll+x+self.toHit >= 20+self.toHit:
                    listOfValues.append(random.randint((roll-x+self.toHit),(20+self.toHit+1)))  
                else:
                    listOfValues.append(random.randint((roll-x+self.toHit),(roll+x+self.toHit+1)))   
            valueOfList = self.add(listOfValues)
            meanOfList = round(valueOfList/self.enemiesLeft,None)
            iterations += 1
        if meanOfList == roll+self.toHit:
            for n, x in enumerate(listOfValues):
                if x < 1:
                    listOfValues[n] = 1
                if x > 20+self.toHit:
                    listOfValues[n] = 20+self.toHit   
                if x >= AC:
                    hits += 1
            listOfValues.sort()
            print(listOfValues)
            print("It took " + str(iterations) + " to get this value")
        return hits

    def damage(self,attacks):
        damageList = []
        for x in range(0,attacks):
            damageList.append(self.damageDice())
        total = self.add(damageList)
        damageList.sort(reverse=True)
        print("Total Damage: "+ str(total))
        print(damageList)
        return damageList

    def damageDice(self):
        damageValue = (self.attackDiceNo * random.randint(1,self.attackDice)) + self.attackModifier
        return damageValue

    def hit(self,a):
        # positive = self.add(a)
        positive = a
        value = -positive
        print(self.enemyHealth)
        resultingList = self.enemyHealth.copy()
        for x in self.enemyHealth:
            result = x+value
            if result <= 0:
                value = result
                del resultingList[0]
            elif result > 0:
                resultingList[0] = result
                value = result
                break
        # resultingList.sort()
        self.enemyHealth = resultingList
        self.enemiesLeft = len(resultingList)
        print(str(self.enemiesLeft) + " Enemies Remain")
        return resultingList

def startState():
    def createMob():
        enemies = int(entry1.get())
        hd = int(entry2.get())
        numberofHd = int(entry3.get())
        hdMod = int(entry4.get())
        ac = int(entry5.get())
        attackDice = int(entry6.get())
        attackDiceNo = int(entry7.get())
        attackModifier = int(entry8.get())
        toHit = int(entry9.get())
        mob = mobBattle(enemies,hd,numberofHd,hdMod,ac,attackDice,attackDiceNo,attackModifier,toHit)
        return mob

    def changeWindow():
        list = window.grid_slaves()
        for l in list:
            l.destroy()

    def damageValue():
        global Damage
        damage = int(Damage.get())
        return damage
    
    def attackValue():
        global AttackerAC
        global EnemyRoll
        roll = int(EnemyRoll.get())
        ac = int(AttackerAC.get())
        response = mob.mobAttacks(roll,ac)
        damageValue = mob.damage(response)
        return damageValue

    def state2(res,number):
        EnemyHealth = tk.Label(master=window, text=res)
        EnemyHealth.grid(column=1,row=1)
        label1 = tk.Label(master=window, text='Enemies Health:')
        label1.grid(column=0,row=1)
        label2 = tk.Label(master=window,text='Enemies Remaining:')
        label2.grid(column=0, row=2)
        EnemiesLeft = tk.Label(master=window, text=number)
        EnemiesLeft.grid(column=1,row=2)
        section1 = tk.Label(master=window, text='Attack With Mob')
        section1.grid(columnspan=2,row=3)
        global EnemyRoll
        EnemyRoll = tk.Entry(master=window)
        EnemyRoll.grid(column=1,row=4)
        RollLabel = tk.Label(master=window, text='Mob Roll:')
        RollLabel.grid(column=0,row=4)
        global AttackerAC
        AttackerAC = tk.Entry(master=window)
        AttackerAC.grid(column=1,row=5)
        RollLabel2 = tk.Label(master=window, text='AC Attacked:')
        RollLabel2.grid(column=0,row=5)
        section1 = tk.Label(master=window, text='Damage This Mob')
        section1.grid(columnspan=2,row=6)
        attackWithIt = tk.Button(text="Attack With Mob", command=attackWithMob)
        attackWithIt.grid(columnspan=2,row=7)
        global Damage
        Damage = tk.Entry(master=window)
        Damage.grid(column=1,row=8)
        RollLabel3 = tk.Label(master=window, text='Damage to Mob:')
        RollLabel3.grid(column=0,row=8)
        damageit = tk.Button(text="Damage Mob", command=damageMob)
        damageit.grid(columnspan=2,row=9)
        button1 = tk.Button(text="Reset", command=reset)
        button1.grid(columnspan=2,row=12)

    def setupClick():
        global mob
        mob = createMob()
        changeWindow()
        response = mob.enemyHealth
        number = str(mob.enemiesLeft)
        s = [str(i) for i in response]
        res = ",".join(s)
        state2(res,number)
        
    def damageMob():
        damage = damageValue()
        changeWindow()
        mob.hit(damage)
        response = mob.enemyHealth
        number = str(mob.enemiesLeft)
        s = [str(i) for i in response]
        res = ",".join(s)
        state2(res,number)
    
    def attackWithMob():
        attackList = attackValue()
        x = [str(i) for i in attackList]
        attackHits = ",".join(x)
        hitValue = mob.add(attackList)
        totalValue = str(hitValue)
        attackHits = attackHits + ' - Total Hit Damage: ' + totalValue
        changeWindow()
        response = mob.enemyHealth
        number = str(mob.enemiesLeft)
        s = [str(i) for i in response]
        res = ",".join(s)
        state2(res,number)
        sectionlast = tk.Label(master=window, text='Attack Values:')
        sectionlast.grid(columnspan=2,row=10)
        damageLabel = tk.Label(master=window, text=attackHits)
        damageLabel.grid(columnspan=2,row=11)
        button1 = tk.Button(text="Reset", command=reset)
        button1.grid(columnspan=2,row=12)

    global window
    window = tk.Tk()
    window.title("Mob Attack and Damage Calculator")
    label1 = tk.Label(text="DND Mob Attack Calculator")
    label1.grid(columnspan=2,row=0)
    label2 = tk.Label(text="How Many Enemies")
    label2.grid(column=0,row=1)
    label3 = tk.Label(text="Enemy HD")
    label3.grid(column=0,row=2)
    label4= tk.Label(text="Number of HD")
    label4.grid(column=0,row=3)
    label5 = tk.Label(text="HD Modifier")
    label5.grid(column=0,row=4)
    label6 = tk.Label(text="Enemy AC")
    label6.grid(column=0,row=5)
    label7 = tk.Label(text="Attack Dice")
    label7.grid(column=0,row=6)
    label8 = tk.Label(text="Number of AD")
    label8.grid(column=0,row=7)
    label9 = tk.Label(text="Damage Modifier")
    label9.grid(column=0,row=8)
    label10 = tk.Label(text="To Hit Value")
    label10.grid(column=0,row=9)

    # Entry
    entry1 = tk.Entry()
    entry1.grid(column=1,row=1)
    entry2 = tk.Entry()
    entry2.grid(column=1,row=2)
    entry3 = tk.Entry()
    entry3.grid(column=1,row=3)
    entry4 = tk.Entry()
    entry4.grid(column=1,row=4)
    entry5 = tk.Entry()
    entry5.grid(column=1,row=5)
    entry6 = tk.Entry()
    entry6.grid(column=1,row=6)
    entry7 = tk.Entry()
    entry7.grid(column=1,row=7)
    entry8 = tk.Entry()
    entry8.grid(column=1,row=8)
    entry9 = tk.Entry()
    entry9.grid(column=1,row=9)

    # Start Button
    button1 = tk.Button(text="Create Mob", command=setupClick)
    button1.grid(columnspan=2,row=10)
    window.mainloop()
    
if __name__ == '__main__':
    def reset():
        window.destroy()
        startState()
    startState()
