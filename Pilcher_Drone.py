#Author Name: Stephen Pilcher
#Date: 5/15/2022
#Program Name: Pilcher_Drone
#Purpose: Simulation using button, drone movement in x, y, z location

class Drone:
    def __init__(self, x, y, z, o):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__o = o
    def moveUp(self, z):
        self.__z += 1
    def moveDown(z):
        self.__z -= 1
    def moveForward(self, x, y, o):
        if self.__o == 0:
            self.__y =+ 1
        elif self.__o == 1:
            self._x=+ 1
        elif self.__o == 2:
            self.__y -= 1
        else:
            self.__x -= 1
    def moveBack(self, x, y, o):
        if self.__o == 0:
            self.__y -= 1
        elif self.__o == 1:
            self.__x -= 1
        elif self.__o == 2:
            self.__y =+ 1
        else:
            self._x=+ 1
    def turnLeft(self, o):
        if self.__o == 0:
            self.__o = 3
        elif self.__o == 1:
            self.__o = 0
        elif self.__o == 2:
            self.__o = 1
        else:
            self.__o = 2
    def turnRight(self, o):
        if self.__o == 0:
            self.__o = 1
        elif self.__o == 1:
            self.__o = 2
        elif self.__o == 2:
            self.__o = 3
        else:
            self.__o = 0
    def displayPos(self, x, y, z, o):
        if self.__o == 0:
            orientation = "North"
        elif self.__o == 1:
            orientation = "East"
        elif self.__o == 2:
            orientation = "South"
        else:
            orientation = "West"
        print("x_pos = " + x + ", y_pos = " + y + ", z_pos = " + z + ", orientation = " + orientation)

def main():

    x = 0
    y = 0
    z = 0
    o = 0
    nav = 0
    drone1 = Drone (x, y, z, o)

    while nav < 8:
        print("Which direction would you like to move the drone?")
        print("1 - Move Up")
        print("2 - Move Down")
        print("3 - Move Forward")
        print("4 - Move Backward")
        print("5 - Turn Left")
        print("6 - Turn Right")
        print("7 - Display Position")
        print("8 - Exit Navigation")
        nav = input()
        if nav == 1:
            drone1.moveUp(z)
        elif nav == 2:
            drone1.moveDown(z)
        elif nav == 3:
            drone1.moveForward(x, y, o)
        elif nav == 4:
            drone1.moveBack(x, y, o)
        elif nav == 5:
            drone1.turnLeft(o)
        elif nav == 6:
            drone1.turnRight(o)
        elif nav == 7:
            drone1.displayPos(x, y, z, o);

main()