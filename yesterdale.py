import time###small pauses between blocks of text seemed to improve readibility and make things less confusing###
import sys###this was required for the sys.exit function if they player chooses to terminate the game###
from random import random###used to generate chance throughout the game###
##defines each area of the mall###
class mallArea:
    def __init__(self, name, itemsList, enemy):
        self.name = name
        self.itemsList = itemsList
        self.enemy = enemy
###devines each inventory item###
class inventoryItem:
    def __init__(self, name, description, rarity, pointValue):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.pointValue = pointValue
###defines each enemy###
class enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
###enables changing of font color###
class bcolors:
    cyan = '\033[96m'
    green = '\033[92m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    

    def disable(self):
        self.cyan = ''
        self.green = ''
        self.fail = ''
        self.endc = ''
        self.bold = ''
        self.underline = ''
###list of enemies###
parkingLotGremlin = enemy('Parking Lot Gremlin', 1000)
mallKaren = enemy('Mall Karen', 1000)
tonyTheTeenMallrat = enemy('Tony the Teen Mallrat', 1000)
becky = enemy('Becky', 1000)
brad = enemy('Brad', 1000)
bobTheImpatientOfficeWorker = enemy('Bob the Impatient Office Worker', 1000)
gothTeenJessica = enemy('Goth Teen Jessica', 1000)
techieChris = enemy('Techie Chris', 1000)
kevinTheMusicBuff = enemy('Kevin the Music Buff', 1000)
garyTheMallSanta = enemy('Gary the Mall Santa', 1000)


###this is the default name for the robot dog special item###
companionName = 'Robomax'        
###this is the list of all items in the game, grouped by game area. special items at the bottom###
parkingLotCommonItem = inventoryItem('Dusty Traffic Cone', "It's just a dusty traffic cone, nothing special to see here.", 'Common', 100 )
parkingLotUncommonItem = inventoryItem('AOL Free Trial CD', "It's a free trial disc for America Online, good for 1000 free hours!", 'Uncommon', 200 )
parkingLotRareItem = inventoryItem('Forgotten Beanie Baby', "Uh oh, someone dropped their Beanie Baby in the parking lot!\nIt's Pinky the Flamingo. Maybe it's worth something now?", 'Rare', 500 )

macysCommonItem = inventoryItem('Mom Jeans', 'It\'s a pair of 90\'s-era Mom Jeans, complete with bellybutton-high waist and functional pockets!', 'Common', 100 )
macysUncommonItem = inventoryItem('George Foreman Grill', 'It\'s a George Foreman grill. Taste the meat, not the grease!', 'Uncommon', 200 )
macysRareItem = inventoryItem('Fanny Pack', 'It\'s a purple fanny pack! You will totally wear this unironically.', 'Rare', 500 )

spencersCommonItem = inventoryItem('Dusty Lava Lamp', "It's a dusty lava lamp. I think the bulb is burnt out", 'Common', 100 )
spencersUncommonItem = inventoryItem('Novelty Plasma Ball', "It's a novelty plasma ball, cool!\nYou put your finger on it and the electric current flows towards you", 'Uncommon', 200 )
spencersRareItem = inventoryItem('Over-the-hill Birthday Cane', "It's a novelty walking cane, equipped with a horn, an 'Old Man Crossing' sign,\nand a convenient carrying case for adult diapers", 'Rare', 500 )

sharperImageCommonItem = inventoryItem('Ionic Breeze Air Purifier', "It's an air purifier that does absolutely nothing!", 'Common', 100 )
sharperImageUncommonItem = inventoryItem('Back Massaging Wand', "It's a massager for your back. And NOTHING ELSE. Only your back.", 'Uncommon', 200 )
sharperImageRareItem = inventoryItem('Toilet Paper Stand with iPod Dock', "It's a toilet paper dispenser with a built in iPod dock!\nStereo speakers help you enjoy your 'me-time' even more.", 'Rare', 500 )

foodCourtCommonItem = inventoryItem('Hot Dog on a Stick', "It's a hot dog. But on a stick!", 'Common', 100 )
foodCourtUncommonItem = inventoryItem('Orange Julius', "Orange and vanilla come together in this sweet and creamy treat!\nIt's a classic mall staple.", 'Uncommon', 200 )
foodCourtRareItem = inventoryItem('Pretzel Dog', "It's a pretzel dog from Auntie Anne's!\nA juicy hot dog wrapped in a fresh, warm pretzel. Comes with nacho cheese dip!", 'Rare', 500 )

clairesCommonItem = inventoryItem('Hair Scrunchie', "It's a standard purple hair scrunchie.", 'Common', 100 )
clairesUncommonItem = inventoryItem('Hello Kitty Earrings', "They're earrings with Hello Kitty on them. Cute!", 'Uncommon', 200 )
clairesRareItem = inventoryItem("90's Tattoo Choker Necklace", "It's a tatooo choker necklace from the 90's. It's the bomb!", 'Rare', 500 )

samGoodyCommonItem = inventoryItem('Sony Discman', "It's a CD player with Electronic Shock Protection and Digital MEGA BASS!" , 'Common', 100 )
samGoodyUncommonItem = inventoryItem('Smashmouth CD', "It's the new Smashmouth album! Somebody once told me this was a good one!", 'Uncommon', 200 )
samGoodyRareItem = inventoryItem('Nirvana Cassette Tape', "It's Nirvana's 'Nevermind' on cassette! Cool! But how are we going to play this?", 'Rare', 500 )

hotTopicCommonItem = inventoryItem('Metallica T-Shirt', "It's a badass Metallica shirt! Sweet!", 'Common', 100 )
hotTopicUncommonItem = inventoryItem('Studded Belt', "It's a belt studded with three rows of metallic pyramids. It's so metal!", 'Uncommon', 200 )
hotTopicRareItem = inventoryItem('10-Pack of Jelly Bracelets', "It's a pack of 10 jelly bracelets in black, red and green.", 'Rare', 500 )

radioShackCommonItem = inventoryItem('Sony Walkman', "It's a portable cassette player. Sweet, now we can listen to that Metallica album!", 'Common', 100 )
radioShackUncommonItem = inventoryItem('Casio Keyboard', "It's a Casio Keyboard. Now you can start that band you and your friends have been talking about!", 'Uncommon', 200 )
radioShackRareItem = inventoryItem('iRiver MP3 Player', "It's an MP3 player with 128mb of storage and an FM tuner!", 'Rare', 500 )

kbToysCommonItem = inventoryItem('Bop-it!', "Bop-it! Pull-it! Twist-it!", 'Common', 100 )
kbToysUncommonItem = inventoryItem('Tamagotchi', "It's a Tamagotchi keychain! I wonder how long it's been since this thing was fed?", 'Uncommon', 200 )
kbToysRareItem = inventoryItem('GameBoy', "It's an original GameBoy from Nintendo. Now you can beat on Bowser on-the-go!", 'Rare', 500 )

specialItem1 = inventoryItem('TJMaxx Coupon', "It's a TJMaxx coupon for 25%-off decorative throw pillows! Sweet! Too bad it expired in 1997.", 'Special', 1000)
specialItem2 = inventoryItem('Bart Simpson T-Shirt', "It's a Bart Simpson T-Shirt, emblazened with his classic catchphrase 'Eat My Shorts!'", 'Special', 1000)
specialItem3 = inventoryItem('Brad\'s Cheesy Love Letter', "It's Brad's cheesy love letter to Becky,\nan apology to her about the Orange Julius incident in the form of a poem.", 'Special', 1000)
specialItem4 = inventoryItem( companionName, "It's your new robotic dog companion! It follows you everywhere. How cute!", 'Special', 1000)
specialItem5 = inventoryItem('Fishnet Fingerless Gloves', "It's a pair of fishnet fingerless gloves! A must-have in the 90's/00's goth scene. Badass!", 'Special', 1000)
specialItem6 = inventoryItem("Becky's Used Lip Gloss", "Becky gave you her used lip gloss! It's cotton candy flavored, and it's at least 2/3 full!\nKinda gross, but it's the thought that counts!", 'Special', 1000)
specialItem7 = inventoryItem("Furby", "It's an old Furby! It keeps staring at you and making weird noises. \nYou can't decide if it's cute or creepy.", 'Special', 1000)
###these lists define acceptable inputs for Yes or No/A, B, or C prompts###
answerA=['a', 'A']
answerB=['b', 'B']
answerC=['c', 'C']
answerYes=['y', 'Y', 'yes', 'Yes', 'YES']
answerNo=['n', 'N', 'no', 'No', 'NO']
###error message for input validation loops###
yesOrNo = ("\nPlease enter either yes or no.\n")
aBorC = ("\nPlease enter A, B or C.\n")
###initialize inventory, score and health###
inventoryList = []
userScore = 0
userHP = 1000
###define divider to provide visual separation between areas###
divider = "\n\n__________________________________________________________________\n"
###initialize number of times player skips to next area###
skipCount = 0
searchValue = 0

