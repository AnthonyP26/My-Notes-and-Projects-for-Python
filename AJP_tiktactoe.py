tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

divider = "-----"
play_board = str(tiles[0]) + "|" + str(tiles[1]) + "|" + str(tiles[2])
play_board_1 = str(tiles[3]) + "|" + str(tiles[4]) + "|" + str(tiles[5])
play_board_2 = str(tiles[6]) + "|" + str(tiles[7]) + "|" + str(tiles[8])

def board():
  print(play_board)
  print(divider)
  print(play_board_1)
  print(divider)
  print(play_board_2)

board()

win = False
while win == False:

  def X_():
    x_turn = int(input("X take your turn: "))
    if isinstance(x_turn, int) == True:
      if x_turn in range(0, 8):
        board()
        Y_()
      else:
        print("Not an option")
        X_()
    else:
      print("Not an option")
      X_()

    tiles(range(0, 8)) == x_turn
    board()
    
  def Y_():
    y_turn = int(input("Y take your turn: "))
    if isinstance(y_turn, int) == True:
      if y_turn in range(0, 8):
        board(board())
        X_()
      else:
        print("Not an option")
        Y_()
    else:
      print("Not an option")
      Y_()

    
  
  X_()
