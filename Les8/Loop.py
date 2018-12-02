# secret = 22
# guess = 0

# while guess !=  secret:
#     guess = int(raw_input("Raad het geheime nummer (tussen 1 en 30): "))

#     if guess == secret:
#         print "juist geraden, proficiat!! het is nummer 22:)"
#     else:
#         print "sorry, verkeer geraden het geheime nummer is niet "+ str(guess)
            

# secret = 22


# for x in range(5):
#     guess = int(raw_input("raad het geheime nummer tussen 1 en  30: "))

#     if guess == secret:
#         print "juist geraden, proficiat!! het is nummer 22:)"
#         break
#     else:
#         print "sorry, verkeer geraden het geheime nummer is niet "+ str(guess)

# secret = 22


# while True:
#     guess = int(raw_input("raad het geheime nummer tussen 1 en  30: "))

#     if guess == secret:
#         print "juist geraden, proficiat!! het is nummer 22:)"
#         break
#     else:
#         print "sorry, verkeer geraden het geheime nummer is niet "+ str(guess)
            
secret = 22 

while   True:
        guess = int(raw_input("raad het geheime nummer tussen 1 en  30: "))

        if guess == secret:
            print"goed geraden het is nummer 22"
            break
        elif guess > secret:
            print "het getal is kleiner"
        elif guess < secret:
            print "het getal is groter"