def main():
    print(divider)
    global playerName
    print(r"""
┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐
│││├┤ │  │  │ ││││├┤    │ │ │
└┴┘└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘ 

     ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌
    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ 
    ▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          
    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌
     ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ 
         ▐░▌     ▐░▌                    ▐░▌     ▐░▌     ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          
         ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
         ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
          ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
                                                                                       
                                                                                         ███    ███  █████  ██      ██                   
            -.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.   ████  ████ ██   ██ ██      ██  .-.     .-.
              `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._██ ████ ██ ███████ ██      ██.'   `._.'
                                                                                         ██  ██  ██ ██   ██ ██      ██
                                                                                         ██      ██ ██   ██ ███████ ███████ 
      
          
            """)
    playerName = input("Please enter your name: ")
    print( divider )
    ##Game Instructions##
    print(bcolors.bold+"\n\nHello {0}, and welcome to the mall!".format( playerName )+bcolors.endc)
    time.sleep(0.5)
    print("\nYour goal is to make it out of the mall alive while collecting as many items as possible.\nEach item is worth points, which vary based on the rarity of the item.\n\nEach area you search in the mall has three items--one common, one uncommon and one rare.\nThere are also"+bcolors.cyan+bcolors.bold+" seven special items "+bcolors.endc+"hidden throughout the game--try to find them all!\n(Hint: You will not find bonus items by searching!)")
    time.sleep(0.3)
    ###Item Values List###
    print(bcolors.underline+"\nItem Type:          Points:\n"+bcolors.endc)
    print("Common..............100")
    print("Uncommon............200")
    print("Rare................500")
    print("Special.............1000")
    time.sleep(0.3)
    userChoice = input("\n\nSo, {0}, are you ready to begin?\n\n>>> ".format(playerName))
    while True:
        if userChoice in answerYes or userChoice in answerNo:
            break
        userChoice = input("\nI don't understand '{0}', {1}.\nPlease answer either yes or no!\n\n>>> ".format(userChoice, playerName))
    if userChoice in answerYes:
        parkingLot()
    elif userChoice in answerNo:
        print("Goodbye!")
        time.sleep(1)
        sys.exit(0)
###this function is for each stage in the game###        
def gameArea( headerArt, areaDescription, specialAction, commonItem, uncommonItem, rareItem, nextArea, enemy, enemyApproachMsg, attackMsg, attackSuccessMsg, attackFailMsg, negotiationMsg, negotiationSuccessMsg, negotiationFailMsg, fleeFailMsg, fleeSuccessMsg, specialActionFunction ):
    userChoice = ""
    nestedUserChoice = ""
    global skipCount
    global enemyTime
    global userScore
    global inventoryList
    global userHP
    print( divider )
    ###if the player skips three stages they receive this message###
    if skipCount > 2:
        print(bcolors.fail+bcolors.bold+"You're doing that too much, {}!".format(playerName))
        time.sleep(3)
        print("The game is more fun if you search areas,\nsince the goal of the game is to collect items!"+bcolors.endc)
        time.sleep(1)
        print("Do you want to start over?")
        userChoice = input(">>> ")
        if userChoice in answerYes:
            skipCount = 0
            print( divider )
            main()
    ###player has random chance of recovering health between stagess###
    if userHP < 1000:
        if random() > .8:
            print("On your way to the next area you find a broken vending machine with some old candy bars inside!\nYou eat one to regain your strength and recover some HP!")
            vendingHP = int(random() * 600)
            userHP = userHP + vendingHP
            if userHP > 1000:
                userHP = 1000
            print(bcolors.green+bcolors.bold+"\n{0} regains {1} HP. Current HP: {2}".format( playerName, vendingHP, userHP)+bcolors.endc)
            time.sleep(3)
            print( divider )
    print( headerArt )
    print( '\n'+areaDescription )
    time.sleep(0.5)
    print("\nYou consider your options. What do you do?\n")
    time.sleep(0.3)
    print("A. Search the area\nB. Continue on to the next area\nC.", specialAction)
    time.sleep(0.3)
    userChoice = input("\n>>> ")
    while True:
        if userChoice in answerA or userChoice in answerB or userChoice in answerC:
            break
        print( aBorC )
        userChoice = input("\n>>> ")
    ###searching for items###    
    if userChoice in answerA:
        print("\nYou search around the area.")
        enemyTime = 0
        ###initialize number of items left in area to find###
        itemsLeft = 3
        ###enemy time is incremented by some random fraction of 1 for each time a search is conducted###
        ###once enemy time reaches threshold, enemy appears##
        while enemyTime < 2.5:
            ###search value is randomly generated fraction of 1, determines which item is found (if any) based on the criteria below###
            searchValue = random()
            enemyTime = enemyTime + random()
            if searchValue < .4 and commonItem not in inventoryList:
                print(bcolors.bold+bcolors.green+"\n***You found a common item!***"+bcolors.endc)
                time.sleep(0.5)
                print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(commonItem.name, commonItem.description, commonItem.rarity, commonItem.pointValue))
                inventoryList.append(commonItem)
                itemsLeft = itemsLeft - 1
                userScore = userScore + 100
            elif searchValue >= .5 and searchValue < .75 and uncommonItem not in inventoryList:
                print(bcolors.bold+bcolors.green+"\n***You found an uncommon item!***"+bcolors.endc)
                print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(uncommonItem.name, uncommonItem.description, uncommonItem.rarity, uncommonItem.pointValue))
                inventoryList.append(uncommonItem)
                itemsLeft = itemsLeft - 1
                userScore = userScore + 200
            elif searchValue >= .8 and rareItem not in inventoryList:
                print(bcolors.bold+bcolors.cyan+"\n***You found a rare item!***"+bcolors.endc)
                print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(rareItem.name, rareItem.description, rareItem.rarity, rareItem.pointValue))
                inventoryList.append(rareItem)
                itemsLeft = itemsLeft - 1
                userScore = userScore + 500
            else:
                print(bcolors.fail+"\nYou search the area and find nothing."+bcolors.endc)
            if itemsLeft == 0:
                print(bcolors.bold+"\n\nThere are no more items to search for here!"+bcolors.endc)
                time.sleep(1)
                print("\nYou decide to continue exploring elsewhere.")
                time.sleep(0.5)
                nextArea()
            time.sleep(0.3)    
            print("\nTotal score: ", userScore )
            time.sleep(0.3)
            print("\nThere are at least {0} items left to be found here.\nWould you like to keep searching or do something else?\n".format(itemsLeft))
            time.sleep(0.3)
            print("A. Continue Search\nB.", specialAction, "\nC. Continue on to next area")
            userChoice = input(">>> ")
            while True:
                if userChoice in answerA or userChoice in answerB or userChoice in answerC:
                    break
                print( aBorC )
                
                userChoice = input("\n>>> ")
            if userChoice in answerA:
                continue
            elif userChoice in answerB:
                specialActionFunction()
            elif userChoice in answerC:
                nextArea()
        ###enemy approach###
        else:
            print( divider )
            print( "\n"+enemyApproachMsg )
            time.sleep(0.5)
            print("\n\n"+playerName.ljust(33)+"HP: "+str(userHP).ljust(6)+"SCORE: "+str(userScore).ljust(6))
            print("\n"+enemy.name.ljust(33)+"HP: "+str(enemy.hp).ljust(6))
            time.sleep(0.3)
            print( "\n\nWhat do you do?")
            time.sleep(0.3)
            print("\nA. Attack\nB. Negotiate\nC. Flee\n")
            time.sleep(0.3)
            nestedUserChoice = input(">>> ")
            while True:
                if nestedUserChoice in answerA or nestedUserChoice in answerB or nestedUserChoice in answerC:
                    break
                print( aBorC )
                nestedUserChoice = input("\n>>> ")
            ###attack enemy choice###
            while nestedUserChoice in answerA:
                print( "\nYou attack", enemy.name )
                successChance = random()
                if successChance < .7:
                    attackStrength = ''
                    attackDamage = int(random() * 1000)
                    enemy.hp = enemy.hp - attackDamage    
                    if attackDamage <= 200:
                        attackStrength = 'weak'
                    elif attackDamage > 200 and attackDamage < 600:
                        attackStrength = 'moderate'
                    else:
                        attackStrength = 'strong'
                    print( bcolors.bold+bcolors.green+'\n\nYou successfully land a {0} attack and deal'.format( attackStrength), attackDamage, 'HP of damage to', enemy.name+'.'+bcolors.endc)
                    time.sleep(0.5)
                    if enemy.hp < 0:
                        print( bcolors.bold+bcolors.cyan+"\n***{0} successfully defeats {1}!***".format( playerName, enemy.name )+bcolors.endc)
                        time.sleep(0.3)
                        print("\n\n"+playerName.ljust(33)+"HP: "+str(userHP).ljust(6)+"SCORE: "+str(userScore).ljust(6))
                        print("\n"+enemy.name.ljust(33)+"HP: "+'0')
                        time.sleep(3)
                        nextArea()
                    else:
                        print("\n\n"+playerName.ljust(33)+"HP: "+str(userHP).ljust(6)+"SCORE: "+str(userScore).ljust(6))
                        print("\n"+enemy.name.ljust(33)+"HP: "+str(enemy.hp).ljust(6))
                        time.sleep(0.3)
                        print("\n\nWould you like to continue your attack or try something else?")
                        print("\nA. Attack\nB. Negotiate\nC. Flee\n")
                        nestedUserChoice = input(">>> ")
                        if nestedUserChoice in answerA:
                            continue
                        else:
                            break
                if successChance > .7:
                    print( bcolors.fail+'\nYour attack failed!', enemy.name, 'attacks you!'+bcolors.endc )
                    enemyAttackStrength = ''
                    enemyAttackDamage = int(random() * 500)
                    if enemyAttackDamage < 200:
                        enemyAttackStrength = 'weak'
                    else:
                        enemyAttackStrength = 'moderate'
                    time.sleep(0.5)
                    print( bcolors.fail+'\n\n'+enemy.name, 'successfully lands a', enemyAttackStrength, 'attack and deals', enemyAttackDamage, 'HP of damage to you.'+bcolors.endc)
                    userHP = userHP - enemyAttackDamage
                    time.sleep(0.3)
                    if userHP < 0:
                        userHP = 0
                        gameOver()
                    else:
                        print("\n\n"+playerName.ljust(33)+"HP: "+str(userHP).ljust(6)+"SCORE: "+str(userScore).ljust(6))
                        print("\n"+enemy.name.ljust(33)+"HP: "+str(enemy.hp).ljust(6))
                        time.sleep(0.3)
                        print("\n\nWould you like to continue your attack or try something else?")
                        print("\nA. Attack\nB. Negotiate\nC. Flee\n")
                        nestedUserChoice = input(">>> ")
                        if nestedUserChoice in answerA:
                            continue
                        else:
                            break
            ###negotiate with enemy choice###
            if nestedUserChoice in answerB:
                print( '\n'+negotiationMsg )
                time.sleep(0.5)
                successChance = random()
                if successChance > .5:
                    print( bcolors.bold+bcolors.green+'\n'+negotiationSuccessMsg+bcolors.endc )
                    time.sleep(2)
                    nextArea()
                else:
                    print( '\n'+negotiationFailMsg )
                    userScore = userScore - 100
                    print("\nTotal score: ", userScore)
                    time.sleep(2)
                    nextArea()
            ###flee from enemy choice###
            elif nestedUserChoice in answerC:
                successChance = random()
                if successChance < .5:
                    print( bcolors.fail+'\n'+fleeFailMsg+bcolors.endc )
                    userScore = userScore - 100
                    print("\nTotal score: ", userScore)
                    time.sleep(2)
                    nextArea()
                else:
                    print( bcolors.bold+bcolors.green+'\n'+fleeSuccessMsg+bcolors.endc )
                    time.sleep(2)
                    nextArea()
    ###skip area choice###
    elif userChoice in answerB:
        skipCount = skipCount + 1
        nextArea()
    ###special action choice###
    ###each area in the game has a special action, defined in the functions below###
    elif userChoice in answerC:
        specialActionFunction()
