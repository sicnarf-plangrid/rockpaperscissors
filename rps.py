#!/usr/bin/python

from rps_lib import RpsCommand, Player, RpsLogic

def main():
  print "Rock Paper Scissors"

  print "Player 1, please enter rock/paper/scissors:"
  player_one_move = RpsCommand.get_rps_input(
    raw_input())
  while player_one_move == RpsCommand.INVALID:
    print "Invalid, please enter rock/paper/scissors:"
    player_one_move = RpsCommand.get_rps_input(
      raw_input())

  print "Player 2, please enter rock/paper/scissors"
  player_two_move = RpsCommand.get_rps_input(
    raw_input())
  while player_two_move == RpsCommand.INVALID:
    print "Invalid, please enter rock/paper/scissors:"
    player_two_move = RpsCommand.get_rps_input(
      raw_input())

  winner = RpsLogic.get_winner_from_move(
    player_one_move, player_two_move)

  if winner == Player.NONE:
    print "Draw!"
  elif winner == Player.ONE:
    print "Player 1 won!"
  else:
    print "Player 2 won!"
  
if __name__ == "__main__":
  main()
