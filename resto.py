#créer un menu
#créer une classe pour client + menu
#demander au client ce qu'il veut manger
#pour combien de personnes
#bilan fin de service

#class menu
class Menu :
    def __init__(self,plate,food,price):
        self.plate=plate
        self.food=food
        self.price=price


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