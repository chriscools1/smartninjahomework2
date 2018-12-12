class Dad(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print self.first_name + " " + self.last_name


class Son(Dad):
    def __init__(self, first_name, last_name, toy):
        Dad.__init__(self, first_name, last_name)
        self.toy = toy

Johnny = Son(first_name="Johnny", last_name="Brown", toy="Tractor")
Johnny.full_name()