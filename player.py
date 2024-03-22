#player.py
import die


class Player:
  """Attributes: Represents a player who rolled 3 dice.
  Points = cumulative points
  Dice = list of 3 die objects
  """

  def __init__(self):
    """Initializes the player's dice, points, and rolls."""
    self.points = 0
    self.dice = [die.Die(), die.Die(), die.Die()]

  def get_points(self):
    """Returns the player's points."""
    return self.points
    
  def roll_dice(self):
    """ Rolls the player's dice and sorts them in ascending order"""
    for d in self.dice:
        d.roll()
    self.dice = sorted(self.dice, key=lambda x: x.value)
    return self.dice
    
  def has_pair(self):
    """Returns true if the player has a pair of dice that match. Increases points by 1"""
    if self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2] or self.dice[0] == self.dice[2]:
      self.points += 1
      return True
    else:
      return False


  def has_three_of_a_kind(self):
    """Returns true if the player has 3 dice that match. Increases points by 3"""
    if self.dice[0] == self.dice[1] == self.dice[2]:
      self.points += 3
      return True
    else:
      return False

  def has_series(self):
    """Returns true if the player has a series of 3 dice. Increases points by 2"""
    if self.dice[2] - self.dice[1] == 1 and self.dice[1] - self.dice[0] == 1:
      self.points += 2
      return True
    else:
      return False

  def __str__(self):
    """Returns a string representation of the player's dice."""
    return f"D1={self.dice[0]}, D2={self.dice[1]}, D3={self.dice[2]}"