def parkingLotSpecialAction():
    print("\nYou run screaming into the night, flailing your arms wildly above your head.\nYou have no idea where you're going, but you know you're NOT going towards that creepy building!\nYou flee into the surrounding forest, never to be seen or heard from again.\n")
    gameOver()
    
def macysSpecialAction():
    global userScore
    global inventoryList
    print("\nYou see all of these mannequins lined up front-to-back and you just can't resist.\nYour inner child needs to be set free!\n\nYou gleefully run up to the first mannequin in the row and gently push it backwards.\nThe entire cavalcade of threadbare mannequins begins to fall, one by one,\ngenerating a tremendous racket that echoes throughout the abandoned store.")
    time.sleep(0.5)
    print("\nYou begin to regret your decision as you hear footsteps rapidly approach from behind.\nYou turn around and see an irate Mall Karen heading towards you!\n\nShe screams 'Why won't they take my expired Kohl's coupons!? I need your corporate number!'\nat no one in particular as she rapidly approaches you.\n\nWhat do you do?")
    time.sleep(0.5)
    print("\nA. Attack\nB. Negotiate\nC. Flee\n")
    time.sleep(0.3)
    nestedUserChoice = input(">>> ")
    while True:
        if nestedUserChoice in answerA or nestedUserChoice in answerB or nestedUserChoice in answerC:
            break
        print( aBorC )
        nestedUserChoice = input("\n>>> ")
        time.sleep(0.3)
    if nestedUserChoice in answerA:
        print("\nYou quickly grab one of the threadbare mannequins and flail it at the Karen in self-defense.")
        time.sleep(0.5)
        successChance = random()
        if successChance < .7:
            print(bcolors.bold+bcolors.green+"\nThe mannequin connects with Karen with an audible 'thwack'. She falls backwards but is cushioned by her stylish hair-do.\nThe Mall Karen is temporarily stunned, let's get the heck out of here!"+bcolors.endc)
            time.sleep(0.5)
            spencers()
        if successChance > .7:
            print(bcolors.fail+"\nYou swing and miss as the more-agile-than-expected Mall Karen swiftly dodges your attack.\nKaren mounts an incredible verbal assault that leaves you feeling gutted and full of shame.\nYou lose 200 points.\nLet's get out of here before she can tear into you any further."+bcolors.endc)
            time.sleep(0.5)
            userScore = userScore - 200
            time.sleep(0.5)
            print("\nTotal score: ", userScore)
            spencers()
    elif nestedUserChoice in answerB:
        print("\nYou attempt to speak with the Mall Karen. Perhaps she will listen to reason?\n")
        time.sleep(0.5)
        print(bcolors.bold+bcolors.cyan+"\nYou sympathize with Karen and make up some story\nabout how you had problems with coupons in the past\nand how awful customer service is these days. This appeases the Mall Karen\nas she warms up to you with your relatable story.\n\nKaren has taken a liking to you, and gifts you a TJMaxx coupon!\n")
        time.sleep(0.3)
        print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(specialItem1.name, specialItem1.description, specialItem1.rarity, specialItem1.pointValue)+bcolors.endc)
        inventoryList.append(specialItem1)
        userScore = userScore + 1000
        print("\nTotal score: ", userScore)
        time.sleep(0.3)
        print("\nLet's move on to the next area.\n")
        time.sleep(3)
        spencers()
    elif nestedUserChoice in answerC:
        successChance = random()
        if successChance < .5:
            print(bcolors.fail+"\nYou attempt to flee. In your haste you damage one of your items, but you manage to escape.\nYou lose 100 points.\n"+bcolors.endc)
            userScore = userScore - 100
            time.sleep(0.5)
            print("\nTotal score: ", userScore)
            time.sleep(2)
            spencers()
        else:
            print(bcolors.bold+bcolors.green+"\nYou successfully escape from the Mall Karen unscathed!\nWhew! That was a close one.\n"+bcolors.endc)
            time.sleep(2)
            spencers()

def spencersSpecialAction():
    global userScore
    global inventoryList
    print( "\nYou decide to check out the back room." )
    time.sleep(2)
    print( "\nYou slowly approach the door and try to peer through the crack in the door\n but it's too bright for you to make out anything.\nYou decide to just go for it and push the door open.\nAs your eyes adjust to the brightness you see...")
    time.sleep(5)
    print( "\nAn empty room with a few empty cardboard boxes on the floor, lit by a single pullstring lightbulb hanging from the ceiling.\nWell that was disappointing." )
    time.sleep(4)
    print( bcolors.bold+bcolors.cyan+"\nBut wait, what's this?\nIn one of the boxes in the corner you see something.\nIt's a Bart Simpson T-Shirt! ¡Ay, caramba!\n" )
    time.sleep(0.3)
    print( "\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(specialItem2.name, specialItem2.description, specialItem2.rarity, specialItem2.pointValue)+bcolors.endc)
    inventoryList.append(specialItem2)
    userScore = userScore + 1000
    time.sleep(0.3)
    print("\nTotal score: ", userScore)
    time.sleep(0.3)
    print("\nLet's move on to the next area.\n")
    time.sleep(1)
    claires()

def clairesSpecialAction():
    global userScore
    global inventoryList
    print("You decide to check out the jewelry cabinet.\nIt looks like there isn't much of interest in here, just a bunch of dusty old earrings and tacky bracelets.\nIn the corner, you see a crumpled up piece of paper. Out of curiosity, you grab it and open it up.\n\nIt's a discarded love letter to Becky, signed by Brad!")
    time.sleep(0.5)
    print("\n    Dear Becky, hey, it's Brad\n       Just wanted to say you're pretty rad\n    Sorry about the Orange Julius\n       I know I can be foolish \n    But I hope you can forgive me, babe!\n      Forever Yours,\n           Brad")
    time.sleep(0.3)
    print("\nAww...how, uh...endearing?")
    time.sleep(0.3)
    print(bcolors.bold+bcolors.cyan+"\nYou got Brad's Cheesy Love Letter!")
    time.sleep(0.3)    
    print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(specialItem3.name, specialItem3.description, specialItem3.rarity, specialItem3.pointValue)+bcolors.endc)
    inventoryList.append(specialItem3)
    userScore = userScore + 1000
    time.sleep(0.3)
    print("\nTotal score: ", userScore)
    time.sleep(0.3)
    print("\nLet's move on to the next area.\n")
    time.sleep(1)
    foodCourt()
    
