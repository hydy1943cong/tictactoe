

def display_board(board):
        for i in range(13):
            if i ==0:
                print((((("+")+("-"*7))*3)+"+"))
            elif i ==4:
                print((((("+")+("-"*7))*3)+"+"))
            elif i ==8:
                print((((("+")+("-"*7))*3)+"+"))
            elif i ==12:
                print((((("+")+("-"*7))*3)+"+"))
            elif i==1:
                print("|""       ""|""       ""|""       ""|")
            elif i==3:
                print("|""       ""|""       ""|""       ""|")
            elif i==5:
                print("|""       ""|""       ""|""       ""|")
            elif i==7:
                print("|""       ""|""       ""|""       ""|")
            elif i==9:
                print("|""       ""|""       ""|""       ""|")
            elif i==11:
                print("|""       ""|""       ""|""       ""|")
            elif i ==2:
                print("|""   "+str(board[0][0])+"   ""|""   "+str(board[0][1])+"   ""|""   "+str(board[0][2])+"   ""|")
            elif i ==6:
                print("|""   "+str(board[1][0])+"   ""|""   "+str(board[1][1])+"   ""|""   "+str(board[1][2])+"   ""|")
            elif i ==10:
                print("|""   "+str(board[2][0])+"   ""|""   "+str(board[2][1])+"   ""|""   "+str(board[2][2])+"   ""|")

def make_list_of_free_fields(board):
    freelist=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]=="O" or board[i][j]=="X":
                continue
            else:
                freelist.append(board[i][j])
    return freelist
    
def victory_for(board, sign):
    if sign == "O":
        if board[0][0]==board[0][1]==board[0][2]:
            print("You won!")
            return 1
        elif board[1][0]==board[1][1]==board[1][2]:
            print("You won!")
            return 1
        elif board[2][0]==board[2][1]==board[2][2]:
            print("You won!")
            return 1
        elif board[0][0]==board[1][0]==board[2][0]:
            print("You won!")
            return 1
        elif board[0][1]==board[1][1]==board[2][1]:
            print("You won!")
            return 1
        elif board[0][2]==board[1][2]==board[2][2]:
            print("You won!")
            return 1
        elif board[0][0]==board[1][1]==board[2][2]:
            print("You won!")
            return 1
        elif board[0][2]==board[1][1]==board[2][0]:
            print("You won!")
            return 1
            
    if sign=="X":
        if board[0][0]==board[0][1]==board[0][2]:
            print("You lose!")
            return 1
        elif board[1][0]==board[1][1]==board[1][2]:
            print("You lose!")
            return 1
        elif board[2][0]==board[2][1]==board[2][2]:
            print("You lose!")
            return 1
        elif board[0][0]==board[1][0]==board[2][0]:
            print("You lose!")
            return 1
        elif board[0][1]==board[1][1]==board[2][1]:
            print("You lose!")
            return 1
        elif board[0][2]==board[1][2]==board[2][2]:
            print("You lose!")
            return 1
        elif board[0][0]==board[1][1]==board[2][2]:
            print("You lose!")
            return 1
        elif board[0][2]==board[1][1]==board[2][0]:
            print("You lose!")
            return 1
    if len(make_list_of_free_fields(board))== 0:
        print("It's a tie.")
        return 1
    else: 
        return 0
     

def enter_move(board):
        enter=int(input("Please enter the number of the square you choose:"))
        if enter==1:
            board[0][0]="O"
        elif enter==2:
            board[0][1]="O"
        elif enter==3:
            board[0][2]="O"
        elif enter==4:
            board[1][0]="O"
        elif enter==5:
            board[1][1]="O"
        elif enter==6:
            board[1][2]="O"
        elif enter==7:
            board[2][0]="O"
        elif enter==8:
            board[2][1]="O"
        elif enter==9:
            board[2][2]="O"
        display_board(board)
    



from random import randrange


def draw_move(board):
        compnum = randrange(1,10)
        if compnum == board[0][0]:
            board[0][0]="X"
        elif compnum == board[0][1]:
            board[0][1]="X"
        elif compnum == board[0][2]:
            board[0][2]="X"   
        elif compnum == board[1][0]:
            board[1][0]="X"
        elif compnum == board[1][1]:
            board[1][1]="X" 
        elif compnum == board[1][2]:
            board[1][2]="X" 
        elif compnum == board[2][0]:
            board[2][0]="X"
        elif compnum == board[2][1]:
            board[2][1]="X" 
        elif compnum == board[2][2]:
            board[2][2]="X"
        else:
            draw_move(board)
        display_board(board)

status=0
myboard = [[1,2,3],[4,5,6],[7,8,9]]
myboard[1][1]="X"
display_board(myboard)
while status==0:
    enter_move(myboard)
    status=victory_for(myboard,"O")
    if status==1:
        break 
    draw_move(myboard)
    status=victory_for(myboard,"X")
    if status==1:
        break
print("The end.")



