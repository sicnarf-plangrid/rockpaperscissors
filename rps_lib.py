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


class RpsStats():
  @staticmethod
  def load_stats(filename):
    try:
      with file(filename, 'r') as f:
        raw_stats = f.read()
        player_one_stats, player_two_stats, draws= raw_stats.split(' ')
        return (int(player_one_stats), int(player_two_stats), int(draws))
    except:
      return None

  @staticmethod
  def save_stats(
      filename,
      player_one_wins, 
      player_two_wins,
      draws):

    try:
      with file(filename, 'w') as f:
        f.write('{} {} {}'.format(
          player_one_wins, player_two_wins, draws))
      return True
    except:
      return False