def foodCourtSpecialAction():
    global userScore
    global inventoryList
    print("You decide to take advantage of the atrium's great acoustics and take some time to practice your yodeling skills!\n\nYodel-ay-heeeeeeeeeee")
    time.sleep(3)
    print("Yodel-ay-HEEEEEEEEEEEEEEEEEEEE!")
    time.sleep(3)
    print("YODELAYHEEEEEEEHOOOOOOOOOOOO!")
    time.sleep(1)
    print(bcolors.fail+"\nYou hear a low rumbling sound coming from above you.\n\nAvalanche!?\nNo...we're in a mall stupid.\nYou look up towards the second-floor walkway to see a tidal wave of bouncy balls coming towards you from the toy store!\nYour glorious pipes must have dislodged an ancient display of balls!\nYou get pummelled by the balls and one of your items becomes severely damaged!\nYou lose 300 points."+bcolors.endc)
    userScore = userScore - 300
    time.sleep(0.3)
    print("\nTotal score: ", userScore)
    time.sleep(0.3)
    print("\nLet's move on to the next area.\n")
    time.sleep(1)
    sharperImage()

def sharperImageSpecialAction():
    global userScore
    global inventoryList
    print("\nYou decide to check out some of the fancy gizmos and gadgets lining the shelves.\nYou can't really tell what any of them do, so you decide it's best to just press buttons until something happens.")
    time.sleep(0.5)
    print(bcolors.bold+bcolors.cyan+"Eventually, one of the objects lights up and begins making a sound.\nIt's a robotic dog companion!")
    time.sleep(0.3)
    print("\n\"W00f W00f! PL3ASE SAY A C0MMAND.\"\nYou say nothing but it continues to follow you. I guess it's yours now!\nLet's give him a name! "+bcolors.endc)
    time.sleep(0.3)
    print("\nWhat is your new companion's name?")
    time.sleep(0.3)
    companionName = input(">>> ")
    print("\nYou got", companionName+", your new robotic canine friend!")
    time.sleep(0.5)
    print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(companionName, specialItem4.description, specialItem4.rarity, specialItem4.pointValue))
    inventoryList.append(specialItem4)
    userScore = userScore + 1000
    time.sleep(0.3)
    print("\nTotal score: ", userScore)
    time.sleep(0.3)
    print("\nLet's move on to the next area.\n")
    time.sleep(1)
    hotTopic()
def hotTopicSpecialAction():
    global userScore
    global inventoryList
    print("You decide to check out the back of the store.\nIt's a little bit dark but it looks like there's some cool stuff back here.\n\nWait, what was that? It almost sounded like movement...")
    time.sleep(4)
    print("Suddenly Goth Teen Jessica appears from the shadows of Hot Topic! And she looks distraught!\n\n'AAGHH!! Who took my fishnet fingerless gloves?? Was it YOU!?\nGoth Teen Jessica charges at you!")
    time.sleep(0.5)
    print("\nA. Attack\nB. Negotiate\nC. Flee\n")
    time.sleep(0.3)
    nestedUserChoice = input(">>> ")
    while True:
        if nestedUserChoice in answerA or nestedUserChoice in answerB or nestedUserChoice in answerC:
            break
        print( aBorC )
        time.sleep(0.3)
        nestedUserChoice = input("\n>>> ")
    if nestedUserChoice in answerA:
        print("\nYou quickly grab the first thing you see and hurl some makeup at the Goth Teen.")
        successChance = random()
        time.sleep(0.5)
        if successChance < .7:
            print(bcolors.bold+bcolors.green+"\nGoth Teen Jessica catches the makeup before it can do any damage.\n\n\"What the hell are you doing!? What is...\nOoh! Black lipstick! This is PERFECT! Thanks, stranger!\"\n\nQuick, let's get out of here while Jessica is distracted!"+bcolors.endc)
            time.sleep(1)
            radioShack()
        if successChance > .7:
            print(bcolors.fail+"\nGoth Teen Jessica ducks as the makeup whizzes past her, crashing against the wall behind her.\n\n\"What the hell are you doing!?\" she screams as she comes charging towards you.\nThe Goth Teen damages one of your items in the ensuing scuffle.\nYou lose 200 points."+bcolors.endc)
            userScore = userScore - 200
            time.sleep(0.3)
            print("\nTotal score: ", userScore)
            time.sleep(1)
            radioShack()
    elif nestedUserChoice in answerB:
        print("\nYou attempt to talk your way out of the situation.\n")
        time.sleep(0.5)
        print(bcolors.bold+bcolors.cyan+'\n"Fishnet fingerless gloves? I didn\'t take them, but I think I saw a pair right over there by the Evanescence shirt" you say,\nas you direct the Goth Teen away from you.\n\n"Hey thanks! Actually, there area couple pairs here. You look like you could use some yourself!"\nJessica tosses some fishnet fingerless gloves to you!')
        time.sleep(0.3)
        print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(specialItem5.name, specialItem5.description, specialItem5.rarity, specialItem5.pointValue)+bcolors.endc)
        inventoryList.append(specialItem5)
        userScore = userScore + 1000
        time.sleep(0.3)
        print("\nTotal score: ", userScore)
        time.sleep(0.3)
        print("\nLet's move on to the next area.\n")
        time.sleep(1)
        radioShack()
    elif nestedUserChoice in answerC:
        successChance = random()
        if successChance < .5:
            print(bcolors.fail+"\nYou attempt to flee. In your haste you damage one of your items, but you manage to escape.\nYou lose 100 points.\n"+bcolors.endc)
            userScore = userScore - 100
            time.sleep(0.3)
            print("\nTotal score: ", userScore)
            time.sleep(1)
            radioShack()
        else:
            print(bcolors.bold+bcolors.green+"\nYou successfully escape from the Goth Teen Jessica unscathed!\nWhew! That was a close one.\n"+bcolors.endc)
            time.sleep(1)
            radioShack()
def radioShackSpecialAction():
    global userScore
    global inventoryList
    print(bcolors.bold+bcolors.cyan+"You decide to rock out some tunes on the keyboard!\n\nWhile you're busy jamming out, someone stealthily approaches you from behind without you realizing.\nSuddenly you feel a tap on your shoulder and are jolted out of your musical trance.\n\nYou turn around in shock only to see Becky!\n\n\"Ohhhmygawd I looooove that song! You are saooooo good! Here, you totally deserve this hun!\"\n\nBecky hands you her used lip gloss.\n\n\"Uhh, thanks! I guess!\"")
    time.sleep(3)
    print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(specialItem6.name, specialItem6.description, specialItem6.rarity, specialItem6.pointValue)+bcolors.endc)
    inventoryList.append(specialItem6)
    userScore = userScore + 1000
    time.sleep(0.3)
    print("\nTotal score: ", userScore)
    time.sleep(0.3)
    print("\nLet's move on to the next area.\n")
    time.sleep(1)
    samGoody()
def samGoodySpecialAction():
    global userScore
    global inventoryList
    print(bcolors.fail+"You decide to put on some music while you poke around the store.\n\nWhile you're jamming out, you are completely unaware that the loud music\nis attracting all of the nefarious characters from around the mall!\n\nWhen you open your eyes from your dancing session, you see a store filled with bogeys!\n\nYour only option is to run for it!")
    time.sleep(3)
    print("You manage to escape the store, but you lose two of your items to the crowd!")
    print("You lost your {0} and your {1}.".format( inventoryList[0].name, inventoryList[1].name)+bcolors.endc)
    userScore = userScore - inventoryList[0].pointValue - inventoryList[1].pointValue
    inventoryList.pop(0)
    inventoryList.pop(0)
    print("\nTotal score: ", userScore)
    time.sleep(0.3)
    print("\nLet's move on to the next area.\n")
    time.sleep(1)
    kbToys()
def kbToysSpecialAction():
    global userScore
    global inventoryList
    print("You decide to check out the basement.\nCome on now, does this really seem like a good idea?")
    time.sleep(2)
    print("You head down the stairs. You pull out your phone flashlight to light the way.\nYou can only see a few feet in front of you, but when you come to the bottom of the stairs you find a light switch.\nYou flip the switch and find...")
    time.sleep(5)
    print(bcolors.bold+bcolors.cyan+"/n/n/nA room completely full of Furbies! And they're somehow all still functioning!\nThe Furbies greet you in unison, as a feeling of warm nostalgia flows over you.\nYou can't help yourself, as you grab a little Furby to take with you.")
    time.sleep(0.5)
    print("\nName: {0}\nDescription: {1}\nRarity: {2}\nPoint Value: {3}".format(specialItem7.name, specialItem7.description, specialItem7.rarity, specialItem7.pointValue)+bcolors.endc)
    inventoryList.append(specialItem7)
    userScore = userScore + 1000
    time.sleep(0.3)
    print("\nTotal score: ", userScore)
    time.sleep(0.3)
    print("\nLet's move on to the next area.\n")
    gameWin()
    
