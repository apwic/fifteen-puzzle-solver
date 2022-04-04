from puzzle import *
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
node that can expand when the Puzzle is moved
"""
class Node:

  def __init__(self, parent, puzzle, cost, level, emptyPos, dir):
    self.parent = parent
    self.puzzle = puzzle
    self.cost = cost
    self.level = level
    self.emptyPos = emptyPos
    self.dir = dir

  def __lt__(self, nxt):
    if (self.cost + self.level) == (nxt.cost + nxt.level):
      return self.cost < nxt.cost
    else:
      return self.cost + self.level < nxt.cost + nxt.level


"""
create node
"""
def createNode(parent, puzz, movedPuzz, dir, emptyPos, level) -> Node:

  if (dir == "up"):
    newEmptyPos = emptyPos - 4
  elif (dir == "down"):
    newEmptyPos = emptyPos + 4
  elif (dir == "right"):
    newEmptyPos = emptyPos + 1
  else:
    newEmptyPos = emptyPos - 1
  
  # O(1) cost finding
  cost = parent.cost
  if (puzz.getElmt(newEmptyPos) != newEmptyPos):
    cost -= 1
  if (puzz.getElmt(newEmptyPos) != emptyPos):
    cost += 1

  newNode = Node(parent, movedPuzz, cost, level, newEmptyPos, dir)

  return newNode  

"""
print steps to goal
"""
def printPath(root):
  if (root == None):
    return

  printPath(root.parent)
  print(f"dir: {root.dir}")
  print(root.puzzle)

"""
find Puzzle elmt
that is j < i and posisi(j) > posisi(i)
"""
def kurang(Puzzle, i):
  if (i == 16):
    iPos = Puzzle.getEmpty()
  else:
    iPos = Puzzle.pos(i)
  kur = 0

  for x in range(1,i):
    if (Puzzle.pos(x) > iPos):
      kur += 1;

  print(f"kurang[{i}]\t: {kur}")
  return kur

"""
check if Puzzle is solveable
"""
def checkBnB(Puzzle):
  if (Puzzle.isValid()):
    kur = 0

    for i in range(1, 17):
      kur += kurang(Puzzle, i)

    check = kur + Puzzle.X()
    print(f"\nsigma(kurang): {kur}, X: {Puzzle.X()}")

    if (check % 2 == 0):
      return True
    else:
      return False
  else:
    return False

"""
cost from nodes to goal
"""
def costGoal(cur):
  cost = 0
  for i in range(1, 16):
    if (cur.getElmt != EMPTY):
      if (cur.getElmt(i) != i):
        cost += 1

  return cost

"""
different cost function
"""
def costGoalManhattan(cur):
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
    # puzzleIter = ["up", "right", "down", "left"]
    puzzleIter = ["down", "up", "right", "left"]
    # puzzleIter = ["down", "right", "left", "up"]
    # puzzleIter = ["down", "right", "up", "left"]
    memory = set()
    pq = PriorityQueue()

    cost = costGoal(initial)
    root = Node(None, initial, cost, 0, initial.getEmpty(), "-")

    pq.push(root)
    count = 0

    while not pq.empty():
      minimum = pq.pop()
      count += 1

      if minimum.cost == 0:
        return minimum, len(memory)

      memory.add(minimum.puzzle)
      
      for i in puzzleIter:
        movedPuzzle = minimum.puzzle.move(i, minimum.emptyPos)
        if (movedPuzzle):
          if movedPuzzle not in memory:
            child = createNode(minimum, minimum.puzzle, movedPuzzle, i, minimum.emptyPos, minimum.level + 1)
            pq.push(child)

  else:
    print("puzzle unsolveable")

  return None, 0