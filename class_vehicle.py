class vehicle:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def print_(self):
        print("the type of vehilce is " + str(self.type.title()) + ".")
        print("the name of vehicle is " + str(self.name.title()) + ".")


car = vehicle("miaoyin","car")
car.print_()

