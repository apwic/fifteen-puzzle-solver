from matrix import *
from bnb import *
import time

def readFromFile(fileName):
  path = "./test/" + fileName

  try:
    matr = []
    countLine = 0
    with(open(path)) as f:
      for line in f:
        splitted = line.split(" ")
        try:
          row = [int(x) for x in splitted]
          matr.append(row)
          countLine += 1
        except:
          print("Element invalid")

    if countLine != 4:
      raise Exception("Invalid txt file")
    else:
      return matr

  except:
    print(f"{path} not found")
    print("Will use randomize matrix")


def start():
  fileInput = input("Enter file name: ")
  matr = Matrix(readFromFile(fileInput))
  print(matr)

  start_time = time.time()
  solution, nodes = solve(matr)
  end_time = time.time()
  if (solution):
    print(f"{solution.level} steps and {nodes} nodes explored")
    print(f"time taken: {end_time - start_time} seconds")