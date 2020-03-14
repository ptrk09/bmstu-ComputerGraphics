from tkinter import Tk, Button

def createRootWindow(size, position):
    rootWindow = Tk()
    rootWindow["bg"] = "gray"
    strSetings = "{}x{}+{}+{}".format(size[0], size[1],
                                      position[0], position[1])
    rootWindow.geometry(strSetings)

    return rootWindow


def createButton(rootWindow, label, size, myFunc):
    button = Button(rootWindow)
    button["text"] = label
    button["width"] = size[0]
    button["height"] = size[1]
    button["background"] = "gray"
    button["activeforeground"] = 'red'
    button["command"] = myFunc

    return button