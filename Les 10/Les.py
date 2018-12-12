import datetime

current_year = int(datetime.datetime.now().year)

print current_year

class Person(object):
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = phone_number
            self.birth_year = birth_year
            self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        return current_year - int(self.birth_year)

john = Person(first_name="John", last_name="Clark", phone_number=89348239429, birth_year=1979, email="john@clark.com")

marissa = Person(first_name="Marissa", last_name="Mayer", phone_number=83483204032, birth_year=1978, email="marissa@yahoo.com")

bruce = Person(first_name="Bruce", last_name="Wayne", phone_number=902432309443, birth_year=1939, email="bruce@batman.com")

print john.first_name
print marissa.email
print marissa.last_name
print bruce.email
print "lege lijn \n"

contact_book = [john, marissa, bruce]

for Person in contact_book:
    print Person.first_name
    print Person.last_name
    print Person.first_name + " qgdqsdg " + Person.last_name
    print Person.get_full_name()
    print Person.birth_year
    print Person.get_age()
    print Person.email
    print " " #lege lijn
