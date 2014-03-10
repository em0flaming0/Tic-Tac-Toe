#!/usr/bin/python

def CheckMove(row, col, board, valid):
  if not board[row][col] == "-":
    print "Move Not Valid Please Select New Move..."
    valid = False
    return valid
  else:
    valid = True
    return valid
 
def testCheckWin(board):
  if(board[0][0] and board [0][1] and board[0][2] == "X"):
    return True
  else:
    return False
  

def CheckWin(board):
  if (
    (board[0][0] == "X" and board [0][1] == "X" and board[0][2] == "X") or
    (board[1][0] == "X" and board [1][1] == "X" and board[1][2] == "X") or
    (board[2][0] == "X" and board [2][1] == "X" and board[2][2] == "X") or
    (board[0][0] == "X" and board [1][0] == "X" and board[2][0] == "X") or
    (board[0][1] == "X" and board [1][1] == "X" and board[2][1] == "X") or
    (board[0][2] == "X" and board [1][2] == "X" and board[2][2] == "X") or
    (board[0][0] == "X" and board [1][1] == "X" and board[2][2] == "X") or
    (board[0][2] == "X" and board [1][1] == "X" and board[2][0] == "X")):
      return True
  elif (  
    (board[0][0] == "O" and board [0][1] == "O" and board[0][2] == "O") or
    (board[1][0] == "O" and board [1][1] == "O" and board[1][2] == "O") or
    (board[2][0] == "O" and board [2][1] == "O" and board[2][2] == "O") or
    (board[0][0] == "O" and board [1][0] == "O" and board[2][0] == "O") or
    (board[0][1] == "O" and board [1][1] == "O" and board[2][1] == "O") or
    (board[0][2] == "O" and board [1][2] == "O" and board[2][2] == "O") or
    (board[0][0] == "O" and board [1][1] == "O" and board[2][2] == "O") or
    (board[0][2] == "O" and board [1][1] == "O" and board[2][0] == "O")):
      return True
  else:
      return False

def FlipPlayer(bit, mark):
  if bit == 1:
    bit = 2
  else:
    bit = 1
  if mark == "X":
    mark = "O"
  else:
    mark = "X"
  return bit, mark
  
def Move(bit, mark, board):
  valid = False #reset valid move variable
  print "\nPlayer %s (%s)" % (bit, mark) 
  while valid == False:
    r = raw_input("Select Row: "); row = (int(r))-1
    while row < 0 or row >=  3:
      print "Please Re-Enter Number Between 1 and 3"
      r = raw_input("Select Row: "); row = (int(r))-1
    c = raw_input("Select Column: "); col = (int(c))-1   
    while col < 0 or col >= 3:
      print "Please Re-Enter Number Between 1 and 3"
      c = raw_input("Select Column: "); col = (int(c))-1 
    valid = CheckMove(row, col, board, valid)
  board[row][col] = mark
  return board

def PrintBoard(board):
  print "%s  |  %s  |  %s" % (board[0][0], board[0][1], board[0][2])
  print "--------------"
  print "%s  |  %s  |  %s" % (board[1][0], board[1][1], board[1][2])
  print "--------------"
  print "%s  |  %s  |  %s" % (board[2][0], board[2][1], board[2][2])

#----------------main------------------#

def main():
  ## Define Variables
  board = [["-" for n in xrange(3)] for n in xrange(3)]
  player_bit = 1; player_mark = "X"; win = False

  ## main()
  print "\nTic Tac Toe... in Python!\n"  
  while True:
    board = Move(player_bit, player_mark, board) 
    win = CheckWin(board)
    PrintBoard(board)
    if win == True:
      print "Player ", player_bit, " Wins!"; break
    player_bit, player_mark = FlipPlayer(player_bit, player_mark)
if __name__ == "__main__":
  main()
