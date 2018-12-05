# convert datatypes
#omzetten getal naar string om bvb te gebruiken in print
age = 13
print "ik ben " + str(age) + " jaar oud"

#string omzetten naar integer
number1 = "100"
number2 = "20"

string_optellen = number1 + number2
print string_optellen

int_optellen = int(number1) + int(number2)
print int_optellen

#float omzetten naar string of behouden bij print
string_num = "7.5"  # type: str

print float(string_num)


float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
print product
big_string = "product is gelijk aan " + str(product)
print big_string



# item vanuit variabele toevoegen aan een lijst:
todo_list = []   # hiermee wordt de lijst aangemaakt
taak = raw_input("Voeg een taak toe: ")
print ("Uw taak is: ") + taak
todo_list.append(taak) # zo voegen we een variabele toe aan een lijst


todo_file = open("todo.txt", "w+") # file variabele aanmaken en file openen of aanmaken indien niet bestaand
todo_file.write("Voltooide taken in overzicht:\n") # schrijven in de aangemaakte tekstfile
todo_file.write("- " + x + "\n")  # taak toevoegen in de tekstfile
