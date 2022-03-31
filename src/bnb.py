from xml.dom.minicompat import NodeList
from matrix import *
from heapq import heappush, heappop

"""
priority queue for determining the next node to be expanded
"""
class PriorityQueue:
  def __init__(self):
    self.heap = []

  def push(self, k):
    heappush(self.heap, k)

  def pop(self):
    return heappop(self.heap)

  def empty(self):
    if not self.heap:
      return True
    else :
      return False

"""
node that can expand when the matrix is moved
"""
class Node:

  def __init__(self, parent, matr, cost, level, emptyPos):
    self.parent = parent
    self.matr = matr
    self.cost = cost
    self.level = level
    self.emptyPos = emptyPos

  def __lt__(self, nxt):
    return self.cost + self.level < nxt.cost + nxt.level

"""
create node
"""
def createNode(parent, matr, dir, emptyPos, level) -> Node:

  newMatr = matr.move(dir, emptyPos)

  if (dir == "up"):
    newEmptyPos = emptyPos - 4
  elif (dir == "down"):
    newEmptyPos = emptyPos + 4
  elif (dir == "right"):
    newEmptyPos = emptyPos + 1
  else:
    newEmptyPos = emptyPos - 1
  
  # if (newMatr.getElmt(emptyPos) == emptyPos):
  #   cost = parent.cost - 1
  # else:
  #   cost = parent.cost
  # print(f"Cost : {cost}")
  # print(newMatr)

  cost = costGoal(newMatr)
  newNode = Node(parent, newMatr, cost, level, newEmptyPos)

  return newNode  

"""
print steps to goal
"""
def printPath(root):
  if (root == None):
    return

  printPath(root.parent)
  print(root.matr)

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
  if (matrix.isValid()):
    kur = 0

    for i in range(1, 17):
      kur += kurang(matrix, i)

    check = kur + matrix.X()
    print(f"{check} = {kur} + {matrix.X()}")

    if (check % 2 == 0):
      return True
    else:
      return False
  else:
    return False

"""
cost from nodes to goal
"""
def costGoal(cur: Matrix):
  cost = 0
  for i in range(1, 16):
    if (cur.getElmt(i) != i):
      cost += 1

  return cost

"""
different cost function
"""
def costGoalManhattan(cur: Matrix):
  cost = 0
  for i in range(1, 16):
    if (cur.getElmt(i) != i):
      curIndex = cur.pos(i)
      xDiff = abs(curIndex // 4 - i // 4)
      yDiff = abs(curIndex % 4 - curIndex % 4)
      cost += xDiff + yDiff
  
  return cost


"""
solve the puzzle using branch and bound
"""
def solve(initial):

  if (checkBnB(initial)):
    matrIter = ["up", "right", "down", "left"]
    memory = set()
    pq = PriorityQueue()

    cost = costGoal(initial)
    root = Node(None, initial, cost, 0, initial.getEmpty())

    pq.push(root)
    count = 0

    while not pq.empty():
      minimum = pq.pop()
      print(f"{count} : {minimum.cost}")
      count += 1

      if minimum.cost == 0:
        print("--------------------------------")
        printPath(minimum)
        return minimum, len(memory)

      memory.add(minimum)
      
      for i in matrIter:
        movedMatr = minimum.matr.move(i, minimum.emptyPos)
        if (movedMatr):
          if movedMatr not in memory:
            child = createNode(minimum, minimum.matr, i, minimum.emptyPos, minimum.level + 1)
            pq.push(child)

  else:
    print("Matrix unsolveable")