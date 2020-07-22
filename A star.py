#this code is basically using python and specifically
#PYGAME and TKINTER module to implement the 2D Graphical Representation
#of A star algorithm to find the shortest movement between two points
#with adding obstacles too and I will be providing an option of either
#just getting the movement and distance or the user can also watch the step by step demonstration

#I have these modules installed and I am running this program on Python IDLE 3.8 (32 bit)
#It will not run under Python 3.8 versions
# a TRY EXCEPT catch just to make the user install these modules
try:
    import pygame
    import sys
    import math
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import os
# install packages    
except:
    import install_requirements  

    import pygame
    import sys
    import math
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import os

#this is just setting the display screen size using a variable screen
screen = pygame.display.set_mode((600, 600))
#main screen background color set close to White 
screencolor = [224, 224, 224]
screen.fill(screencolor)
#The main caption in the title bar
pygame.display.set_caption("Code with Salman")

#the main class that i am using
class point:
#initialization / constructor in a way    
    def __init__(personal, x, y):
        personal.i = x
        personal.j = y
        personal.f = 0
        personal.g = 0
        personal.h = 0
        personal.adjacents = []
        personal.previous = None
        personal.obs = False
        personal.closed = False
        personal.value = 1
#defining a function display() which when called will create rectangles
#the function is as follows:
#pygame.draw.rect(the surface to be drawn on, color (can be R,G,B form),(x axis,y axis, width height))        
    def display(personal, color, st):
        if personal.closed == False :
            pygame.draw.rect(screen, color, (personal.i * w, personal.j * h, w, h), st)
#this updates the changes on screen            
            pygame.display.update()
#the movement function, it is implemented at many places
    def movement(personal, color, st):
        pygame.draw.rect(screen, color, (personal.i * w, personal.j * h, w, h), st)
        pygame.display.update()
#this function is used while running the step by step process where it will add the
#adjacents if the fall in the OpenSET
    def addadjacents(personal, grid):
        i = personal.i
        j = personal.j
        if i < cols-1 and grid[personal.i + 1][j].obs == False:
            personal.adjacents.append(grid[personal.i + 1][j])
        if i > 0 and grid[personal.i - 1][j].obs == False:
            personal.adjacents.append(grid[personal.i - 1][j])
        if j < row-1 and grid[personal.i][j + 1].obs == False:
            personal.adjacents.append(grid[personal.i][j + 1])
        if j > 0 and grid[personal.i][j - 1].obs == False:
            personal.adjacents.append(grid[personal.i][j - 1])

#the main screen declaration
#no. of columns (can be changed (recommended that the it divides the screen size for even display ))            
cols = 30
grid = [0 for i in range(cols)]
#no. of rows (can be changed (recommended that the it divides the screen size for even display ))
row = 30
#openset closeset to be used in the A star Algorithm
openSet = []
closedSet = []
#some already made color combinations
red = (255, 0, 0)
purple = (153,51, 255)
blue = (0, 102, 204)
#the color around the edges of screen
bordercolor = (0, 102,51)
w = 600 / cols
h = 600 / row
cameFrom = []
#the grid lines color
boxborder= (0,204,102)

# 2d array creation
for i in range(cols):
    grid[i] = [0 for i in range(row)]

#initializing class point
for i in range(cols):
    for j in range(row):
        grid[i][j] = point(i, j)


#if user doesnot enter the start and end points, then these start and end node are selected automatically
start = grid[7][5]
end = grid[20][16]
# the creation of boxes on main window
for i in range(cols):
    for j in range(row):
        grid[i][j].display((boxborder), 1)
#the creation of a different color border around the screen
for i in range(0,row): 
    grid[cols-1][i].obs = True
    grid[cols-1][i].display(bordercolor, 0)
    grid[i][row-1].display(bordercolor, 0)
    grid[i][0].display(bordercolor, 0)
    grid[i][0].obs = True
    grid[i][row-1].obs = True
    grid[0][i].display(bordercolor, 0)
    grid[0][i].obs = True

#this part will run after the SUBMIT/ ENTER button is pressed
def onsubmit():
    global start
    global end
#this split function will separate two values from the start and end points by recognizing parts
#before and after the " , " and store those values   
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()
    
