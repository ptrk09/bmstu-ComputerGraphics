from tkinter import Entry, END, Canvas, messagebox
from graph_operation import *


dataError = "Введите в поле х: координату х(число)\n"\
            "в поле у: координату у(число)\nв поле множество: "\
            "1 - первое мн., 2- второе мн."


def delPoint(listsPoints, listsBox, placeGraph):
    select = list(listsBox[0].curselection())
    select2 = list(listsBox[1].curselection())
    try:
        listsBox[0].delete(select[0])
        listsPoints[0].remove(listsPoints[0][select[0]])
        showPoints(placeGraph, listsPoints)
    except:
        print("del point: no del point in listPoint 1\n")

    try:
        listsBox[1].delete(select2[0])
        listsPoints[1].remove(listsPoints[1][select2[0]])
        showPoints(placeGraph, listsPoints)
    except:
        print("del point: no del point in listPoint 2\n")


def showPoints(placeGraph, listPoints, singlePiece=None, minX=None, minY=None):
    placeGraph.delete("all")
    listPoints = listPoints[0] + listPoints[1]

    if singlePiece is None:
        singlePiece, minX, minY = calcSinglePiece(listPoints)

    for point in listPoints:
        x, y = getСoordPoint(point, singlePiece, minX, minY)
        printPoint(placeGraph, point, singlePiece, minX, minY)

        if point[2] == 1:
            paintPoint(placeGraph, x, y, "green")
        elif point[2] == 2:
            paintPoint(placeGraph, x, y, "red")
        else:
            paintPoint(placeGraph, x, y, "blue")


def createGraph(placeGraph, listPoints, isVisual=False):
    allPoints = listPoints[0] + listPoints[1]
    list1, list2 = [], []
    para = 0
    x, y = 0, 0

    if len(listPoints[0]) >= 3:
        list1 = findCircle(listPoints[0])
    if len(listPoints[1]) >= 3:
        list2 = findCircle(listPoints[1])

    curSinglePiece, minX, minY = calcSinglePiece(allPoints)
    list1, list2 = getCircleRadius(list1), getCircleRadius(list2)
    for el in list1 + list2:
        allPoints.append((el[0] + el[2], el[1] + el[2]))
        allPoints.append((el[0] - el[2], el[1] - el[2]))

    curSinglePiece, minX, minY = calcSinglePiece(allPoints)
    allPoints = allPoints[:len(allPoints)
                        - len(list2) * 2 - len(list1) * 2]

    showPoints(placeGraph, listPoints,
               singlePiece=curSinglePiece,
               minX=minX, minY=minY)

    if not(isVisual):
        for i in range(len(list1)):
            for j in range(len(list2)):
                isRightBorder = abs(list1[i][0] + list1[i][2] 
                    - list2[j][0] + list2[j][2]) <= 0.01

                isLeftBorder = abs(list1[i][0] - list1[i][2] 
                    - list2[j][0] - list2[j][2]) <= 0.01   

                if isRightBorder:
                    x, y = getСoordPoint((list1[i][0] + list1[i][2], 1000), 
                                          curSinglePiece, minX, minY)
                elif isLeftBorder:
                    x, y = getСoordPoint((list1[i][0] - list1[i][2], 1000), 
                                          curSinglePiece, minX, minY)
                
                if isRightBorder or isLeftBorder:
                    paintCircle(placeGraph, curSinglePiece, minX, minY, list1[i], color="gray")
                    paintCircle(placeGraph, curSinglePiece, minX, minY, list2[j])
                    placeGraph.create_line(x, 0, x, 800, width=2)
                    para += 1

        if not(para):
            messagebox.showinfo(title=None, message="Подходящих пар окружностей не найдено")
    else:
        for point in list1:
            paintCircle(placeGraph, curSinglePiece, minX, minY, point, color="gray")
        for point in list2:
            paintCircle(placeGraph, curSinglePiece, minX, minY, point)


def addPoint(placeGraph, listEntry, listPoints, listBoxs):
    typePoint = 0
    try:
        typePoint = int(listEntry[2].get())
        if typePoint in [1, 2]:
            print("add point: true type point\n")
        else:
            print("add point: false type point -> clear entry\n")
            messagebox.showinfo(title="Некорректный ввод",
                                message="Введите в поле множество: "
                                "1 - первое мн., 2- второе мн.")
            list(map(lambda x: x.delete(0, END), listEntry))
    except:
        messagebox.showinfo(title="Некорректный ввод", message=dataError)
        print("add point: error type!\n")
        return

    line = (listEntry[0].get() + " " + listEntry[1].get()).split()
    try:
        print(len(line), typePoint in [1, 2])
        if len(line) == 2:
            if typePoint in [1, 2]:
                i = typePoint - 1
                print(2)
                listPoints[i].append((float(line[0]), float(line[1]), typePoint))
                data = "".join(["(", str(listPoints[i][-1][0]), 
                    ", ", str(listPoints[i][-1][1]), ")"])
                print(3)
                listBoxs[i].insert(END, data)
                print(4)
            # elif typePoint == 2:
            #     listPoints[1].append((float(line[0]), float(line[1]), typePoint))
            #     listBoxs[1].insert(END, str("(" + str(listPoints[1][-1][0]) + ", "
            #     + str(listPoints[1][-1][1]) + ")"))
    except:
        print("add point: type value error")
        messagebox.showinfo(title="Некорректный ввод", message=dataError)

    list(map(lambda el: el.delete(0, END), listEntry))
    showPoints(placeGraph, listPoints)


def editPoint(placeGraph, listEntry, listsBox, listsPoints):
    select, select2, typePoint = 0, 0, 0
    try:
        select = list(listsBox[0].curselection())
        if len(select) > 0: select = select[0]

        select2 = list(listsBox[1].curselection())
        if len(select2) > 0: select2 = select2[0]

        typePoint = int(listEntry[2].get())
        if typePoint not in [1, 2]:
            list(map(lambda el: el.delete(0, END), listEntry))
    except:
        print("error type")
        list(map(lambda el: el.delete(0, END), listEntry))
        return


    line = "  ".join([listEntry[0].get(), listEntry[1].get()]).split()
    print("join line:", line)
    try:
        if len(line) == 2 and typePoint in [1, 2]:
            newData = (float(line[0]), float(line[1]), typePoint)
            listsPoints[typePoint - 1][select] = newData

            listsBox[typePoint - 1].delete(0, END)
            for line in listsPoints[typePoint - 1]:
                data = "".join(["(", str(line[0]), ", ", str(line[1]), ")"])
                listsBox[typePoint - 1].insert(END, data)
    except:
        print("Error")

    list(map(lambda el: el.delete(0, END), listEntry))
    showPoints(placeGraph, listsPoints)


def cleanAll(placeGraph, listEntry, listsBox, listsPoints):
    placeGraph.delete("all")
    listsBox[0].delete(0, END)
    listsBox[1].delete(0, END)
    # list(map(lambda entry: entry.delete(0, END), lis))
    listEntry[0].delete(0, END)
    listEntry[1].delete(0, END)
    listEntry[2].delete(0, END)
    # list(map(lambda list: list.clear(), listsPoints))
    listsPoints[0].clear()
    listsPoints[0].clear()


def clearPlaceGraph(placeGraph):
    placeGraph.delete("all")