###variables for each area, along with gameArea class item###    
    
def parkingLot():
    parkingLotHeaderArt = """
                          _    _               _       _   
         _ __   __ _ _ __| | _(_)_ __   __ _  | | ___ | |_ 
        | '_ \ / _` | '__| |/ / | '_ \ / _` | | |/ _ \| __|
        | |_) | (_| | |  |   <| | | | | (_| | | | (_) | |_ 
        | .__/ \__,_|_|  |_|\_\_|_| |_|\__, | |_|\___/ \__|
        |_|                            |___/                
                                                            """

    parkingLotAreaDescription = "You find yourself in a desolate parking lot,\ndimly lit by the pale glow of the sodium-vapor streetlights overhead.\nWith not a single car in sight,\nthrough the mist you are just barely able to detect the outline \nof a massive building against the pitch-black, starless night sky.\nWith no memory of how you got here, you consider your options."
    parkingLotSpecial = "Run screaming into the night"
    parkingLotEnemyApproachMsg = "Suddenly, you hear a strange grunting sound just behind you.\nYou turn around and see angry-looking parking lot gremlin heading directly towards you!"
    parkingLotAttackMsg = "You grab a nearby rock and throw it at the gremlin."
    parkingLotAttackSuccessMsg = "The rock slams directly into the gremlin's face, knocking him out cold!\nLet's get out of here while we have the chance!"
    parkingLotAttackFailMsg = "You miss as the rock whizzes over the gremlin's shoulder. Now he's angry!\nHe grabs the rock and throws it back at you, nailing you square in the face.\nLet's just get out of here before he comes after you again!\nYou lose 200 points."
    parkingLotNegotiationMsg = "You decide to talk your way out of the situation."
    parkingLotNegotiationSuccessMsg = "The gremlin, clearly not understanding a word you say, retreats in confusion.\nWhew! That was close."
    parkingLotNegotiationFailMsg = "You attempt to negotiate with the parking lot gremlin, but it seems apparent that he (or she? it?) does not speak English.\nYour communication attempts only enrage the gremlin further, prompting a physical assault.\nLet's get out of here before it comes after you again!\nYou lose 100 points."
    parkingLotFleeFailMsg = "You attempt to flee. In your haste you trip over a pothole and sprain your ankle, but you manage to escape.\nYou lose 100 points."
    parkingLotFleeSuccessMsg = "You successfully escape from the parking lot gremlin unscathed!\nWhew! That was a close one."
    
    gameArea( parkingLotHeaderArt, parkingLotAreaDescription, parkingLotSpecial, parkingLotCommonItem, parkingLotUncommonItem, parkingLotRareItem, macys, parkingLotGremlin, parkingLotEnemyApproachMsg, parkingLotAttackMsg, parkingLotAttackSuccessMsg, parkingLotAttackFailMsg, parkingLotNegotiationMsg, parkingLotNegotiationSuccessMsg, parkingLotNegotiationFailMsg, parkingLotFleeFailMsg, parkingLotFleeSuccessMsg, parkingLotSpecialAction)

def macys():
    macysHeaderArt =  """ 
                                             ★                       
            ,--,--,--. ,--,--. ,---.,--. ,--.,---.  
            |        |' ,-.  || .--' \  '  /(  .-'  
            |  |  |  |\ '-'  |\ `--.  \   ' .-'  `) 
            `--`--`--' `--`--' `---'.-'  /  `----'  
                                    `---'           
                                    """
    macysAreaDescription = "You walk up to the building and begin to approach the first door you see.\nYou realize you're walking into a Macy's department store connected to a dead mall.\nYou're not sure if the mall is still operating given the condition of your surroundings.\nNevertheless, you choose to enter the building.\n\nYou find yourself in an abandoned Macy's.\nImmediately upon entering the store you find a large collection of unclothed mannequins surrounded by empty shelving and fixtures."
    macysSpecial = "Play dominos with the mannequins"
    macysEnemyApproachMsg = "Suddenly, you hear the sound of footsteps approaching from behind.\n\nYou turn around and see an irate Mall Karen heading towards you!\nShe screams 'Why won't they take my expired Kohl's coupons!? I need your corporate number!'\nat no one in particular as she rapidly approaches you."
    macysAttackMsg = "You quickly grab one of the threadbare mannequins and flail it at the Karen in self-defense."
    macysAttackSuccessMsg = "The mannequin connects with Karen with an audible 'thwack'. She falls backwards but is cushioned by her stylish hair-do.\nThe Mall Karen is temporarily stunned, let's get the heck out of here!"
    macysAttackFailMsg = "You swing and miss as the more-agile-than-expected Mall Karen swiftly dodges your attack.\nKaren mounts an incredible verbal assault that leaves you feeling gutted and full of shame.\nYou lose 200 points.\nLet's get out of here before she can tear into you any further."
    macysNegotiationMsg = "You attempt to speak with the Mall Karen. Perhaps she will listen to reason?"
    macysNegotiationSuccessMsg = "You sympathize with Karen and make up some story\nabout how you had problems with coupons in the past\nand how awful customer service is these days. This appeases the Mall Karen\nas she warms up to you with your relatable story.\n\nKaren has taken a liking to you, and let's you go free.\n\nLet's get out of here while we have the chance!"
    macysNegotiationFailMsg = "You try to sympathize with Karen but she is obviously not in the mood to chat.\nKaren mounts an incredible verbal assault that leaves you feeling gutted and full of shame.\nYou lose 100 points.\nLet's get out of here before she can tear into you any further."
    macysFleeFailMsg = "You attempt to flee. In your haste you damage one of your items, but you manage to escape.\nYou lose 100 points."
    macysFleeSuccessMsg = "You successfully escape from the Mall Karen unscathed!\nWhew! That was a close one."
    
    gameArea( macysHeaderArt, macysAreaDescription, macysSpecial, macysCommonItem, macysUncommonItem, macysRareItem, spencers, mallKaren, macysEnemyApproachMsg, macysAttackMsg, macysAttackSuccessMsg, macysAttackFailMsg, macysNegotiationMsg, macysNegotiationSuccessMsg, macysNegotiationFailMsg, macysFleeFailMsg, macysFleeSuccessMsg, macysSpecialAction)

