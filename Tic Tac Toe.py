"""
PROJECT-1
HAS BEEN COMPLETED 
PLEASE DO NOT MAKE ANY CHANGES"""


#Tic tac toe in terminal
class Player:
    def __init__(self,positionX,positionY,string):
        self.positionX=positionX
        self.positionY=positionY
        self.string=string
    
    def moves(self,x,y):
        self.positionX[x]+=1
        self.positionY[y]+=1
        
    def decision(self,board):
        count1=0
        count2=0
        for i in range(1,4):
            if self.positionX[i]==3 or self.positionY[i]==3:
                return True
            if board[2*i][2*i]==self.string:
                count1+=1
            if board[2*i][8-2*i]==self.string:
                count2+=1
        if count1==3 or count2==3:
            return True
        return False


def print_board(board):
    print()
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    print()
    
board=[
    [" "," ","1"," ","2"," ","3"," "],
    [" ","+","-","+","-","+","-","+"],
    ["1","|"," ","|"," ","|"," ","|"],
    [" ","+","-","+","-","+","-","+"],
    ["2","|"," ","|"," ","|"," ","|"],
    [" ","+","-","*","-","*","-","+"],
    ["3","|"," ","|"," ","|"," ","|"],
    [" ","+","-","+","-","+","-","+"]
    ]

memorization=list()

player_X=Player({1:0,2:0,3:0},{1:0,2:0,3:0},"X")

player_O=Player({1:0,2:0,3:0},{1:0,2:0,3:0},"O")

number_of_moves=1

print("\n+=========================+")
print("| Tic Tac Toe In Terminal |")
print("+=========================+")

print_board(board)
#Game loop
while (number_of_moves<10):

#Deciding which player 
    p=player_X
    if number_of_moves % 2==0:
        p=player_O
    print("+================+")
    print("|Player",p.string,"`s Turn|")
    print("+================+")
    print()

#Taking input from the user
    while (True):
        row=int(input("Enter The Row: "))
        column=int(input("Enter The Column: "))
        if row in [1,2,3] and column in [1,2,3]:
            if (row,column) not in memorization:
                memorization.append((row,column))
                break
            else:
                print("\n!!Input Was Repeated!!")
        else:
            print("\n!!Invalid Input!!")
        print("\n!!Try Again!!")
    print()
#Adding element to the list  
    p.moves(row,column)
    
#Incrementing the number of turns          
    number_of_moves+=1

#Adding to the board
    board[2*row][2*column]=p.string

#Printing the board  
    print_board(board)

#Checking if some one won
    if p.decision(board):
        print("+====================+")
        print("|!!Player",p.string,"Has Won!!|")
        print("+====================+")
        break
    else:
        if number_of_moves==10:
            print("+=================+")
            print("|!!It Was A Draw!!|")
            print("+=================+")
        