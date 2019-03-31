# DnD-Mob-Battles
This small application is designed to permit DMs to run mob battles in DND in a simple way, but still have the depth and randomness that using the dice for each member of the mob would permit

Running the App
----
Everything including the class that runs the mob logic is all in the same script 'gui.py'. Also there are only native libaries from python3.6. So to run simply make sure you're using python3 and then run the gui.py script from the commpand line with
`python3 gui.py`

How it Works
----
1. Setup
When you run the app, or you click the reset button, you will be asked to enter the base stats of the mob
- How Many Enemies
This is the number of enemies you want in the mob
- Enemy HD
The HD (as in the number of sides), that the enemy has, for a d10 enter just '10' for a d4 enter just '4 etc.
- Number of HD
The number of HD that are used to calculate the health of an individual creature in the mob. for example (3d8 + 2), would mean enter 3 in this field
- HD Modifier
The + value that shows next to the creatures HD, so in the above example you would enter 2. If you have no modifier you must enter 0 (the space can't be empty)
- Enemy AC
The AC of the creature
- Attack Dice
Like HD, just enter the value of the number of sides on the dice, so d12 for a great axe, just enter '12'
- Number of AD
The number of the dice to be rolled for each attack
- Damage Modifer
Any extra value entered so (1d12 + 3) would mean in this value enter the '3'
- To Hit Value
What is the value to hit in the monster stats +5 to hit, enter 5

2. Attack with Mob
To attack with your newly created mob, just roll one d20 on the table and then enter the vale in the screen. Then enter the AC of the target the mob is attacking.
When you click 'Attack with this mob' the system will then roll a d20 and add the 'to hit' modifier for each creature in the mob. It will keep rolling numbers until the average of all the rolls for the mob equals the roll you entered. This means that you get a spread of hit and miss based on the roll and the AC you provided adding some randomness to the game.
It will provide you with the damage that the mob manages to do.

3. Damage Mob
Simply enter the Damage you want to do the mob in the box and click. This will subtract from the enemies in the mob. If you manage to kill one of the enemies, the rest of the damage will carry over.