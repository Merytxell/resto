# utiliser typage statique
# utilise classes, héritage et classe abstraite-->ok
# la salle du restaurant contient un certain nombre de tables
# un table a une capacité pour un certain nombre de personnes
# les personnes arrivent en groupe et se voit allouer une table libre pouvant les accueillir, mais de préférence la plus petite possible, pour ne pas nuire à futures arrivées
# en option, possibilité de gérer des réservation existantes
# en option, possibilité de gérer l'heure d'arrivée et de départ d'un groupe => selon l'estimation de la durée d'un repas, on peut ou pas allouer une table réservée après l'heure du départ ; possibilité de simplifier avec 2 horaires : premier et second service
# les personnes d'un groupe commandent chacune leur repas (entrée + plat + dessert + boisson, + optionnel)
# au moment de partir, le groupe règle l'addition
# ne pas faire de menu interaction, mais simplement un main de test
from abc import ABC, abstractmethod
from typing import List

#class menu
class Menu(ABC):
    def __init__(self,category,name,price):
        self.category=category
        self.name=name
        self.price=price
    def __str__(self):
        return f"{self.category} - {self.name}:{self.price}"

    @abstractmethod
    def get_category(self):
        return self.category

class Entree(Menu):
    def get_category(self):
        return "Entree"

class Plat(Menu):
    def get_category(self):
        return "Plat"

class Dessert(Menu):
    def get_category(self):
        return "Dessert"

class Drink(Menu):
    def get_category(self):
        return "Drink"

#création du menu
menu_list =[
    Menu("Entree", "salade",7),
    Menu("Entree", "quiche", 7),
    Menu("Entree", "soupe",6),
    Menu("Plat","boeuf bourguignon", 10),
    Menu("Plat", "poulet basquaise", 10),
    Menu("Plat","tagliatelles à la sauce aux cèpes", 12),
    Menu("Dessert","tiramisu", 6),
    Menu("Dessert", "mousse au chocolat",4),
    Menu("Dessert", "tarte au citron", 6),
    Menu("Boisson","eau",0),
    Menu("Boisson", "vin", 3),
    Menu("Boisson", "soda", 3)
]

class Table:
    def __init__(self, name: str, seat: int):
        self.name = name
        self.seat = seat
        self.is_reserved = False  # Suivi si la table est réservée

def assign_table(self, group_size: int) -> Table:
    available_tables = [table for table in self.tables if table.seat >= group_size and not table.is_reserved]
    if available_tables:
        table = min(available_tables, key=lambda table: table.seat)
        table.is_reserved = True  # Marquer la table comme réservée
        return table
    else:
        return None

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
    def __init__(self, name: str, group_size: int) -> None:
        self.name = name
        self.group_size = group_size
        self.command: List[Menu] = []

    def add_to_command(self, plate: Menu):
        self.command.append(plate)

class Boy:
    def __init__(self,name):
        self.name=name

    # demander au client ce qu'il veut manger
    def get_client_choise(self,client):
        print(f"Bonjour {client.name}, voici le menu du jour")
        for index, plate in enumerate(menu_list, 1):
            print(f"{index}. {plate}")

        choice = input("Choisissez les plats en entrant les numéros séparés par des espaces : ")
        choice_list = [int(i) - 1 for i in choice.split() if i.isdigit() and 0 <= int(i) - 1 < len(menu_list)]

        if choice_list:
            for i in choice_list:
                client.add_to_command(menu_list[i])
            print(f"{client.name}, bon appétit !")
        else:
            print("Aucun choix valide n'a été fait.")

    def ask_money(self, client):
        total=client.command.display_command()
        money = float(input(f"Pour lutter contre le resto basket, veuillez payer : {total}€"))

def simulation_service():
    boy = Boy("Jeannot")

    client_name = input("Entrez votre nom :")
    client = Client(client_name)

    boy.get_client_choise(client)
    boy.ask_money(client)

if __name__=="__main__":
    simulation_service()


