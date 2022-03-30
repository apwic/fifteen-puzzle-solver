from matrix import *
from operator import itemgetter
from typing import Tuple
import copy
from heapq import heappush, heappop

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

# def solve(matr: Tuple[Matrix, int], cost = 0):
#   # placeholder for each iteration
#   cost += 1
#   matrIter = ["up", "right", "down", "left"]
#   matrQueue = []

#   for i in matrIter:
#     movedMatr = matr[0].move(i)
#     if (movedMatr):
#       temp = (movedMatr, cost + costGoal(movedMatr))
#       matrQueue.append(temp)

#   # sort by cost
#   matrQueue.sort(key=itemgetter(1))
#   smallestCost = matrQueue[0]

#   print(f"{smallestCost[0]}\nCost: {smallestCost[1]}\n")
#   if (costGoal(smallestCost[0]) == 0):
#     return
#   else:
#     solve(smallestCost, cost)

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

class Node:

  def __init__(self, parent, matr, cost, level):
    self.parent = parent
    self.matr = matr
    self.cost = cost
    self.level = level

  def __lt__(self, nxt):
    return self.cost < nxt.cost


def createNode(matr, dir, level, parent) -> Node:
  newMatr = matr.move(dir)

  cost = costGoal(newMatr)
  print(cost)
  print(newMatr)
  newNode = Node(parent, newMatr, cost, level)

  return newNode  

def printPath(root):
  if (root == None):
    return

  printPath(root.parent)
  print(root.matr)

def solve(initial):

  if (checkBnB(initial)):
    matrIter = ["up", "right", "down", "left"]
    pq = PriorityQueue()

    cost = costGoal(initial)
    root = Node(None, initial, cost, 0)

    pq.push(root)

    while not pq.empty():
      minimum = pq.pop()

      if minimum.cost == 0:
        printPath(minimum)
        return minimum

      for i in matrIter:
        if (minimum.matr.move(i)):
          print(i)
          child = createNode(minimum.matr, i, minimum.level + 1, minimum)
          pq.push(child)

  else:
    print("Matrix unsolveable")

  