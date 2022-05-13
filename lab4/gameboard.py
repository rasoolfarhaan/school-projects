import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading

EMPTYBOARD = [["", "", ""], ["", "", ""], ["", "", ""]]

class BoardClass:
    myName = ""
    oppenentName = ""
    board = EMPTYBOARD
    turn = None
    def __init__ (self, myName, oppenentName, numGames, wins, ties, losses, socket):
        self.myName = myName
        self.oppenentName = oppenentName
        self.numGames = numGames
        self.wins = wins
        self.ties = ties
        self.losses = losses
        #print("My name", self.myName)
        if self.myName != "player1":
            self.turn = self.myName
        else:
            self.turn = self.oppenentName
        global Socket
        Socket = socket
        gui = TTTGui(myName, oppenentName, self.playMoveOnBoard, self.board, self.getTurn, Socket, self.quitMain, self.setTurn, self.isBoardFull, self.isGameFinished)
        threading.Thread(target = gui.start_GUI, args = [myName, self.playMoveOnBoard, self.board, self.getTurn, Socket, self.quitMain]).start()
        #print("HERE22222RE")
        gui.receivePlay(Socket)
        #print("HERERE")



    def recordGamePlayed(self):
        self.numGames
    def resetGameBoard(self):
        board = EMPTYBOARD
    def playMoveOnBoard(self, rowIndex, colIndex):
        #print("playMoveOnBoard")
        if self.turn != "player1":
            self.board[rowIndex][colIndex] = "X"
            #print("My name:", self.myName, self.turn)
            if self.myName == self.turn:
                #print("SENDING MOVE RN")
                move = "" + str(rowIndex) + "" + str(colIndex)
                move = move.encode('utf-8')
                Socket.send(move)
            self.turn = "player1"
        elif self.turn == "player1":
            self.board[rowIndex][colIndex] = "O"
            if self.myName == "player1":
                #print("SENDING MOVE RN")
                move = "" + str(rowIndex) + "" + str(colIndex)
                move = move.encode('utf-8')
                Socket.send(move)
            self.turn = oppenentName
        #print("Play Move:", self.board)
    def isBoardFull(self):
        for list in self.board:
            if all([True if x != "" else False for x in list]):
                continue
            return False
    def isGameFinished(self):
        #print(self, self.board)
        if (self.board[0][0] == self.board[0][1] == self.board[0][2]) and self.board[0][0] != "":
            return self.board[0][0]
        if (self.board[1][0] == self.board[1][1] == self.board[1][2]) and self.board[1][0]!= "":
            return self.board[1][0]
        if (self.board[2][0] == self.board[2][1] == self.board[2][2]) and self.board[2][0] != "":
            return self.board[2][0]
        if (self.board[0][0] == self.board[1][0] == self.board[2][0]) and self.board[0][0] != "":
            return self.board[0][0]
        if (self.board[0][1] == self.board[1][1] == self.board[2][1]) and self.board[0][1] != "":
            return self.board[0][1]
        if (self.board[0][2] == self.board[1][2] == self.board[2][2]) and self.board[0][2] != "":
            return self.board[0][2]
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != "":
            return self.board[0][0]
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] != "":
            return self.board[0][2]
        return "NONE"
        # cols = [[],[],[]]
        # diagonals = [[],[]]
        # for (row, i) in enumerate(self.board):
        #     if all([True if x == "X" else False for x in list]):
        #         return "X";
        #     if all([True if x == "O" else False for x in list]):
        #         return "O";
        #     for (item, j) in enumerate(row):
        #         cols[j].append(item)
        #         if (i == j):
        #             diagonals[0].append(item)
        #         if (i == 2-j):
        #             diagonals[1].append(item)
        # for (row, i) in enumerate(cols):
        #      if all([True if x == "X" else False for x in list]):
        #           return "X";
        #      if all([True if x == "O" else False for x in list]):
        #          return "O";
        # for diagonalsEntry in diagonals:
        #     if all([True if x == "X" else False for x in list]):
        #          return "X";
        #     if all([True if x == "O" else False for x in list]):
        #         return "O";
        # return "NONE"
    def computeStats(self):
            pass
    def setTurn(self, name):
        self.turn = name
    def getTurn(self):
        return self.turn
    def quitMain(self):
        Socket.close()
        exit()



