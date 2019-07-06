import random
import math


class Environment(object):
    def __init__(self):
        # 0 indicates Clean, 1 indicates Dirty
        self.locationCondition = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
        # 0 indicates open, 1 indicates boundary
        self.locationBoundary = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]

        # Location state 1= open, 0= obstacle

        # randomize conditions in locations
        for row in range(4):
            for coloumn in range(4):
                self.locationCondition[row][coloumn] = random.randint(0, 1)
                if (self.locationBoundary[row][coloumn] == 1):
                    self.locationCondition[row][coloumn] = 0
                # print("At Location:", row, " ,", coloumn, "Conditions is", self.locationCondition[i][j])


class ReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        # Instantiate performance measurement
        self.Score = 0
        # Visited Locations 1 = unvisited
        self.VisitedLocations = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        # place vacuum at random location: 0 is row, 1 is coloumn
        self.vacuumLocation = [random.randint(0, 3), random.randint(0, 3)]
        # sets intial location to visted
        self.VisitedLocations[self.vacuumLocation[0]][self.vacuumLocation[1]] = 0
        # Define distance array
        self.DistanceToUnvisitedTile = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        # Define movement to closest tile (0 is row, 1 is coloumn)
        self.MovementToTile = [0, 0]

        # While tile is unvisited
        while (1 in self.VisitedLocations[0]) or (1 in self.VisitedLocations[1]) or (1 in self.VisitedLocations[2]) or (
                1 in self.VisitedLocations[3]):
            # Clean or leave alone

            if (Environment.locationCondition[self.vacuumLocation[0]][self.vacuumLocation[1]] == 1):
                # print("Location ",vacuumLocation[0],vacuumLocation[1]," is Dirty.")
                # suck the dirt  and mark it clean
                Environment.locationCondition[self.vacuumLocation[0]][self.vacuumLocation[1]] = 0;
                self.Score += 1
                # print("Location ",self.vacuumLocation[0],self.vacuumLocation[1],"has been cleaned")
                # else:
                # print("Location ",vacuumLocation[0],vacuumLocation[1],"is clean")

            # Update distance array
            self.UpdateDistanceToUnvisitedTile()
            self.moveClosestTile()

        # print(Environment.locationCondition)
        # print("Performance Measurement: " + str(self.Score))
        # print(self.VisitedLocations)

    def access_method(self):
        return self.Score

    def moveClosestTile(self):

        for i in range(int(math.fabs(self.MovementToTile[0]))):
            if (self.MovementToTile[0] < 0):
                self.moveLeft()

            if (self.MovementToTile[0] > 0):
                self.moveRight()

        for i in range(int(math.fabs(self.MovementToTile[1]))):
            if (self.MovementToTile[1] < 0):
                self.moveDown()

            if (self.MovementToTile[1] > 0):
                self.moveUp()

    def moveLeft(self):
        self.vacuumLocation[0] -= 1
        self.Score -= 1
        if (self.vacuumLocation[0] < 0):
            self.vacuumLocation[0] = 0
            self.Score += 1
        else:
            self.VisitedLocations[self.vacuumLocation[0]][self.vacuumLocation[1]] = 0

    def moveRight(self):
        self.vacuumLocation[0] += 1
        self.Score -= 1
        if (self.vacuumLocation[0] > 3):
            self.vacuumLocation[0] = 3
            self.Score += 1
        else:
            self.VisitedLocations[self.vacuumLocation[0]][self.vacuumLocation[1]] = 0

    def moveUp(self):
        self.vacuumLocation[1] += 1
        self.Score -= 1
        if (self.vacuumLocation[1] > 3):
            self.vacuumLocation[1] = 3
            self.Score += 1
        else:
            self.VisitedLocations[self.vacuumLocation[0]][self.vacuumLocation[1]] = 0

    def moveDown(self):
        self.vacuumLocation[1] -= 1
        self.Score -= 1
        if (self.vacuumLocation[1] < 0):
            self.vacuumLocation[1] = 1
            self.Score += 1
        else:
            self.VisitedLocations[self.vacuumLocation[0]][self.vacuumLocation[1]] = 0

    def UpdateDistanceToUnvisitedTile(self):
        Minimum = 10000

        for row in range(4):
            for coloumn in range(4):
                if (self.VisitedLocations[row][coloumn] == 0):
                    self.DistanceToUnvisitedTile[row][coloumn] = 'V'
                else:
                    self.DistanceToUnvisitedTile[row][coloumn] = math.fabs(self.vacuumLocation[0] - row) + math.fabs(
                        self.vacuumLocation[1] - coloumn)
                    if (Minimum > self.DistanceToUnvisitedTile[row][coloumn]):
                        self.MovementToTile[0] = row - self.vacuumLocation[0]
                        self.MovementToTile[1] = coloumn - self.vacuumLocation[1]
                        Minimum = self.DistanceToUnvisitedTile[row][coloumn]


avg = 0
for i in range(10000):
    theEnvironment = Environment()
    theVacuum = ReflexVacuumAgent(theEnvironment)
    avg += theVacuum.access_method()

avg = avg / 10000
print(avg)