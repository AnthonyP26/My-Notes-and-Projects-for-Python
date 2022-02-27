tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tiles_str = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

global turn_count
turn_count = 0


def board():
  divider = "-----"
  play_board = str(tiles[0]) + "|" + str(tiles[1]) + "|" + str(tiles[2])
  play_board_1 = str(tiles[3]) + "|" + str(tiles[4]) + "|" + str(tiles[5])
  play_board_2 = str(tiles[6]) + "|" + str(tiles[7]) + "|" + str(tiles[8])
  
  print(play_board)
  print(divider)
  print(play_board_1)
  print(divider)
  print(play_board_2)

while True:

  def Turn_X():
    board()
    x_turn = input("X take your turn: ")
    if x_turn in tiles_str:
      x_turn = int(x_turn)
      if x_turn in tiles:
        if isinstance(tiles[x_turn], int):
          global turn_count
          turn_count = turn_count+1
          tiles[x_turn -1] = "X"
          if turn_count < 9:
            Turn_O()
        else:
          print("Not an option")
          Turn_X()
      else:
        print("Not an option")
        Turn_X()
    else:
      print("Not an option")
      Turn_X()

  def Turn_O():
    board()
    o_turn = input("O take your turn: ")
    if o_turn in tiles_str:
      o_turn = int(o_turn)
      if o_turn in tiles:
        if isinstance(tiles[o_turn], int):
          global turn_count
          turn_count = turn_count+1
          tiles[o_turn -1] = "O"
          print(turn_count)
          Turn_X()
        else:
          print("Not an option")
          Turn_O()
      else:
        print("Not an option")
        Turn_O()
    else:
      print("Not an option")
      Turn_O()
  if turn_count >= 9:
    board()
    print("\nDraw")
    break
    
  #if tiles[0] == "X" and tiles[1] == "x" and tiles[2] =="X":
  #  print("X wins")
  #  break
  
  Turn_X()
  
