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
