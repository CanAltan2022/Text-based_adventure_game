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
