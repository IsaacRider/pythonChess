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
                        Y = (int(Location[1]))
                        Location[1] = int(Location[1])
                else:
                        return None
                Location[0] = Y - 1
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
        
        def correctPawn(currentBoard, color, convertOld, convertNew): #Returns True if the move was a correct pawn move and false if it was an incorrect pawn move.
                print("Pawn")
                return True

        def correctRook(currentBoard, color, convertOld, convertNew):
                print("Rook")
                return True

        def correctKnight(currentBoard, color, convertOld, convertNew):
                print("Knight")
                return True

        def correctBishop(currentBoard, color, convertOld, convertNew):
                print("Bishop")
                return True

        def correctQueen(currentBoard, color, convertOld, convertNew):
                print("Queen")
                return True

        def correctKing(currentBoard, color, convertOld, convertNew):
                print("King")
                return True

        def checkmate(currentBoard, color):
                return False
        
Board = board.chessBoard
print(Board[7][7])
playerCount = 0
board.start()
while board.checkmate(Board, playerCount) != True:
        board.printBoard(Board, playerCount)
        oldMove, newMove = board.makeMove(Board, playerCount)
        print(oldMove, newMove)
        playerCount = playerCount + 1