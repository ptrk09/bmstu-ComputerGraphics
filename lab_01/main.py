from tkinter import mainloop, Label, Canvas, Scrollbar, Listbox, Pack, RIGHT
from functools import partial
from menu_operation import *
from ui import *

sizeTuple = (1280, 800)
positionTuple = (100, 50)
listPoints = []#[(0.0, 3.0, 1), (0.0, -3.0, 1), (3.0, 0.0, 1)]
listPoints2 = []#[(3.0, 0.0, 2), (6.0, 3.0, 2), (6.0, -3.0, 2)]

# create window and canvas for screen
window = createRootWindow(sizeTuple, positionTuple)
placeGraph = Canvas(window, width=800, height=800, bg="white")

# create listboxs and scrollbars for sets points
listBox = Listbox(window, width=20, height=20)
listBox2 = Listbox(window, width=20, height=20)

scrollbar = Scrollbar(orient="vertical", command=listBox.yview)
scrollbar2 = Scrollbar(orient="vertical", command=listBox2.yview)

listBox.config(yscrollcommand=scrollbar.set)
listBox2.config(yscrollcommand=scrollbar2.set)

# create labels 
labelEntry = Label(text="Ввод точки:", width=30)
labelX = Label(text="x = ", width=3, bg="gray")
labelY = Label(text="y =", width=3, bg="gray")
labelType = Label(text="множество = ", width=16, bg="gray")
label1Type = Label(text="1 множество", width=15, bg="gray")
label2Type = Label(text="2 множество", width=15, bg="gray")

# create entry for input point
entryX = Entry(width=5, bg="white")
entryY = Entry(width=5, bg="white")
entryType = Entry(width=5, bg="white")

# lists elements
listAllPoint = [listPoints, listPoints2]
listEntry = [entryX, entryY, entryType]
listBoxs = [listBox, listBox2]

# create buttons
buttonAdd = createButton(window, "добавить точку", (15, 2), 
    partial(addPoint, placeGraph, listEntry, listAllPoint, listBoxs))
buttonRemove = createButton(window, "удалить точку", (15, 2), 
    partial(delPoint, listAllPoint, listBoxs, placeGraph))
buttonEdit = createButton(window, "изменить точку", (15, 2), 
    partial(editPoint, placeGraph, listEntry, listBoxs, listAllPoint))
buttonCreateGraph = createButton(window, "показать решение", (15, 2), 
    partial(createGraph, placeGraph, listAllPoint))
buttonShowPoints = createButton(window, "показать точки", (15, 2), 
    partial(showPoints, placeGraph, listAllPoint))

# set location
placeGraph.pack(side=RIGHT)

listBox.place(x=5, y=400, anchor="nw")
listBox2.place(x=240, y=400, anchor="nw")

entryX.place(x=40, y=35, anchor="nw")
entryY.place(x=160, y=35, anchor="nw")
entryType.place(x=330, y=35, anchor="nw")

labelX.place(x=5, y=37)
labelY.place(x=120, y=37)
labelType.place(x=205, y=37)
labelEntry.place(x=5, y=8, anchor="nw")
label1Type.place(x=5, y=370)
label2Type.place(x=270, y=370)

buttonShowPoints.place(x=5, y=80, anchor="nw")
buttonAdd.place(x=5, y=130, anchor="nw")
buttonRemove.place(x=5, y=180, anchor="nw")
buttonEdit.place(x=5, y=230, anchor="nw")
buttonCreateGraph.place(x=5, y=280, anchor="nw")

scrollbar.place(x=190, y=400)
scrollbar2.place(x=425, y=400)

window.mainloop()
