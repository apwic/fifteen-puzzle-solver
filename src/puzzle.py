from random import shuffle
import numpy as np

EMPTY = 0

"""
using 1 dimensional array because it is faster than 2 dimensional array
"""
class Puzzle:

  def __init__(self, arg = None):
    if (arg):
      self.Puzzle = self.inputPuzzle(arg)
    else:
      self.Puzzle = self.randomizePuzzle();

  def copy(self):
    copy = Puzzle()
    copy.Puzzle = np.copy(self.Puzzle)
    return copy

  def __eq__(self, other):
    return self.Puzzle.tobytes() == other.Puzzle.tobytes()

  def __hash__(self):
    return hash(bytes(self.Puzzle))

  """
  method overriding for printing Puzzle
  """
  def __str__(self):
    puzzle = np.zeros((4,4), dtype=int)
    for i in range(4):
      for j in range(4):
        puzzle[i][j] = self.Puzzle[i*4 + j]

    s = [["-" if e == 0 else str(e) for e in row] for row in puzzle]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return('\n'.join(table) + '\n')

  """
  input Puzzle manually
  """
  def inputPuzzle(self, Puzzle):

    inputPuzz = np.zeros((16,), dtype=int)

    for i in range(4):
      for j in range(4):
        if (Puzzle[i][j] == 16):
          inputPuzz[i * 4 + j] = EMPTY;
        else:
          inputPuzz[i * 4 + j] = Puzzle[i][j]

    return inputPuzz

  """
  randomize Puzzle
  """
  def randomizePuzzle(self):
    PuzzleElmt = [i for i in range(0,16)]
    randPuzzle = np.zeros((16,), dtype=int)
    # randomize the element
    shuffle(PuzzleElmt)

    # assign each element
    for i in range(16):
      popped = PuzzleElmt.pop()
      randPuzzle[i] = popped

    return randPuzzle;

  """
  check valid
  """
  def isValid(self):
    for i in range(0, 16):
      if (self.pos(i) == -1):
        return False
    return True
    

  """
  elemet getter
  """
  def getElmt(self, n):
    n -= 1;
    return self.Puzzle[n]

  """
  element setter
  """
  def setElmt(self, elmt, n):
    n -= 1;
    self.Puzzle[n] = elmt

  """
  get index of element
  """
  def pos(self, x):
    pos = 1;
    for i in range(1, 17):
      if (self.getElmt(i) == x):
        return pos
      else:
        pos += 1
    
    return -1

  """
  get index of empty element
  """
  def getEmpty(self):
    return self.pos(EMPTY)

  """
  move empty element
  """
  def move(self, dir, emptIndex):
    puzz = self.copy()
    # move empty element up
    if (dir == "up"):
      moveIndex = emptIndex - 4
      if (moveIndex < 1):
        return False
    # move empty element down
    elif (dir == "down"):
      moveIndex = emptIndex + 4
      if (moveIndex > 16):
        return False
    # move empty element right
    elif (dir == "right"):
      if (emptIndex % 4 == 0):
        return False
      moveIndex = emptIndex + 1
    # move empty element left
    elif (dir == "left"):
      if (emptIndex % 4 == 1):
        return False
      moveIndex = emptIndex - 1
    else:
      print("direction undefined")
      return

    temp = puzz.getElmt(moveIndex)
    # switch
    puzz.setElmt(temp, emptIndex)
    puzz.setElmt(EMPTY, moveIndex)

    return puzz


  def X(self):
    emptIndex = self.getEmpty() - 1
    i = emptIndex // 4
    j = emptIndex % 4
    return (i + j) % 2