class TTTGui:
    def __init__ (self, myNames, oppenentNames, playMoveOnBoards, boards, getTurns, sockets, quitMains, setTurns, isBoardFulls, isGameFinisheds):
        #quitMain = quitMain
        self.games = 0
        self.getTurn = None
        self.quitMain = None
        self.ties = 0
        self.wins = 0
        self.losses = 0
        global myName
        myName = myNames
        global oppenentName
        oppenentName = oppenentNames
        global playMoveOnBoard
        playMoveOnBoard = playMoveOnBoards
        global board
        board = boards
        global getTurn
        getTurn = getTurns
        global socket
        socket = sockets
        global quitMain
        quitMain = quitMains
        global setTurn
        setTurn = setTurns
        global isBoardFull
        isBoardFull = isBoardFulls
        global isGameFinished
        isGameFinished = isGameFinisheds
    def start_GUI(self, myName, playMoveOnBoard, board, getTurn, Socket, quitMain):
        self.TicTacToeGUI(myName, playMoveOnBoard, board, getTurn, Socket, quitMain)
        t.mainloop()
    def receivePlay(self, Socket):
        while True:
             #print("waiting for move to be sent")
             clientData = Socket.recv(1024)
             move = clientData.decode('ascii')
             if move != "Fun times":

             #print(move)
                 Label2['text'] = "Current Player:" + " " + str(getTurn())
                 global player2name
                 player2name = oppenentName
                 if myName != "player1":
                     player2name = myName
                 turn = getTurn()
                 if move == "00":
                     if turn == player2name:
                         but1["text"] = "X"
                     if turn == "player1":
                         but1["text"] = "O"
                 elif move == "01":
                     if turn == player2name:
                         but2["text"] = "X"
                     if turn == "player1":
                         but2["text"] = "O"
                 elif move == "02":
                     if turn == player2name:
                         but3["text"] = "X"
                     if turn == "player1":
                         but3["text"] = "O"
                 elif move == "10":
                     if turn == player2name:
                         but4["text"] = "X"
                     if turn == "player1":
                         but4["text"] = "O"
                 elif move == "11":
                     if turn == player2name:
                         but5["text"] = "X"
                     if turn == "player1":
                         but5["text"] = "O"
                 elif move == "12":
                     if turn == player2name:
                         but6["text"] = "X"
                     if turn == "player1":
                         but6["text"] = "O"
                 elif move == "20":
                     if turn == player2name:
                         but7["text"] = "X"
                     if turn == "player1":
                         but7["text"] = "O"
                 elif move == "21":
                     if turn == player2name:
                         but8["text"] = "X"
                     if turn == "player1":
                         but8["text"] = "O"
                 elif move == "22":
                     if turn == player2name:
                         but9["text"] = "X"
                     if turn == "player1":
                         but9["text"] = "O"
                 rowIndex = int(move[0])
                 colIndex = int(move[1])
                 if turn == player2name:
                     board[rowIndex][colIndex] == "X"
                     setTurn("player1")
                     #Label2['text'] = "Current Player:" + " " + str(getTurn())
                 elif turn == "player1":
                     board[rowIndex][colIndex] == "O"
                     setTurn(player2name)
                     #Label2['text'] = "Current Player:" + " " + str(getTurn())
                 self.checkIfDone()
             else:
                 self.checkIfDone()
                 popUp2 = tk.Tk()
                 Lab1=Label(popUp2,text="Wins:" + " " + str(self.wins),font=("Arial",6,"bold"),bg="white")
                 Lab1.grid(row=1,column=1)
                 Lab2=Label(popUp2,text="Losses:" + " " + str(self.losses),font=("Arial",6,"bold"),bg="white")
                 Lab2.grid(row=4,column=1)
                 Lab1=Label(popUp2,text="Ties:" + " " + str(self.ties),font=("Arial",6,"bold"),bg="white")
                 Lab1.grid(row=8,column=1)
                 popUp2.mainloop()


    def checkIfDone(self):
        isFinished = isGameFinished()
        if isBoardFull():
            #print("BOARD IS FULL")
            self.ties += 1
            board = EMPTYBOARD
            self.TicTacToeGUI(myName, playMoveOnBoard, board, getTurn, Socket, quitMain)
            self.playAgain()
        elif isFinished != "NONE":
            print("SOMEONE HAS WON", isFinished)
            if isFinished == "X" and player2name != "player1":
                self.losses += 1
            elif isFinished == "X" and player2name == "player1":
                self.wins += 1
            elif isFinished == "O" and player2name == "player1":
                self.losses += 1
            elif isFinished == "O" and player2name != "player1":
                self.wins += 1
            self.playAgain()
    def quitButton(self, quitMain):
        quitMain()

        exit()
    def placeMove(self, myName, playMoveOnBoard, board, button, getTurn, position):
        currentTurn = getTurn()
        #print("Current turn:", currentTurn)
        player2name = oppenentName
        if myName != "player1":
            player2name = myName
        if currentTurn == player2name == myName:
            Label2['text'] = "Current Player:" + " " + str(getTurn())
            button['text'] = "X"
            playMoveOnBoard(position[0],position[1])
            #print(button)
            self.checkIfDone()
        if currentTurn == "player1" == myName:
            Label2['text'] = "Current Player:" + " " + str(getTurn())
            button['text'] = "O"
            playMoveOnBoard(position[0],position[1])
            #print(button)
            self.checkIfDone()
    def TicTacToeGUI(self, myName, playMoveOnBoard, board, getTurn, socket, quitMain):
        #print("GUI Here")
        global t
        t = tk.Tk()
        t.title("TIC TAC TOE BOARD")
        t.configure(bg="black")
        #Making the background of the window as white#Displaying the
        #canvas = tk.Canvas(t, width)
        Label1=Label(t,text=myName,font=("Arial",10,"bold"),bg="white")
        Label1.grid(row=0,column=0)#Quit button
        print("Turn",getTurn())
        global Label2
        Label2=Label(t,text="Current Player:" + " " + str(getTurn()),font=("Arial",8,"bold"),bg="white")
        Label2.grid(row=5,column=1)
        exitBut=Button(t,text="Quit",command=lambda: self.quitButton(quitMain),font=("Arial",10,"bold"))
        exitBut.grid(row=0,column=2)#Gid buttons
        global but1, but2, but3, but4, but5, but6, but7, but8, but9
        but1=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but1, getTurn, (0,0))])
        but2=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but2, getTurn, (0,1))])
        but3=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but3, getTurn, (0,2))])
        but4=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but4, getTurn, (1,0))])
        but5=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but5, getTurn, (1,1))])
        but6=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but6, getTurn, (1,2))])
        but7=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but7, getTurn, (2,0))])
        but8=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but8, getTurn, (2,1))])
        but9=Button(t,text="",height=5,width=10,bg="green",fg="pink",font="Arial 15 bold",command=lambda: [self.placeMove(myName, playMoveOnBoard, board, but9, getTurn, (2,2))])
        but1.grid(row=2,column=0)
        but2.grid(row=2,column=1)
        but3.grid(row=2,column=2)
        but4.grid(row=3,column=0)
        but5.grid(row=3,column=1)
        but6.grid(row=3,column=2)
        but7.grid(row=4,column=0)
        but8.grid(row=4,column=1)
        but9.grid(row=4,column=2)

    def playAgain(self):
        popUp = tk.Tk()
        popUp.title("Do you want to play again?")
        popUp.configure(bg="black")
        Label2=Label(popUp,text="Do You Want To Play Again(Y/N)",font=("Arial",8,"bold"),bg="white")
        Label2.grid(row=1,column=2)
        var = tk.StringVar()
        var = tk.StringVar()
        text = ttk.Entry(popUp,textvariable = var)
        text.grid(row=2, column = 2)
        def submit():
            if text.get().lower() == "n":
                if myName != "player1":
                    #print("SENDING MOVE RN")
                    move1 = "Fun times"
                    move1 = move1.encode('utf-8')
                    Socket.send(move1)
            #print("yeah",var)
            #print(var)
            #print(str1)
        #e1 = Entry(popUp,textvariable = var,font=("Arial",10,"bold"),bg="white" )
        #e1.grid(row=2,column=2)
        #print("hi",e1.get())
        button1=Button(popUp,text="Submit",height=4,width=8,bg="black",fg="white",font="Arial 5 bold",command=submit)
        button1.grid(row=6, column=2)
        popUp.mainloop()

        #print(var)
