import tkinter
import random 

main_window = tkinter.Tk()
main_window.title("text-based adventure game")
main_window.geometry("400x400")
name = str(input("Enter your name: "))
money = random.randint(50,310)
point = 0 
health = 100
i =0
win = False
RoomM=0 
RoomP = 0
TreasureC = 0
TreasureP =0



inventory ={"Weapon": [], "Armour":[], "Key": []}
Shop ={"Weapon": [], "Key": [],"Healing_Pad":[] ,"Armour":[]}
inventory["Weapon"].append({"name": "knife", "damage": 10, "price": 50})
inventory["Armour"].append({"durability": 2 , "price": 200})
inventory["Key"].append({"code": int(0), "price": int(200)})
Enemies ={"Enemy": []}

def add_enemies():
    
    with open('Room1.txt', 'r') as file:
        whole_file = file.readlines()
        for idx, item in enumerate(whole_file):
            if "Enemy" in item:
                enemy = whole_file[idx+1].strip().split(",")
                Enemies["Enemy"].append({"name": enemy[0],"damage": int(enemy[1]),"health": int(enemy[2])})
    

    with open('Room2.txt', 'r') as file:
        whole_file = file.readlines()
        for idx, item in enumerate(whole_file):
            if "Enemy" in item:
                enemy = whole_file[idx+1].strip().split(",")
                Enemies["Enemy"].append({"name": enemy[0],"damage": int(enemy[1]),"health": int(enemy[2])})
    

    
    with open('Room3.txt', 'r') as file:
        whole_file = file.readlines()
        for idx, item in enumerate(whole_file):
            if "Enemy" in item:
                enemy = whole_file[idx+1].strip().split(",")
                Enemies["Enemy"].append({"name": enemy[0],"damage": int(enemy[1]),"health": int(enemy[2])})
    



    
    with open('Room4.txt', 'r') as file:
        whole_file = file.readlines()
        for idx, item in enumerate(whole_file):
            if "Enemy" in item:
                enemy = whole_file[idx+1].strip().split(",")
                Enemies["Enemy"].append({"name": enemy[0],"damage": int(enemy[1]),"health": int(enemy[2])})
    
add_enemies()
# ---------- first commit
top_frame = tkinter.Frame(main_window)
top_frame.pack(anchor="n")

name_label = tkinter.Label(top_frame, text = "Name: " +name,font=("Arial,16"))
name_label.grid(row=0, column =0)

Health_label = tkinter.Label(top_frame, text = "Health: " +str(health),font=("Arial,16"))
Health_label.grid(row=1, column =0)

Money_label = tkinter.Label(top_frame, text = "Money: " +str(money),font=("Arial,16"))
Money_label.grid(row=0, column =1)

Point_label = tkinter.Label(top_frame, text = "Point: " +str(point),font=("Arial,16"))
Point_label.grid(row=1, column =1)

def change_labels(health, money, point):
    Health_label.configure(text="Health: " + str(health))
    Money_label.configure(text="Money: " + str(money))
    Point_label.configure(text="Point: " + str(point))


bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(anchor="s")
def showWandA():
    Counter =0 
    if len(inventory["Weapon"])>0:
        print("Category:Weapon")
        print("\nWeapons in inventory:")
        while Counter< len(inventory["Weapon"]):
            print(Counter+1,"|",*[str(k) + ':' + str(v) +"|" for k,v in inventory["Weapon"][Counter].items()])
            Counter+=1
    else:
        print("There are no weapons in your inventory")

    Counter = 0
    if len(inventory["Armour"])>0:
        print("\nCategory:Armour")
        print("\nArmours in inventory:")
        while Counter<len(inventory["Armour"]):
            print(Counter+1,"|",*[str(k) + ':' + str(v) +"|" for k,v in inventory["Armour"][Counter].items()])
            Counter+=1
    else:
        print("There are no Armours in your inventory")
# ---------- second commit
def IFlose(FileName): 
    global health,point
    print("you died and lost 2 points. respawn in progress")
    health = 0
    point-=2
    with open(str(FileName)+'.txt', 'r') as file:
        whole_file = file.readlines()

        for idx, item in enumerate(whole_file):
                if "Enemy" in item:
                    enemy = whole_file[idx+1].strip().split(",")
                    enemyUpdatedHealth = int(enemy[2])
                    enemy[2]= str(enemyUpdatedHealth)
    

