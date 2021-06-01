import time

print("Welcome to X&O\n")
currentPlayer = "X"

"""
So I need a 2D array that will store the state of the board
This also needs to be read and then displayed visually to the user
"""


# Not sure if I have done this correctly but here we have a 2D array that makes up the board
# The _ means that the space is empty
"""
board = [["r0w", "no", "3"],
         ["b", "2", "q"],
         ["1", "_", "a"]]
"""
board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]


# This is the board display, I realise I have set it up without using variables in the slots
print("    [A] [B] [C]\n\n[1] _"+board[0][0]+"_ _"+board[0][1]+"_ _"+board[0][2]+"_\n\n[2] _"+board[1][0]+"_ _"+board[1][1]+"_ _"+board[1][2]+"_\n\n[3] _"+board[2][0]+"_ _"+board[2][1]+"_ _"+board[2][2]+"_\n")



# This function returns the position that the player enters numerically in a list
# A1 becomes [0, 0] (There is also data validation)
def getNumPosition():
    numPosition = [0, 0]
    keepGoing = True
    while keepGoing:
        print("\nIt is " + currentPlayer + "'s turn")
        InPosition = input("Please input the position you would like to take: ")
        # Remove inputs that are too short 
        if len(InPosition) < 2:
            print("Your input is too short (Example: A1)")
            time.sleep(1)
        else:
            # Just translates a to 0 ect.
            if InPosition[0].lower() == "a":
                numPosition[0] = 0
            elif InPosition[0].lower() == "b":
                numPosition[0] = 1
            elif InPosition[0].lower() == "c":
                numPosition[0] = 2
            else:
                print ("First character should be a, b, or c (Example: A1)")
                time.sleep(1)

            if InPosition[1] == "1":
                numPosition[1] = 0
                keepGoing = False
            elif InPosition[1] == "2":
                numPosition[1] = 1
                keepGoing = False
            elif InPosition[1] == "3":
                numPosition[1] = 2
                keepGoing = False
            else:
                print("Second character should be 1, 2, or 3 (Example: A1)")
                time.sleep(1)


    # Debug Stuff: print (numPosition)
    return numPosition



def setPosition(numPosition):
    global currentPlayer
    pos = board[numPosition[1]][numPosition[0]]
    if pos == "_":
        board[numPosition[1]][numPosition[0]] = currentPlayer
        print("    [A] [B] [C]\n\n[1] _"+board[0][0]+"_ _"+board[0][1]+"_ _"+board[0][2]+"_\n\n[2] _"+board[1][0]+"_ _"+board[1][1]+"_ _"+board[1][2]+"_\n\n[3] _"+board[2][0]+"_ _"+board[2][1]+"_ _"+board[2][2]+"_\n")
    else:
        setPosition(getNumPosition())



def checkWinState():
    global currentPlayer
    
    # Itterate down through the rows - check if they are all the current players character
    for row in range(3):
        count = 0
        for col in range(3):
            if board[row][col] == currentPlayer:
                count = count + 1
            if count == 3:
                return currentPlayer
                
    # Itterate across the vertical lines - check if they are all the current players character
    for col in range(3):
        count = 0
        for row in range(3):
            if board[row][col] == currentPlayer:
                count = count + 1
            if count == 3:
                return currentPlayer
    
    # Finally check the two horizontals
    count = 0
    for i in range(3):
        if board[i][i] == currentPlayer:
            count = count + 1
            if count == 3:
               return currentPlayer

    count = 0
    j = 3
    for i in range(3):   
        j = j - 1
        if board[j][i] == currentPlayer:
            count = count + 1
            if count == 3:
                return currentPlayer
            

    #this dumb fix it
            """
    up = 0
    down = 2
    keepGoing = True
    while keepGoing:
        print("up " + str(up))
        print("down " + str(down))
        print(board[down][up])
        keepGoing = False
        
        if board[up][up] == currentPlayer:       
           keepGoing = True
           up = up + 1
           if up == 3:
               print("This should be the win state or something 1")
               break
    
        if board[down][up] == currentPlayer:
            print(board[up][down])
            keepGoing = True
            down = down - 1
            if down == -1:
                break
   """     
        
def switchPlayer(player):
    if player == "X":
        return "O"
    else:
        return "X"    


while True:
    setPosition(getNumPosition())
    win = checkWinState()
    if win == "X" or win == "O":
        print(currentPlayer + " has won!")
        time.sleep(5)
        break
    else: 
        currentPlayer = switchPlayer(currentPlayer)
    


