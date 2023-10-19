from tkinter import *
import tkinter.messagebox
from random import choice
def player_vs_computer():
    option_window.destroy()
    def start():
        window = Tk()
        window.geometry("600x400")
        window.title("TIC TAC TOE")
        window.configure(background = 'skyblue')
        heading = Label(text = "  TIC TAC TOE", font = ("Ravie",27), fg = 'red', bg = 'skyblue')
        heading.grid(row = 0, column = 0,columnspan = 10)        
        def stop():
            for i in range(3):
                for j in range(3):
                    if matrix2[i][j] == 0:
                        matrix1[i][j] =Button(state = "disable",font=("algerian",27),width=5,height = 2,bg="aqua")
                        matrix2[i][j] = " "
        #funtion to take the user chance and update the button with a cross
        def take(r,c):
            global mark,countchance
            if matrix2[r][c] == 0 :
                matrix1[r][c].configure(text = "X",fg="yellow",bg="red",state = "disable") # change the button text and disable that button
                matrix2[r][c] =  "X" 
                mark = "O"  # afer users chance update the sign for computer to use it
                countchance+=1 # count the number of chances
                my_list.remove(tuple([r,c])) # removes the utilised place from mylist 
                player_list.append(tuple([r,c])) # pushes the place into player_list for checking the wining position
            AI() # function to call computer's turn
        # program to find the best postion for computer to win
        def AI():
            global countchance
            if tuple([1,1]) in my_list: # checks whether middle block is empty or not
                x , y = (1,1)
                computer_list.append(tuple([1,1])) # pushes the place into computer_list for checking the winnig position
                my_list.remove(tuple([1,1])) # removes the utilisesd place from my_list
                countchance+=1 # updates the number of chances
                do = 'yes'
            elif countchance == 1: # if center position is occupied
                x,y = choice(my_list) # it puts 'O' on any of the surrounding position
                computer_list.append(tuple([x,y])) # pushes this position into the computer_list for checkin the wining position
                my_list.remove(tuple([x,y])) # removes the utilised place from mylist
                do = 'yes'
                countchance+=1
            # this code searches for the best position from the fourth chance(turn)
            else:
                # first checks for the defending move to not allow user to win
                i = 0
                kv = [''] # an element is already present in the list because chance countin start from 1 i.e. index 1 so anything is placed at index 0
                while i < len(player_list)-1:
                    j = i +1
                    while j < len(player_list):
                        k = 0
                        while k < len(my_list):
                            if [player_list[i],player_list[j],my_list[k]] in win_list: # makes combinations and check for the defending move
                                kv.append(my_list[k])
                                break
                            k+=1
                        j+=1
                    i+=1
                # checks whether the computer is winnig at any position
                if countchance>=4:
                    i = 0
                    while i < len(computer_list)-1:
                        j = i +1
                        while j < len(computer_list):
                            k = 0
                            while k < len(my_list):
                                if [computer_list[i],computer_list[j],my_list[k]] in win_list: # makes combinations and checks for the wining move
                                    kv.append(my_list[k])
                                    break
                                k+=1
                            j+=1
                        i+=1
                if len(kv) == 1 and countchance != 9 and len(my_list) != 0:
                    x,y = choice(my_list)
                    computer_list.append(tuple([x,y]))
                    do = 'yes'
                # choose from the winning and the defending position
                elif len(kv) != 1 and countchance !=9:
                    index = 2 if len(kv) == 3 else 1
                    x,y = kv[index]
                    computer_list.append(tuple([x,y]))
                    my_list.remove(tuple([x,y]))
                    do = 'yes'
                else :
                    x,y = choice(my_list) # it puts 'O' on any of the surrounding position
                    computer_list.append(tuple([x,y])) # pushes this position into the computer_list for checkin the wining position
                    my_list.remove(tuple([x,y])) # removes the utilised place from mylist
                    countchance+=1
                    do = 'yes'
            # updates the button after finding the best position 
            if do == 'yes':
                if matrix2[x][y] == 0 :
                    matrix1[x][y].configure(text = "O",fg= "red",bg="yellow",state = "disable") # updates the button and disable them
                    matrix2[x][y] =  "O"
                    mark = "X" #changes the sign to 'X' for the use of user
                    countchance+=1 # updates the number of chance
                winner()
        # checks for the winner and changes the buttons to grey color 
        def winner():
            global matrix2
            # all the winning combinations are created using for loop
            for i in range(3):
                if matrix2[i][0] == matrix2[i][1] == matrix2[i][2] != 0 :
                    matrix1[i][0].config(bg="grey")
                    matrix1[i][1].config(bg="grey")
                    matrix1[i][2].config(bg="grey")
                    stop() # calls the function to stop the game           
            for i in range(3):
                if matrix2[0][i] == matrix2[1][i] == matrix2[2][i] != 0 :
                    matrix1[0][i].config(bg="grey")
                    matrix1[1][i].config(bg="grey")
                    matrix1[2][i].config(bg="grey")
                    stop() # calls the function to stop the game
            if matrix2[0][0] == matrix2[1][1] == matrix2[2][2]!=0:
                matrix1[0][0].config(bg="grey")
                matrix1[1][1].config(bg="grey")
                matrix1[2][2].config(bg="grey")
                stop() # calls the function to stop the game
            if matrix2[2][0] == matrix2[1][1] == matrix2[0][2] !=0:
                matrix1[0][2].config(bg="grey")
                matrix1[1][1].config(bg="grey")
                matrix1[2][0].config(bg="grey")            
                stop() # calls the function to stop the game
        # creating the buttons of 3 x 3 
        for i in range(3):
            for j in range(3):
                matrix1[i][j]=Button(activebackground = "violet",font=("algerian",27),width=5,height = 2,bg="aqua",command= lambda r = i, c=j: take(r,c))
                matrix1[i][j].grid(row=i+2,column=j+2)
        playagainb = Button(text = "playgain", font=('Ravie',22),width = 8, command = lambda : clearwindow()) # play again button
        playagainb.grid(row = 2 , column = 6,columnspan = 30)
        quitb = Button(text = "quit", font=('Ravie',22),width = 8,command = lambda : window.destroy()) # quit button
        quitb.grid(row = 3 , column = 6,columnspan = 30)
        back = Button(text = 'back',font = ('ravie',22),width = 8,command = lambda : new_game())
        back.grid(row = 4 ,column = 6,columnspan = 30)
        # on clicking playagain button it deletes current window and recreates it again
        def new_game():
            window.destroy()
            start_game()
        def clearwindow():
            window.destroy()
            matrix()
    #main
    def matrix():
        global matrix1, matrix2,mark,countchance,my_list,win_list,player_list,computer_list
        my_list = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)] # list of the places not utilised by any sign
        # the list of all the winnig combinations in the game
        win_list = [[(0,0),(0,1),(0,2)],[(0,0),(0,2),(0,1)],[(0,1),(0,0),(0,2)],[(0,1),(0,2),(0,0)],[(0,2),(0,0),(0,1)],[(0,2),(0,1),(0,0)],
                    [(1,0),(1,1),(1,2)],[(1,0),(1,2),(1,1)],[(1,1),(1,2),(1,0)],[(1,1),(1,0),(1,2)],[(1,2),(1,1),(1,0)],[(1,2),(1,0),(1,1)],
                    [(2,0),(2,1),(2,2)],[(2,0),(2,2),(2,1)],[(2,1),(2,2),(2,0)],[(2,1),(2,0),(2,2)],[(2,2),(2,1),(2,0)],[(2,2),(2,0),(2,1)],
                    [(0,0),(1,0),(2,0)], [(0,0),(2,0),(1,0)],[(2,0),(1,0),(0,0)],[(2,0),(0,0),(1,0)],[(1,0),(0,0),(2,0)],[(1,0),(2,0),(0,0)],
                    [(0,1),(1,1),(2,1)], [(0,1),(2,1),(1,1)],[(2,1),(1,1),(0,1)],[(2,1),(0,1),(1,1)],[(1,1),(0,1),(2,1)],[(1,1),(2,1),(0,1)],
                    [(0,2),(1,2),(2,2)],[(0,2),(2,2),(1,2)],[(2,2),(1,2),(0,2)],[(2,2),(0,2),(1,2)],[(1,2),(0,2),(2,2)],[(1,2),(2,2),(0,2)],
                    [(0,0),(1,1),(2,2)],[(1,1),(0,0),(2,2)],[(0,0),(2,2),(1,1)],[(1,1),(2,2),(0,0)],[(2,2),(1,1),(0,0)],[(2,2),(0,0),(1,1)],
                    [(0,2),(1,1),(2,0)],[(0,2),(2,0),(1,1)],[(1,1),(2,0),(0,2)],[(1,1),(0,2),(2,0)],[(2,0),(1,1),(0,2)],[(2,0),(0,2),(1,1)]]
        player_list = [] # this list contains all the positions on which user has clicked
        computer_list = [] # this list contains all the positions which computer has picked
        matrix1 =[[0,0,0] ,  [0,0,0],[0,0,0]]
        matrix2 =[ [0,0,0], [0,0,0], [0,0,0]]
        mark = "X"
        countchance = 0
        start()
    matrix()

