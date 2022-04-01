from random import shuffle
import numpy as np

EMPTY = 0

class Matrix:

  def __init__(self, arg = None):
    if (arg):
      self.matrix = self.inputMatrix(arg)
    else:
      self.matrix = self.randomizeMatrix();

  def copy(self):
    copy = Matrix()
    copy.matrix = np.copy(self.matrix)
    return copy

  def __eq__(self, other):
    return self.matrix.tobytes() == other.matrix.tobytes()

  def __hash__(self):
    return hash(bytes(self.matrix))

  """
  method overriding for printing matrix
  """
  def __str__(self):
    s = [["-" if e == 0 else str(e) for e in row] for row in self.matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return('\n'.join(table) + '\n')

  """
  input matrix manually
  """
  def inputMatrix(self, matrix):

    inputMatr = np.zeros((4,4), dtype=int)

    for i in range(4):
      for j in range(4):
        if (matrix[i][j] == 16):
          inputMatr[i][j] = EMPTY;
        else:
          inputMatr[i][j] = matrix[i][j]

    return inputMatr

  """
  randomize matrix
  """
  def randomizeMatrix(self):
    matrixElmt = [i for i in range(0,16)]
    randMatrix = np.zeros((4,4), dtype=int)
    # randomize the element
    shuffle(matrixElmt);

    # assign each element
    for i in range(4):
      for j in range(4):
        popped = matrixElmt.pop()
        randMatrix[i][j] = popped;

    return randMatrix;

  """
  check valid
  """
  def isValid(self):
    for i in range(1, 16):
      if (self.pos(i) == -1):
        return False
    return True
    

  """
  elemet getter
  """
  def getElmt(self, n):
    n -= 1;
    return self.matrix[n // 4][n % 4]

  """
  element setter
  """
  def setElmt(self, elmt, n):
    n -= 1;
    self.matrix[n // 4][n % 4] = elmt

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
    matr = self.copy()
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

    temp = matr.getElmt(moveIndex)
    # switch
    matr.setElmt(temp, emptIndex)
    matr.setElmt(EMPTY, moveIndex)

    return matr


  def X(self):
    emptIndex = self.getEmpty() - 1
    i = emptIndex // 4
    j = emptIndex % 4
    return (i + j) % 2





