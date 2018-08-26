# Script by Anthony and Pablo

inputData = [input("a,b,c type in this format > "),
             input("a,b,c type in this format > "),
             input("a,b,c type in this format > ")]

points = []

class AnthonyPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " "  + str(self.z)

def createPoint(a,b,c):
    return AnthonyPoint(a,b,c)

def subtract(pointA, pointB):
    return AnthonyPoint(pointA.x - pointB.x, pointA.y - pointB.y, pointA.z - pointB.z)

def crossProduct(pointA, pointB):
    i = (pointA.y * pointB.z) - (pointA.z * pointB.y)
    j = -((pointA.x * pointB.z) - (pointA.z * pointB.x))
    k = (pointA.x * pointB.y) - (pointA.y * pointB.x)
    return AnthonyPoint(i,j,k)

def findPlaneEquation(pointOne, pointTwo, pointThree):
    pass

for input in inputData:
    # input = "1,2,3"
    print("Iterating through: " + input)
    rawPoints = input.split(",") # ["1", "2", "3"]
    points.append(createPoint(float(rawPoints[0]), float(rawPoints[1]), float(rawPoints[2])))


vectorP = subtract(points[1], points[0])
vectorQ = subtract(points[2], points[0])

normalVector = crossProduct(vectorP, vectorQ)
space = " + "

for point in points:
    coeff = normalVector.x * point.x + normalVector.y * point.y + normalVector.z * point.z
    print(str(normalVector.x) + "x" + space + str(normalVector.y) + "y" + space + str(normalVector.z) + "z = " + str(coeff))
