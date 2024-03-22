# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 02/29/2024
# Module 5 - Yahtzee
# Purpose - Create a game where a player rolls three dice and scores points based on the combination of the dice.

import die
import player
import random
import check_input

def take_turn(player):
  """Perform a turn for the player."""
  print()
  player.roll_dice()
  print(player)
  if player.has_three_of_a_kind():
    print("You got 3 of a kind!")
  elif player.has_pair():
    print("You got a pair!")
  elif player.has_series():
    print("You got a series of 3!")
  else:
    print("Aww. Too Bad.")
  print("Score =", player.get_points())


def main():
  """Main function to run the Yahtzee game."""
  print("-Yahtzee-")
  play = player.Player()
  play_again = True
  while play_again:
    take_turn(play)
    play_again = check_input.get_yes_no("Play again? (y/n): ")
  print("\nGame over.")
  print("Final score =", play.get_points())


main()