def IFWin(FileName):
    global health,RoomM,RoomP,point,money,i,TreasureP,TreasureC
    Counter=0
    with open(str(FileName)+'.txt', 'r') as file:
            whole_file = file.readlines()
            for idx, item in enumerate(whole_file):

                if "money" in item.lower():
                    RoomM = int(whole_file[idx+1])
                    money+=RoomM 
                if "points" in item.lower():
                    RoomP = int(whole_file[idx+1])
                    point+=RoomP

                if "weapon" in item.lower():
                    weapon = whole_file[idx+1].strip().split(",")
                    inventory["Weapon"].append({"name": weapon[0], "damage": int(weapon[1]), "price": int(weapon[2])})
                
                if "Key" in item.lower():
                    key = whole_file[idx+1].strip().split(",")
                    inventory["Key"].append({"code": int(key[0]), "price": int(key[1])})

                if "treasure" in item.lower():
                    TreasureP = int(whole_file[idx+1][2])
                    
                    
            if len(inventory["Key"])>0:
                choice= str(input("would you like to try to open the treasure chest? type yes or no>>>"))
                if choice == "yes":       
                    print("\nKeys in inventory:")
                    while Counter< len(inventory["Key"]):
                        print(Counter+1,"|",*[str(k) + ':' + str(v) +"|" for k,v in inventory["Key"][Counter].items()])
                        Counter+=1
                        num= int(input("which enter the number of the key you would like to use>>>"))      
                    if TreasureC== inventory["Key"][num-1]["code"]:
                        point+=TreasureP
                        print("You collected",TreasureP,"Points from the chest")



    print("You defeated the enemy and earned",RoomP,"Points, collected",RoomM,"amount of money","and acquired a new weapon")
    i+=1
    with open(str(FileName)+'.txt', "w") as f:
        f.truncate(0)
        f.write("You have already defeated the enemy in this room and collected its contents")
        f.write(", Please choose another room")
# ---------- third commit
def Combat(RoomNO):  
    global health,win
    if len(inventory["Weapon"])>0:
        weaponChoice= int(input("\nWhat weapon would you like to fight with? type its number >>>"))
        if len(inventory["Armour"])>0:
            Choice= str(input("\nWould you like to use armour? type yes or no>>>"))
            if Choice == "yes":
                ArmourChoice= int(input("\nWhat armour would you like to use? Type its number>>>"))
                print("\nYour Health\t\tEnemy's Health")
                while health>0 and Enemies["Enemy"][RoomNO-1]["health"]>0:
                    
                    print(health,"\t\t\t",Enemies["Enemy"][RoomNO-1]["health"])
                    Enemies["Enemy"][RoomNO-1]["health"]-=inventory["Weapon"][weaponChoice-1]["damage"] 
                    health-=Enemies["Enemy"][RoomNO-1]["damage"]/inventory["Armour"][ArmourChoice-1]["durability"]
                if Enemies["Enemy"][RoomNO-1]["health"]<=0:
                    win = True

                elif health<=0:
                    win = False

                del inventory["Weapon"][weaponChoice-1]
                del inventory["Armour"][ArmourChoice-1]


            if Choice=="no":
                print("Your Health\t\tEnemy's Health")
                while health>0 and Enemies["Enemy"][RoomNO-1]["health"]>0:

                    print(health,"\t\t\t",Enemies["Enemy"][RoomNO-1]["health"])
                    Enemies["Enemy"][RoomNO-1]["health"]-=inventory["Weapon"][weaponChoice-1]["damage"] 
                    health-=Enemies["Enemy"][RoomNO-1]["damage"]
                

                if Enemies["Enemy"][RoomNO-1]["health"]<=0:
                    win = True

                elif health<=0:
                    win = False

                del inventory["Weapon"][weaponChoice-1]
                

        else:
            while health>0 and Enemies["Enemy"][RoomNO-1]["health"]>0:
                print(health, Enemies["Enemy"][RoomNO-1]["health"])
                
                Enemies["Enemy"][RoomNO-1]["health"]-=inventory["Weapon"][weaponChoice-1]["damage"] 
                health-=Enemies["Enemy"][RoomNO-1]["damage"]
            if Enemies["Enemy"][RoomNO-1]["health"]<=0:
                win = True

            elif health<=0:
                win = False
            del inventory["Weapon"][weaponChoice-1]
