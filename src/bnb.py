from matrix import *
from operator import itemgetter

"""
find matrix elmt
that is j < i and posisi(j) > posisi(i)
"""
def kurang(matrix : Matrix, i):
  if (i == 16):
    iPos = matrix.getEmpty()
  else:
    iPos = matrix.pos(i)
  kur = 0

  for x in range(1,i):
    if (matrix.pos(x) > iPos):
      kur += 1;

  print(f"Kurang[{i}] = {kur}")
  return kur

"""
check if matrix is solveable
"""
def checkBnB(matrix : Matrix):
  kur = 0

  for i in range(1, 17):
    kur += kurang(matrix, i)

  check = kur + matrix.X()
  print(f"{check} = {kur} + {matrix.X()}")

  if (check % 2 == 0):
    return True
  else:
    return False

# """
# cost to nodes from root
# """
# def costRoot(root, cur):
#   pass

"""
cost from nodes to goal
"""
def costGoal(cur: Matrix):
  cost = 0
  for i in range(1, 16):
    if (cur.getElmt(i) != i):
      cost += 1

  return cost

def solve(matr: (Matrix, int), cost = 0):
  # placeholder for each iteration
  cost += 1
  matrIter = ["up", "right", "down", "left"]
  matrQueue = []

  for i in matrIter:
    movedMatr = matr[0].move(i)
    if (movedMatr):
      temp = (movedMatr, cost + costGoal(movedMatr))
      matrQueue.append(temp)

  # sort by cost
  matrQueue.sort(key=itemgetter(1))
  smallestCost = matrQueue[0]

  print(f"{smallestCost[0]}\nCost: {smallestCost[1]}\n")
  if (costGoal(smallestCost[0]) == 0):
    return
  else:
    solve(smallestCost, cost)


# class Tree:

#   def __init__(self, matrix: Matrix, cost):
#     self.root = (matrix, cost)
#     self.up = None
#     self.right = None
#     self.down = None
#     self.left = None

#   def costGoal(self):
#     for i in range(1, 16):
#       if (self.root[0].getELmt(i) == i):

  