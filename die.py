#die.py
import random
class Die:
  """Attributes: Represents a single die
  Sides = 6 sided die
  Value = the value of the random roll"""
    
  def __init__(self, sides=6):
    self.sides = sides
    self.value = 0

  def roll(self):
    """Roll the die and return the result."""
    self.value = random.randint(1, self.sides)
    return self.value

  def __str__(self):
    """Return the current value of the die."""
    return f"{self.value}"

  def __lt__(self, other):
    """Return true if the value of self is less than other."""
    return self.value < other.value

  def __eq__(self, other):
    """Return true if both values are equal."""
    return self.value == other.value

  def __sub__(self, other):
    """Return the difference between the values of self and other."""
    return self.value - other.value

  