def player_vs_player():
    option_window.destroy()
    def start():
        window = Tk()
        window.geometry("600x400")
        window.title("TIC TAC TOE")
        window.configure(background = 'skyblue')
        heading = Label(text = "  TIC TAC TOE", font = ("Ravie",27), fg = 'red', bg = 'skyblue')
        heading.grid(row = 0, column = 0,columnspan = 10)
        def stop():
            a = "X" if mark == "O" else "O"
            message = "WINNER " + a 
            tkinter.messagebox.showinfo(message,[a,"has won the game"])
            for i in range(3):
                for j in range(3):
                    if matrix2[i][j] == 0:
                        matrix1[i][j] =Button(state = "disable",font=("algerian",27),width=5,height = 2,bg="aqua")
                        matrix2[i][j] = " "
        def take(r,c):
            global mark,countchance
            if mark == "X" and matrix2[r][c] == 0 :
                matrix1[r][c].configure(text = "X",fg="yellow",bg="red")
                matrix2[r][c] =  "X"
                mark = "O"
                countchance+=1
            elif mark == "O" and matrix2[r][c] == 0 :
                matrix1[r][c].configure(text = "O",fg= "red",bg="yellow")
                matrix2[r][c] =  "O"
                mark = "X"
                countchance+=1
            if countchance>=5:
                winner()
        def winner():
            global matrix2
            for i in range(3):
                if matrix2[i][0] == matrix2[i][1] == matrix2[i][2] != 0 :
                    matrix1[i][0].config(bg="grey")
                    matrix1[i][1].config(bg="grey")
                    matrix1[i][2].config(bg="grey")
                    stop()                 
            for i in range(3):
                if matrix2[0][i] == matrix2[1][i] == matrix2[2][i] != 0 :
                    matrix1[0][i].config(bg="grey")
                    matrix1[1][i].config(bg="grey")
                    matrix1[2][i].config(bg="grey")
                    stop()
            if matrix2[0][0] == matrix2[1][1] == matrix2[2][2]!=0:
                matrix1[0][0].config(bg="grey")
                matrix1[1][1].config(bg="grey")
                matrix1[2][2].config(bg="grey")
                stop()
            if matrix2[2][0] == matrix2[1][1] == matrix2[0][2] !=0:
                matrix1[0][2].config(bg="grey")
                matrix1[1][1].config(bg="grey")
                matrix1[2][0].config(bg="grey")            
                stop()
        for i in range(3):
            for j in range(3):
                matrix1[i][j]=Button(activebackground = "violet",font=("algerian",27),width=5,height = 2,bg="aqua",command= lambda r = i, c=j: take(r,c))
                matrix1[i][j].grid(row=i+2,column=j+2)
        playagainb = Button(text = "playgain", font=('Ravie',22),width = 8, command = lambda : clearwindow())
        playagainb.grid(row = 2 , column = 6,columnspan = 30)
        quitb = Button(text = "quit", font=('Ravie',22),width = 8,command = lambda : window.destroy())
        quitb.grid(row = 3 , column = 6,columnspan = 30)
        back = Button(text = 'back',font = ('ravie',22),width = 8,command = lambda : new_game())
        back.grid(row = 4 ,column = 6,columnspan = 30)
        def new_game():
            window.destroy()
            start_game()
        def clearwindow():
            window.destroy()
            matrix()
    #main
    def matrix():
        global matrix1, matrix2,mark,countchance
        matrix1 =[[0,0,0] ,      
                      [0,0,0],
                      [0,0,0]]
        matrix2 =[
                      [0,0,0], 
                      [0,0,0],
                      [0,0,0]]
        mark = "X"
        countchance = 0
        start()
    matrix()
def start_game():
    global option_window
    option_window = Tk()
    option_window.geometry("610x450")
    option_window.configure(background = "green")
    option_window.title("TIC TAC TOE")
    heading1= Label(text = "  TIC TAC TOE", font = ("Ravie",35),bg = 'green')
    heading1.grid(row = 0, column = 0,columnspan = 10,pady = 10)
    pp = Button(text= "Player V/S Player",activebackground = "violet",font=("ravie",27),width=20,height = 2,bg="skyblue",command = lambda : player_vs_player())
    pc = Button(text= "Player V/S Computer",activebackground = "violet",font=("ravie",27),width=20,height = 2,bg="aqua",command = lambda : player_vs_computer())
    pp.grid(row = 1, column = 1)
    pc.grid(row = 2 , column = 1)
start_game()
mainloop()
