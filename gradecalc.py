#Name: Arka Ganguli

from graphics import *

#main function
def main():
    name = raw_input("Enter filename(grades): ") 
    Units,Avg = processFile(name) #stores value from the processfile function
    win = GraphWin("Grades", 500,200)    #size of graphics window
    outputGUI(win,Units,Avg)

def processFile(name):
    file1 = open(name, 'r') #opens file (to be read)
    data1 = file1.read()
    data1 = data1.split("\n") #split data by new lines

    Units = 0
    for i in data1:
        j = i.split("\t")   #loops through by going through splitting by tabs
        Units = int(j[1])+ Units #counts the units of each course

    B = 0
    for y in data1:
        k = y.split("\t")
        B = B + (int(k[1])*int(k[2])) #multiplies units and grade of each course
        B = float(B)
    Avg = B/Units #divides by total number of units to get average
    return Units,Avg

def outputGUI(win,Units,Avg):
    sentence = Text(Point(250,110),"Units = "+str(Units)+", Average = "+str(Avg))
    sentence.setSize(15)
    sentence.setTextColor("purple")
    sentence.draw(win)
    win.getMouse()
    win.close()
main ()
