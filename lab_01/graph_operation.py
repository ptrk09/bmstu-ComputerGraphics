import math
from tkinter import Canvas

def calcSinglePiece(listPoints):
    try:
        minY, maxY = 100000000, -100000000
        minX, maxX = 100000000, -100000000
        for el in listPoints:
            if el[0] > maxX: maxX = el[0]
            if el[0] < minX: minX = el[0]
            if el[1] > maxY: maxY = el[1]
            if el[1] < minY: minY = el[1]
        Dx = abs(maxX - minX)
        Dy = abs(maxY - minY)
        maxDelta = max(Dx, Dy)
        singlePiece = 700 / maxDelta
    except:
        singlePiece = 0
        print("calcSinglePiece: error\n")
    return singlePiece, minX, minY


def getСoordPoint(point, singlePiece, minX, minY):
    x, y = 0, 0

    #print("getCoordPoint: point[0] - minX=", point[0], minX, point[1], minY, singlePiece)
    x = 50 + ((point[0] - minX) * singlePiece)
    y = 750 - ((point[1] - minY) * singlePiece)

    return x, y


def paintPoint(placeGraph, x, y, color):
    placeGraph.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color)


def checkExistTriangle(point1, point2, point3):
    if ((point2[1] - point1[1]) * (point3[0] - point1[0])
    != (point3[1] - point1[1]) * (point2[0] - point1[0])):
        return True

    return False


def findCircle(points):
    listNeedPoints = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                if checkExistTriangle(points[i], points[j], points[k]):
                    listNeedPoints.append([points[i], points[j], points[k]])

    listUniquePoints = []
    for i in listNeedPoints:
        if i not in listUniquePoints:
            listUniquePoints.append(i)

    return listUniquePoints


def getCircleRadius(list):
    absLen = lambda x1, y1, x2, y2: ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    # calc center Circle
    newList = []
    for i in range(len(list)):
        midSideA = [list[i][0][0] + (list[i][1][0] - list[i][0][0]) / 2,
                    list[i][0][1] + (list[i][1][1] - list[i][0][1]) / 2]
        midSideB = [list[i][1][0] + (list[i][2][0] - list[i][1][0]) / 2,
                    list[i][1][1] + (list[i][2][1] - list[i][1][1]) / 2]

        A1, A2 = list[i][1][0] - list[i][0][0], list[i][2][0] - list[i][1][0]

        B1, B2 = list[i][1][1] - list[i][0][1], list[i][2][1] - list[i][1][1]

        C1 = -(A1 * midSideA[0] + B1 * midSideA[1])
        C2 = -(A2 * midSideB[0] + B2 * midSideB[1])

        x, y = 0, 0
        try:
            x = (B2 * C1 - B1 * C2) / (B1 * A2 - B2 * A1)
            y = -(A1 * x + C1) / B1
        except:
            if B1 < 0.001:
                B1 = 0.0001
            #if B2 < 0.001:
                #B2 = 0.0001
            x = (B2 * C1 - B1 * C2) / (B1 * A2 - B2 * A1)
            y = -(A1 * x + C1) / B1

        newList.append([x, y, absLen(x, y, list[i][0][0], list[i][0][1])])

    print("getCircleRadius: ", newList)
    return newList


def printPoint(placeGraph, point, singlePiece, minX, minY):
    x, y = getСoordPoint(point, singlePiece, minX, minY)
    curText = str("(" + str(point[0]) + ", " + str(point[1]) + ")")
    placeGraph.create_text(x + 20, y - 15, text=curText)


def paintCircle(placeGraph, singlePiece, minX, minY, point, color="blue"):
    x, y = getСoordPoint(point, singlePiece, minX, minY)

    printPoint(placeGraph, point, singlePiece, minX, minY)
    paintPoint(placeGraph, x, y, color)

    firstBorderPoints = (point[0] - point[2], point[1] - point[2])
    secondBorderPoints = (point[0] + point[2], point[1] + point[2])
    x1, y1 = getСoordPoint(firstBorderPoints, singlePiece, minX, minY)
    x2, y2 = getСoordPoint(secondBorderPoints, singlePiece, minX, minY)

    placeGraph.create_oval(x1, y1, x2, y2, width=2, outline=color)
