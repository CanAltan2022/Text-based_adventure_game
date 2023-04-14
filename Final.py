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
