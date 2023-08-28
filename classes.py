from utils.calculator import Calculator

class Car:
    def __init__(self,color,plate_number,brand,no_of_wheels):
        self.color= color
        self.plate_number= plate_number
        self.brand = brand
        self.no_of_wheels = no_of_wheels

    def print_no_of_wheels(self):
        print(self.no_of_wheels)

    def drive():
        print("The car is moving forard")

    def playMusic():
        print("I love the music")

car1 = Car("red","VR16","TOYATA",4)
#print(car1.no_of_wheels)
ty= Calculator(23,0)
print(ty.divide())