print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
tool=input('As you\'re preparing for your mission, you may choose one tool to aid you. Type "knife" to bring a knife, or "rope" to bring rope-> ').lower()

direction=input("\nThere are two clearly marked paths on the old worn-out map. The left path is shorter, but you must cross a river. The right path is longer, and is known for booby traps. Type 'left' or 'right' to choose your path. -> ").lower()

if direction=="left":
    raccoon=input("\nYou have chosen the left path. As you travel along, you approach a raccoon, entangled in a hunter\'s trap. You can choose to free the raccoon. Type 'free' to let the raccoon loose, or 'ignore' to leave the raccoon to the hunter.  -> ").lower()
    if raccoon =="free":
        river=input("\nYou carefully free the raccoon and it scurries off into the woods. \nThe sound of rushing water grows louder as you trek down the path. As you approach the river, you notice a rickety bridge over a rushing river. You can choose to try to cross the rickety bridge, or attempt to ford the river. Type 'cross' to try the bridge, and 'ford' to cross without it.  -> ")
        if river=="cross":
            if (tool=="rope"):
                print("\nHalfway across the bridge, you notice the rope on the bridge start to fray. Luckily, you brought extra rope! You secure the bridge and cross unharmed. ")
                treasure=input("\nYou have reached the treasure! There is an old wooden sign post that reads \n'You\'ve made it here! But beware:this gimmick.\nOne has treasure, the others are mimics.\nBefore you can choose, the raccoon you saved appears, running to the red chest. The red chest transforms, consumes the raccoon, and disappears. Now you must choose. Do you open the green, or blue chest? Type which color you want to try  -> ").lower()
                if treasure== "green":
                    print("The chest opens! You are welcomed with pound of gold coins, pearls, and other treasure. Congrats! You won!")
                else: print("\nAs you approach the chest, it transforms. It is a mimic! You are quickly consumed. Game over.")
            else: print("\nHalfway across the bridge, you notice the rope on the bridge start to fray. You fall into the raging river. Game over.")
        else: treasure=input("\nYou carefully hop from stone to stone, successfully crossing the river.\nYou have reached the treasure! There is an old wooden sign post that reads\n 'You\'ve made it here! But beware:this gimmick.\nOne has treasure, the others are mimics.\nNow you must choose. Do you open the red, green, or blue chest? Type which color you want to try  -> ").lower()


       

else: 
    raccoon=input("\nAs you travel along, you approach a raccoon, entangled in a hunter\'s trap. You can choose to free the raccoon. Type 'free' to let the raccoon loose, or 'ignore' to leave the raccoon to the hunter.  -> ").lower()
    if raccoon =="free":
        if tool =="knife":
            print("\nYou carefully free the raccoon and it scurries off into the woods. \nYou travel along the path, keeping a watchful eye out for traps. You see a wire stretching along the trail.\nYou remember your trusty tool. Pulling out the knife, you cut the wire, causing a series of booby traps to be set off down the trail. Luckily, once all the traps have been set, you are clear to continue.")
            treasure=input("\nYou have reached the treasure! There is an old wooden sign post that reads \n'You\'ve made it here! But beware:this gimmick.\nOne has treasure, the others are mimics.\nBefore you can choose, the raccoon you saved appears, running to the red chest. The red chest transforms, consumes the raccoon, and disappears. Now you must choose. Do you open the green, or blue chest? Type which color you want to try  -> ").lower()
            if treasure== "green":
                print("\nThe chest opens! You are welcomed with pound of gold coins, pearls, and other treasure. Congrats! You won!")
            else: print("\nAs you approach the chest, it transforms. It is a mimic! You are quickly consumed. Game over.")
        else: print("\nYou carefully free the raccoon and it scurries off into the woods. \nYou travel along the path, keeping a watchful eye out for traps. You see a wire stretching along the trail.\nYou carefully step over the wire, but get tangled and fall flat on your face. You are quickly met with the fate of several boulders crushing you.' Game over.")
    else: print("\nYou carefully free the raccoon and it scurries off into the woods. \nYou travel along the path, keeping a watchful eye out for traps. You see a wire stretching along the trail.\nYou carefully step over the wire, but get tangled and fall flat on your face. You are quickly met with the fate of several boulders crushing you.' Game over.")