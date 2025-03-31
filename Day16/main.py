from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def cafe_open():
    nespresso = CoffeeMaker()
    cashier = MoneyMachine()
    menu = Menu()
    status_machine = True
    while status_machine:
         
        user_input = input("What would you like to order? ").lower()
       
        if user_input == "report":
            print(nespresso.report())
        elif user_input == "off":
            print("Coffee machine is closed see u later. <3 ")
            status_machine = False
        else:
            drinks = menu.find_drink(user_input)
            if drinks == None:
                print("Try again.")
            elif nespresso.is_resource_sufficient(drink=drinks):
                if cashier.make_payment(cost=drinks.cost):
                    nespresso.make_coffee(drinks)
                else: 
                    print("Not enough money try again!")
 
cafe_open()
    
    