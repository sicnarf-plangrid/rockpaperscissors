#!/usr/bin/python

class RpsCommand: # Enum
  INVALID = 0
  ROCK = 1
  PAPER = 2
  SCISSORS = 3


class Player: # Enum
  NONE = 0
  ONE = 1
  TWO = 2


def get_rps_input():
  user_input = raw_input().lower()
  if user_input == "rock":
    return RpsCommand.ROCK
  elif user_input == "paper":
    return RpsCommand.PAPER
  elif user_input == "scissors":
    return RpsCommand.SCISSORS
  else:
    return RpsCommand.INVALID


def get_winner_from_move(move1, move2):
  return {
    (RpsCommand.ROCK, RpsCommand.PAPER): Player.TWO,
    (RpsCommand.ROCK, RpsCommand.ROCK): Player.NONE,
    (RpsCommand.ROCK, RpsCommand.SCISSORS): Player.ONE,
    (RpsCommand.PAPER, RpsCommand.PAPER): Player.NONE,
    (RpsCommand.PAPER, RpsCommand.ROCK): Player.ONE,
    (RpsCommand.PAPER, RpsCommand.SCISSORS): Player.TWO,
    (RpsCommand.SCISSORS, RpsCommand.PAPER): Player.ONE,
    (RpsCommand.SCISSORS, RpsCommand.ROCK): Player.TWO,
    (RpsCommand.SCISSORS, RpsCommand.SCISSORS): Player.NONE,
  }[(move1, move2)]


def main():
  print "Rock Paper Scissors"

  print "Player 1, please enter rock/paper/scissors:"
  player_one_move = get_rps_input()
  while player_one_move == RpsCommand.INVALID:
    print "Invalid, please enter rock/paper/scissors:"
    player_one_move = get_rps_input()

  print "Player 2, please enter rock/paper/scissors"
  player_two_move = get_rps_input()
  while player_two_move == RpsCommand.INVALID:
    print "Invalid, please enter rock/paper/scissors:"
    player_two_move = get_rps_input()

  winner = get_winner_from_move(player_one_move, player_two_move)
  if winner == Player.NONE:
    print "Draw!"
  elif winner == Player.ONE:
    print "Player 1 won!"
  else:
    print "Player 2 won!"
  
if __name__ == "__main__":
  main()
