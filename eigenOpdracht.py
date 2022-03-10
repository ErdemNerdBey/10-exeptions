# waterfles verkoop
a = False

prijzen = {
    "kleine flessen" : 0.32,
    "normale flessen" : 0.47,
    "grote flessen" : 0.69,
}
aantalFlessen = {}

print('     welkom bij 瓶裝天堂\n')
print('           (flessen)\n')
for i in prijzen:
    print(f'{i}: €{prijzen[i]}')


def vragenHoeveelFlessen(welkeFlessen):
    global a
    hoeveelFlessen = input(f'\nHoeveel {welkeFlessen} wilt u?\n')
    try: 
        aantalFlessen[welkeFlessen] = int(hoeveelFlessen)
        if aantalFlessen[welkeFlessen] == 0:
            aantalFlessen.pop(welkeFlessen)
        a = True
    except:
        print("voer een hele getal in.\n")

def bonnetje():
    bedrag = 0
    for i in aantalFlessen:
        bedrag += aantalFlessen[i] * prijzen[i]
        print(f"{aantalFlessen[i]} {i}: €{aantalFlessen[i] * prijzen[i] :.2f}")
    print(f"totaal: {bedrag:.2f}")

for i in prijzen:
    while a == False:
        vragenHoeveelFlessen(i)
    a = False

bonnetje()