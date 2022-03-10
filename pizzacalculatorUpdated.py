#Erdem Uysal opdracht:pizza calculator
smallPizzaPrijs = 5.69
medium_pizza_prijs = 6.97
large_pizza_prijs = 8.98
aantal_small_pizza = 0
aantal_medium_pizza = 0
aantal_large_pizza = 0

print('welkom bij Pizza Lakakakaa')
print('wat wilt u vandaag eten?\n')
print('           MENU')
print('| small pizza: 5,69 euro   |')
print('| medium pizza: 6,97 euro  |')
print('| large pizza : 8,98 euro  |\n')

def smallPizzas():
    global aantal_small_pizza
    print('Hoeveel small pizzas wilt u?\n')
    aantal_small_pizza = input('small pizza: ')
    try: 
        aantal_small_pizza = int(aantal_small_pizza)
        if aantal_small_pizza < 0:
            print("je kan niet minder dan 0 bestellen")
            smallPizzas()
        mediumPizzas()
    except:
        print("voer een hele getal in.\n")
        smallPizzas()

def mediumPizzas():
    global aantal_medium_pizza
    print('Hoeveel medium pizzas wilt u?\n')
    aantal_medium_pizza = input('medium pizza: ')
    try: 
        aantal_medium_pizza = int(aantal_medium_pizza)
        if aantal_large_pizza < 0:
            print("je kan niet minder dan 0 bestellen")
            mediumPizzas()
        largePizzas()
    except:
        print("voer een hele getal in.\n")
        mediumPizzas()

def largePizzas():
    global aantal_large_pizza
    print('Hoeveel large pizzas wilt u?\n')
    aantal_large_pizza = input('large pizzas: ')
    try: 
        aantal_large_pizza = int(aantal_large_pizza)
        if aantal_large_pizza < 0:
            print("je kan niet minder dan 0 bestellen")
            largePizzas()
    except:
        print("voer een hele getal in.\n")
        largePizzas()

smallPizzas()

bedrag = aantal_small_pizza * smallPizzaPrijs + aantal_medium_pizza * medium_pizza_prijs + aantal_large_pizza * large_pizza_prijs

print(f'u heeft {aantal_small_pizza} small pizzas met totale prijs van {round(smallPizzaPrijs * aantal_small_pizza, 2)} euro, {aantal_medium_pizza} medium pizzas met totale prijs van {round(medium_pizza_prijs * aantal_medium_pizza, 2)} euro en {aantal_large_pizza} large pizzas bestelt met totale prijs van {round(large_pizza_prijs * aantal_large_pizza, 2)} euro. \n')
print(f'uw totale bedrag is {round(bedrag,2)} euro\n')