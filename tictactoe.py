#!/usr/bin/python

def CheckMove(row, col, board, valid):
  if not board[row][col] == 0:
    print "Move Not Valid Please Select New Move..."
    valid = False
    return valid
 
def CheckWin():
  print "\nDEBUG\n"

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
  valid = True #reset valid move variable
  print "\nPlayer %s (%s)" % (bit, mark) 
  while valid == True:
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
  return bit, mark, board

def PrintBoard(board):
  for row in board:
    print row

#----------------main------------------#

def main():
  ## Define Variables
  board = [[0 for n in xrange(3)] for n in xrange(3)]
  player_bit = 1; player_mark = "X"; win = False

  ## main()
  print "\nTic Tac Toe... in Python!\n"  
  while True:
    player_bit, player_mark, board = Move(player_bit, player_mark, board) 
    win = CheckWin()
    if win == True:
      print player_bit+" Wins!"; break
    player_bit, player_mark = FlipPlayer(player_bit, player_mark)
    PrintBoard(board)

if __name__ == "__main__":
  main()
