class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self, no):
        pass

    def InsertLast(self, no):
        pass

    def InsertAtPos(self, no, pos):
        pass

    def DeleteFirst(self, no):
        pass

    def DeleleLast(self, no):
        pass

    def DeleteAtPos(self, pos):
        pass

    def Display(self):
        pass

    def Count(self):
        return self.count

def main():
    sobj = SinglyLL()

    sobj.InsertFirst(11)
    sobj.InsertLast(21)
    sobj.Display()

if __name__ == "__main__":
    main()