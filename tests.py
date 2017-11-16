#!/usr/bin/python

from rps_lib import RpsCommand, Player, RpsLogic

def test_rps_command():
  assert RpsCommand.get_rps_input("rock") == RpsCommand.ROCK
  assert RpsCommand.get_rps_input("paper") == RpsCommand.PAPER
  assert RpsCommand.get_rps_input("scissors") == RpsCommand.SCISSORS
  assert RpsCommand.get_rps_input("RoCk") == RpsCommand.ROCK
  assert RpsCommand.get_rps_input("rock!") == RpsCommand.INVALID
  assert RpsCommand.get_rps_input("invalid!") == RpsCommand.INVALID

def test_get_winner_from_move():
  assert RpsLogic.get_winner_from_move(
    RpsCommand.ROCK, RpsCommand.ROCK) == Player.NONE
  assert RpsLogic.get_winner_from_move(
    RpsCommand.ROCK, RpsCommand.PAPER) == Player.TWO
  assert RpsLogic.get_winner_from_move(
    RpsCommand.PAPER, RpsCommand.ROCK) == Player.ONE

if __name__ == "__main__":
  test_rps_command()
  test_get_winner_from_move()
