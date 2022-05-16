from random import random
import time
import numpy as np

def randomSpace(size):
    """
    Return a matrix with random "1" surrounded by "0"
    """
    #Generate the playing space
    space=np.random.randint(0,2,(size,size))

    #Add 0 all around the playing space
    space=np.vstack([np.zeros(size),space])
    space=np.vstack([space,np.zeros(size)])
    space=np.hstack([(np.zeros(size+2).reshape(size+2,1)),space])
    space=np.hstack([space,(np.zeros(size+2).reshape(size+2,1))])

    return(space)

def GameOfLifeOneTic(space):
    """
    Take a matrix and return another matrix with the game of life rules applied once
    """
    size=space.shape[0]-2

    #Generation of the matrix where the number of neighbors will be stocked
    neighborSpace=np.zeros(np.shape(space))
    newSpace=np.zeros(np.shape(space))

    #Counts the number of neighbors of the [i,j] cell
    for i in range(1,size+1):
        for j in range(1,size+1):
            neighbor=0
            for p in range(-1,2):
                    for q in range(-1,2):
                        if space[i-p,j-q]==1:
                            neighbor=neighbor+1
            if space[i,j]==1:
                    neighbor=neighbor-1
            neighborSpace[i,j]=neighbor

    #Advance of one tick
    for i in range(1,size+1):
        for j in range(1,size+1):
            if (space[i,j]==1):
                if (neighborSpace[i,j]==2 or neighborSpace[i,j]==3):
                    newSpace[i,j]=1
                else:
                    newSpace[i,j]=0
            elif space[i,j]==0:
                if neighborSpace[i,j]==3:
                    newSpace[i,j]=1
    return(newSpace)

def buildHtml(file,matrix,title="matrix",backgroundColor="white",deadCellColor="black",aliveCellColor="red",cellSize="20px"):
    """
    Generate an .html file, which draws the matrix taken as input
    """
    top="0"
    intTop=int(top)
    bottom="0"
    intBottom=int(bottom)
    left="0"
    intLeft=int(left)
    right="0"
    intRight=int(right)
    space=2*20+2

    #Generate the beginning of the html file
    fp=open(file,"w")
    fp.write("<!DOCTYPE html>\n")
    fp.write("<html>\n")
    fp.write("<head>\n")
    fp.write("<title>"+title+"</title>\n")
    fp.write('<meta http-equiv="refresh" content="1" />\n')
    fp.write("</head>\n")
    fp.write('<body style="background-color:'+backgroundColor+';">\n')  

    #Draws the matrix
    for i in range(np.shape(matrix)[0]):
        left="0"
        intLeft=int(left)
        intTop=intTop+space
        top=str(intTop)
        for j in range(np.shape(matrix)[0]):
            if matrix[i,j]==1:
                fp.write('<div style="position:absolute; top:'+top+'px; bottom:'+bottom+'px; left:'+left+'px; right:'+right+'px; margin:auto; width:'+cellSize+'; height:'+cellSize+'; background-color:'+aliveCellColor+';"></div>\n')
            else:
                fp.write('<div style="position:absolute; top:'+top+'px; bottom:'+bottom+'px; left:'+left+'px; right:'+right+'px; margin:auto; width:'+cellSize+'; height:'+cellSize+'; background-color:'+deadCellColor+';"></div>\n')
                                                  
            intLeft=intLeft+space
            left=str(intLeft)

    #Generate the ending of the html file
    fp.write("</body>\n")
    fp.write("</html>\n")
    fp.close()


matrix=randomSpace(20) #Generate a 10x10 playing space filled with random alive cells
while True: #Warning, infinite loop. To stop, press CTRL+C
    time.sleep(1) #Wait one second to avoid crashes
    print(matrix) #Print the matrix in the terminal
    buildHtml("gol.html",matrix,"matrix","white","black","red","20px") #Generate the .html file called "gol;html", with the drawing of the matrix
    matrix=GameOfLifeOneTic(matrix) #Advance one tick in the game of life