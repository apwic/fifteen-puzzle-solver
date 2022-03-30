from bnb import *
from utils import *

if __name__ == "__main__":
  matr = readFromFile("bisa2.txt")
  print(matr)
  solution = solve(matr)
  print(solution.level)