def spencers():
    spencersHeaderArt = """
            ..`                                                                                         
     `/hmNmy:`----`                                                                                 
    /dMMMMMMMdMMMM:                                   `.                                            
  `yMMMMNyhMMMMMMM.`                               ./ymy                       `                    
  hMMMMd.  hMMMMMmod           ``                 .NMMMo                    `yhh/  -+`              
 +MMMMd`   +MMMMMMMM+         +dh-          ``    .MMMM+       ./.          -MMMs .NN+   ```        
 mMMMM:    :MMMMMMMMN/       -NMMMy-`     -ydd`   `MMMM:  ::-`.NMNy:`       `MMMN .s. `/ymNd/-.` ++`
 MMMMM`    :MMMMMoMMMMo`      /MMMMMd/`   oMMMh    MMMM- `NMM+`oMMMMNy+.`    sMMM/   :mMMhoMMMMs .. 
 NMMMM/    :MMMMd yMMMMm+`    :MMNdNMMNy-`oMMMM+   MMMM  +MMMo  mMMdNMMMds:`omMMMN- -NMN:  NMMN`    
 sMMMMm.   .yhdm+  mMMMMMNs-  :MMh -omMMMmdMMMMM-  MMMM `NMMMs  sMM:`:ohNMMNNMMMMMN/yMM+  .MMM:     
 `mMMMMN/          /MMMMMMMMd+hMMh    -ohNMMMMMMm` MMMm sMMMMm `dMMo`    .:/mMMMsmMMNMMy  +MMy      
  .mMMMMMd/         mMMN:+hMMMMMMMds/-    sMMMMMMy MMMh:MMhdMM++MMMMMmdyo/. MMMM `hMMMMMs` `-`      
   `sMMMMMMNy/.     :MMMh  `oNMMMMMMMMNds-hMMddMMM+MMMdNMM-:MNs -NMMdmMMMy`.MMMy   mMMMMMNo.        
     .smMMMMMMMmy+-  dMMM/  -hMMMs-/+oso- hMMh`mMMMMMMMMMh  :`   hMM`      :MMMMNmNMNy.-sdMMh+`     
        :ohdMMMMMMMNyoMMMN+dNsyMMo        hMMy -MMMMMMMMM:      .hMM:      sMMNMMd-`      `/hMNo    
            `./ohNMMMMMMMMm+` oMMo        NMMo  +MMMMMMMN      `NMMMo     .dMMo:mMm-  -o/    hMM-   
                 `:mMMMMMMd   oMM+    .:/+MMMo   yMMMMMMh       hMMMd`./yNNMMM. `hMN: hMm/:/hMN+    
          `.       sMMMMMMM.  oMMy:/smNMMNMMM:   `mMMMMMm`     :MMMMMNNMNmmMMd    oMM+-dMMMMms.     
        -smy      -NMMdyMMMo  oMMMMMMds/-yMMM:    -ho/mMMd+--/hNMy/yys/-``sMMh     /NMs``--.`       
        mMMM+`  .+NMMh`:MMMm  -yhys/.`   dMMM`        .ohmNNNNds-         mNdo      -mMy`           
        /MMMMmmmNMMNo` `MMMM.            Nmho           ``....`          `/.`        .mMh`          
         oMMMMMMMms.    hNh/`            .`                                           .NMd.         
          -+os+/-`      ..                                                             :syy`        
                                                                                          ``        
                                                                                          """
    spencersAreaDescription = "Moving on to the next store, you find an old Spencer's store!\nThis was always one of your favorite stores as a kid.\nLike the previous store, this one is mostly empty aside from a few dusty lava lamps and novelty mugs.\nOn the rear wall you see a door cracked open, casting a sliver of dim yellow light onto the dark sales floor."
    spencersSpecial = "Check out the mysterious back room"
    spencersEnemyApproachMsg = "Suddenly, you hear a low guttural moan coming from the front end of the store.\nYou turn to see Tony the Teen Mallrat slowly approaching you!\n'AAGHHH! THEY PIERCED THE WRONG SIDE!!'\nTony is apparently upset that the Piercing Pagoda pierced the wrong side of his nose,\nand apparently he's looking to take out his frustration on you!"
    spencersAttackMsg = "You quickly grab a dusty lava lamp off the shelf and hurl it towards the angsty teen."
    spencersAttackSuccessMsg = "The lava lamp connects with Tony's noggin with a loud and hollow 'THUNK'\nTony falls backwards and appears to be temporarily stunned.\nQuick, let's get out of here before he comes to!"
    spencersAttackFailMsg = "The lava lamp misses Tony, whizzes over his shoulder and shatters on the floor behind him with a loud crash.\nThis only enrages the angsty teen further, as he charges towards you!\nTony tackles you, and while he doesn't manage to do much damage to you, he does damage to one of your items.\nYou lose 200 points.\nLet's get out of here before he can do any more damage!"
    spencersNegotiationMsg = "You decide to negotiate with the angsty teen." 
    spencersNegotiationSuccessMsg = "You relate to Tony with a story about how you had your ear pierced at the mall when you were 13\nand how traumatic of an experience it was for you.\nYour story placates Tony, and he allows you to escape unscathed!" 
    spencersNegotiationFailMsg = "You attempt to relate to Tony with a story about how you had your ear pierced at the mall when you were 13.\nUnfortunately, the angsty teen mallrat is in no mood to listen to other people's problems.\nTony charges at you and damages one of your items!\nYou lose 100 points.\nLet's get out of here!"
    spencersFleeFailMsg = "You attempt to flee. In your haste you trip over a forgotten novelty t-shirt and damage one of your items.\nYou lose 100 points."
    spencersFleeSuccessMsg = "You successfully escape from the angsty teen mallrat unscathed!\nWhew! That was a close one."
    
    gameArea( spencersHeaderArt, spencersAreaDescription, spencersSpecial, spencersCommonItem, spencersUncommonItem, spencersRareItem, claires, tonyTheTeenMallrat, spencersEnemyApproachMsg, spencersAttackMsg, spencersAttackSuccessMsg, spencersAttackFailMsg, spencersNegotiationMsg, spencersNegotiationSuccessMsg, spencersNegotiationFailMsg, spencersFleeFailMsg, spencersFleeSuccessMsg, spencersSpecialAction)


def claires():
    clairesHeaderArt = """
              _       _           __     
          ___| | __ _(_)_ __ ___ /_/____ 
         / __| |/ _` | | '__/ _ \  / __|
        | (__| | (_| | | | |  __/  \___\

         \___|_|\__,_|_|_|  \___|  |___/

                                """
    clairesAreaDescription = "You decide to check out the Claire's across the way.\nAmong the dusty shelves you see some old earrings and dried up lip gloss."
    clairesSpecial = "Check out the jewelry cabinet"
    clairesEnemyApproachMsg = "Suddenly you hear footsteps approaching from behind you.\nYou turn to see Becky, and she looks upset!\n\nBrad spilled his Orange Julius all over Becky's top, and she's ready to attack!"
    clairesAttackMsg = "You grab the first thing you see and hurl some long-expired lip gloss at Becky"
    clairesAttackSuccessMsg = "Becky catches the lip gloss and her expression changes.\nShe begins to smile and says 'Wow, thanks! How did you know this is my favorite brand?' as she begins to apply the goo to her face.\nLet's get out of here while she's distracted!"
    clairesAttackFailMsg = "The container of expired goo smacks Becky square in the face.\nThis only serves to enrage her further, and she charges at you!\nBecky damages one of your items, and you lose 200 points.\nLet's get out of here before she comes after you again!"
    clairesNegotiationMsg = "You decide to talk it out with Becky"
    clairesNegotiationSuccessMsg = "You tell her how Brad is such a jerk and that she deserves better. Becky starts weeping softly and agrees. Let's get out of here while she's distracted!"
    clairesNegotiationFailMsg = "You tell her how Brad is such a jerk and that she deserves better. Becky screams 'What!? I LOVE Brad! He's my soulmate, you jerk!' as she charges at you.\nBecky damages one of your items, and you lose 100 points.\nLet's get out of here before she comes after you again!"
    clairesFleeFailMsg = "You attempt to flee, but in your haste trip over a forgotten sun hat and damage one of your items.\nYou lose 100 points."
    clairesFleeSuccessMsg = "You successfully escape from the enraged Becky unscathed!\nWhew! That was a close one."
    
    gameArea( clairesHeaderArt, clairesAreaDescription, clairesSpecial, clairesCommonItem, clairesUncommonItem, clairesRareItem, foodCourt, becky, clairesEnemyApproachMsg, clairesAttackMsg, clairesAttackSuccessMsg, clairesAttackFailMsg, clairesNegotiationMsg, clairesNegotiationSuccessMsg, clairesNegotiationFailMsg, clairesFleeFailMsg, clairesFleeSuccessMsg, clairesSpecialAction)

def foodCourt():
    foodCourtHeaderArt = """
      __                 _                        _   
     / _| ___   ___   __| |   ___ ___  _   _ _ __| |_ 
    | |_ / _ \ / _ \ / _` |  / __/ _ \| | | | '__| __|
    |  _| (_) | (_) | (_| | | (_| (_) | |_| | |  | |_ 
    |_|  \___/ \___/ \__,_|  \___\___/ \__,_|_|   \__|
                                                     """

    foodCourtAreaDescription = "As you continue down the hallway, you approach a large atrium. It's the food court!\n\nAmong the rows of tables and chairs you see dusty food trays and discarded fast-food containers." 
    foodCourtSpecial = "Practice your yodeling skills"
    foodCourtEnemyApproachMsg = 'Suddenly you hear footsteps quickly approaching from behind you.\nYou turn to see a disgruntled Brad, who is making a bee-line towards you!\n"I saw you talking to Becky earlier. She\'s mine!'
    foodCourtAttackMsg = "You quickly grab the first thing you see and chuck half a stale pretzel in Brad's direction."
    foodCourtAttackSuccessMsg = 'The pretzel skims across the top of Brad\'s head, gently ruffling his hair.\n"Noooo! My sweet hair-do! I worked on this for hours!"\nBrad runs off to the bathroom to fix his sweet hair-do.\nNow seems like a good time to get the heck outta here!'
    foodCourtAttackFailMsg = 'The pretzel skims across the top of Brad\'s head, gently ruffling his hair.\n"Noooo! My sweet hair-do! I worked on this for hours!"\nBrad screams as he charges you, knocking you down and damaging one of your items.\nYou lose 200 points.\nLet\'s get out of here before he comes after you again!'
    foodCourtNegotiationMsg = "You attempt to appease Brad. Maybe he will listen to reason if you just talk to him?"
    foodCourtNegotiationSuccessMsg = "You tell Brad that Becky is a cool chick and that you think they're perfect for each other.\nBrad blushes and thanks you, as he bashfully walks away.\nLet's use this as our chance to escape!"
    foodCourtNegotiationFailMsg = "You tell Brad that he needs to chill out, and it's his fault he spilled the Orange Julius\nall over Becky's top in the first place! This only enrages\nBrad further, as he screams and charges at you.\nBrad damages one of your items and you lose 100 points.\nLet's get out of here before he comes after you again!"
    foodCourtFleeFailMsg = "You attempt to flee, but in your haste you trip over half a stale pretzel and damage one of your items!\nYou lose 100 points."
    foodCourtFleeSuccessMsg = "You successfully escape from the disgruntled Brad unscathed!\nWhew! That was a close one."
    
    gameArea( foodCourtHeaderArt, foodCourtAreaDescription, foodCourtSpecial, foodCourtCommonItem, foodCourtUncommonItem, foodCourtRareItem, sharperImage, brad, foodCourtEnemyApproachMsg, foodCourtAttackMsg, foodCourtAttackSuccessMsg, foodCourtAttackFailMsg, foodCourtNegotiationMsg, foodCourtNegotiationSuccessMsg, foodCourtNegotiationFailMsg, foodCourtFleeFailMsg, foodCourtFleeSuccessMsg, foodCourtSpecialAction)

