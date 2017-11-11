from tkinter import *
import hero

####################################
# Initialize data
####################################

def init(data):
	data.player = hero.HeroPlayer(data.width*1/2, data.height*1/2, 1)

####################################
# Define user interaction, timing
####################################
    
def mousePressed(event, data): pass

def keyPressed(event, data): pass

def timerFired(data): pass

def mouseMoved(event, data):
	data.player.currX = event.x
	data.player.currY = event.y
	print(data.player.currX, data.player.currY)

####################################
# Draw graphics
####################################

def redrawAll(canvas, data):
	data.player.drawHero(canvas)

####################################
# Provided run function
####################################

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
    def mouseMovedWrapper(event, data):
    	mouseMoved(event, data)
    	#redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 50
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind('<Motion>', lambda event:
    						mouseMovedWrapper(event, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Thanks for playing!")

run(1400,750)