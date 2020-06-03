# singly linked list
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def set_data(self,d):
        self.data = d
    def get_data(self):
        return self.data

class linkedList(object):
    def __init__(self,r,n = None):
        self.root = Node(r)
        self.size = 0
    def get_size(self):
        return self.size
    
    def add(self,d):
        # Adding in front
        new_node = Node(d, self.root)
        self.root = new_node
        self.size+=1
    
    def addB(self,d):
        new_node = Node(d)
        this_node = self.root
        
        while this_node:
            if this_node.next_node is None:
                this_node.next_node = new_node 
            else:
                this_node = this_node.next_node


    def remove(self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size-=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self,d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    def display(self):
        this_node = self.root
        while this_node:
            print(this_node.get_data())
            this_node = this_node.get_next()
# operations on linked list
myList = linkedList(5)
myList.add(6)
myList.add(7)
myList.add(8)
#myList.addB(4)
#myList.remove(7)
myList.display()