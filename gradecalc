#Name: Arka Ganguli

from graphics import *

#main function
def main():
    name = raw_input("Enter filename(grades): ") 
    U,A = processFile(name) #stores value from the processfile function
    win = GraphWin("Year 1 Grades", 500,200)    #size of graphics window
    outputGUI(win,U,A)

def processFile(name):
    file1 = open(name, 'r') #opens file (to be read)
    data1 = file1.read()
    data1 = data1.split("\n") #split data by new lines

    U = 0
    for i in data1:
        j = i.split("\t")   #loops through by going through splitting by tabs
        U = int(j[1])+ U #counts the units of each course

    B = 0
    for y in data1:
        k = y.split("\t")
        B = B + (int(k[1])*int(k[2])) #multiplies units and grade of each course
        B = float(B)
    A = B/U #divides by total number of units to get average
    return U,A

def outputGUI(win,U,A):
    sentence = Text(Point(250,110),"Units = "+str(U)+", Average = "+str(A))
    sentence.setSize(15)
    sentence.setTextColor("purple")
    sentence.draw(win)
    win.getMouse()
    win.close()
main ()
