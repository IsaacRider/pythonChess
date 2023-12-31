#I developed this program using bottom-up development.

class board:
        chessBoard = [["r", "n", "b", "q", "k", "b", "n", "r"], #White is on the bottom and black is on the top.
                  ["p", "p", "p", "p", "p", "p", "p", "p"], 
                  ["-", "-", "-", "-", "-", "-", "-", "-"], 
                  ["-", "-", "-", "-", "-", "-", "-", "-"], 
                  ["-", "-", "-", "-", "-", "-", "-", "-"], 
                  ["-", "-", "-", "-", "-", "-", "-", "-"], 
                  ["P", "P", "P", "P", "P", "P", "P", "P"], 
                  ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        
        newLocation = ["", ""]
        oldLocation = ["", ""]
        whitePieces = ["P", "R", "N", "B", "Q", "K"]
        blackPieces = ["p", "r", "n", "b", "q", "k"]

        def printBoard(currentBoard, color):#Prints the chess board.
                if color % 2 == 0:
                        print("  a  b  c  d  e  f  g  h")
                        number = 8
                        for i in currentBoard:
                                print(number, end=" ")
                                for j in i:
                                        print(f"{j : <2}", end=" ")
                                print()
                                number = number - 1
                        del number
                        return
                else:
                        print("  a  b  c  d  e  f  g  h")
                        number = 1
                        for i in reversed(currentBoard):
                                print(number, end=" ")
                                for j in i:
                                        print(f"{j : <2}", end=" ")
                                print()
                                number = number + 1
                        del number
                        return

        def start():#This function gives the user a nice startup message.
                print("Hello, welcome to python chess! The uppercase pieces are white and the lowercase pieces are black.")
                return
    
        def makeMove(currentBoard, color):#Returns the old location and new location a piece chosen by the player.
                if color % 2 == 0:
                        print("HELLO, PLAYER 1 (WHITE)")
                else:
                        print("HELLO, PLAYER 2 (BLACK)")
                board.oldLocation = ["",""]
                board.newLocation = ["",""]
                while(board.correctMove(currentBoard, color, board.oldLocation, board.newLocation) == False):
                        print("Please type the column of the peice you would like to move:", end=" ")
                        board.oldLocation[0] = input()
                        print("Please type the row of the piece you would like to move:", end=" ")
                        board.oldLocation[1] = input()
                        print("Please type the column of the space you would like to move this piece:", end=" ")
                        board.newLocation[0] = input()
                        print("Please type the row of the space you would like to move this piece:", end=" ")
                        board.newLocation[1] = input()
                return (board.oldLocation, board.newLocation)

        def correctMove(currentBoard, color, oldLocation, newLocation):#Returns a True or False value.
                if (oldLocation[0] == "") or (oldLocation[1] == "") or (newLocation[0] == "") or (newLocation[1] == ""):
                        return False

                convertOld = board.convertLocation(oldLocation)
                convertNew = board.convertLocation(newLocation)
                print(convertOld, convertNew)
                # if color % 2 == 0:
                #         if currentBoard[convertOld[0]][convertOld[1]] not in board.blackPieces:
                #                 print("WHITE")
                #                 print(currentBoard[convertOld[0]][convertOld[1]])
                #                 return False
                # if color % 2 != 0:
                #         if currentBoard[convertOld[0]][convertOld[1]] not in board.whitePieces:
                #                 print("Black")
                #                 print(currentBoard[convertOld[0]][convertOld[1]])
                #                 return False

                if (currentBoard[convertOld[0]][convertOld[1]] == "P") or (currentBoard[convertOld[0]][convertOld[1]] == "p"):
                        return (board.correctPawn(currentBoard, color, convertOld, convertNew))  
                          
                if (currentBoard[convertOld[0]][convertOld[1]] == "R") or (currentBoard[convertOld[0]][convertOld[1]] == "r"):
                        return (board.correctRook(currentBoard, color, convertOld, convertNew))
                
                if (currentBoard[convertOld[0]][convertOld[1]] == "N") or (currentBoard[convertOld[0]][convertOld[1]] == "n"):
                        return (board.correctKnight(currentBoard, color, convertOld, convertNew))
                
                if (currentBoard[convertOld[0]][convertOld[1]] == "B") or (currentBoard[convertOld[0]][convertOld[1]] == "b"):
                        return (board.correctBishop(currentBoard, color, convertOld, convertNew))
                
                if (currentBoard[convertOld[0]][convertOld[1]] == "Q") or (currentBoard[convertOld[0]][convertOld[1]] == "q"):
                        return (board.correctQueen(currentBoard, color, convertOld, convertNew))
                
                if (currentBoard[convertOld[0]][convertOld[1]] == "K") or (currentBoard[convertOld[0]][convertOld[1]] == "k"):
                        return (board.correctKing(currentBoard, color, convertOld, convertNew))
                
                return False
        
        def convertLocation(Location):#Converts the strings given by the user into numbers corresponding to the board array. Location[0] is a letter. Location[1] is a number
                if Location[1].isdigit():
                        X = Location[0]
                        Y = Location[1]
                else:
                        return None
                Y = int(Y)
                Location[0] = board.flip(Y)
                print(Y)
                if (Y > 8) or (Y < 0):
                        return None
                if (X == "a") or (X == "A"):
                        Location[1] = 0
                        return Location
                if (X == "b") or (X == "B"):
                        Location[1] = 1
                        return Location
                if (X == "c") or (X == "C"):
                        Location[1] = 2
                        return Location
                if (X == "d") or (X == "D"):
                        Location[1] = 3
                        return Location
                if (X == "e") or (X == "E"):
                        Location[1] = 4
                        return Location
                if (X == "f") or (X == "F"):
                        Location[1] = 5
                        return Location
                if (X == "g") or (X == "G"):
                        Location[1] = 6
                        return Location
                if (X == "h") or (X == "H"):
                        Location[1] = 7
                        return Location
                return None
        
        #Pawn can only move forward. It can only move two spaces forward if that is it's first time moveing. It only attacks one space diagonally.
        def correctPawn(currentBoard, color, convertOld, convertNew): #Returns True if the move was a correct pawn move and false if it was an incorrect pawn move.
                print("Pawn", currentBoard[convertOld[0]][convertOld[1]])
                if color % 2 == 0:#If White
                        print("W")
                        if currentBoard[convertOld[0]][convertOld[1]] != "P":#If not white pawn
                                return False
                
                if color % 2 != 0:#If Black
                        print("B")
                        if currentBoard[convertOld[0]][convertOld[1]] != "p":#If not black pawn
                                return False
                
                ####If pawn is moving two spaces forward.
                if color % 2 == 0:#If White
                        if convertOld[0] == 6:#If pawn is on second row
                                if (currentBoard[convertOld[0]-1][convertOld[1]] == "-"):#If the space infront of pawn is empty.
                                        if (currentBoard[convertOld[0]-2][convertOld[1]] == "-"):#If the space two spaces infront of the pawn is empty.
                                                if (currentBoard[convertOld[0]-2][convertOld[1]] == currentBoard[convertNew[0]][convertNew[1]]):#If the pawn is moving two spaces forward
                                                        return True

                if color % 2 != 0:#If Black
                        if convertOld[0] == 1:#If pawn is on second row
                                if (currentBoard[convertOld[0]+1][convertOld[1]] == "-"):#If the space infront of pawn is empty.
                                        if (currentBoard[convertOld[0]+2][convertOld[1]] == "-"):#If the space two spaces infront of the pawn is empty.
                                                if (currentBoard[convertOld[0]+2][convertOld[1]] == currentBoard[convertNew[0]][convertNew[1]]):#If the pawn is moving two spaces forward
                                                        return True
                                                
                ####If pawn is moving one space forward.
                if color % 2 == 0:#If White
                        if (currentBoard[convertOld[0]-1][convertOld[1]] == "-"):#If the space infront of pawn is empty.
                                if (currentBoard[convertOld[0]-1][convertOld[1]] == currentBoard[convertNew[0]][convertNew[1]]):#If the pawn is moving two spaces forward
                                        if convertNew[0] == 7:#If pawn reached the end
                                                pass##########################      
                                        return True

                if color % 2 != 0:#If Black
                        if (currentBoard[convertOld[0]+1][convertOld[1]] == "-"):#If the space infront of pawn is empty.
                                if (currentBoard[convertOld[0]+1][convertOld[1]] == currentBoard[convertNew[0]][convertNew[1]]):#If the pawn is moving two spaces forward
                                        if convertNew[0] == 1:#If pawn reached the end
                                                pass##########
                                        return True
                                
                ####If pawn is attacking.
                if color % 2 == 0:#If White
                        if (currentBoard[convertOld[0]-1][convertOld[1]-1] != "-"):#If the space (left) diagonal of pawn is Full.
                                if currentBoard[convertNew[0]][convertNew[1]] in board.blackPieces:#Attacking black piece
                                        if convertNew[0] == 7:#If pawn reached the end
                                                pass##########
                                        return True

                        if (currentBoard[convertOld[0]-1][convertOld[1]+1] != "-"):#If the space (right) diagonal of pawn is Full.
                                if currentBoard[convertNew[0]][convertNew[1]] in board.blackPieces:#Attacking black piece
                                        if convertNew[0] == 7:#If pawn reached the end
                                                pass##########
                                        return True

                if color % 2 != 0:#If Black
                        if (currentBoard[convertOld[0]+1][convertOld[1]-1] != "-"):#If the space (left) diagonal of pawn is Full.
                                if currentBoard[convertNew[0]][convertNew[1]] in board.whitePieces:#Attacking white piece
                                        if convertNew[0] == 1:#If pawn reached the end
                                                pass##########
                                        return True

                        if (currentBoard[convertOld[0]+1][convertOld[1]+1] != "-"):#If the space (right) diagonal of pawn is Full.
                                if currentBoard[convertNew[0]][convertNew[1]] in board.whitePieces:#Attacking white piece
                                        if convertNew[0] == 1:#If pawn reached the end
                                                pass##########
                                        return True

                return False

        def correctRook(currentBoard, color, convertOld, convertNew):
                print("Rook")
                if color % 2 == 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "R":
                                return False
                if color % 2 != 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "r":
                                return False
                return True

        def correctKnight(currentBoard, color, convertOld, convertNew):
                print("Knight")
                if color % 2 == 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "N":
                                return False
                if color % 2 != 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "n":
                                return False
                return True

        def correctBishop(currentBoard, color, convertOld, convertNew):
                print("Bishop")
                if color % 2 == 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "B":
                                return False
                if color % 2 != 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "b":
                                return False
                return True

        def correctQueen(currentBoard, color, convertOld, convertNew):
                print("Queen")
                if color % 2 == 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "Q":
                                return False
                if color % 2 != 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "q":
                                return False
                return True

        def correctKing(currentBoard, color, convertOld, convertNew):
                print("King")
                if color % 2 == 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "K":
                                return False
                if color % 2 != 0:
                        if currentBoard[convertOld[0]][convertOld[1]] != "k":
                                return False
                return True

        def checkmate(currentBoard, color):
                return False
        def flip(Y):
                if Y == 8:
                        return 0
                if Y == 7:
                        return 1
                if Y == 6:
                        return 2
                if Y == 5:
                        return 3
                if Y == 4:
                        return 4
                if Y == 3:
                        return 5
                if Y == 2:
                        return 6
                if Y == 1:
                        return 7
                return False
        
Board = board.chessBoard
playerCount = 0
board.start()
print(Board[0][1])
while board.checkmate(Board, playerCount) != True:
        board.printBoard(Board, playerCount)
        oldMove, newMove = board.makeMove(Board, playerCount)
        print(oldMove, newMove)
        playerCount = playerCount + 1