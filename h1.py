class ConveyorBelt:
    def __init__(self):
        self.belt = [None] * 8

    def updateSlot(self, index, product):
        if 0 <= index < 8:
            self.belt[index] = product
            print(product, "stored at slot", index)
        else:
            print("Invalid slot!")

    def checkSlot(self, index):
        if 0 <= index < 8:
            print("Slot", index, ":", self.belt[index])
        else:
            print("Invalid slot!")

    def findProduct(self, product):
        if product in self.belt:
            print(product, "found at slot", self.belt.index(product))
        else:
            print("Product not found.")

    def isFull(self):
        if None in self.belt:
            print("Conveyor Belt is NOT Full")
        else:
            print("Conveyor Belt is Full")



c = ConveyorBelt()

c.updateSlot(0, "Laptop")
c.updateSlot(1, "Mouse")
c.updateSlot(2, "Keyboard")
c.updateSlot(3, "Keyboard")
c.updateSlot(4, "Keyboard")
c.updateSlot(5, "Keyboard")
c.updateSlot(6, "Keyboard")
c.updateSlot(7, "Keyboard")
c.updateSlot(8, "Keyboard")


c.checkSlot(1)
c.findProduct("Keyboard")
c.isFull()

print("\nCurrent Belt:")
print(c.belt)