# ---------- fourth commit 
def Room1():
   
    myfile = open("Room1.txt", "r")
    first_line = myfile.readline()
    if "Welcome" in first_line:
        global health,i,point
        point =6
        print("Welcome to room 1\n")
        change_labels(health,money,point)

        with open('Room1.txt', 'r') as file:
            whole_file = file.readlines()
            print(whole_file[0])
            print(whole_file[1],"\nEnemy: ")
        
        print(*[str(key) + ':' + str(value) +"|" for key,value in Enemies["Enemy"][0].items()],"\n\nWeapons in inventory:\n")
        
        showWandA()
    
        if  len(inventory["Weapon"])>0:
            Combat(1)
            
            if win == True:
                IFWin("Room1")
            
            elif win != True:
                IFlose("Room1")

        elif len(inventory["Weapon"])==0:
            print("You do not have any weapons. go to shop to buy one in order to initiate a fight")    
            
        GameState()

    else: 
        print(whole_file[0])
        print(whole_file[1])

    pass    
    

def Room2():
    myfile = open("Room2.txt", "r")
    first_line = myfile.readline()
    if "Welcome" in first_line:
        global health,i
        print("Welcome to room 1\n")
        change_labels(health,money,point)

        with open('Room2.txt', 'r') as file:
            whole_file = file.readlines()
            print(whole_file[0])
            print(whole_file[1],"\nEnemy: ")
        
        

        print(*[str(key) + ':' + str(value) +"|" for key,value in Enemies["Enemy"][1].items()],"\n\nWeapons in inventory:\n")
        print(health, Enemies["Enemy"][1]["health"])
        showWandA()

        if  len(inventory["Weapon"])>0:
            Combat(2)
            
            if win == True:
                IFWin("Room2")
            
            elif win != True:
                IFlose("Room2")

        elif len(inventory["Weapon"])==0:
            print("You do not have any weapons. go to shop to buy one in order to initiate a fight")    

        GameState()

    else: 
        with open('Room2.txt', 'r') as file:
            whole_file = file.readlines()
            print("\n",whole_file[0])
            

    pass
# ---------- fifth commit
def Room3():
    myfile = open("Room3.txt", "r")
    first_line = myfile.readline()
    if "Welcome" in first_line:
        global health,i
        print("Welcome to room 1\n")
        change_labels(health,money,point)

        with open('Room3.txt', 'r') as file:
            whole_file = file.readlines()
            print(whole_file[0])
            print(whole_file[1],"\nEnemy: ")
        

            for idx, item in enumerate(whole_file):
                if "Enemy" in item:
                    enemy = whole_file[idx+1].strip().split(",")
                    Enemies["Enemy"].append({"name": enemy[0],"damage": int(enemy[1]),"health": int(enemy[2])})
        

        print(*[str(key) + ':' + str(value) +"|" for key,value in Enemies["Enemy"][2].items()],"\n\nWeapons in inventory:\n")
        
        showWandA()
        
        if  len(inventory["Weapon"])>0:
            Combat(3)
            
            if win == True:
                IFWin("Room3")
            
            elif win != True:
                IFlose("Room3")

        elif len(inventory["Weapon"])==0:
            print("You do not have any weapons. go to shop to buy one in order to initiate a fight")    

        GameState()

    else: 
        print("Hello")

    pass

def Room4():
    myfile = open("Room4.txt", "r")
    first_line = myfile.readline()
    if "Welcome" in first_line:
        global health,i
        print("Welcome to room 1\n")
        change_labels(health,money,point)

        with open('Room4.txt', 'r') as file:
            whole_file = file.readlines()
            print(whole_file[0])
            print(whole_file[1],"\nEnemy: ")
        

            for idx, item in enumerate(whole_file):
                if "Enemy" in item:
                    enemy = whole_file[idx+1].strip().split(",")
                    Enemies["Enemy"].append({"name": enemy[0],"damage": int(enemy[1]),"health": int(enemy[2])})
        

        print(*[str(key) + ':' + str(value) +"|" for key,value in Enemies["Enemy"][3].items()],"\n\nWeapons in inventory:\n")
        
        showWandA()

        if  len(inventory["Weapon"])>0:
            Combat(4)
            
            if win == True:
                IFWin("Room4")
            
            elif win != True:
                IFlose("Room4")

        elif len(inventory["Weapon"])==0:
            print("You do not have any weapons. go to shop to buy one in order to initiate a fight")    

        GameState()

    else: 
        print("Hello")

    pass
# ---------- sixth commit
def Buy():
    global health,money
    Category = str(input("\nPlease enter the name of the item's category >>> "))
    if Category != "Healing_Pad":
        ItemNo= int(input("\nPlease enter the number of the item >>> "))
        if money>=Shop[Category][ItemNo-1]["price"]:
                inventory[Category].append(Shop[Category][ItemNo-1])
                money-=Shop[Category][ItemNo-1]["price"]
        else: 
            print("\nYou do not have enough money to buy this item")

    else: 
        if money>=Shop[Category][0]["price"]:
            print("\nYou have bought a healing pad. Current health increased")
            money-=Shop[Category][0]["price"]
            if health+Shop[Category][0]["health"]<=100:
                health+=Shop[Category][0]["health"]
            elif health+Shop[Category][0]["health"]>100:
                health =100
        else:
            print("\nYou do not have enough money to buy this item")