#a new window(dialogue box) is initiated here for the entering of values  
#I have added a unique color scheme to each button, label to give a better look
window = Tk()
window.configure(background='black')
label = Label(window, text='ENTER Starting Points like this: x,y (must be between 1,1 and 29,29)',fg='white', bg='black')
startBox = Entry(window)
label1 = Label(window, text='ENTER Ending Points like this: x,y (must be between 1,1 and 29,29)',fg='white', bg='black')
endBox = Entry(window)
var = IntVar()
displaymovement = ttk.Checkbutton(window, text='Click for step by step demo', onvalue=1, offvalue=0, variable=var )
submit = Button(window, text='Enter',bg='blue', fg='white', command=onsubmit)

#the padding, managing and spacing of the labels text in the dialogue box 
displaymovement.grid(columnspan=3, row=3)
submit.grid(columnspan=4, row=4)
label1.grid(row=1, pady=4)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=4)

window.update()
mainloop()

#this part of code will display a dialogue box for the assist of a new person runnign this code
#to guide him of how the working should be done in the next few phases
def printSomething():
    # if you want the button to disappear:
    button.destroy()
    label = Label(root, text= "(1)- First add obstacles between point using 'mouse press or the mouse drag'\n\n  (2)- Then Press the 'ENTER Key' once you are done adding obstacles.\n\n (close this Dialogue Box to Continue)")
    #this creates a new label to the GUI
    label.pack() 
#a new window initiated
root = Tk()
#the designing of the button
button = Button(root, text="Guide that will help you understand \nClick HERE",bg='blue', fg='white', command=printSomething) 
button.pack()
root.mainloop()

#initialization of pygame module (necesarry)
pygame.init()
openSet.append(start)

#these are the events and the functions defined that are invoke by the user actions
#by the mouse click or dragging for obstacles and this is displayn by a color change
def mousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (600 // cols)
    g2 = w // (600 // row)
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if acess.obs == False:
            acess.obs = True
            acess.display((255, 255, 20), 0)

end.display((255, 127, 0), 0)
start.display((255, 127,0), 0)



#this part of code is a check for the events occuring during the run
loop = True
while loop:
#initialized events to occur    
    ev = pygame.event.get()
    for event in ev:
#this is the check for if the user presses red cross (close) button       
        if event.type == pygame.QUIT:
            pygame.quit()
#this is the check for mouse press which we will use to add obstacles            
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
#this the check for keyboard press (ENTER) which is used to start the Search            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                loop = False
                break
#the use of addadjacents function
for i in range(cols):
    for j in range(row):
        grid[i][j].addadjacents(grid)

#the heuristic function that is used in the A star search Algorithm
def heurisitic(n, e):
    d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    #d = abs(n.i - e.i) + abs(n.j - e.j)
    return d

#this is where the A star function and its working is done
#by comaprisons and heuristic values and considering closeset openset, we decide
#if we want to add the movement or neighbor here
def main():
    end.display((255, 255, 255), 0)
    start.display((255, 255, 255), 0)
    if len(openSet) > 0:
        lowestIndex = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[lowestIndex].f:
                lowestIndex = i

        current = openSet[lowestIndex]
        if current == end:
            print('done', current.f)
            start.display((255,255, 255),0)
            temp = current.f
            for i in range(round(current.f)):
#if the desired movement(shortest) is found, we simply change the color of it to dstinguish it from the other
                current.closed = False
                current.display((0,0,0), 0)
                current = current.previous
            end.display((255, 255, 255), 0)

#in this part of code, the new window appears after finding the shortest movement
#I have used tkinter function of creating a information message box just to display
#the output and result of the distance that is being calculated
            Tk().wm_withdraw()
            result = messagebox.showinfo('Program Finished', ('The shortest distance to the movement is ' + str(temp) + ' blocks\n\n created by Salman Zahid'))
#here all I have done is made the screen to get stillso that the user can see the whole working 
            ag = True
            while ag:
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.KEYDOWN:
                        ag = False
            pygame.quit()

        openSet.pop(lowestIndex)
        closedSet.append(current)
        
#the A star search algorithm part considering the heuristics and the actual values and
#deciding meanwhile if the movement should be in the neighbor or not and it is represented by a different color 
        adjacents = current.adjacents
        for i in range(len(adjacents)):
            neighbor = adjacents[i]
            if neighbor not in closedSet:
                tempG = current.g + current.value
                if neighbor in openSet:
                    if neighbor.g > tempG:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)

            neighbor.h = heurisitic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].display(purple, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].display(blue, 0)
    current.closed = True

#the necessary checks for the proper working of the project
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()
#end of code
