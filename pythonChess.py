#I developed this program using bottom-up development.

class board:
        chessBoard = [["r", "n", "b", "q", "k", "b", "n", "r"], 
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

        def printBoard(currentBoard):
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

        def start(currentBoard):
                print("Hello, welcome to python chess!")
                board.printBoard(currentBoard)
                return
    
        def makeMove(currentBoard, color):
                if color == 1:
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

        def correctMove(currentBoard, color, oldLocation, newLocation):
                convertOld = board.convertLocation(oldLocation)
                convertNew = board.convertLocation(newLocation)
                if (convertNew or convertOld) == None:
                        print(convertNew)
                        return False
                return True
        
                if (convertOld or convertNew) == None:
                        return False
                if currentBoard[convertOld[0]][convertOld[1]] == "P" or "p":
                        return (board.correctPawn(currentBoard, color, convertOld, convertNew))
                if currentBoard[convertOld[0]][convertOld[1]] == "R" or "r":
                        return (board.correctRook(currentBoard, color, convertOld, convertNew))
                if currentBoard[convertOld[0]][convertOld[1]] == "N" or "n":
                        return (board.correctKnight(currentBoard, color, convertOld, convertNew))
                if currentBoard[convertOld[0]][convertOld[1]] == "B" or "b":
                        return (board.correctBishop(currentBoard, color, convertOld, convertNew))
                if currentBoard[convertOld[0]][convertOld[1]] == "Q" or "q":
                        return (board.correctQueen(currentBoard, color, convertOld, convertNew))
                if currentBoard[convertOld[0]][convertOld[1]] == "K" or "k":
                        return (board.correctKing(currentBoard, color, convertOld, convertNew))
                return False

        def correctPawn(currentBoard, color, convertOld, convertNew):
                return True

        def correctRook():
                pass

        def correctKnight(currentBoard, color, convertOld, convertNew):
                pass

        def correctBishop(currentBoard, color, convertOld, convertNew):
                pass

        def correctQueen(currentBoard, color, convertOld, convertNew):
                pass

        def correctKing(currentBoard, color, convertOld, convertNew):
                pass

        def convertLocation(Location):
                if Location[1].isdigit():
                        X = Location[0]
                        Y = int(Location[1])
                        Location[1] = int(Location[1])
                else:
                        return None
                if (Y > 8) or (Y < 0):
                        return None
                if X == "a" or "A":
                        Location[0] = 1
                        return Location
                if X == "b" or "B":
                        Location[0] = 2
                        return Location
                if X == "c" or "C":
                        Location[0] = 3
                        return Location
                if X == "d" or "D":
                        Location[0] = 4
                        return Location
                if X == "e" or "E":
                        Location[0] = 5
                        return Location
                if X == "f" or "F":
                        Location[0] = 6
                        return Location
                if X == "g" or "G":
                        Location[0] = 7
                        return Location
                if X == "H" or "h":
                        Location[0] = 8
                        return Location
                return None
                
        
Board = board.chessBoard
board.printBoard(Board)
oldMove, newMove = board.makeMove(Board, 1)
print(oldMove, newMove)