def Sell():
    global money
    Inventory()
    Category = str(input("\nPlease enter the name of the item's category >>> "))
    ItemNo= int(input("\nPlease enter the number of the item you would like to sell>>> "))
    money+=inventory[Category][ItemNo-1]["price"]
    del inventory[Category][ItemNo-1]
# ---------- seventh commit
def shop():
    global health,money 
    i =1
    print("\nWelcome to the shop")
    point = 10
    change_labels(health,money,point)
    with open('Shop.txt', 'r') as file:
        whole_file = file.readlines()
        for idx, item in enumerate(whole_file):
            if "Weapon" in item:
                print("\nCategory:Weapon:\n")
                while "weapon" in whole_file[idx+i]:
                    weapon = whole_file[idx+i].strip().split(",")
                    Shop["Weapon"].append({"name": weapon[0], "damage": int(weapon[1]), "price": int(weapon[2])})
                    print(i,"|",*[str(key) + ':' + str(value) +"|" for key,value in Shop["Weapon"][i-1].items()])
                    i+=1
            if "Key" in item:
                i=1
                print("\nCategory:Key:\n")
                key = whole_file[idx+1].strip().split(",")
                Shop["Key"].append({"code": key[0], "price": int(key[1])})
                print(i,"|",*[str(key) + ':' + str(value) +"|" for key,value in Shop["Key"][0].items()])
            
            if "Healing" in item:
                i=1
                print("\nCategory:Healing_Pad:\n")
                heal = whole_file[idx+1].strip().split(",")
                Shop["Healing_Pad"].append({"health": int(heal[0]), "price": int(heal[1])})
                print(i,"| Healing Pad|",*[str(key) + ':' + str(value) +"|" for key,value in Shop["Healing_Pad"][0].items()])

            if "Armour" in item:
                i=1
                print("\nCategory:Armour:\n")
                for x in range(1,3): # for some reason when 'while' is used it gives an error
                    
                    armour = whole_file[idx+x].strip().split(",")
                    Shop["Armour"].append({"durability": armour[0], "price": int(armour[1])})
                    print(i,"|",*[str(key) + ':' + str(value) +"|" for key,value in Shop["Armour"][x-1].items()])
                    i+=1 
    answer=str(input("\nWould you like to buy or sell anything? Type yes or no >>> "))
    # add sell option after creating inv func.
    if answer == "yes":
        answer2=str(input("\nWould you like to buy or sell anything? Type buy or sell >>> "))
        if answer2 == "buy":
            Buy()
        elif answer2 == "sell":
            Sell()
            
    pass
# ---------- eight commit
def GameState():
    global point 
    if point >=10:
        print("You have won the game. thanks for playing")
        main_window.quit()
        

    elif point < 0: 
        print("You have lost the game. thanks for playing ")
    
        main_window.quit()

def Inventory():
    print("Welcome to inventory\n")
    point = 10
    change_labels(health,money,point)
    showWandA()
    Counter =0 
    if len(inventory["Key"])>0:
        print("\nCategory:Key")
        print("\nKeys in inventory:")
        while Counter< len(inventory["Key"]):
            print(Counter+1,"|",*[str(k) + ':' + str(v) +"|" for k,v in inventory["Key"][Counter].items()])
            Counter+=1
    else:
        print("\nThere are no keys in your inventory")
    pass




R1_btn = tkinter.Button(bottom_frame, text= "Room 1", command = Room1)
R1_btn.grid(row=0, column =0)

R2_btn = tkinter.Button(bottom_frame, text = "Room 2", command= Room2)
R2_btn.grid(row=1, column =0)


R3_btn = tkinter.Button(bottom_frame, text = "Room 3", command= Room3)
R3_btn.grid(row=0, column =1)

R4_btn = tkinter.Button(bottom_frame, text = "Room 4", command= Room4)
R4_btn.grid(row=1, column =1)

R5_btn = tkinter.Button(bottom_frame, text = "shop", command= shop)
R5_btn.grid(row=2, column =0)

R6_btn = tkinter.Button(bottom_frame, text = "Inventory", command= Inventory)
R6_btn.grid(row=2, column =1)


main_window.mainloop()
# ---------- final commit
