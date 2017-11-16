#!/usr/bin/python

from rps_lib import \
  RpsCommand, Player, RpsLogic, RpsStats

def test_rps_command():
  assert RpsCommand.get_rps_input("rock") == RpsCommand.ROCK
  assert RpsCommand.get_rps_input("paper") == RpsCommand.PAPER
  assert RpsCommand.get_rps_input("scissors") == RpsCommand.SCISSORS
  assert RpsCommand.get_rps_input("RoCk") == RpsCommand.ROCK
  assert RpsCommand.get_rps_input("rock!") == RpsCommand.INVALID
  assert RpsCommand.get_rps_input("invalid!") == RpsCommand.INVALID

def test_rps_logic():
  assert RpsLogic.get_winner_from_move(
    RpsCommand.ROCK, RpsCommand.ROCK) == Player.NONE
  assert RpsLogic.get_winner_from_move(
    RpsCommand.ROCK, RpsCommand.PAPER) == Player.TWO
  assert RpsLogic.get_winner_from_move(
    RpsCommand.PAPER, RpsCommand.ROCK) == Player.ONE

def test_rps_stats():
  assert RpsStats.load_stats("test_valid.txt") == (1, 2, 3) 
  assert not RpsStats.load_stats("test_invalid.txt")
  assert not RpsStats.load_stats("file_doesnt_exist.txt")

  RpsStats.save_stats("test_new_stats.txt", 4, 5, 6)
  with file("test_new_stats.txt", 'r') as f:
    raw_stats = f.read()
    assert raw_stats == '4 5 6'

if __name__ == "__main__":
  test_rps_command()
  test_rps_logic()
  test_rps_stats()
