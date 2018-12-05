print ("Laat ons het menu voor vandaag samenstellen: ")

import datetime
now = datetime.datetime.now()
print (now.strftime("%d-%m-%Y"))
print  ("Het menu voor: "+ now.strftime("%d-%m-%Y"))

menu = {}

while True:
    gerecht = raw_input("Wat kan de klant kiezen: ")
    gerecht_prijs = raw_input("wat moet het gerecht kosten: ")
    print ("het gerecht is: ") + gerecht + (" en de klant moet %s betalen")% gerecht_prijs
    menu[gerecht]= gerecht_prijs
    print menu

    nieuw_gerecht = raw_input("Nog een nieuw gerecht toevoegen? (j/n)")

    if nieuw_gerecht.lower() == "n":
        break

with open("menu.txt", "w+") as menu_file:

    print ("Het menu voor: "+ now.strftime("%d-%m-%Y"))
    menu_file.write("Het menu voor: " + now.strftime("%d-%m-%Y") + "\n\n")

    for item in menu:
        print ("* ") + item
        menu_file.write("* "+item+"\n")

print ("Maak uw keuze uit bovenstaande gerechten, daarna gaan wij aan het werk en mag u genieten!! (en betalen)")
