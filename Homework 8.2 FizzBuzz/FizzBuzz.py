nummer = int(raw_input("Kies een nummer tussen 1 en  100: "))
print nummer

startGetal = 1

while startGetal < nummer:
    if (startGetal % 15 ) == 0: print "FizzBuzz"
    elif (startGetal % 5 ) == 0:  print "Buzz"
    elif (startGetal % 3 ) == 0: print "Fizz"
    else: print str(startGetal)
    startGetal +=1

