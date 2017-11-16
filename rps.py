#!/usr/bin/python

from rps_lib import \
  RpsCommand, Player, RpsLogic, RpsStats

RPS_SCORE_FILENAME = "scores.txt"

def main():
  print "******"
  print "Rock Paper Scissors"
  print "******"

  player_one_wins = 0
  player_two_wins = 0
  num_draws = 0
  stats = RpsStats.load_stats(RPS_SCORE_FILENAME)
  if stats:
    player_one_wins, player_two_wins, num_draws = stats
    print "Player 1 has won {} games".format(
      player_one_wins)
    print "Player 2 has won {} games".format(
      player_two_wins)
    print "# draws: {}".format(num_draws)
  else:
    print "Could not load existing scores, initializing empty scores"

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
    num_draws += 1
  elif winner == Player.ONE:
    print "Player 1 won!"
    player_one_wins += 1
  else:
    print "Player 2 won!"
    player_two_wins += 1
  
  print "Player 1 has won {} games".format(
    player_one_wins)
  print "Player 2 has won {} games".format(
    player_two_wins)
  print "# draws: {}".format(num_draws)

  if not RpsStats.save_stats(
      RPS_SCORE_FILENAME, player_one_wins, player_two_wins, num_draws):
    print "Could not save scores"

if __name__ == "__main__":
  main()
