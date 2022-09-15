import sys

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

        if boardSet[0] == boardSet[1] == boardSet[2]:
          board(boardSet)
          sys.exit(player[i] + " wins!")

        if boardSet[3] == boardSet[4] == boardSet[5]:
          board(boardSet)
          sys.exit(player[i] + " wins!")

        if boardSet[6] == boardSet[7] == boardSet[8]:
          board(boardSet)
          sys.exit(player[i] + " wins!")

        if boardSet[0] == boardSet[3] == boardSet[6]:
          board(boardSet)
          sys.exit(player[i] + " wins!")

        if boardSet[1] == boardSet[4] == boardSet[7]:
          board(boardSet)
          sys.exit(player[i] + " wins!")

        if boardSet[2] == boardSet[5] == boardSet[8]:
          board(boardSet)
          sys.exit(player[i] + " wins!")
          
        if boardSet[0] == boardSet[4] == boardSet[8]:
          board(boardSet)
          sys.exit(player[i] + " wins!")
          
        if boardSet[2] == boardSet[4] == boardSet[6]:
          board(boardSet)
          sys.exit(player[i] + " wins!")

          

        print("\n")
        break
      else:
        print("That spot is not available, pick again.\n")


turn(boardSet)
