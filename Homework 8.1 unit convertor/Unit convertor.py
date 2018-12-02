print "convertor die km naar mijl kan omzetten"

while True:
    print "geef km voor omzetting. alleen getallen ingeven!"
    km = raw_input("kilometers: ")

    try:
        km = float (km.replace(",",".")) # komma's vervangen door een punt

        miles = km * 0.621371

        print "{0} kilometers is {1} mijlen.".format(km, miles)
    except Exception as e:
        print "nummers ingeven, geen letters"
    
    keuze = raw_input("wil u nog een conversie doen? (y/n): ")

    if keuze.lower() != "y" and keuze.lower() !="yes":
        break