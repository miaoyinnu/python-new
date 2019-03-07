class vehicle(object):
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
bike = vehicle("bike",10)
print(" name: " + str(bike.name) +" and speed:" + str(bike.speed))