def sharperImage():
    sharperImageHeaderArt = """
  ____    _   _      _      ____    ____    _____   ____  
 / ___|  | | | |    / \    |  _ \  |  _ \  | ____| |  _ \ 
 \___ \  | |_| |   / _ \   | |_) | | |_) | |  _|   | |_) |
  ___) | |  _  |  / ___ \  |  _ <  |  __/  | |___  |  _ < 
 |____/__|_| |_| /_/   \_\ |_| \_\_|_|  ___|_____| |_| \_\
       ___   __  __      _        ___   _____
      |_ _| |  \/  |    / \     / ___| | ____|            
       | |  | |\/| |   / _ \   | |  _  |  _|              
       | |  | |  | |  / ___ \  | |_| | | |___             
      |___| |_|  |_| /_/   \_\  \____| |_____|            
                                                """          

    
    sharperImageAreaDescription = "From the foodcourt you see another store worth checking out--The Sharper Image!\n\nInside you see a row of dusty massage chairs, along with some weird gadgets whose functions aren't immediately clear." 
    sharperImageSpecial = "Check out the weird gadgets on the shelf"
    sharperImageEnemyApproachMsg = 'Suddenly you hear footsteps quickly approaching from behind you.\nYou turn to see Bob the Impatient Office Worker with a full suit and briefcase heading towards you!\nBob doesn\'t look happy, as he shouts "Where\'s my refund!" Refund for what? We may never know.'
    sharperImageAttackMsg = "You quickly grab the first thing you see and hurl an overpriced gizmo at Bob."
    sharperImageAttackSuccessMsg = 'Bob catches the overpriced gizmo before it can do any damage.\n"Huh? What\'s this? A talking foot massager? With built in iPod dock!? What a great idea! Thanks, kid!"\nAnd with that, Bob walks off with his new gadget. Let\'s get out of here while we have the chance!'
    sharperImageAttackFailMsg = 'The overpriced gizmo smacks Bob in the chest, sending him flying backwards. That thing had some heft to it!\nBefore you can get away Bob returns to his feet and charges at you, damaging one of your items.\nYou lose 200 points.'
    sharperImageNegotiationMsg = "You try to talk your way out of this situation. Perhaps he will listen to reason?"
    sharperImageNegotiationSuccessMsg = "You tell Bob a relatable story about your past experiences with refunds.\nThis seems to appease Bob, and he calms down a bit.\nNow's your chance to slip past him--let's go!"
    sharperImageNegotiationFailMsg = "You ask Bob 'Refund? Refund for what? I don\'t even work here. I just...\nbut before you can finish Bob charges at you in a fit of rage, damaging one of your items.\nYou lose 100 points."
    sharperImageFleeFailMsg = "You attempt to flee, but in your haste you trip over a voice-activated shoe-tying machine and damage one of your items.\nYou lose 100 points."
    sharperImageFleeSuccessMsg = "You successfully escape from Bob the Impatient Office Worker unscathed!\nWhew! That was a close one."
    
    gameArea( sharperImageHeaderArt, sharperImageAreaDescription, sharperImageSpecial, sharperImageCommonItem, sharperImageUncommonItem, sharperImageRareItem, hotTopic, bobTheImpatientOfficeWorker, sharperImageEnemyApproachMsg, sharperImageAttackMsg, sharperImageAttackSuccessMsg, sharperImageAttackFailMsg, sharperImageNegotiationMsg, sharperImageNegotiationSuccessMsg, sharperImageNegotiationFailMsg, sharperImageFleeFailMsg, sharperImageFleeSuccessMsg, sharperImageSpecialAction)

def hotTopic():
    hotTopicHeaderArt = ''
    hotTopicAreaDescription = "Next you find an old Hot Topic store!\n\nAnother one of your favorites from back in the day, this is where all the cool kids would shop.\nNot much is left here, besides a wall of T-shirts and some retro accessories."
    hotTopicSpecial = "Check out the back of the store."
    hotTopicEnemyApproachMsg = "Suddenly you hear footsteps approaching from the back of the store. You turn to see someone quickly heading towards you.\nIt's Goth Teen Jessica! And she looks distraught!\n\n'AAGHH!! Who took my fishnet fingerless gloves?? Was it YOU!?\nGoth Teen Jessica charges at you!"
    hotTopicAttackMsg = "You quickly grab the first thing you see and hurl some makeup at the Goth Teen."
    hotTopicAttackSuccessMsg = "Goth Teen Jessica catches the makeup before it can do any damage.\n\n\"What the hell are you doing!? What is...\nOoh! Black lipstick! This is PERFECT! Thanks, stranger!\"\n\nQuick, let's get out of here while Jessica is distracted!"
    hotTopicAttackFailMsg = "Goth Teen Jessica ducks as the makeup whizzes past her, crashing against the wall behind her.\n\n\"What the hell are you doing!?\" she screams as she comes charging towards you.\nThe Goth Teen damages one of your items in the ensuing scuffle.\nYou lose 200 points."
    hotTopicNegotiationMsg = "You attempt to talk your way out of the situation."
    hotTopicNegotiationSuccessMsg = '"Fishnet fingerless gloves? I didn\'t take them, but I think I saw a pair right over there by the Evanescence shirt" you say,\nas you direct the Goth Teen away from you. Quick, now\'s our chance to escape while she\'s distracted!'
    hotTopicNegotiationFailMsg = '"Fishnet fingerless gloves? As if! I definitely have enough fashion sense to know I would NEVER wear something like that" you proudly assert.\nThis was obviously not the right thing to say, as the Goth Teen immediately charges you in a fit of rage.\nJessica the Goth Teen damages one of your items in the ensuing scuffle, and you lose 100 points.\nLet\'s get out of here before she comes after you again!'
    hotTopicFleeFailMsg = "You attempt to flee, but in your haste trip over a forgotten Korn backpack.\nYour fall damages one of your items, and you lose 100 points."
    hotTopicFleeSuccessMsg = "You successfully escape from Jessica the Goth Teen unscathed!\nWhew! That was a close one."
    
    gameArea( hotTopicHeaderArt, hotTopicAreaDescription, hotTopicSpecial, hotTopicCommonItem, hotTopicUncommonItem, hotTopicRareItem, radioShack, gothTeenJessica, hotTopicEnemyApproachMsg, hotTopicAttackMsg, hotTopicAttackSuccessMsg, hotTopicAttackFailMsg, hotTopicNegotiationMsg, hotTopicNegotiationSuccessMsg, hotTopicNegotiationFailMsg, hotTopicFleeFailMsg, hotTopicFleeSuccessMsg, hotTopicSpecialAction)

def radioShack():
    radioShackHeaderArt = ''
    radioShackAreaDescription = "Across the way you spot what looks like an abandoned electronics store\n\nYou found an old Radio Shack and decide to go check it out.\nInside you don't see much aside from a bunch of empty shelves, some cheap extension cords and a couple Yamaha keyboards."
    radioShackSpecial = "Play some tunes on the keyboard"
    radioShackEnemyApproachMsg = "You suddenly hear footsteps approaching from behind you. You turn around and see Techie Chris quickly coming towards you, looking riled up!\n\n\"Ahem, excuse me but you seem to have misappropriated my hybrid semiconductor module! Prepare to face severe ramifications!" 
    radioShackAttackMsg = "In defense you grab the first thing you see and chuck a Nokia phone at Techie Chris."
    radioShackAttackSuccessMsg = "The Nokia phone knocks Techie Chris out cold with its indestructible brick-like power.\nQuick, now's your chance to escape!"
    radioShackAttackFailMsg = "Techie Chris quickly predicts the device's trajectory and successfully intercepts. Now enraged, Techie Chris charges at you!\nIn the ensuing scuffle one of your items becomes damaged and you lose 200 points.\nLet's get out of here before he comes after you again!"
    radioShackNegotiationMsg = "You attempt to negotiate your way out of the situation."
    radioShackNegotiationSuccessMsg = '"You\'re looking for a hybrid semiconductor module? Why I just so happen to have seen one just over there\n behind the line-replacable leveraged circuit converters!"/nYou direct Techie Chris away from you as you slip out of the store unnoticed!'
    radioShackNegotiationFailMsg = '"Hybrid semiconductor module? That just sounds like meaningless technobabble!" you posit.\n\n"Meaningless technobabble!? I\'ll show you meaningless technobabble!" spits Techie Chris, as he charges you.\n"Ouch! Right in the advanced paradigm-shift voltage-source! That really smarts." you say as you hobble away.\nYou lose 100 points.'
    radioShackFleeFailMsg = "You attempt to flee, but in your haste trip over an abandoned CD changer.\nYour fall damages one of your items and you lose 100 points."
    radioShackFleeSuccessMsg = "You successfully escape from Techie Chris unscathed!\nWhew! That was a close one."
    
    gameArea( radioShackHeaderArt, radioShackAreaDescription, radioShackSpecial, radioShackCommonItem, radioShackUncommonItem, radioShackRareItem, samGoody, techieChris, radioShackEnemyApproachMsg, radioShackAttackMsg, radioShackAttackSuccessMsg, radioShackAttackFailMsg, radioShackNegotiationMsg, radioShackNegotiationSuccessMsg, radioShackNegotiationFailMsg, radioShackFleeFailMsg, radioShackFleeSuccessMsg, radioShackSpecialAction)

