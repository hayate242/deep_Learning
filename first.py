import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([1.0, 2.0, 3.0])
# print(x)
# type(x)

class Array:
    def __init__(self):
        self.x = np.array([1,2,3])
        self.y = np.array([4,5,6])
        self.z = self.x ** self.y


    def printHello(self):
        print(self.z)
        print(self.x)



m = Array()
m.printHello()
m.printHello()
print("やば，完璧やん")
