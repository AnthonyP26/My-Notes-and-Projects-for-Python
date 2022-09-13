import sys
56
boardSet = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def board(boardSet):
  print(boardSet[0], " | ",boardSet[1], " | ",boardSet[2])
  print("--------------")
  print(boardSet[3], " | ",boardSet[4], " | ",boardSet[5])
  print("--------------")
  print(boardSet[6], " | ",boardSet[7], " | ",boardSet[8])


def turn(boardSet):
  
  player = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
  for i in range(len(player)):
    board(boardSet)

    while True:
      
      turn = input("Take Your Turn "+ player[i] +" : ")
      if int(turn) in boardSet:
        boardSet[int(turn)] = player[i]

        if boardSet[0] and boardSet[1] and boardSet[2] == player[i]:
          sys.exit(player[i] + "wins!")

        if boardSet[3] and boardSet[4] and boardSet[5] == player[i]:
          sys.exit(player[i] + "wins!")

        if boardSet[6] and boardSet[7] and boardSet[8] == player[i]:
          sys.exit(player[i] + "wins!")

        if boardSet[0] and boardSet[3] and boardSet[6] == player[i]:
          sys.exit(player[i] + "wins!")

        if boardSet[1] and boardSet[4] and boardSet[7] == player[i]:
          sys.exit(player[i] + "wins!")

        if boardSet[2] and boardSet[5] and boardSet[8] == player[i]:
          sys.exit(player[i] + "wins!")
          
        if boardSet[0] and boardSet[4] and boardSet[8] == player[i]:
          sys.exit(player[i] + "wins!")
          
        if boardSet[2] and boardSet[4] and boardSet[6] == player[i]:
          sys.exit(player[i] + "wins!")

        print("\n")
        break
      else:
        print("That spot is not available, pick again.\n")


turn(boardSet)
