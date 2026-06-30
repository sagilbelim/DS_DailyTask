class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, vehicle):
        if self.count == self.size:
            print("Queue is Full")
            return

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = vehicle
        self.count += 1

        print(vehicle, "entered the Toll Plaza")

    def dequeue(self):
        if self.count == 0:
            print("Queue is Empty")
            return

        print(self.queue[self.front], "left the Toll Plaza")

        self.front = (self.front + 1) % self.size
        self.count -= 1

    def display(self):
        if self.count == 0:
            print("Queue is Empty")
        else:
            print("\nVehicles in Queue:")
            print(self.queue)


q = CircularQueue(5)

q.enqueue("Car")
q.enqueue("Bus")
q.enqueue("Truck")
q.enqueue("Bike")
q.enqueue("Auto")

q.display()

q.dequeue()
q.dequeue()

q.enqueue("Taxi")
q.enqueue("Van")

q.display()