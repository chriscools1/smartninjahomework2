# print ("Welkom op ons todo programma.")
#
# while True:
#     task = raw_input("Voeg een taak toe: ")
#     print ("Uw taak is: ") + task
#
#     new = raw_input("Wil je nog een taak toevoegen? (ja/nee) ")
#
#     if new == "nee":
#         break
#
# print "geen nieuwe taken meer"


# empty_list = []
# print   empty_list
#
# list_with_items = ["first item","second item", 34, 12.4]
# print list_with_items
#
# var1 = "eerste variable"
# var2 = "tweede variabele"
# nieuwe_lijst = [var1, var2]
# print nieuwe_lijst


#
#
#
# print ("Welkom in ons to do programme!")
#
# todo_list = []
#
# while True:
#     taak = raw_input("Voeg een taak toe: ")
#     print ("Uw taak is: ") + taak
#     todo_list.append(taak) # zo voegen we een variabele toe aan een lijst
#
#     nieuwe_taak = raw_input("wilt u nog een nieuwe taak toevoegen? (ja/nee) ")
#
#     if nieuwe_taak == "nee":
#         break
#
# print ("alle taken zijn: %s") %todo_list
# print ("this is the end!")

# een_lijst = ["item 1", "item 2", "item 3"]
#
# for jos in een_lijst:
#     print jos

# print ("welkom in ons todo programma. ")
#
# todo_list = []
#
# while True:
#     taak = raw_input("voeg een todo toe: ")
#     print ("Uw taak is: ") + taak
#     todo_list.append(taak)
#
#     new = raw_input("Wil u nog een taak toevoegen? (ja / nee)  ")
#
#     if new == "nee":
#         break
#
# print ("Alle taken zijn: ")
#
# for taken in todo_list:
#     print taken
#
# print "gedaan"
#
# some_dictionary = {"1":"eerste","2":"tweede","3":"derde"}
# print some_dictionary
#
# taken = {"taak 1" : False, "taak 2" : True , "taak 3" : False}
# print taken

print ("Welkom in onze todo-app! ")

todo_lijst = {}

while True:
    taak = raw_input("voeg een todo toe: ")
    taak_status = raw_input("Is de taak gedaan? (ja/nee)")
    print ("uw taak is: ") + taak

    if taak_status == "ja":
        todo_lijst[taak] = True
    else:
        todo_lijst[taak] = False
    print todo_lijst

    nieuwe_taak = raw_input("wil u een nieuwe taak toevoegen? (ja / nee) ")

    if nieuwe_taak == "nee":
        break

print ("alle taken: %s") % todo_lijst

todo_file = open("todo.xlsx", "w+") # file variabele aanmaken en file openen of aanmaken indien niet bestaand


print ("voltooide taken: ")
todo_file.write("Voltooide taken in overzicht:\n") # schrijven in de aangemaakte tekstfile
for x in todo_lijst:
    if todo_lijst[x] is True:
        print ("- ") + x
        todo_file.write("- "+ x + "\n") # taak toevoegen in de tekstfile

print ("openstaande taken: ")
todo_file.write("Onvoltooide taken in overzicht:\n")
for x in todo_lijst:
    if todo_lijst[x] is False:
        print ("- ") + x
        todo_file.write("- "+x+"\n")

todo_file.close()



print ("geen nieuwe taken meer! ")