def samGoody():
    samGoodyHeaderArt = ''
    samGoodyAreaDescription = "Further down the hallway you come to a store you'd all but forgotten had ever existed--Sam Goody.\n\nAs you enter, you see an array of dusty CDs, cassette tapes and vinyl records.\nApparently this place didn't bother to clear out much of their inventory."
    samGoodySpecial = "Listen to some music."
    samGoodyEnemyApproachMsg = "You suddenly hear someone approaching you from behind. You turn and see Kevin the Music Buff approaching you!\n\n\"Hey man, you're in the 'pop' section? That's not even real music, you fool!"
    samGoodyAttackMsg = "You quickly grab the nearest thing you see and hurl a stack of CDs at Kevin."
    samGoodyAttackSuccessMsg = "The CDs hit Kevin and clatter to the floor. Looking down at the stack, Kevin leans down and picks one up at random.\n\n\"The Beach Boys? Yeah, man! Now this is good music! You're alright, my guy.\"\nIt looks like you've appeased the Music Buff! Use this as your opportunity to escape!"
    samGoodyAttackFailMsg = "The CDs hit Kevin and clatter to the floor. Looking down at the stack, Kevin leans down and picks one up at random.\n\n\"Aaron Carter? Come on, man! You can't even have good taste in your attacks! It looks like I have no choice...\"\nKevin suddenly charges you and damages one of your items in the ensuing scuffle.\nYou lose 200 points. Let's get out of here before he comes at you again!"
    samGoodyNegotiationMsg = "You decide to talk to Kevin. Maybe he will listen to reason!"
    samGoodyNegotiationSuccessMsg = "\"Hey man, this stuff isn't really my style. I was actually just on my way to that section over there...\" you stammer as you point vaguely in some other direction.\n\n\"Oh yeah, cool man! I like Celine Dion, too! No shame in it--she's got the voice of an angel. You're alright with me bud.\n\nIt looks like you got on Kevin's good side! You slip past him and back out into the mall unscathed."
    samGoodyNegotiationFailMsg = "\"Hey man, this stuff isn't really my style. I was actually just on my way to that section over there...\" you stammer as you point vaguely in some other direction.\n\n\"Huh? The Backstreet Boys? Ugh come on man, you leave me no choice!\" he says as he Kevin suddenly charges you!\nIn the ensuing scuffle one of your items is damaged and you lose 100 points."
    samGoodyFleeFailMsg = "You attempt to flee, but in your haste you trip over an old record player!\nYour fall damages one of your items and you lose 100 points."
    samGoodyFleeSuccessMsg = "You successfully escape from Kevin the Music Buff unscathed!\nWhew! That was a close one."
    
    gameArea( samGoodyHeaderArt, samGoodyAreaDescription, samGoodySpecial, samGoodyCommonItem, samGoodyUncommonItem, samGoodyRareItem, kbToys, kevinTheMusicBuff, samGoodyEnemyApproachMsg, samGoodyAttackMsg, samGoodyAttackSuccessMsg, samGoodyAttackFailMsg, samGoodyNegotiationMsg, samGoodyNegotiationSuccessMsg, samGoodyNegotiationFailMsg, samGoodyFleeFailMsg, samGoodyFleeSuccessMsg, samGoodySpecialAction)

def kbToys():
    kbToysHeaderArt = ''
    kbToysAreaDescription = "At the end of the hallway you see KB Toys. They still have a display out front with a random assortment of cheap toys and knick-knacks.\nInside you see a collection of forlorn dolls, toy cars, and some containers of dried up Gak.\nTowards the back of the store you spot a mysterious staircase heading down into darkness." 
    kbToysSpecial = "Check out the basement."
    kbToysEnemyApproachMsg = "Out of the darkness you hear a strange sound. What is that? It sounds like...sleigh bells?\n\nHO HO HO!\n\nSuddenly Gary the Mall Santa approaches you!\n\n\"You're on my naughty list this year, {0} and it's time you pay penance for your sins!".format( playerName )
    kbToysAttackMsg = "In your terror you grab the nearest thing available and launch a Nintendo 64 towards the Mall Santa!"
    kbToysAttackSuccessMsg = "The N64 smacks the Mall Santa square in the gut, knocking the wind out of him!\nNow's your chance to escape! You slip past Gary unscathed!" 
    kbToysAttackFailMsg = "The N64 smacks the Mall Santa square int he gut as he staggers backwards.\n\nThat was very, very naughty of you, {0}! Prepare to pay for your sins!\n\nGary the Mall Santa charges at you and damages one of your items.\nYou lose 200 points."
    kbToysNegotiationMsg = "You decide to speak with Gary. Perhaps he will listen to reason?"
    kbToysNegotiationSuccessMsg = "\"No, Santa, please forgive me! I'll do whatever it takes to get on the nice list.\nLook, I even got you a present!\" you bluff, as you reach behind your back and grasp for the nearest toy.\nYou present whatever ended up in your hand, which turns out to be one of those creepy-looking Cabbage Patch dolls.\n\n\"Oh...my, that looks just like my little Timmy. Well, I suppose I can forgive you this time. After all, it is Christmas!\"\n\nYou use this as your opportunity to escape!\n\"It's not Christmas!\" you yell as you run out of the store."
    kbToysNegotiationFailMsg = "\"What are you talking about? You don't even know me, and Santa isn't even real! This is ridiculous.\"\n\nThis doesn't go over well with Gary the Mall Santa, who charges at you in a fit of rage.\nOne of your items is damaged in the ensuing scuffle and you lose 100 points."
    kbToysFleeFailMsg = "You attempt to flee, but in your haste you trip over a forlorn Furbee as it vocalizes in protest.\nYou damage one of your items in the fall and lose 100 points."
    kbToysFleeSuccessMsg = "You successfully escape from Gary the Mall Santa unscathed!\nWhew! that was a close one."
    
    gameArea( kbToysHeaderArt, kbToysAreaDescription, kbToysSpecial, kbToysCommonItem, kbToysUncommonItem, kbToysRareItem, gameWin, garyTheMallSanta, kbToysEnemyApproachMsg, kbToysAttackMsg, kbToysAttackSuccessMsg, kbToysAttackFailMsg, kbToysNegotiationMsg, kbToysNegotiationSuccessMsg, kbToysNegotiationFailMsg, kbToysFleeFailMsg, kbToysFleeSuccessMsg, kbToysSpecialAction)
###successful end of game###        
def gameWin():
    global userScore
    global inventoryList
    print( divider )
    print("You head back out into the hallway and see an emergency exit!\nFreedom is near! You sprint to the exit and burst out through the door.")
    print(bcolors.bold+bcolors.cyan+"\nYOU MADE IT OUT ALIVE!\n\nFINAL SCORE: {0}\n\nITEMS FOUND:\n".format( userScore )+bcolors.endc)
    for item in range(len(inventoryList)):
        print ( inventoryList[item].name, "\n" )
    if len(inventoryList) < 1:
        print( bcolors.fail+'None'+bcolors.endc )
    print( divider )
    print(bcolors.bold+"Would you like to play again?\n"+bcolors.endc)
    userChoice = input(">>> ")
    while True:
        if userChoice in answerYes or userChoice in answerNo:
            break
        print( "{0} is not a valid option. How many times have we been over this, {1}?\nI'm beginning to think you're doing this on purpose.\nPlease enter yes or no!".format( userChoice, playerName )  )
        userChoice = input("\n>>> ")
    if userChoice in answerYes:
        main()
    else:
        print("Goodbye!")
        time.sleep(2)
        sys.exit(0)
###unsuccessful end of game###
def gameOver():
    print ( divider )
    global userScore
    global inventoryList
    print(bcolors.fail+"GAME OVER\n\nFINAL SCORE: {0}\n\n\nITEMS FOUND:\n".format( userScore )+bcolors.endc)
    for item in range(len(inventoryList)):
        print ( inventoryList[item].name )
    if len(inventoryList) < 1:
        print( bcolors.fail+"NONE!"+bcolors.endc )
    print(bcolors.bold+"\n\nWould you like to play again?\n"+bcolors.endc)
    userChoice = input(">>> ")
    while True:
        if userChoice in answerYes or userChoice in answerNo:
            break
        print( "{0} is not a valid option. How many times have we been over this, {1}?\nI'm beginning to think you're doing this on purpose.\nPlease enter yes or no!".format( userChoice, playerName )  )
        userChoice = input("\n>>> ")
    if userChoice in answerYes:
        main()
    else:
        print("Goodbye!")
        time.sleep(2)
        sys.exit(0)

main()
            
    

    
