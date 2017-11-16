#!/usr/bin/python

class RpsCommand(): 
  INVALID = 0
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

  @staticmethod
  def get_rps_input(user_input):
    user_input = user_input.lower()
    if user_input == "rock":
      return RpsCommand.ROCK
    elif user_input == "paper":
      return RpsCommand.PAPER
    elif user_input == "scissors":
      return RpsCommand.SCISSORS
    else:
      return RpsCommand.INVALID


class Player: 
  NONE = 0
  ONE = 1
  TWO = 2


class RpsLogic():
  """
  Game logic
  """

  @staticmethod
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

