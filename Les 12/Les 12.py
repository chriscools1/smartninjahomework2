#linked list

class Node(object):
    def __init__(self, payload=0,prev=None, nextt=None):
        self.nextt = nextt
        self.prev = prev
        self.payload = payload

    def __str__(self):
         return str(self.payload)

def _ count_elements(e):
    temp = start
            self.size = 1
            while  temp.nextt != None:
                size +=1
                temp = temp. n


class LinkedList(object):
    def __init__(self, start=None ):
        self.start = start
        self.end = start
        print (ype(start))
        if type(start) != Node and start !=None:
            raise TypeError
        if start != None:
            self.start.prev = None
            extt
            self.end = temp
        else:
            self.size = 0

    def add_element(self, e):
        if type(e) != Node :
            return False
        else:
            temp = e
            size = 1
            while temp.nextt !=None:
                size += 1
                temp = temp.nextt
            self.size += size
            self.end.nextt = e
            e.prev = self.end
            self.end = temp




ll = LinkedList(Node())