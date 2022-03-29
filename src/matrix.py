from random import shuffle

class Matrix:

  def __init__(self, arg = None):
    if (arg):
      self.matrix = self.inputMatrix(arg)
    else:
      self.matrix = self.randomizeMatrix();

  """
  input matrix manually
  """
  def inputMatrix(self, matrix):
    inputMatr = [["" for j in range(4)] for i in range(4)]

    for i in range(4):
      for j in range(4):
        inputMatr[i][j] = matrix[i][j]

    return inputMatr

  """
  randomize matrix
  """
  def randomizeMatrix(self):
    matrixElmt = [i for i in range(1,16)] + [""]
    randMatrix = [["" for j in range(4)] for i in range(4)]
    # randomize the element
    shuffle(matrixElmt);

    # assign each element
    for i in range(4):
      for j in range(4):
        popped = matrixElmt.pop()
        randMatrix[i][j] = popped;

    return randMatrix;

  """
  method overriding for printing matrix
  """
  def __str__(self):
    s = [[str(e) for e in row] for row in self.matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return('\n'.join(table) + '\n')

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

  """
  get index of empty element
  """
  def getEmpty(self):
    return self.pos("")

  """
  move empty element
  """
  def move(self, dir):
    matr = Matrix(self.matrix)
    emptIndex = matr.getEmpty()
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
    matr.setElmt("", moveIndex)

    return matr


  def X(self):
    emptIndex = self.getEmpty()
    if ((emptIndex // 4) % 2 == 0 and emptIndex % 2 == 0) or ((emptIndex // 4) % 2 == 1 and emptIndex % 2 == 1):
      return 1
    else:
      return 0





