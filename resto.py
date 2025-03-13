#pour combien de personnes
#bilan fin de service

#class menu
class Menu :
    def __init__(self,category,name,price):
        self.category=category
        self.name=name
        self.price=price
    def __str__(self):
        return f"{self.category} - {self.name}:{self.price}"


#création du menu
menu_list =[
    Menu("Entrée", "salade",7),
    Menu("Entrée", "quiche", 7),
    Menu("Entrée", "soupe",6),
    Menu("Plat","boeuf", 10),
    Menu("Plat", "poulet", 8),
    Menu("Plat","Oeuf mollet", 5),
    Menu("Accompagnement","Frites", 3),
    Menu("Accompagnement","Légumes",5),
    Menu("Accompagnements","pates",3),
    Menu("Dessert","tiramisu", 6),
    Menu("Dessert", "mousse au chocolat",4),
    Menu("Dessert", "tarte au citron", 6),
    Menu("Boisson","eau",0),
    Menu("Boisson", "vin", 3),
    Menu("Boisson", "soda", 3)
]

#créer une classe commande
class Command:
    def __init__(self):
        self.plate=[]

    def add_plate(self,plate):
        self.plate.append(plate)

    def display_command(self):
        print("commande :")
        for plate in self.plate:
            print(f" {plate.name}({plate.price}€)")
        total=sum(plate.price for plate in self.plate)
        print(f"Total à payer : {total}€")
        return total

#créer une classe client
class Client :
    def __init__(self,name,seat):
        self.name=name
        self.seat=seat
        self.command=Command()

class Boy:
    def __init__(self,name):
        self.name=name

    # demander au client ce qu'il veut manger
    def get_client_choise(self,client):
        print(f"Bonjour {client.name}, voici le menu du jour")
        for index, plate in enumerate (menu_list,1):
            print(f"{index}.{plate}")

        choice = input("Choisissez les plats en entrant les numéros")
        choice_list = [int(i) -1 for i in choice.split() if i.isdigit() and 0 <= int(i) -1 <len(menu_list)]

        for i in choice_list:
            client.command.add_plate(menu_list[i])

        print(f"{client.name}, bon appétit !")

    def ask_money(self, client):
        total=client.command.display_command()
        money = float(input(f"Pour lutter contre le resto basket, veuillez payer : {total}€"))



