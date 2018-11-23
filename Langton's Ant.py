# Updated Animation Starter Code

from tkinter import *

def init(data):
    data.cellSize = 10
    data.cols = data.width // data.cellSize
    data.rows = data.cols
    data.board = [[0] * data.cols for _ in range(data.rows)]
    data.left = False
    data.dcol = 0
    data.drow = 0
    data.ant = (data.rows//2, data.cols//2)

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] == 0:
                fill = "white"
            else: fill = "black"
            drawCell(canvas, data, row, col, fill)

def drawCell(canvas, data, cellRow, cellCol, fill):
    x0 = cellCol * data.cellSize
    x1 = (cellCol + 1) * data.cellSize
    y0 = cellRow * data.cellSize
    y1 = (cellRow + 1) * data.cellSize
    canvas.create_rectangle(x0, y0, x1, y1, fill = fill)

def dirControl(data):
    if data.left:
        dirTup = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    else:
        dirTup = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(len(dirTup)):
        if (data.dcol, data.drow) == dirTup[i]:
            data.dcol, data.drow = dirTup[(i+1)%4]

def switchOnOff(data):
    antRow, antCol = data.ant
    if data.board[antRow][antCol] == 0:
        data.left = True
        data.board[antRow][antCol] = 1
    else:
        data.left = False
        data.board[antRow][antCol] = 0
    dirControl(data)
    antRow += data.drow
    antCol += data.dcol
    data.ant = (antRow, antCol)

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawBoard(canvas, data)
    # dirControl(data)
    switchOnOff(data)
    # dirControl(data)


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 400)